from fpdf import FPDF
from source.utils.questions import (key_a, key_b, key_c, key_d, key_e, key_question, key_options, key_answer,
                                    key_rationale)


def export_to_pdf(questions, include_answer_directly_after_question=False):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.multi_cell(0, 10, 'Exported questions')
        pdf.ln()

        answers = []
        for index, question in enumerate(questions):
            question_text = question[key_question]

            pdf.multi_cell(0, 10, f'{index + 1}) {question_text}')

            if key_a in question[key_options]:
                pdf.multi_cell(0, 10, f'{key_a.upper()}) {question[key_options][key_a]}')
            if key_b in question[key_options]:
                pdf.multi_cell(0, 10, f'{key_b.upper()}) {question[key_options][key_b]}')
            if key_c in question[key_options]:
                pdf.multi_cell(0, 10, f'{key_c.upper()}) {question[key_options][key_c]}')
            if key_d in question[key_options]:
                pdf.multi_cell(0, 10, f'{key_d.upper()}) {question[key_options][key_d]}')
            if key_e in question[key_options]:
                pdf.multi_cell(0, 10, f'{key_e.upper()}) {question[key_options][key_e]}')

            answer_text = f'{question[key_answer].upper()}'
            if key_rationale in question.keys():
                answer_text += f', {question[key_rationale]}'
            answers.append(f'{index + 1}) {answer_text}')

            if include_answer_directly_after_question:
                pdf.ln()
                pdf.multi_cell(0, 10, f'{answer_text}')

            pdf.ln()

        pdf.add_page()
        pdf.multi_cell(0, 10, f'Answers')
        pdf.ln()
        for answer in answers:
            pdf.multi_cell(0, 10, f'{answer}')

        filename = 'questions_exported.pdf'
        pdf.output(filename)
        return True, f'Questions have been exported to the file <i>{filename}</i>.'
    except KeyError as e:
        return False, f'Error generating PDF. Key error: missing key {str(e)}.'
    except Exception as e:
        return False, f'Error generating PDF, {str(e)}.'
