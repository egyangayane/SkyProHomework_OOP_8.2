import json

from questions import Question


def load_questions(filename):
    """Получает данные из json-файла и обрабатывает
    полученные данные, формируя список вопросов
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item['q']
        complexity = int(item['d'])
        correct_answer = item['a']
        question = Question(text=text, complexity=complexity, correct_answer=correct_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    """Возвращает пользователю статистику
    в конце программы (после ответа на все вопросы)
    """
    score, count = 0, 0

    for question in questions:
        if question.is_correct():
            count += 1
            score += question.get_points()

    return f'Вот и всё! \n' \
           f'Отвечено {count} вопроса из 10 \n' \
           f'Набрано баллов: {score}'
