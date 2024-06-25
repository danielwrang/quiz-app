import json
from pathlib import Path


def _find_whitespace_before_index(text, max_index):
    # Start searching backward from the given max_index
    for index in range(max_index, -1, -1):
        if text[index].isspace():
            return index
    # If no whitespace is found before the given max_index, return None
    return None


def wrap_too_long_option_text(option_text):
    # Since QCheckBox doesn't have a "setWordWrap" function, add "\n" if string is too long
    max_index = 80
    if len(option_text) > max_index:
        newline_break_index = _find_whitespace_before_index(option_text, max_index)
        option_text = option_text[:newline_break_index] + "\n" + option_text[newline_break_index + 1:]
    return option_text


def load_config():
    config_filepath = 'config/config.json'
    path = Path(config_filepath)
    if path.exists():
        with open(config_filepath, 'r') as config_file:
            config_raw = json.load(config_file)
            config = {
                'shuffle_questions': config_raw.get('shuffle_questions', True),
                'num_test_questions': config_raw.get('test_quiz', {}).get('number_questions', 10),
                'test_quiz_length_minutes': config_raw.get('test_quiz', {}).get('length_minutes', 10),
                'pdf_include_answer_directly_after_question':
                    config_raw.get('export_pdf', {}).get('include_answer_directly_after_question', False),
            }
            return config
    else:
        config = {
            'shuffle_questions': True,
            'num_test_questions': 10,
            'test_quiz_length_minutes': 10,
            'pdf_include_answer_directly_after_question': False,
        }
        return config
