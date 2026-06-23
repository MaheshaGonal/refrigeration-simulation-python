# Vapour Compression Cycle Simulator

**Author:** Mahesha Gonal | Cooling R&D Engineer | LG Soft India

---

## What This Does

A complete Python-based vapour compression cycle simulator built on CoolProp. Input any refrigerant name, evaporator temperature, and condenser temperature — get full cycle analysis as output.

---

## Features

- P-H diagram with saturation dome + cycle overlay
- COP calculation with real isentropic compressor efficiency
- Subcooling and superheating support (validated on R134a + R600a)
- Multi-refrigerant comparison: R134a, R600a, R290
- Parametric COP vs evaporator temperature plots

---

## Notebooks

| Notebook | Description |
|----------|-------------|
| `day01`–`day07` | Week 1: setup, state points, P-H diagram, COP, parametric study |
| `day08_compressor.ipynb` | Isentropic compressor with efficiency |
| `day09_subcool_superheat.ipynb` | Real cycle with subcooling + superheating |
| `day10_refrigerant_comparison.ipynb` | R134a vs R600a side by side |
| `day11_r290_cycle.ipynb` | R290 (propane) full cycle |
| `day12_multi_refrigerant.ipynb` | COP comparison chart — all 3 refrigerants |
| `day13_superheat_subcooling_r134a_r600a.ipynb` | Superheat/subcooling COP impact — R134a + R600a |

---

## Quick Start

Open any notebook in Google Colab, run Cell 1 (installs CoolProp), then run all cells top to bottom.

---

## Engineering Context

Built by a refrigeration R&D engineer with experience in BEE regulatory testing, compressor selection, and heat exchanger optimization at IFB Industries and LG Soft India. The refrigerant comparison work here maps directly to the global industry transition driven by EU F-Gas regulations phasing out HFCs before 2030.
