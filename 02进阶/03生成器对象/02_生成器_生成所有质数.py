def generate_num():
    yield 1
    i = 2
    while True:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


if __name__ == '__main__':
    g = generate_num()
    num = next(g)
    while num <= 100:
        print(num)
        num = next(g)