
# day11_captube_LD_model.py
# Mahesha Gonal — Refrigeration Simulation Portfolio
# Day 11: Proper cap tube model — Darcy-Weisbach with L and ID
# R600a | T_cond=40C | Target T_evap=-25C
# Fix: diameter-specific mass flow rates for realistic results

import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

def cap_tube_pressure_drop(L, D, T_cond_C, refrigerant="R600a", m_dot=0.001):
    T_cond_K   = T_cond_C + 273.15
    P_cond     = CP.PropsSI("P","T",T_cond_K,"Q",0,refrigerant)
    rho_liquid = CP.PropsSI("D","T",T_cond_K,"Q",0,refrigerant)
    mu_liquid  = CP.PropsSI("V","T",T_cond_K,"Q",0,refrigerant)
    A_cross    = np.pi*(D/2)**2
    velocity   = m_dot/(rho_liquid*A_cross)
    Re         = rho_liquid*velocity*D/mu_liquid
    f          = 64/Re if Re < 2300 else 0.316/(Re**0.25)
    delta_P    = f*(L/D)*(rho_liquid*velocity**2/2)
    P_evap_new = P_cond - delta_P
    if P_evap_new <= 0: return None, None
    T_evap_new = CP.PropsSI("T","P",P_evap_new,"Q",1,refrigerant) - 273.15
    return P_evap_new, T_evap_new

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

# Fixed conditions
T_cond_C    = 40
refrigerant = "R600a"
L_range     = np.linspace(1.5, 4.5, 30)

# Diameter-specific mass flow rates
# Smaller ID carries less flow at realistic pressure drops
diameter_mdot = {
    "0.5mm ID": (0.0005, 0.00040),
    "0.6mm ID": (0.0006, 0.00055),
    "0.7mm ID": (0.0007, 0.00075),
    "0.8mm ID": (0.0008, 0.00100),
}

# ── Chart ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1 — T_evap vs L for each diameter
for label, (D, m_dot) in diameter_mdot.items():
    T_evap_list = []
    for L in L_range:
        _, T_evap = cap_tube_pressure_drop(L, D, T_cond_C, refrigerant, m_dot)
        T_evap_list.append(T_evap)
    axes[0].plot(L_range, T_evap_list, linewidth=2, label=label)

axes[0].axhline(y=-25, color="gray", linestyle="--", alpha=0.7, label="Target -25C")
axes[0].set_xlabel("Cap Tube Length (m)")
axes[0].set_ylabel("Evaporator Temperature (C)")
axes[0].set_title("T_evap vs L and ID | R600a | T_cond=40C")
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# Plot 2 — COP vs L for each diameter
for label, (D, m_dot) in diameter_mdot.items():
    COP_list = []
    for L in L_range:
        _, T_evap = cap_tube_pressure_drop(L, D, T_cond_C, refrigerant, m_dot)
        if T_evap is not None:
            try:
                COP, *_ = calculate_cycle(T_evap, T_cond_C, refrigerant)
                COP_list.append(COP)
            except:
                COP_list.append(None)
        else:
            COP_list.append(None)
    axes[1].plot(L_range, COP_list, linewidth=2, label=label)

axes[1].set_xlabel("Cap Tube Length (m)")
axes[1].set_ylabel("COP")
axes[1].set_title("COP vs L and ID | R600a | T_cond=40C")
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

fig.suptitle("Cap Tube Selection Map — R600a | L and ID Effect",
             fontweight="bold")
plt.tight_layout()
plt.savefig("day11_captube_LD_model.png", dpi=150)
plt.show()

# ── Selection Table ──────────────────────────────────────────
diameter_mdot_table = {
    0.0005: 0.00040,
    0.0006: 0.00055,
    0.0007: 0.00075,
    0.0008: 0.00100,
}

L_fine = np.linspace(1.0, 6.0, 200)

print("=" * 65)
print("  CAP TUBE SELECTION TABLE — R600a")
print("  Target: T_evap = -25C | T_cond = 40C")
print("=" * 65)
print(f"  ID (mm)   Length (m)   T_evap (C)      COP")
print("-" * 65)

for D, m_dot in diameter_mdot_table.items():
    best_L=None; best_T=None; best_COP=None; min_diff=999
    for L in L_fine:
        _, T_evap = cap_tube_pressure_drop(L, D, T_cond_C, refrigerant, m_dot)
        if T_evap is None: continue
        diff = abs(T_evap - (-25))
        if diff < min_diff:
            min_diff=diff; best_L=L; best_T=T_evap
            try:
                COP,*_ = calculate_cycle(T_evap, T_cond_C, refrigerant)
                best_COP = COP
            except: best_COP=None
    if best_L and best_COP:
        print(f"  {D*1000:.1f}mm      {best_L:.2f}m        {best_T:.1f}C        {best_COP:.3f}")

print("=" * 65)
print("  Darcy-Weisbach model | diameter-specific m_dot assumed")
print("=" * 65)
