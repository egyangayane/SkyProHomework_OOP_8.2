from utils import load_questions, build_statistics
from random import shuffle

if __name__ == '__main__':
    filename = 'questions.json'
    questions = load_questions(filename)

    shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Введите ваш ответ: ')
        question.user_answer = user_answer
        print(question.build_feedback())
        print()

    print(build_statistics(questions))
