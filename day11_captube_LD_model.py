
# day11_captube_LD_model.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 11: Proper cap tube model using Darcy-Weisbach — L and ID both considered
# R600a | T_cond=40C | Target T_evap=-25C

import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

def cap_tube_pressure_drop(L, D, T_cond_C, refrigerant="R600a", m_dot=0.001):
    T_cond_K   = T_cond_C + 273.15
    P_cond     = CP.PropsSI("P","T",T_cond_K,"Q",0,refrigerant)
    rho_liquid = CP.PropsSI("D","T",T_cond_K,"Q",0,refrigerant)
    mu_liquid  = CP.PropsSI("V","T",T_cond_K,"Q",0,refrigerant)
    A_cross    = np.pi*(D/2)**2
    velocity   = m_dot/(rho_liquid*A_cross)
    Re         = rho_liquid*velocity*D/mu_liquid
    f          = 64/Re if Re < 2300 else 0.316/(Re**0.25)
    delta_P    = f*(L/D)*(rho_liquid*velocity**2/2)
    P_evap_new = P_cond - delta_P
    if P_evap_new <= 0: return None, None
    T_evap_new = CP.PropsSI("T","P",P_evap_new,"Q",1,refrigerant) - 273.15
    return P_evap_new, T_evap_new

def calculate_cycle(T_evap_C, T_cond_C, refrigerant="R600a"):
    T_evap = T_evap_C + 273.15
    T_cond = T_cond_C + 273.15
    P_evap = CP.PropsSI("P","T",T_evap,"Q",1,refrigerant)
    P_cond = CP.PropsSI("P","T",T_cond,"Q",1,refrigerant)
    h1 = CP.PropsSI("H","T",T_evap,"Q",1,refrigerant)
    s1 = CP.PropsSI("S","T",T_evap,"Q",1,refrigerant)
    h2 = CP.PropsSI("H","P",P_cond,"S",s1,refrigerant)
    h3 = CP.PropsSI("H","T",T_cond,"Q",0,refrigerant)
    h4 = h3
    return (h1-h4)/(h2-h1), 100/(h1-h4), h1, h2, h3, h4, P_evap, P_cond

T_cond_C  = 40
diameters = {"0.5mm":0.0005,"0.6mm":0.0006,"0.7mm":0.0007,"0.8mm":0.0008}
L_range   = np.linspace(1.5, 4.5, 30)
m_dot_est = 0.001

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for lbl,D in diameters.items():
    T_list = []
    for L in L_range:
        _,T = cap_tube_pressure_drop(L,D,T_cond_C,m_dot=m_dot_est)
        T_list.append(T)
    plt.plot(L_range,T_list,linewidth=2,label=lbl)
plt.axhline(y=-25,color="gray",linestyle="--",alpha=0.7,label="Target -25C")
plt.xlabel("Cap Tube Length (m)"); plt.ylabel("T_evap (C)")
plt.title("T_evap vs L and ID"); plt.legend(); plt.grid(True,alpha=0.3)

plt.subplot(1,2,2)
for lbl,D in diameters.items():
    COP_list = []
    for L in L_range:
        _,T = cap_tube_pressure_drop(L,D,T_cond_C,m_dot=m_dot_est)
        if T:
            try:
                COP,*_ = calculate_cycle(T,T_cond_C)
                COP_list.append(COP)
            except: COP_list.append(None)
        else: COP_list.append(None)
    plt.plot(L_range,COP_list,linewidth=2,label=lbl)
plt.xlabel("Cap Tube Length (m)"); plt.ylabel("COP")
plt.title("COP vs L and ID"); plt.legend(); plt.grid(True,alpha=0.3)

plt.suptitle("Cap Tube Selection Map — R600a | L and ID Effect",fontweight="bold")
plt.tight_layout()
plt.savefig("day11_captube_LD_model.png",dpi=150)
plt.show()
