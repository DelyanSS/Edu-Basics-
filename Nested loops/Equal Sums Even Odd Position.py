# 1. входни данни -> 2 цели числа
# 2. всички числа в диапазона на въведените
start_number = int(input())  # началото на диапазона
end_number = int(input())  # края на диапазона
# всички числа в диапазона: [start_number, end_number]

for number in range(start_number, end_number + 1):
    # проверка
    # сумата от цифрите на четни и нечетни позиции да са равни
    # 872345
    hundred_thousands = number // 100000  # стохилядни (1) -> нечетна позиция
    ten_thousands = (number // 10000) % 10  # десетохилядни (2) -> четна позиция
    thousands = (number // 1000) % 10  # хилядни (3) -> нечетна позиция
    hundreds = (number // 100) % 10  # стотици (4) -> четна позиция
    tens = (number // 10) % 10  # десетици (5) -> нечетна позиция
    units = number % 10  # единици (6) -> четна позиция

    sum_even = ten_thousands + hundreds + units
    # сума от цифирите на четни позиции (дестохил + стотици + единици)
    sum_odd = hundred_thousands + thousands + tens
    # сума от цифрите на нечетни позиции (стохил + хилядни + десетици)
    if sum_even == sum_odd:
        print(number, end=" ")