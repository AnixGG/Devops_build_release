def go():
    for i in range(100):
        print(i, "*", i, "=", i * i)


def say_meow(n):
    print("Meeeow   " * n)


if __name__ == "__main__":
    print("Hello My Dear friend ^_^ ")
    go()
    print("Bye My Dear friend ^_^ ")
    say_meow(3)
