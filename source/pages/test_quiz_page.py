from PyQt6.QtWidgets import QCheckBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

from source.pages.base_quiz_page import BaseQuizPage


class TestQuizPage(BaseQuizPage):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Timer label
        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(15)  # Set margin between buttons
        self.previous_button = QPushButton('Previous question')
        self.next_button = QPushButton('Next question')
        self.finish_button = QPushButton('Finish quiz')

        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.previous_button)
        self.button_layout.addWidget(self.next_button)
        self.button_layout.addWidget(self.finish_button)
        self.button_layout.addStretch(1)

        # Add all components to the layout
        self.quiz_layout = QVBoxLayout()
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.quiz_layout.addWidget(self.timer_label)
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.quiz_layout.addWidget(self.question_number_label)
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.quiz_layout.addWidget(self.question_label)
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.quiz_layout.addLayout(self.checkboxes_layout)
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.quiz_layout.addLayout(self.button_layout)
        self.quiz_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Set the layout to the widget
        self.setLayout(self.quiz_layout)

    def update_timer_label(self, total_time_in_seconds):
        hours = total_time_in_seconds // 3600
        minutes = (total_time_in_seconds % 3600) // 60
        seconds = total_time_in_seconds % 60
        time_label = f'{hours:02}:{minutes:02}:{seconds:02}'
        self.timer_label.setText(time_label)
