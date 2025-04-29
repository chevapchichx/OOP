from typing import List
from models import Node, Edge, TaskType


class InputData:
    def __init__(self):
        self.list_of_nodes: List[Node] = []
        self.list_of_edges: List[Edge] = []
        self.selected_task_type: TaskType = None
        self.start_node: Node = None
        self.end_node: Node = None

    def is_valid(self) -> bool:
        if self.selected_task_type == TaskType.SHORTEST_PATH:
            return (len(self.list_of_nodes) > 0 and
                    len(self.list_of_edges) > 0 and
                    self.selected_task_type is not None and
                    self.start_node is not None and
                    self.end_node is not None)
        return (len(self.list_of_nodes) > 0 and
                len(self.list_of_edges) > 0 and
                self.selected_task_type is not None)
