"""
interpreter_script.py

This script demonstrates the use of StringInterpreter and TernaryInterpreter classes to
interpret user input and print the results.

Usage:
    $ python interpreter_script.py

Author:
    [Your Name]

Date:
    [Current Date]
"""

from hw1.string_to_dict_interpreter import StringInterpreter as Si
from hw1.ternary_operator_practice import TernaryInterpreter as Ti


def run_interpreter(interpreter):
    """
    Runs the specified interpreter and prints the result.

    Parameters:
        interpreter: An instance of the interpreter class.

    Returns:
        None
    """
    print(interpreter.get_result())


if __name__ == '__main__':
    # 1
    # Prompt the user to enter a string
    user_string = input("Enter string:")
    run_interpreter(Si(user_string))

    # 2
    # Prompt the user to enter X and Y
    user_x = input("Enter X:")
    user_y = input("Enter Y:")
    run_interpreter(Ti(user_x, user_y))

# Task 1
# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if name == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації
#
# Task 2
# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"documentate