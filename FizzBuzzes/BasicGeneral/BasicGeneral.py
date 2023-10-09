
# Generalized basic FizzBuzz
def fizz_buzz_general(n: int = 15, d: dict = {3: 'Fizz', 5: 'Buzz'}):
    for i in range(1, n + 1):
        wordlist = [d[k] for k in filter(lambda a: i % a == 0, d.keys())]
        print(f"{i} {''.join(wordlist)}")


if __name__ == "__main__":
    fizz_buzz_general()