from PyQt6.QtWidgets import QCheckBox, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class BaseQuizPage(QWidget):
    def __init__(self):
        super().__init__()

        # Checkboxes
        self.option_a = QCheckBox()
        self.option_b = QCheckBox()
        self.option_c = QCheckBox()
        self.option_d = QCheckBox()
        self.option_e = QCheckBox()

        # Checkbox layout
        self.checkboxes_layout = QVBoxLayout()
        self.checkboxes_layout.setSpacing(20)  # Set margin between options
        self.checkboxes_layout.addWidget(self.option_a)
        self.checkboxes_layout.addWidget(self.option_b)
        self.checkboxes_layout.addWidget(self.option_c)
        self.checkboxes_layout.addWidget(self.option_d)
        self.checkboxes_layout.addWidget(self.option_e)
        self.checkboxes_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Question number label
        self.question_number_label = QLabel()
        self.question_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Question label
        self.question_label = QLabel()
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_question_number_label(self, text):
        self.question_number_label.setText(text)

    def set_checkbox_a(self):
        self.option_a.setChecked(True)

    def set_checkbox_b(self):
        self.option_b.setChecked(True)

    def set_checkbox_c(self):
        self.option_c.setChecked(True)

    def set_checkbox_d(self):
        self.option_d.setChecked(True)

    def set_checkbox_e(self):
        self.option_e.setChecked(True)
