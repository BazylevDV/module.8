def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if isinstance(numbers, str):
            # Разбиваем строку на числа, игнорируя пробелы и запятые
            numbers = [num.strip() for num in numbers.split(',')]
        elif isinstance(numbers, (int, float)):
            numbers = [numbers]

        if not isinstance(numbers, (list, tuple, set)):
            print("В numbers записан некорректный тип данных")
            return None

        total, incorrect_data = personal_sum(numbers)

        # Вычисляем среднее арифметическое
        if incorrect_data == len(numbers):
            return 0

        average = total / (len(numbers) - incorrect_data) if len(numbers) > incorrect_data else 0

        return average

    except ZeroDivisionError:
        return 0


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать