from langgraph.graph import StateGraph, END

from app.state.planner_state import PlannerState

from app.agents.goal_refiner import GoalAgent
from app.agents.task_decomposer import TaskDecomposer
from app.agents.dependency_analyzer import DependencyAnalyzer
from app.agents.dag_builder_agent import DAGBuilderAgent
from app.agents.optimizer import OptimizerAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.execution_planner import ExecutionPlanner


workflow = StateGraph(PlannerState)

# Nodes
workflow.add_node("goal_agent", GoalAgent.run)
workflow.add_node("task_agent", TaskDecomposer.run)
workflow.add_node("dependency_agent", DependencyAnalyzer.run)
workflow.add_node("dag_builder_agent", DAGBuilderAgent.run)
workflow.add_node("optimizer_agent", OptimizerAgent.run)
workflow.add_node("validation_agent", ValidationAgent.run)
workflow.add_node("execution_planner", ExecutionPlanner.run)

# Flow
workflow.set_entry_point("goal_agent")

workflow.add_edge("goal_agent", "task_agent")
workflow.add_edge("task_agent", "dependency_agent")
workflow.add_edge("dependency_agent", "dag_builder_agent")
workflow.add_edge("dag_builder_agent", "optimizer_agent")
workflow.add_edge("optimizer_agent", "validation_agent")
workflow.add_edge("validation_agent", "execution_planner")
workflow.add_edge("execution_planner", END)

graph = workflow.compile()