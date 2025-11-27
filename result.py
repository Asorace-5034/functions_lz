import circle                                           #импортируем вссе файлы
import temperature
import sum
import is_even


def main():                                             #вызываем их всех по очереди
    circle.main()
    temperature.main()
    sum.main()
    is_even.main()


if __name__ == "__main__":                              #Выполнение кода, если он запущен как самостоятельный файл
    main()