# AsbestosAI-Agent 🧬

**Dene-built fungal bioremediation simulator**  
Gift to Dr. Martin Pritchard & Leeds Beckett bioremed team.

Simulates asbestos fiber degradation using fungal strains (e.g., *Aspergillus niger*).  
20 lines. Runs anywhere. No GPU. No PhD.

---

## What It Does
- **Input**: Strain, days, initial fiber mass  
- **Output**:  
  - `degradation_plot.png` — visual decay curve  
  - `degradation_report.csv` — data table  
  - **Risk Score** — scaled toxin mobility drop  

> *Goal: Help Leeds refine models. Help Baie Verte heal.*

---

## Quick Start

```bash
# 1. Clone & install
git clone https://github.com/lyleantoine-collab/AsbestosAI-Agent.git
cd AsbestosAI-Agent
pip install numpy matplotlib

# 2. Run sim
python asbestos_sim.py --strain Aspergillus_niger --days 180
