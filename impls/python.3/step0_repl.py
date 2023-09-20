prompt = 'user> '
def READ(x):
    return x

def EVAL(x):
    return x

def PRINT(x):
    return x

def rep(x):
    return PRINT(EVAL(READ(x)))

def main():
    while True:
        try:
            line = input(prompt)
            print(rep(line))
        except EOFError:
            return

if __name__ == '__main__':
    main()