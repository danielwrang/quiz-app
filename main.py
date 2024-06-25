import sys
from PyQt6.QtWidgets import QApplication

from source.quiz_app import QuizApp


def main():
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
