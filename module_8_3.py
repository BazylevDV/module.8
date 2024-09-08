class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        # Проверка корректности VIN номера
        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        # Проверка корректности номеров автомобиля
        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

    def __is_valid_vin(self, vin_number):
        return isinstance(vin_number, int)

    def __is_valid_numbers(self, numbers):
        return isinstance(numbers, str)


# Пример выполняемого кода
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')