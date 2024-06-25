import hashlib
import json
import jsonschema
import os


key_question = 'question'
key_options = 'options'
key_answer = 'answer'
key_rationale = 'rationale'

key_a = 'a'
key_b = 'b'
key_c = 'c'
key_d = 'd'
key_e = 'e'


def _load_questions_schema():
    schema_file = 'schema/questions_schema.json'
    with open(schema_file, 'r') as schema_file:
        schema = json.load(schema_file)
        return schema


def _validate_json_against_schema(filename, data, schema):
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as err:
        print(f'Given JSON data for file: {filename} is not valid')
        print(err)
        return False, filename


def _add_one_question():
    question = {"question": "What year was Python released?",
                "options": {
                    "a": "1990",
                    "b": "1991",
                    "c": "1992"
                },
                "answer": "b"}
    return [question]


def load_questions():
    excluded_postfix = '_excluded.json'
    questions_folder = 'questions'

    questions_schema = _load_questions_schema()
    questions = []
    for filename in os.listdir(questions_folder):
        if filename.endswith('.json') and not filename.endswith(excluded_postfix):
            file_path = os.path.join(questions_folder, filename)
            with open(file_path, 'r') as file:
                new_questions = json.load(file)
                success, filename = _validate_json_against_schema(filename, new_questions, questions_schema)
                if not success:
                    return [], filename
                questions += new_questions
    if len(questions) == 0:
        questions = _add_one_question()
    return questions, None


def compute_question_id(question_dict):
    json_str = json.dumps(question_dict, sort_keys=True)
    hash_object = hashlib.sha256(json_str.encode())
    hash_value = int(hash_object.hexdigest(), 16)
    return hash_value
