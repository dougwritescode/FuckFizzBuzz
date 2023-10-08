
# Basic FizzBuzz
def FizzBuzz():
    for i in range(1, 16):
        if i % 5 == 0 and i % 3 == 0:
            print(f'{i} FizzBuzz')
        elif i % 5 == 0:
            print(f'{i} Buzz')
        elif i % 3 == 0:
            print(f'{i} Fizz')
        else:
            print(i)


if __name__ == "__main__":
    FizzBuzz()