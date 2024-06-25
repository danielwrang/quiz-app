import copy
import random
import sys
from functools import partial
from PyQt6.QtWidgets import QStackedWidget, QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication, QTimer
from PyQt6.QtGui import QIcon, QScreen

from source.pages.practice_quiz_page import PracticeQuizPage
from source.pages.summary_page import SummaryPage
from source.pages.test_quiz_page import TestQuizPage
from source.pages.welcome_page import WelcomePage

from source.utils.pdf_exporter import export_to_pdf
from source.utils.questions import (load_questions, compute_question_id, key_a, key_b, key_c, key_d, key_e,
                                    key_question, key_options, key_answer, key_rationale)
from source.utils.utils import wrap_too_long_option_text, load_config


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load stylesheet from file
        with open('styles/styles.qss', 'r') as file:
            self.setStyleSheet(file.read())
        self.icon = QIcon('styles/quiz_icon.png')
        self.setWindowIcon(self.icon)

        # Load questions and verify them
        self.all_questions, filename_with_issues_or_none = load_questions()
        if filename_with_issues_or_none:
            error_message = (f'There are errors in the file <i>{filename_with_issues_or_none}</i>.\nNo questions have '
                             f'been loaded. Please fix the issue and restart the program.')
            QMessageBox.warning(self, 'Incorrect format', f'{error_message}')
            sys.exit(1)

        # Load configuration
        self.config = load_config()

        # Countdown timer - for test quiz
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_over = False

        # Setup window
        self.current_question_index = 0
        self.answers = {}
        self.practice_mode = False
        self.init_ui()
        self.show_welcome_page()

    def init_ui(self):
        self.setWindowTitle('Quiz Application')
        self.resize(1200, 800)
        self.center_application_window_on_screen()

        # Initialize all pages
        self.welcome_widget = WelcomePage(len(self.all_questions))
        self.practice_quiz_widget = PracticeQuizPage()
        self.summary_widget = SummaryPage()
        self.test_quiz_widget = TestQuizPage()

        # Setup StackedWidget to hold all pages
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.welcome_widget)
        self.stackedWidget.addWidget(self.practice_quiz_widget)
        self.stackedWidget.addWidget(self.summary_widget)
        self.stackedWidget.addWidget(self.test_quiz_widget)

        # Connect buttons on all pages
        self.init_welcome_page_buttons()
        self.init_practice_quiz_page_buttons()
        self.init_summary_page()
        self.init_test_quiz_page_buttons()

    def init_welcome_page_buttons(self):
        self.welcome_widget.start_quiz_practice_button.clicked.connect(partial(self.start_quiz, practice_mode=True))
        self.welcome_widget.start_quiz_test_button.clicked.connect(partial(self.start_quiz, practice_mode=False))
        self.welcome_widget.export_pdf_button.clicked.connect(self.export_to_pdf)
        self.welcome_widget.exit_button.clicked.connect(self.exit_quiz)

    def init_practice_quiz_page_buttons(self):
        self.practice_quiz_widget.next_button.clicked.connect(self.next_question)
        self.practice_quiz_widget.finish_button.clicked.connect(self.finish_quiz)

    def init_test_quiz_page_buttons(self):
        self.test_quiz_widget.previous_button.clicked.connect(self.previous_question)
        self.test_quiz_widget.next_button.clicked.connect(self.next_question)
        self.test_quiz_widget.finish_button.clicked.connect(self.finish_quiz)

    def init_summary_page(self):
        self.summary_widget.start_over_button.clicked.connect(self.show_welcome_page)
        self.summary_widget.exit_button_summary.clicked.connect(self.exit_quiz)

    def center_application_window_on_screen(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        center_point = screen.center()
        qt_rectangle = self.frameGeometry()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def set_all_options_invisible(self, quiz_widget):
        quiz_widget.option_a.setVisible(False)
        quiz_widget.option_b.setVisible(False)
        quiz_widget.option_c.setVisible(False)
        quiz_widget.option_d.setVisible(False)
        quiz_widget.option_e.setVisible(False)

    def set_all_options_unchecked(self, quiz_widget):
        quiz_widget.option_a.setChecked(False)
        quiz_widget.option_b.setChecked(False)
        quiz_widget.option_c.setChecked(False)
        quiz_widget.option_d.setChecked(False)
        quiz_widget.option_e.setChecked(False)

    def setup_options(self, quiz_widget, question):
        quiz_widget.question_label.setText(f'{self.current_question_index + 1}) {question[key_question]}')
        quiz_widget.question_label.setWordWrap(True)
        if key_a in question[key_options]:
            option_text = wrap_too_long_option_text(question[key_options][key_a])
            quiz_widget.option_a.setText(f'{key_a.upper()}) {option_text}')
            quiz_widget.option_a.setVisible(True)
        if key_b in question[key_options]:
            option_text = wrap_too_long_option_text(question[key_options][key_b])
            quiz_widget.option_b.setText(f'{key_b.upper()}) {option_text}')
            quiz_widget.option_b.setVisible(True)
        if key_c in question[key_options]:
            option_text = wrap_too_long_option_text(question[key_options][key_c])
            quiz_widget.option_c.setText(f'{key_c.upper()}) {option_text}')
            quiz_widget.option_c.setVisible(True)
        if key_d in question[key_options]:
            option_text = wrap_too_long_option_text(question[key_options][key_d])
            quiz_widget.option_d.setText(f'{key_d.upper()}) {option_text}')
            quiz_widget.option_d.setVisible(True)
        if key_e in question[key_options]:
            option_text = wrap_too_long_option_text(question[key_options][key_e])
            quiz_widget.option_e.setText(f'{key_e.upper()}) {option_text}')
            quiz_widget.option_e.setVisible(True)

    def start_quiz(self, practice_mode=False):
        if self.config['shuffle_questions']:
            random.shuffle(self.all_questions)

        self.current_question_index = 0
        self.answers = {}
        self.practice_mode = practice_mode

        if practice_mode:
            self.questions = copy.deepcopy(self.all_questions)
            self.stackedWidget.setCurrentWidget(self.practice_quiz_widget)
        else:
            self.questions = copy.deepcopy(self.all_questions)[:self.config['num_test_questions']]
            self.start_timer()
            self.test_quiz_widget.update_timer_label(self.countdown_time_seconds)
            self.stackedWidget.setCurrentWidget(self.test_quiz_widget)
        self.load_question()

    def start_timer(self):
        self.countdown_time_seconds = self.config['test_quiz_length_minutes'] * 60
        self.timer.start(1000)  # Timer timeout interval in milliseconds

    def update_timer(self):
        if self.countdown_time_seconds > 0:
            self.countdown_time_seconds -= 1
            self.test_quiz_widget.update_timer_label(self.countdown_time_seconds)
        else:
            self.timer.stop()
            self.finish_quiz()

    def _set_checkboxes(self, question_hash, quiz_widget):
        for letter in self.answers[question_hash]:
            if letter == key_a:
                quiz_widget.set_checkbox_a()
            elif letter == key_b:
                quiz_widget.set_checkbox_b()
            elif letter == key_c:
                quiz_widget.set_checkbox_c()
            elif letter == key_d:
                quiz_widget.set_checkbox_d()
            elif letter == key_e:
                quiz_widget.set_checkbox_e()

    def load_question(self):
        quiz_widget = self.stackedWidget.currentWidget()
        self.set_all_options_invisible(quiz_widget)
        not_all_questions_completed = self.current_question_index < len(self.questions)
        if not_all_questions_completed:
            question_number_label = f'Question {self.current_question_index + 1} out of {len(self.questions)}'
            quiz_widget.set_question_number_label(question_number_label)
            question = self.questions[self.current_question_index]
            self.setup_options(quiz_widget, question)
            self.set_all_options_unchecked(quiz_widget)

            # Check if user pressed "previous question", i.e. the user has provided an answer earlier
            question_hash = compute_question_id(question)
            if question_hash in self.answers.keys():
                self._set_checkboxes(question_hash, quiz_widget)

        else:
            self.current_question_index -= 1  # Need to reduce since incremented in "next_question"
            self.finish_quiz()

    def get_answer(self, quiz_widget):
        a_click = quiz_widget.option_a.isChecked()
        b_click = quiz_widget.option_b.isChecked()
        c_click = quiz_widget.option_c.isChecked()
        d_click = quiz_widget.option_d.isChecked()
        e_click = quiz_widget.option_e.isChecked()
        answer = ''
        answer += key_a if a_click else ''
        answer += key_b if b_click else ''
        answer += key_c if c_click else ''
        answer += key_d if d_click else ''
        answer += key_e if e_click else ''
        return answer

    def next_question(self):
        # currentWidget() is either "practice_quiz" or "test_quiz"
        answer = self.get_answer(self.stackedWidget.currentWidget())
        if answer != '':
            question = self.questions[self.current_question_index]
            if self.practice_mode:
                correct_answer = question[key_answer]
                answer_is_correct = 'Correct' if answer == correct_answer else 'Incorrect'
                information_text = f'{answer_is_correct}, the right answer is {correct_answer.upper()}.'
                if key_rationale in question:
                    information_text += f', {question[key_rationale]}'
                QMessageBox.information(self, 'Correcting answer', information_text)

            question_id = compute_question_id(question)
            self.answers[question_id] = answer
            self.current_question_index += 1
            self.load_question()
        else:
            QMessageBox.warning(self, 'Selection required', 'Please select an answer before proceeding.')

    def previous_question(self):
        self.current_question_index -= 1
        self.load_question()

    def finish_quiz(self):
        # Check if user has answered the current questions
        answer = self.get_answer(self.stackedWidget.currentWidget())
        if answer != '':
            question = self.questions[self.current_question_index]
            question_id = compute_question_id(question)
            self.answers[question_id] = answer
            self.current_question_index += 1

        result, summary = self.generate_summary()
        self.summary_widget.result_label.setText(result)
        self.summary_widget.summary_label.setText(summary)
        self.stackedWidget.setCurrentWidget(self.summary_widget)

    def _get_answers_in_text(self, multiletter_answer, question_options):
        answers_text = ''
        for answer_key in multiletter_answer:
            answers_text += f'{question_options[answer_key]}, '
        answers_text = answers_text[:-2]  # Remove trailing ", "
        return answers_text

    def generate_summary(self):
        num_correct_answers = 0
        summary = ''
        num_answered_questions = 0
        for index, question in enumerate(self.questions):
            question_id = compute_question_id(question)
            user_answer = self.answers.get(question_id, '')
            if user_answer != '':
                num_answered_questions += 1
                # Only summarize for questions the user has answered
                question_base = f'Question {index + 1}) {question[key_question]}'
                user_answer_text = self._get_answers_in_text(user_answer, question[key_options])
                correct_answer = question[key_answer]
                if user_answer == correct_answer:
                    num_correct_answers += 1
                    summary += f'{question_base} Correct, {correct_answer.upper()}) {user_answer_text}.'
                else:
                    correct_answer_text = self._get_answers_in_text(correct_answer, question[key_options])
                    summary += (f'{question_base} Incorrect, your answer: {user_answer.upper()}) {user_answer_text}. '
                                f'Correct answer: {correct_answer.upper()}) {correct_answer_text}.')
                summary += '\n\n'
        if num_answered_questions == 0:
            percentage = 0
        else:
            percentage = int(100 * num_correct_answers / num_answered_questions)
        result = f'You answered {num_correct_answers} out of {num_answered_questions} ({percentage} %) questions correctly.'
        return result, summary

    def show_welcome_page(self):
        self.current_question_index = 0
        self.answers = {}
        self.stackedWidget.setCurrentWidget(self.welcome_widget)

    def exit_quiz(self):
        QCoreApplication.quit()

    def export_to_pdf(self):
        result, message = export_to_pdf(self.all_questions, self.config['pdf_include_answer_directly_after_question'])
        QMessageBox.information(self, 'Export to PDF', message)
