def fizzbuzz():
    for i in range(1,15+1):
        if i% 3 == 0:
            print(f'{i}th num is fizz')
        elif i%5 == 0:
            print(f'{i}th num is buzz')
        else:
            print(f'{i}th')

if __name__ == '__main__':
    fizzbuzz()
