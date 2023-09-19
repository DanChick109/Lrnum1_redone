def main():
    sides = [3, 7 ,6, 125, 352, 768]
    sides = sorted(sides, reverse=True)

    S_max = 0
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            for k in range(j + 1, len(sides)):  # Оптимизированный перебор
                a, b, c = sides[i], sides[j], sides[k]
                if (a + b > c) and (a + c > b) and (b + c > a):  # Проверка существования треугольника
                    p = (a + b + c) * .5  # Находим полупериметр
                    s = (p * (p - a) * (p - b) * (p - c)) ** .5  # Используем формулу Герона
                    if s > S_max:
                        S_max = s
    print("Максимальная площадь треугольника - {}".format(S_max))


if __name__ == "__main__":
    main()
