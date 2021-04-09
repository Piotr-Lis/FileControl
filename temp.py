from file import File

def file_gen():
    with File('plik_tekstowy.py','r') as plik:
        for line in plik:
            yield line

if __name__ == '__main__':

    test_gen = file_gen()
    print(next(test_gen))
    print(next(test_gen))
    print(next(test_gen))

