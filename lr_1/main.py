import sys
from PyQt6.QtWidgets import QApplication
from interface import UserInterface


def main():
    app = QApplication(sys.argv)
    window = UserInterface()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
