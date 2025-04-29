from typing import List, Tuple
import numpy as np
from models import Node, TaskType
from input_data import InputData


class Solution:
    def __init__(self, result_path: List[Node], total_distance: float, extra_info: str = ""):
        self.result_path = result_path
        self.total_distance = total_distance
        self.extra_info = extra_info

    def generate_report(self) -> 'Report':
        base_report = f"Маршурт: {[node.name for node in self.result_path]}\nРасстояние: {self.total_distance}"
        if self.extra_info:
            base_report = f"{self.extra_info}\n{base_report}"
        return Report(base_report)


class Report:
    def __init__(self, text_content: str):
        self.text_content = text_content

    def save_to_file(self, file_path: str):
        with open(file_path, 'w') as f:
            f.write(self.text_content)


class BnBNode:
    def __init__(self, matrix, level, path, bound, vertex):
        self.matrix = matrix
        self.level = level
        self.path = path
        self.bound = bound
        self.vertex = vertex


class TaskSolver:
    def solve(self, input_data):
        if input_data.selected_task_type == TaskType.TRAVELING_SALESMAN:
            return self.__solve_traveling_salesman(input_data)
        elif input_data.selected_task_type == TaskType.SHORTEST_PATH:
            return self.__solve_shortest_path(input_data)
        else:
            return self.__solve_minimum_spanning_tree(input_data)

    def __solve_traveling_salesman(self, input_data: InputData) -> Solution:
        n = len(input_data.list_of_nodes)
        adj_matrix = np.full((n, n), float('inf'))
        for edge in input_data.list_of_edges:
            i = input_data.list_of_nodes.index(edge.start_node)
            j = input_data.list_of_nodes.index(edge.end_node)
            adj_matrix[i][j] = edge.distance
            adj_matrix[j][i] = edge.distance

        reduced_matrix, cost = self._reduce_matrix(adj_matrix.copy())
        root = BnBNode(reduced_matrix, 0, [0], cost, 0)

        best_path = None
        best_cost = float('inf')
        nodes = [root]

        while nodes:
            current = nodes.pop(0)
            if current.level == n - 1:
                current.path.append(0)
                path_cost = current.bound
                if path_cost < best_cost:
                    best_cost = path_cost
                    best_path = current.path
                continue

            for j in range(n):
                if self._is_valid_next(current, j, n):
                    child_matrix = current.matrix.copy()
                    child_bound = current.bound

                    child_bound += current.matrix[current.vertex][j]

                    child_matrix[current.vertex, :] = float('inf')
                    child_matrix[:, j] = float('inf')
                    child_matrix[j][0] = float('inf')

                    reduced_matrix, reduction_cost = self._reduce_matrix(
                        child_matrix)
                    child_bound += reduction_cost

                    if child_bound < best_cost:
                        child_path = current.path.copy()
                        child_path.append(j)
                        child = BnBNode(reduced_matrix, current.level + 1,
                                        child_path, child_bound, j)
                        nodes.append(child)

            nodes.sort(key=lambda x: x.bound)

        result_path = [input_data.list_of_nodes[i] for i in best_path]
        return Solution(result_path, best_cost)

    def _reduce_matrix(self, matrix: np.ndarray) -> Tuple[np.ndarray, float]:
        total_cost = 0
        n = len(matrix)

        for i in range(n):
            min_val = min(matrix[i])
            if min_val != float('inf') and min_val > 0:
                matrix[i] -= min_val
                total_cost += min_val

        for j in range(n):
            min_val = min(matrix[:, j])
            if min_val != float('inf') and min_val > 0:
                matrix[:, j] -= min_val
                total_cost += min_val

        return matrix, total_cost

    def _is_valid_next(self, node: BnBNode, next_vertex: int, n: int) -> bool:
        if next_vertex in node.path:
            return False

        if node.matrix[node.vertex][next_vertex] == float('inf'):
            return False

        return True

    def __solve_shortest_path(self, input_data: InputData) -> Solution:
        n = len(input_data.list_of_nodes)
        start_idx = input_data.list_of_nodes.index(input_data.start_node)
        end_idx = input_data.list_of_nodes.index(input_data.end_node)

        adj_matrix = np.full((n, n), float('inf'))
        for edge in input_data.list_of_edges:
            i = input_data.list_of_nodes.index(edge.start_node)
            j = input_data.list_of_nodes.index(edge.end_node)
            adj_matrix[i][j] = edge.distance
            adj_matrix[j][i] = edge.distance 

        distances = [float('inf')] * n
        distances[start_idx] = 0  
        previous = [None] * n
        visited = [False] * n

        for _ in range(n):
            min_dist = float('inf')
            min_vertex = -1
            for v in range(n):
                if not visited[v] and distances[v] < min_dist:
                    min_dist = distances[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited[min_vertex] = True

            for v in range(n):
                if (not visited[v] and
                    adj_matrix[min_vertex][v] != float('inf') and
                        distances[min_vertex] + adj_matrix[min_vertex][v] < distances[v]):
                    distances[v] = distances[min_vertex] + \
                        adj_matrix[min_vertex][v]
                    previous[v] = min_vertex

        path = []
        current = end_idx  
        while current is not None:
            path.append(input_data.list_of_nodes[current])
            current = previous[current]
        path.reverse()

        return Solution(path, distances[end_idx])

    def __solve_minimum_spanning_tree(self, input_data: InputData) -> Solution:
        sorted_edges = sorted(input_data.list_of_edges, key=lambda x: x.distance)
        
        parent = {node.id: node.id for node in input_data.list_of_nodes}
        
        def find_set(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find_set(parent[vertex])
            return parent[vertex]
        
        def union_sets(vertex1, vertex2):
            parent[find_set(vertex1)] = find_set(vertex2)
        
        mst_edges = []
        total_weight = 0
        
        for edge in sorted_edges:
            if find_set(edge.start_node.id) != find_set(edge.end_node.id):
                union_sets(edge.start_node.id, edge.end_node.id)
                mst_edges.append(edge)
                total_weight += edge.distance
        
        mst_info = "Ребра минимального остовного дерева:\n"
        for edge in mst_edges:
            mst_info += f"{edge.start_node.name} -- {edge.end_node.name} (вес: {edge.distance})\n"
        
        used_nodes = []
        for edge in mst_edges:
            if edge.start_node not in used_nodes:
                used_nodes.append(edge.start_node)
            if edge.end_node not in used_nodes:
                used_nodes.append(edge.end_node)
        
        used_nodes.sort(key=lambda x: x.id)
        return Solution(used_nodes, total_weight, mst_info)
