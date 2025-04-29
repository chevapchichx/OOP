from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QTextEdit, QComboBox,
                             QApplication, QLineEdit)
from PyQt6.QtCore import Qt
from models import Node, Edge, TaskType
from input_data import InputData
from solver import TaskSolver, Solution


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_solver = TaskSolver()
        self.ui_user_interface()

    def ui_user_interface(self):
        self.setWindowTitle("Решение задач на графах")
        self.setFixedSize(490, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 10, 10, 10)

        node_label = QLabel("Введите узлы:")
        node_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(node_label)
        self.node_input = QLineEdit()
        self.node_input.setPlaceholderText("Пример: 1,A;2,B;3,C")
        layout.addWidget(self.node_input)

        edge_label = QLabel("Введите ребра и веса:")
        edge_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(edge_label)
        self.edge_input = QLineEdit()
        self.edge_input.setPlaceholderText("Пример: A,B,10;B,C,15;C,A,20")
        layout.addWidget(self.edge_input)

        path_points_layout = QHBoxLayout()

        start_label = QLabel("Начальная точка:")
        start_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_point_input = QLineEdit()
        self.start_point_input.setPlaceholderText("Пример: A")
        self.start_point_input.setFixedWidth(100)
        

        end_label = QLabel("Конечная точка:")
        end_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.end_point_input = QLineEdit()
        self.end_point_input.setPlaceholderText("Пример: C")
        self.end_point_input.setFixedWidth(100)

        for widget in (start_label, self.start_point_input, QLabel("->"), end_label, self.end_point_input):
            path_points_layout.addWidget(widget)
        layout.setSpacing(10)
        layout.addLayout(path_points_layout)

        task_layout = QHBoxLayout()
        task_label = QLabel("Выберите задачу:")
        task_layout.addWidget(task_label)

        self.task_combo = QComboBox()
        self.task_combo.setFixedSize(300, 30)
        self.task_combo.addItems([
            " ",
            "Задача коммивояжера",
            "Кратчайший путь",
            "Минимальное остовное дерево"
        ])
        task_layout.addWidget(self.task_combo, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addLayout(task_layout)

        button_layout = QHBoxLayout()
        self.solve_button = QPushButton("Решить")
        self.save_button = QPushButton("Сохранить")

        for button in (self.solve_button, self.save_button):
            button.setFixedWidth(100)
            button_layout.addWidget(button)

        layout.addLayout(button_layout)

        self.result_text = QTextEdit()
        self.result_text.setFixedHeight(150)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.solve_button.clicked.connect(self.solve_problem)
        self.save_button.clicked.connect(self.save_result)

        self.current_solution = None

    def enter_input_data(self) -> InputData:
        input_data = InputData()

        nodes_text = self.node_input.text().strip()
        if nodes_text:
            node_entries = nodes_text.split(';')
            for entry in node_entries:
                if ',' in entry:
                    id_str, name = entry.split(',')
                    input_data.list_of_nodes.append(
                        Node(int(id_str.strip()), name.strip()))

        edges_text = self.edge_input.text().strip()
        if edges_text:
            edge_entries = edges_text.split(';')
            for entry in edge_entries:
                if ',' in entry:
                    start, end, distance = entry.split(',')
                    start_node = next(
                        (n for n in input_data.list_of_nodes if n.name == start.strip()), None)
                    end_node = next(
                        (n for n in input_data.list_of_nodes if n.name == end.strip()), None)
                    if start_node and end_node:
                        input_data.list_of_edges.append(
                            Edge(start_node, end_node, float(distance.strip())))

        start_point = self.start_point_input.text().strip()
        end_point = self.end_point_input.text().strip()
        input_data.start_node = next(
            (n for n in input_data.list_of_nodes if n.name == start_point), None)
        input_data.end_node = next(
            (n for n in input_data.list_of_nodes if n.name == end_point), None)

        return input_data

    def get_selected_task_type(self) -> TaskType:
        index = self.task_combo.currentIndex()
        return {
            1: TaskType.TRAVELING_SALESMAN,
            2: TaskType.SHORTEST_PATH,
            3: TaskType.MINIMUM_SPANNING_TREE
        }[index]

    def solve_problem(self):
        input_data = self.enter_input_data()
        task_type = self.get_selected_task_type()

        if task_type is None:
            self.result_text.setText("Пожалуйста, выберите тип задачи!")
            return

        input_data.selected_task_type = task_type
        self.current_solution = self.task_solver.solve(input_data)
        self.display_solution(self.current_solution)

    def display_solution(self, solution: Solution):
        result_text = f"Маршрут: {[node.name for node in solution.result_path]}\n"
        result_text += f"Общее расстояние: {solution.total_distance}"
        self.result_text.setText(result_text)

    def save_result(self):
        if self.current_solution:
            report = self.current_solution.generate_report()
            report.save_to_file("result.txt")
            self.result_text.append("\nРезультат сохранен в файл result.txt")
