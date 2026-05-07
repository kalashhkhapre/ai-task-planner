from typing import TypedDict, List, Dict, Any


class PlannerState(TypedDict):

    goal: str

    refined_goal: str

    tasks: List[str]

    dependencies: List[Dict[str, Any]]

    dag_edges: List[Dict[str, Any]]

    execution_order: List[str]

    parallel_groups: List[List[str]]

    optimized_tasks: List[Dict[str, Any]]

    validation_report: str

    final_workflow: Dict[str, Any]