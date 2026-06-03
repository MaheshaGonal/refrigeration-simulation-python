# day02_state_points.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 2: All 4 state points of a vapour compression cycle
# Refrigerant: R134a | T_evap: -20C | T_cond: 40C

import CoolProp.CoolProp as CP

refrigerant = 'R134a'
T_evap = -20 + 273.15
T_cond = 40 + 273.15

P_evap = CP.PropsSI('P', 'T', T_evap, 'Q', 1, refrigerant)
P_cond = CP.PropsSI('P', 'T', T_cond, 'Q', 1, refrigerant)

h1 = CP.PropsSI('H', 'P', P_evap, 'Q', 1, refrigerant) / 1000
s1 = CP.PropsSI('S', 'P', P_evap, 'Q', 1, refrigerant)
h2 = CP.PropsSI('H', 'P', P_cond, 'S', s1, refrigerant) / 1000
h3 = CP.PropsSI('H', 'P', P_cond, 'Q', 0, refrigerant) / 1000
h4 = h3

Q_evap = h1 - h4
W_comp = h2 - h1
COP = Q_evap / W_comp

print(f"COP: {COP:.3f}")
print(f"Refrigerating effect: {Q_evap:.2f} kJ/kg")
print(f"Compressor work: {W_comp:.2f} kJ/kg")
