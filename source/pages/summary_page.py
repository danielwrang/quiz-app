from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy,
                             QScrollArea)
from PyQt6.QtCore import Qt


class SummaryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Add result text label
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add summary text label
        self.scroll_content_widget = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content_widget)
        self.summary_label = QLabel()
        self.scroll_content_layout.addWidget(self.summary_label)

        # Add scrollable area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content_widget)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add buttons
        self.summary_button_layout = QHBoxLayout()
        self.start_over_button = QPushButton('Return to start page')
        self.exit_button_summary = QPushButton('Exit program')

        self.summary_button_layout.addStretch(1)
        self.summary_button_layout.addWidget(self.start_over_button)
        self.summary_button_layout.addWidget(self.exit_button_summary)
        self.summary_button_layout.addStretch(1)

        # Add all components to the layout
        self.summary_layout = QVBoxLayout(self)
        self.summary_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum))
        self.summary_layout.addWidget(self.result_label)
        self.summary_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum))
        self.summary_layout.addWidget(self.scroll_area)
        self.summary_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum))
        self.summary_layout.addLayout(self.summary_button_layout)
        self.summary_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum))

        # Set the layout to the widget
        self.setLayout(self.summary_layout)
