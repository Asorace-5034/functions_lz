def Sum(spisok, a=0):                               #функция подсчета суммы набора чисел
    spisok.split()
    for i in spisok:                                #Проходит по всем элементам
        if i == ' ':
            pass
        else:
            a += int(i)
    print("Сумма списка равна:", a)

def main():                                         # функция вывода
    spisok = input('Введите через пробел числа: ')
    Sum(spisok)

if __name__ == '__main__':
    main()


