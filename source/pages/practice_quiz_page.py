from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

from source.pages.base_quiz_page import BaseQuizPage


class PracticeQuizPage(BaseQuizPage):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(15)  # Set margin between buttons
        self.next_button = QPushButton('Next question')
        self.finish_button = QPushButton('Finish quiz')

        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.next_button)
        self.button_layout.addWidget(self.finish_button)
        self.button_layout.addStretch(1)

        # Add all components to the layout
        self.quiz_layout = QVBoxLayout()
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
