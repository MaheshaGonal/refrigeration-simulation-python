# day04_cycle_ph.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 4: Full vapour compression cycle overlaid on P-H diagram
# Refrigerant: R134a | T_evap=-20C | T_cond=40C

import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

refrigerant = "R134a"
T_evap = -20 + 273.15
T_cond =  40 + 273.15

P_evap = CP.PropsSI("P","T",T_evap,"Q",1,refrigerant)
P_cond = CP.PropsSI("P","T",T_cond,"Q",1,refrigerant)

h1 = CP.PropsSI("H","P",P_evap,"Q",1,refrigerant)/1000
s1 = CP.PropsSI("S","P",P_evap,"Q",1,refrigerant)
h2 = CP.PropsSI("H","P",P_cond,"S",s1,refrigerant)/1000
h3 = CP.PropsSI("H","P",P_cond,"Q",0,refrigerant)/1000
h4 = h3

COP = (h1-h4)/(h2-h1)
print(f"COP: {COP:.3f}")
print(f"State points: h1={h1:.1f} h2={h2:.1f} h3={h3:.1f} h4={h4:.1f} kJ/kg")
