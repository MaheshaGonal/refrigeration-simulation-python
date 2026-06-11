
# day05_cop_function.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 5: COP function + Mass Flow Rate calculator
# Refrigerant: R600a | T_evap=-25C | T_cond=40C

import CoolProp.CoolProp as CP

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
    COP   = (h1-h4)/(h2-h1)
    m_dot = 100/(h1-h4)
    return COP, m_dot, h1, h2, h3, h4, P_evap, P_cond

COP, m_dot, h1, h2, h3, h4, P_evap, P_cond = calculate_cycle(-25, 40)
print(f"COP: {COP:.3f} | m_dot: {m_dot*1000:.4f} g/s")
