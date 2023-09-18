def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = (b ** 2 - 4 * a * c)
    d_sqrt = 0
    if d > 0:
        d_sqrt = d ** .5
        x1 = (-b + d_sqrt) / 2 * a
        x2 = (-b + d_sqrt) / 2 * a
        print(x1, x2)
    if d == 0:
        x = -b / 2 * a
        print(x)
    if d < 0:
        print('net korney')


if __name__ == "__main__":
    main()
