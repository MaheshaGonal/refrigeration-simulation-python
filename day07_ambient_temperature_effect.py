
# day07_ambient_temperature_effect.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 7: Effect of ambient temperature on COP, compressor work, annual energy
# Refrigerant: R600a | T_evap = -25C | T_cond = T_ambient + 12C

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

T_evap = -25
refrigerant = "R600a"
T_ambient_range = np.linspace(25, 55, 30)
T_cond_range = T_ambient_range + 12

COP_list, compressor_work_list, annual_energy_list = [], [], []

for T_amb, T_cond in zip(T_ambient_range, T_cond_range):
    try:
        COP, m_dot, h1, h2, h3, h4, P_evap, P_cond = calculate_cycle(T_evap, T_cond, refrigerant)
        W_comp = (h2-h1)/1000
        duty_cycle = 80/100
        W_input = 80/COP
        annual_energy = (W_input * duty_cycle * 8760)/1000
        COP_list.append(COP)
        compressor_work_list.append(W_comp)
        annual_energy_list.append(annual_energy)
    except:
        COP_list.append(None)
        compressor_work_list.append(None)
        annual_energy_list.append(None)

fig, axes = plt.subplots(1, 3, figsize=(15,5))
axes[0].plot(T_ambient_range, COP_list, color="steelblue", linewidth=2)
axes[0].set_title("COP vs Ambient Temp")
axes[0].set_xlabel("Ambient Temp (C)")
axes[0].set_ylabel("COP")
axes[0].grid(True, alpha=0.3)

axes[1].plot(T_ambient_range, compressor_work_list, color="tomato", linewidth=2)
axes[1].set_title("Compressor Work vs Ambient Temp")
axes[1].set_xlabel("Ambient Temp (C)")
axes[1].set_ylabel("Compressor Work (kJ/kg)")
axes[1].grid(True, alpha=0.3)

axes[2].plot(T_ambient_range, annual_energy_list, color="darkorange", linewidth=2)
axes[2].set_title("Annual Energy vs Ambient Temp")
axes[2].set_xlabel("Ambient Temp (C)")
axes[2].set_ylabel("Annual Energy (kWh)")
axes[2].grid(True, alpha=0.3)

fig.suptitle("R600a — Ambient Temperature Effect | T_evap=-25C | Q_load=80W", fontweight="bold")
plt.tight_layout()
plt.savefig("day07_ambient_effect.png", dpi=150)
plt.show()
