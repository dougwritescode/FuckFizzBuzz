# Function composition FizzBuzz

def func_comp_fizz_buzz():

    def fizz_words(n: int, ):
        outwords = ''
        fbwords = {3: 'Fizz', 5: 'Buzz'}
        for num, word in sorted(fbwords.items(), key=lambda a: a[1]):
            if n % num == 0:
                outwords += word
        return outwords
    
    def fizz_line(n: int, words: str):
        return "{a} {b}".format(a=n, b=words)
    
    for i in range(1, 16):
        print(fizz_line(i, fizz_words(i)))


if __name__ == "__main__":
    func_comp_fizz_buzz()