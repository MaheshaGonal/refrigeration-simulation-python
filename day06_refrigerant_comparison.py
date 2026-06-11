
# day06_refrigerant_comparison.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 6: COP vs Evaporator Temperature
# R134a vs R600a vs R290 | T_cond = 40C | T_evap = -35C to -5C

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

T_cond = 40
refrigerants = ["R134a", "R600a", "R290"]
T_evap_range = np.linspace(-35, -5, 30)

plt.figure(figsize=(10,6))
for ref in refrigerants:
    COP_list = []
    for T_evap in T_evap_range:
        try:
            COP, *_ = calculate_cycle(T_evap, T_cond, ref)
            COP_list.append(COP)
        except:
            COP_list.append(None)
    plt.plot(T_evap_range, COP_list, label=ref, linewidth=2)

plt.xlabel("Evaporator Temperature (C)")
plt.ylabel("COP")
plt.title("COP vs Evaporator Temperature — R134a vs R600a vs R290")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("day06_refrigerant_comparison.png", dpi=150)
plt.show()
