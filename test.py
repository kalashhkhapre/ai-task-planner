from app.agents.task_decomposer import TaskDecomposer
from app.agents.dependency_analyzer import DependencyAnalyzer
from app.graph.dag_builder import DAGBuilder
from app.graph.parallel_detector import ParallelTaskDetector

import json

goal = """
Build a full-stack task management SaaS application
with React, FastAPI, PostgreSQL, authentication,
and Stripe payments
"""

# STEP 1 — Task Decomposition
tasks_str = TaskDecomposer.decompose(goal)

tasks_list = json.loads(tasks_str) # type: ignore

print("\nTASKS:\n")
print(tasks_list)

print("\n" + "-" * 50)


# STEP 2 — Dependency Analysis
dependencies_str = DependencyAnalyzer.analyze(tasks_list)

tasks_with_deps = json.loads(dependencies_str) # type: ignore

print("\nDEPENDENCIES:\n")

for task in tasks_with_deps:
    print(task)

print("\n" + "-" * 50)


# STEP 3 — Build DAG
builder = DAGBuilder()

builder.build_graph(tasks_with_deps)

print("\nGRAPH NODES:\n")
print(builder.graph.nodes())

print("\nGRAPH EDGES:\n")
print(builder.graph.edges())

print("\n" + "-" * 50)


# STEP 4 — Detect Parallel Tasks
parallel_phases = ParallelTaskDetector.detect_parallel_tasks(
    tasks_with_deps
)

print("\nPARALLEL EXECUTION PHASES:\n")

for i, phase in enumerate(parallel_phases):

    print(f"Phase {i + 1}")

    for task in phase:
        print(" -", task)

    print()