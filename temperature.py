def temperature(gradus):                                              #функция перевода градусов цельсия в фаренгейты
    value_fah = ((gradus)*(9/5)) + 32                           #Формула перевода в фаренгейты
    print(f"{gradus} градуса по Цельсию будет {value_fah} градуса по Фаренгейту")

def main():
    gradus = int(input('Введите температуру в цельсиях: '))  
    temperature(gradus)

if __name__ == "__main__":                              #Выполнение кода, если он запущен как самостоятельный файл
    main()