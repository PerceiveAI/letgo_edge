# LetGo/Edge Modular Orchestrator

**Modular, Phase-Based, Plug-and-Play AI Orchestration**  
Plug in any number of "gears" (phases), handlers (models/tasks), or logic modules.  
Phase-schedule work for ultra-efficient, scalable, auditable AI, workflow, or hardware orchestration.

## Features

- Infinite gears: Any number, any thresholds/phases
- Modular handlers: Use local models, APIs, anything
- Phase scheduling: Gears only fire on their phase (exponential speed/cost win)
- LetEdgeCortex: Register, orchestrate, and route any handler
- Easy benchmarking and analysis

## Installation

```sh
pip install -e .

Usage Example

from letgo_edge.config import gear_configs
from letgo_edge.scheduler import ModularLetGoScheduler

sched = ModularLetGoScheduler(gear_configs)
for tick in range(10):
    sched.tick(f"Query {tick}")

Demo

See demos/phase_ai_demo.py and demos/googol_demo.py for full examples.
Run all tests with:

pytest

Project Structure

letgo_edge/        # Core package

demos/             # Live demo scripts

analysis/          # Plots/visualizations

tests/             # Pytest & regression/perf tests


Authors

Bradley Sheats / Perceive AI
bradley.sheats88@gmail.com

MIT License (or your preferred)

---