
# day08_captube_length_effect.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 8: Capillary tube length effect on evaporator temp, COP, mass flow rate
# Refrigerant: R600a | T_cond = 40C | Reference L = 3.0m

import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

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
    COP = (h1-h4)/(h2-h1)
    m_dot = 100/(h1-h4)
    return COP, m_dot, h1, h2, h3, h4, P_evap, P_cond

T_cond_C = 40
T_evap_ref = -25
refrigerant = "R600a"

P_cond_ref = CP.PropsSI("P","T",T_cond_C+273.15,"Q",1,refrigerant)
P_evap_ref = CP.PropsSI("P","T",T_evap_ref+273.15,"Q",1,refrigerant)
L_ref = 3.0
dP_per_meter = (P_cond_ref - P_evap_ref) / L_ref

L_range = np.linspace(1.5, 5.0, 30)
COP_list, T_evap_list, m_dot_list, P_evap_list = [], [], [], []

for L in L_range:
    P_evap_new = P_cond_ref - (dP_per_meter * L)
    if P_evap_new <= 0:
        COP_list.append(None); T_evap_list.append(None)
        m_dot_list.append(None); P_evap_list.append(None)
        continue
    T_evap_new_C = CP.PropsSI("T","P",P_evap_new,"Q",1,refrigerant) - 273.15
    try:
        COP, m_dot, h1, h2, h3, h4, P_evap, P_cond = calculate_cycle(T_evap_new_C, T_cond_C, refrigerant)
        COP_list.append(COP)
        T_evap_list.append(T_evap_new_C)
        m_dot_list.append(m_dot*1000)
        P_evap_list.append(P_evap_new/1e5)
    except:
        COP_list.append(None); T_evap_list.append(None)
        m_dot_list.append(None); P_evap_list.append(None)

fig, axes = plt.subplots(2, 2, figsize=(13,9))
axes[0,0].plot(L_range, T_evap_list, color="steelblue", linewidth=2)
axes[0,0].axvline(x=3.0, color="gray", linestyle="--", alpha=0.6)
axes[0,0].set_title("Evaporator Temp vs Cap Tube Length")
axes[0,0].set_xlabel("Cap Tube Length (m)"); axes[0,0].set_ylabel("T_evap (C)")
axes[0,0].grid(True, alpha=0.3)

axes[0,1].plot(L_range, COP_list, color="green", linewidth=2)
axes[0,1].axvline(x=3.0, color="gray", linestyle="--", alpha=0.6)
axes[0,1].set_title("COP vs Cap Tube Length")
axes[0,1].set_xlabel("Cap Tube Length (m)"); axes[0,1].set_ylabel("COP")
axes[0,1].grid(True, alpha=0.3)

axes[1,0].plot(L_range, m_dot_list, color="tomato", linewidth=2)
axes[1,0].axvline(x=3.0, color="gray", linestyle="--", alpha=0.6)
axes[1,0].set_title("Mass Flow Rate vs Cap Tube Length")
axes[1,0].set_xlabel("Cap Tube Length (m)"); axes[1,0].set_ylabel("m_dot (g/s)")
axes[1,0].grid(True, alpha=0.3)

axes[1,1].plot(L_range, P_evap_list, color="darkorange", linewidth=2)
axes[1,1].axvline(x=3.0, color="gray", linestyle="--", alpha=0.6)
axes[1,1].set_title("Evaporator Pressure vs Cap Tube Length")
axes[1,1].set_xlabel("Cap Tube Length (m)"); axes[1,1].set_ylabel("P_evap (bar)")
axes[1,1].grid(True, alpha=0.3)

fig.suptitle("R600a — Capillary Tube Length Effect | T_cond=40C | Ref L=3.0m", fontweight="bold")
plt.tight_layout()
plt.savefig("day08_captube_effect.png", dpi=150)
plt.show()
