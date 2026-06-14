# day12_real_compressor_model.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 12: Real compressor model — EER to isentropic efficiency back-calculation
# R600a | T_cond=40C | T_evap=-23.3C | EER=1.8 | Q=150W

import CoolProp.CoolProp as CP

refrigerant = "R600a"
T_evap_C = -23.3
T_cond_C = 40.0
Q_cooling_W = 150
EER_datasheet = 1.8

W_comp_actual = Q_cooling_W / EER_datasheet

T_evap = T_evap_C + 273.15
T_cond = T_cond_C + 273.15

P_evap = CP.PropsSI("P","T",T_evap,"Q",1,refrigerant)
P_cond = CP.PropsSI("P","T",T_cond,"Q",0,refrigerant)

h1 = CP.PropsSI("H","T",T_evap,"Q",1,refrigerant)
s1 = CP.PropsSI("S","T",T_evap,"Q",1,refrigerant)
h2 = CP.PropsSI("H","P",P_cond,"S",s1,refrigerant)
h3 = CP.PropsSI("H","T",T_cond,"Q",0,refrigerant)
h4 = h3

m_dot = Q_cooling_W / (h1 - h4)
h2_actual = h1 + (W_comp_actual / m_dot)
eta_is = (h2 - h1) / (h2_actual - h1)

COP_ideal = (h1 - h4) / (h2 - h1)
COP_real  = (h1 - h4) / (h2_actual - h1)

print(f"Isentropic Efficiency = {eta_is*100:.2f}%")
print(f"Ideal COP = {COP_ideal:.3f}")
print(f"Real COP  = {COP_real:.3f}")
