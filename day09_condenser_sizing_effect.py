
# day09_condenser_sizing_effect.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 9: Condenser sizing effect — T_cond, COP, compressor power, annual energy
# R600a | T_evap=-25C | T_ambient=32C | U=20 W/m2K | Q_cond=112W

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

T_ambient=32; T_evap_C=-25; refrigerant="R600a"
Q_load=80; U=20; Q_cond=112; A_ref=0.6

A_range = np.linspace(0.2, 1.5, 30)
T_cond_list=[]; COP_list=[]; compressor_W_list=[]; annual_energy_list=[]

for A in A_range:
    T_cond_C = T_ambient + Q_cond/(U*A)
    if T_cond_C >= 130 or T_cond_C <= T_ambient:
        T_cond_list.append(None); COP_list.append(None)
        compressor_W_list.append(None); annual_energy_list.append(None)
        continue
    try:
        COP,m_dot,h1,h2,h3,h4,P_evap,P_cond = calculate_cycle(T_evap_C,T_cond_C,refrigerant)
        W_comp = Q_load/COP
        annual_energy = (W_comp*(Q_load/100)*8760)/1000
        T_cond_list.append(T_cond_C); COP_list.append(COP)
        compressor_W_list.append(W_comp); annual_energy_list.append(annual_energy)
    except:
        T_cond_list.append(None); COP_list.append(None)
        compressor_W_list.append(None); annual_energy_list.append(None)

fig, axes = plt.subplots(2,2,figsize=(13,9))
plots = [
    (T_cond_list,"tomato","Condensing Temp (C)","Condensing Temp vs Area"),
    (COP_list,"steelblue","COP","COP vs Area"),
    (compressor_W_list,"green","Compressor Power (W)","Compressor Power vs Area"),
    (annual_energy_list,"darkorange","Annual Energy (kWh)","Annual Energy vs Area")
]
for ax,(data,color,ylabel,title) in zip(axes.flat, plots):
    ax.plot(A_range, data, color=color, linewidth=2)
    ax.axvline(x=A_ref,color="gray",linestyle="--",alpha=0.6,label=f"Ref {A_ref}m2")
    ax.set_xlabel("Condenser Area (m2)"); ax.set_ylabel(ylabel)
    ax.set_title(title); ax.legend(fontsize=9); ax.grid(True,alpha=0.3)

fig.suptitle("R600a — Condenser Sizing Effect | T_evap=-25C | T_ambient=32C",
             fontweight="bold")
plt.tight_layout()
plt.savefig("day09_condenser_sizing.png", dpi=150)
plt.show()
