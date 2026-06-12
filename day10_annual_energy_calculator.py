
# day10_annual_energy_calculator.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 10: Full annual energy calculator + BEE star rating
# Combines condenser model + cap tube model + cycle function
# R600a | Parametric scenarios | Sensitivity analysis

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

def get_condensing_temp(T_ambient, Q_cond, U, A):
    return T_ambient + Q_cond/(U*A)

def get_evap_temp(L_cap, L_ref, T_evap_ref_C, T_cond_C, refrigerant):
    P_cond_ref = CP.PropsSI("P","T",T_cond_C+273.15,"Q",1,refrigerant)
    P_evap_ref = CP.PropsSI("P","T",T_evap_ref_C+273.15,"Q",1,refrigerant)
    dP_per_m   = (P_cond_ref - P_evap_ref)/L_ref
    P_evap_new = P_cond_ref - (dP_per_m*L_cap)
    if P_evap_new <= 0: return None
    return CP.PropsSI("T","P",P_evap_new,"Q",1,refrigerant) - 273.15

def get_star_rating(aec):
    if aec > 300:   return 1,"1★"
    elif aec > 250: return 2,"2★"
    elif aec > 200: return 3,"3★"
    elif aec > 160: return 4,"4★"
    else:           return 5,"5★"

def full_annual_energy_calculator(refrigerant="R600a", T_ambient=32,
        A_cond=0.6, L_cap=3.0, Q_load=80, U_cond=20, verbose=True):
    Q_cond   = Q_load + Q_load/2.5
    T_cond_C = get_condensing_temp(T_ambient, Q_cond, U_cond, A_cond)
    if T_cond_C >= 130 or T_cond_C <= T_ambient: return None
    T_evap_C = get_evap_temp(L_cap, 3.0, -25, T_cond_C, refrigerant)
    if T_evap_C is None: return None
    try:
        COP,m_dot,h1,h2,h3,h4,P_evap,P_cond = calculate_cycle(T_evap_C,T_cond_C,refrigerant)
    except: return None
    W_comp = Q_load/COP
    annual_energy = (W_comp*(Q_load/100)*8760)/1000
    stars, star_str = get_star_rating(annual_energy)
    if verbose:
        print(f"T_cond={T_cond_C:.1f}C | T_evap={T_evap_C:.1f}C | COP={COP:.3f} | "
              f"AEC={annual_energy:.1f} kWh | {star_str}")
    return dict(T_cond_C=T_cond_C, T_evap_C=T_evap_C, COP=COP,
                W_comp=W_comp, annual_energy=annual_energy,
                stars=stars, star_str=star_str)

# Run three scenarios
r1 = full_annual_energy_calculator(T_ambient=32, A_cond=0.6)
r2 = full_annual_energy_calculator(T_ambient=42, A_cond=0.35)
r3 = full_annual_energy_calculator(T_ambient=32, A_cond=0.9)
