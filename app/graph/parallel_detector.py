from collections import deque, defaultdict

class ParallelTaskDetector:

    @staticmethod
    def detect_parallel_tasks(tasks_with_deps):

        graph = defaultdict(list)
        indegree = defaultdict(int)

        # Build graph
        for task in tasks_with_deps:

            task_name = task["task"]

            if task_name not in indegree:
                indegree[task_name] = 0

            for dep in task["depends_on"]:
                graph[dep].append(task_name)
                indegree[task_name] += 1

        # Find starting nodes
        queue = deque()

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        levels = []

        # Kahn's Algorithm
        while queue:

            level_size = len(queue)
            current_level = []

            for _ in range(level_size):

                node = queue.popleft()
                current_level.append(node)

                for neighbor in graph[node]:

                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            levels.append(current_level)

        return levels