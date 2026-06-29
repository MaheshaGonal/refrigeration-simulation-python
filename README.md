# Refrigeration Simulation Portfolio

**Mahesha Gonal** | Cooling R&D Engineer (IFB Industries → LG Soft India) | 3 granted patents in refrigeration/PCM technology

---

## What this repository is

A complete 21-day, code-first build-up of refrigeration engineering simulation skills — starting from reading a single thermodynamic property, and ending at a general-purpose cycle simulator and BEE star-rating compliance modelling. Every notebook is **runnable in Google Colab** and every notebook's outputs (charts, calculated numbers) are **saved directly in the file**, so you don't need to run any code to see the results — just open a notebook on GitHub and scroll.

Each notebook also includes a short plain-language explanation of what the chart shows and why it matters, so the engineering point comes across even if you don't read Python.

**Refrigerants used throughout:** R134a (HFC, being phased out), R600a (isobutane — used in IFB/LG refrigerators), and R290 (propane — the next-generation natural refrigerant). All simulations use [CoolProp](http://www.coolprop.org/), a free, open-source thermodynamic properties library.

---

## Project 1 — Vapour Compression Cycle Simulator (Days 1–14, 19)

Full cycle simulation for any refrigerant: P-H diagrams, COP analysis, component sizing trade-offs, real (non-ideal) compressor modelling, and a final general-purpose simulator function.

| Notebook | What it shows |
|---|---|
| [`day01_first_property.ipynb`](day01_first_property.ipynb) | Reading boiling point & latent heat for R134a and R600a directly from CoolProp |
| [`day02_state_points.ipynb`](day02_state_points.ipynb) | The four state points of a vapour-compression cycle, and the resulting COP |
| [`day03_ph_diagram.ipynb`](day03_ph_diagram.ipynb) | The Pressure-Enthalpy (P-H) saturation dome — the "map" every cycle is drawn on |
| [`day04_cycle_ph.ipynb`](day04_cycle_ph.ipynb) | The actual refrigeration cycle drawn as a loop on top of the P-H map |
| [`day05_cop_function.ipynb`](day05_cop_function.ipynb) | Turning the cycle math into a reusable function + mass flow rate |
| [`day06_refrigerant_comparison.ipynb`](day06_refrigerant_comparison.ipynb) | COP vs evaporator temperature — R134a vs R600a vs R290 |
| [`day07_ambient_temperature_effect.ipynb`](day07_ambient_temperature_effect.ipynb) | How a hot Indian summer ambient drags down COP and raises annual energy use |
| [`day08_captube_length_effect.ipynb`](day08_captube_length_effect.ipynb) | Capillary tube **length** trade-off: evaporator temp, COP, mass flow |
| [`day09_condenser_sizing_effect.ipynb`](day09_condenser_sizing_effect.ipynb) | Condenser **area** trade-off: diminishing efficiency returns vs material cost |
| [`day10_annual_energy_calculator.ipynb`](day10_annual_energy_calculator.ipynb) | Full calculator combining every model above — same fridge, 3 climates/condensers, 3 different BEE star ratings |
| [`day11_captube_LD_model.ipynb`](day11_captube_LD_model.ipynb) | A proper fluid-mechanics (Darcy-Weisbach) capillary tube model — length **and** bore diameter |
| [`day12_real_compressor_model.ipynb`](day12_real_compressor_model.ipynb) | Back-calculating real isentropic efficiency from a compressor datasheet EER |
| [`day13_superheat_subcooling_r134a_r600a.ipynb`](day13_superheat_subcooling_r134a_r600a.ipynb) | Superheat & subcooling impact on COP — R134a vs R600a |
| [`day14_cop_degradation_dashboard.ipynb`](day14_cop_degradation_dashboard.ipynb) | How much COP every refrigerant loses as condensing temperature climbs through an Indian summer |
| [`day19_refrigeration_simulator.ipynb`](day19_refrigeration_simulator.ipynb) | **Capstone:** one master function — any refrigerant, any condition, full cycle output |

## Project 2 — PCM & Patent-Linked Analysis (Days 15–18, 20)

Phase-change material thermal modelling, defrost-cycle optimization, and BEE compliance — directly recreating the physics behind two of the three granted patents.

| Notebook | What it shows |
|---|---|
| [`day15_pcm_basics.ipynb`](day15_pcm_basics.ipynb) | Phase-change material (PCM) latent-heat storage — why it beats water 3.6x as a thermal buffer |
| [`day16_pcm_integration.ipynb`](day16_pcm_integration.ipynb) | PCM pack improving bottle-cooling response time inside a refrigerator cabin |
| [`day17_defrost_simulation.ipynb`](day17_defrost_simulation.ipynb) | Optimal defrost interval, and the energy a simultaneous cooling/defrosting design eliminates |
| [`day18_bee_energy_analysis.ipynb`](day18_bee_energy_analysis.ipynb) | Official BEE Star Rating Band formula (IS 15750:2006) applied to the simulated annual energy number |
| [`day20_patent_impact_summary.ipynb`](day20_patent_impact_summary.ipynb) | **Capstone:** the four headline patent-linked numbers from Days 15–18, consolidated into one summary |

## Capstone

| Notebook | What it shows |
|---|---|
| [`day21_capstone.ipynb`](day21_capstone.ipynb) | Final wrap: the 21-day arc, the LinkedIn post, and the CV note — kept in the repo itself |

---

## Engineering context

Built by a refrigeration R&D engineer with hands-on experience in BEE regulatory testing, compressor selection, and heat exchanger optimization at IFB Industries and LG Soft India, and three granted patents covering PCM-based cooling, multi-mode air circulation, and simultaneous cooling/defrosting. Days 15–18 and 20 directly recreate the physics behind two of those patents as standalone simulations. The refrigerant comparison work (Days 6, 14) maps directly to the global industry transition away from HFCs like R134a, driven by EU F-Gas regulation and equivalent rules elsewhere.

## Quick start

Open any notebook in Google Colab (the "Open in Colab" badge works on any `.ipynb` file viewed on GitHub), run the first cell (installs CoolProp), then run all cells top to bottom. No local installation needed.
