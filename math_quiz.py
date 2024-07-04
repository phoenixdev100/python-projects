# import random

# def welcome(player_name, champ, highscore):
#     print(f"WELCOME {player_name} TO MATH QUIZ")
#     print("_______________________________")
#     print("_______!! GAME RULES !!_______\n")
#     print("(1) DON'T USE CALCULATOR ")
#     print(f"(2) CHALLENGE TO BREAK {champ}'S HIGHSCORE {highscore}")
#     print("_______________________________")

# # Number generator
# class NumberGenerator:
#     @staticmethod
#     def ones():
#         return random.randint(1, 9)

#     @staticmethod
#     def hundreds():
#         return random.randint(100, 999)

#     @staticmethod
#     def thousands():
#         return random.randint(1000, 9999)

# # Correct/Wrong judge
# class Judge:
#     def __init__(self):
#         self.player_score = 0

#     def correct(self):
#         self.player_score += 10
#         print(f"*CORRECT*\nYour current score is {self.player_score}")
#         return self.player_score

#     def wrong(self):
#         self.player_score -= 10
#         print(f"*WRONG*\nYour current score is {self.player_score}")
#         return self.player_score

# # Operation generator
# class GetOperations:
#     def __init__(self, level, q_no, first_no, second_no, operation, judge):
#         self.first_no = first_no
#         self.second_no = second_no
#         self.operation = operation
#         self.q_no = q_no
#         self.level = level
#         self.judge = judge

#     def question(self):
#         if self.operation == "+":
#             answer = self.first_no + self.second_no
#         elif self.operation == "-":
#             answer = self.first_no - self.second_no
#         elif self.operation == "*":
#             answer = self.first_no * self.second_no
#         elif self.operation == "/":
#             answer = self.first_no / self.second_no
#         else:
#             raise ValueError("Unsupported operation")

#         print(f"{self.q_no}) What is the value of {self.first_no} {self.operation} {self.second_no}?")
#         user_answer = float(input(f"Answer {self.level} {self.q_no}: "))

#         if user_answer == answer:
#             return self.judge.correct()
#         else:
#             return self.judge.wrong()

# # Levels generator
# class GetLevel:
#     def __init__(self, level, q_no, operation, judge):
#         self.level = level
#         self.q_no = q_no
#         self.operation = operation
#         self.judge = judge

#     def second_no(self):
#         if self.operation == "*":
#             return NumberGenerator.ones()
#         else:
#             return NumberGenerator.hundreds()

#     def level_1(self):
#         first_no = NumberGenerator.hundreds()
#         return GetOperations(self.level, self.q_no, first_no, self.second_no(), self.operation, self.judge).question()

# # Example usage
# if __name__ == "__main__":
#     player_name = input("Enter player name: ")
#     champ = "John Doe"
#     highscore = 150

#     welcome(player_name, champ, highscore)

#     judge = Judge()
#     get_level = GetLevel(1, 1, "*", judge)
#     get_level.level_1()


# Without classes and OOPS

import random

def welcome(player_name, champ, highscore):
    print(f"WELCOME {player_name} TO MATH QUIZ")
    print("_______________________________")
    print("_______!! GAME RULES !!_______\n")
    print("(1) DON'T USE CALCULATOR ")
    print(f"(2) CHALLENGE TO BREAK {champ}'S HIGHSCORE {highscore}")
    print("_______________________________")

def ones():
    return random.randint(1, 9)

def hundreds():
    return random.randint(100, 999)

def thousands():
    return random.randint(1000, 9999)

def correct(player_score):
    player_score += 10
    print(f"*CORRECT*\nYour current score is {player_score}")
    return player_score

def wrong(player_score):
    player_score -= 10
    print(f"*WRONG*\nYour current score is {player_score}")
    return player_score

def get_operation_answer(first_no, second_no, operation):
    if operation == "+":
        return first_no + second_no
    elif operation == "-":
        return first_no - second_no
    elif operation == "*":
        return first_no * second_no
    elif operation == "/":
        return first_no / second_no
    else:
        raise ValueError("Unsupported operation")

def ask_question(level, q_no, first_no, second_no, operation, player_score):
    answer = get_operation_answer(first_no, second_no, operation)
    print(f"{q_no}) What is the value of {first_no} {operation} {second_no}?")
    user_answer = float(input(f"Answer {level} {q_no}: "))

    if user_answer == answer:
        return correct(player_score)
    else:
        return wrong(player_score)

def second_no(operation):
    if operation == "*":
        return ones()
    else:
        return hundreds()

def level_1(q_no, operation, player_score):
    first_no = hundreds()
    return ask_question(1, q_no, first_no, second_no(operation), operation, player_score)

if __name__ == "__main__":
    player_name = input("Enter player name: ")
    champ = "Master"
    highscore = 150

    welcome(player_name, champ, highscore)

    player_score = 0
    player_score = level_1(1, "*", player_score)
