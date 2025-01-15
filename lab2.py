import re
import unittest

math_expression_pattern = r'^[\d\.\+\-\*/\(\)\s]+$'

def is_valid_math_expression(expression: str) -> bool:
    expression = expression.replace(" ", "")
    if re.search(r'[+\-*/]{2,}', expression):
        return False
    return bool(re.match(math_expression_pattern, expression)) and is_balanced_parentheses(expression)

def is_balanced_parentheses(expression: str) -> bool:
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def check_expressions_in_file(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines if is_valid_math_expression(line.strip())]
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

def check_user_expression():
    expression = input("Введите математическое выражение: ").strip()
    if is_valid_math_expression(expression):
        print("Выражение синтаксически корректно.")
    else:
        print("Выражение синтаксически некорректно.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Проверить математическое выражение")
        print("2. Проверить выражения из файла")
        print("3. Выход")
        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            check_user_expression()
        elif choice == '2':
            file_path = input("Введите путь к файлу: ").strip()
            valid_expressions = check_expressions_in_file(file_path)
            if valid_expressions:
                print("Корректные выражения из файла:")
                for expr in valid_expressions:
                    print(expr)
            else:
                print("В файле нет корректных выражений или файл не найден.")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

class TestMathExpression(unittest.TestCase):
    def test_valid_expressions(self):
        valid_expressions = [
            "3 + 5",
            "10 - 2 * (3 + 4)",
            "(5 + 6) * 2",
            "3.5 + 2.1",
            "100 / (50 + 2)"
        ]
        for expr in valid_expressions:
            self.assertTrue(is_valid_math_expression(expr))

    def test_invalid_expressions(self):
        invalid_expressions = [
            "3 ++ 5",
            "10 ** 2",
            "(5 + 6 * 2",
            "100 // 50",
            "1+++2",
            "1++2",
            "1---2",
            "1**2",
            "1***2"
        ]
        for expr in invalid_expressions:
            self.assertFalse(is_valid_math_expression(expr))

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    main()
