from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class Node:
    id: int
    name: str


@dataclass
class Edge:
    start_node: Node
    end_node: Node
    distance: float


class TaskType(Enum):
    TRAVELING_SALESMAN = "TRAVELING_SALESMAN"
    SHORTEST_PATH = "SHORTEST_PATH"
    MINIMUM_SPANNING_TREE = "MINIMUM_SPANNING_TREE"
