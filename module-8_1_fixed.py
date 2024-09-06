def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, str):
            return str(a) + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            return str(a) + str(b)
    except Exception as e:
        return f"Ошибка: {e}"

print(add_everything_up(123.456, 'строка'))  # Ожидаемый результат: '123.456строка'
print(add_everything_up('яблоко', 4215))     # Ожидаемый результат: 'яблоко4215'
print(add_everything_up(123.456, 7))         # Ожидаемый результат: 130.456