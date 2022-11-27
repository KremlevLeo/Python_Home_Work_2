# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

def bill_counter(salary, bill):
    count = 0
    while salary >= bill:
        salary -= bill
        count += 1
    print(f'- {count} купюр наминалом {bill}', end= ';\n')
    return salary

 
salary =  int(input("Введите размер зарплаты: "))
bill = (25, 10, 3, 1)
print(f'Для выдачи данной зарплаты Вам понадобиться:')
salary_25 = bill_counter(salary,bill[0])
salary_10 = bill_counter(salary_25,bill[1])
salary_3 = bill_counter(salary_10,bill[2])
salary_1 = bill_counter(salary_3,bill[3])

#Работает но как-то нестабильно врем отв ремени выдает ошибку "ValueError: invalid literal for int() with base 10" например при вводе 12343