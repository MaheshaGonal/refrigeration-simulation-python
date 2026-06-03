# day03_ph_diagram.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 3: P-H Diagram saturation dome with isotherms
# Refrigerant: R134a

import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

refrigerant = "R134a"
T_min  = CP.PropsSI("Tmin",  refrigerant) + 5
T_crit = CP.PropsSI("Tcrit", refrigerant) - 0.1
T_range = np.linspace(T_min, T_crit, 300)

h_liq = [CP.PropsSI("H","T",T,"Q",0,refrigerant)/1000 for T in T_range]
P_liq = [CP.PropsSI("P","T",T,"Q",0,refrigerant)/1e5  for T in T_range]
h_vap = [CP.PropsSI("H","T",T,"Q",1,refrigerant)/1000 for T in T_range]
P_vap = [CP.PropsSI("P","T",T,"Q",1,refrigerant)/1e5  for T in T_range]
h_crit = CP.PropsSI("H","T",T_crit,"Q",0,refrigerant)/1000
P_crit = CP.PropsSI("P","T",T_crit,"Q",0,refrigerant)/1e5

fig, ax = plt.subplots(figsize=(10,6))
ax.plot(h_liq, P_liq, "b-", linewidth=2.5, label="Saturated Liquid")
ax.plot(h_vap, P_vap, "r-", linewidth=2.5, label="Saturated Vapour")
ax.plot(h_crit, P_crit, "ko", markersize=9)

for T_C in [-40,-20,0,20,40]:
    T_K = T_C + 273.15
    if T_K < CP.PropsSI("Tcrit", refrigerant):
        P_s = CP.PropsSI("P","T",T_K,"Q",0,refrigerant)/1e5
        h_l = CP.PropsSI("H","T",T_K,"Q",0,refrigerant)/1000
        h_v = CP.PropsSI("H","T",T_K,"Q",1,refrigerant)/1000
        ax.plot([h_l,h_v],[P_s,P_s],"g--",linewidth=0.8,alpha=0.6)
        ax.text(h_v+2, P_s, f"{T_C}C", fontsize=8, color="green", va="center")

ax.set_yscale("log")
ax.set_xlabel("Enthalpy h (kJ/kg)", fontsize=13)
ax.set_ylabel("Pressure P (bar)",   fontsize=13)
ax.set_title("P-H Diagram — R134a", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
ax.grid(True, which="both", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("day03_ph_diagram.png", dpi=150)
plt.show()
