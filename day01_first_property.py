# day01_first_property.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 1: Extracting thermodynamic properties using CoolProp
# Run in Google Colab: !pip install coolprop

import CoolProp.CoolProp as CP

# --- R134a at 1 bar evaporator pressure ---
P_evap = 1e5  # 1 bar in Pascals

T_sat = CP.PropsSI('T', 'P', P_evap, 'Q', 0, 'R134a')
print(f"R134a saturation temp at 1 bar:   {T_sat - 273.15:.2f} C")

h_liq = CP.PropsSI('H', 'P', P_evap, 'Q', 0, 'R134a')
print(f"Enthalpy saturated liquid (h4):   {h_liq/1000:.2f} kJ/kg")

h_vap = CP.PropsSI('H', 'P', P_evap, 'Q', 1, 'R134a')
print(f"Enthalpy saturated vapour (h1):   {h_vap/1000:.2f} kJ/kg")

latent = (h_vap - h_liq) / 1000
print(f"Latent heat of vaporisation:      {latent:.2f} kJ/kg")

# --- R134a vs R600a comparison ---
refrigerants = ['R134a', 'R600a']
print(f"\n{'Refrigerant':<12} {'T_sat (C)':<12} {'Latent (kJ/kg)'}")
print("-" * 38)
for ref in refrigerants:
    T = CP.PropsSI('T', 'P', 1e5, 'Q', 0, ref) - 273.15
    h_l = CP.PropsSI('H', 'P', 1e5, 'Q', 0, ref) / 1000
    h_v = CP.PropsSI('H', 'P', 1e5, 'Q', 1, ref) / 1000
    print(f"{ref:<12} {T:<12.2f} {h_v - h_l:.2f}")
