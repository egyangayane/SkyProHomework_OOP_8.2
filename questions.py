class Question:

    def __init__(self, text, complexity, correct_answer):
        self.text = text
        self.complexity = complexity
        self.correct_answer = correct_answer

        self.question_is_asked = False
        self.user_answer = None
        self.points = [10, 20, 30, 40, 50]



    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points[self.complexity - 1]

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.user_answer == self.correct_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return (f'Вопрос: {self.text} \n'
                f'Сложность: {self.complexity}/5')


    def build_feedback(self):
        """Возвращает пользователю результат в понятном виде, например:
        Ответ верный, получено __ баллов
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов'
        elif not self.is_correct():
            return f'Ответ неверный, верный ответ {self.correct_answer}'



