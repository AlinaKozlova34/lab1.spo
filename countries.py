import sys
import pickle


class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

    def has_continue(self):
        if self.yes is None and self.no is None:
            return False
        else:
            return True

    def set_yes(self, kid):
        self.yes = kid

    def set_no(self, kid):
        self.no = kid


def check_answer(answer):
    if "да" == answer.lower():
        return True
    elif "нет" == answer.lower():
        return False
    else:
        return None


def ask_question(question):
    question.has_continue = question.has_continue()
    if not question.has_continue:
        print("Ваша страна {}".format(question.question))
        print("Победа! Опрос окончен)")
        return
    print("Вопрос: {}".format(question.question))
    answer = check_answer(sys.stdin.readline().strip())
    if answer is None:
        ask_question(question)
    elif answer:
        ask_question(question.yes)
    else:
        ask_question(question.no)


def create_question(question=None, question_kid=None):
    if question is None:
        print("Введите вопрос")

    elif question_kid == "0":
        print(
            "Введите вопрос или ответ который вы бы сказали, если бы ответили на вопрос {} Да. \n Если вы хотите ввести ответ, то нажмите \"0\"".format(
                question.question))

    else:
        print(
            "Введите вопрос или ответ который вы бы сказали, если бы ответили на вопрос {} Нет. \n Если вы хотите ввести ответ, то нажмите \"0\" ".format(
                question.question))

    one_question = sys.stdin.readline().strip()
    if one_question == "0":
        print("Введите ответ")
        answer = sys.stdin.readline().strip()
        print("Успешно")
        return Node(answer)
    new_question = Node(one_question)
    new_question.set_yes(create_question(new_question, "0"))
    new_question.set_no(create_question(new_question, "1"))
    return new_question


try:
    with open('question_database', 'rb') as f:
        Q = pickle.load(f)
except FileNotFoundError:
    Q = create_question()
    with open('question_database', 'wb') as f:
        pickle.dump(Q, f)
ask_question(Q)
