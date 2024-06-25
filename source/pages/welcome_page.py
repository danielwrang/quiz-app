from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt


class WelcomePage(QWidget):
    def __init__(self, num_questions):
        super().__init__()
        self.setup_ui(num_questions)

    def setup_ui(self, num_questions):
        self.welcome_label = QLabel('Welcome to the Quiz Application!\n')
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label text
        self.welcome_label.setStyleSheet('font-size: 28px;')  # Override stylesheet settings

        self.number_questions_label = QLabel(f'There are {num_questions} questions available.')
        self.number_questions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label text

        self.start_quiz_practice_button = QPushButton('Start practice quiz')
        self.start_quiz_test_button = QPushButton('Start test quiz')
        self.export_pdf_button = QPushButton('Export questions to PDF')
        self.exit_button = QPushButton('Exit program')

        # Set width for the buttons
        button_fixed_width = 200
        self.start_quiz_practice_button.setFixedWidth(button_fixed_width)
        self.start_quiz_test_button.setFixedWidth(button_fixed_width)
        self.export_pdf_button.setFixedWidth(button_fixed_width)
        self.exit_button.setFixedWidth(button_fixed_width)

        # Create a layout for the buttons and center them horizontally
        self.start_button_layout = QVBoxLayout()
        self.start_button_layout.setSpacing(15)  # Set margin between buttons

        button_container = QHBoxLayout()
        button_container.addStretch(1)
        button_container.addWidget(self.start_quiz_practice_button)
        button_container.addStretch(1)

        button_container2 = QHBoxLayout()
        button_container2.addStretch(1)
        button_container2.addWidget(self.start_quiz_test_button)
        button_container2.addStretch(1)

        button_container3 = QHBoxLayout()
        button_container3.addStretch(1)
        button_container3.addWidget(self.export_pdf_button)
        button_container3.addStretch(1)

        button_container4 = QHBoxLayout()
        button_container4.addStretch(1)
        button_container4.addWidget(self.exit_button)
        button_container4.addStretch(1)

        self.start_button_layout.addLayout(button_container)
        self.start_button_layout.addLayout(button_container2)
        self.start_button_layout.addLayout(button_container3)
        self.start_button_layout.addLayout(button_container4)

        # Add some stretchable space before and after the buttons to center them vertically
        self.welcome_layout = QVBoxLayout()
        self.welcome_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.welcome_layout.addWidget(self.welcome_label)
        self.welcome_layout.addWidget(self.number_questions_label)
        self.welcome_layout.addSpacerItem(
            QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))  # Extra space after the label
        self.welcome_layout.addLayout(self.start_button_layout)
        self.welcome_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(self.welcome_layout)
