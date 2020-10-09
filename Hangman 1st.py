words = ['civilization', 'fantasy', 'skyrim']
wrong = [1, 2, 3, 4, 5, 6, 7]
correct = []

def h():
    print('____')
    print('|   |')
    print('|  \O/')
    print('|   |')
    print('|  / \ ')
    print('|_____')

def a():
    print('____')
    print('|   |')
    print('|  \O/')
    print('|   |')
    print('|  / ')
    print('|_____')

def n():
    print('____')
    print('|   |')
    print('|  \O/')
    print('|   |')
    print('|')
    print('|_____')

def g():
    print('____')
    print('|   |')
    print('|  \O/')
    print('|')
    print('|')
    print('|_____')

def m():
    print('____')
    print('|   |')
    print('|  \O')
    print('|')
    print('|')
    print('|_____')

def a():
    print('____')
    print('|   |')
    print('|   O')
    print('|')
    print('|')
    print('|_____')

def n():
    print('____')
    print('|   |')
    print('|')
    print('|')
    print('|')
    print('|_____')
    
import random
r = random.choice(words)
print('_ ' * (len(r)))

while r == 'skyrim':
    if len(correct) == 6:
            print(r)
            print('You Win!')
            break
    if len(wrong) > 0:
        letter = input("guess a letter or word: ")
        if letter == 's':
            correct.append(letter)
            print('s')
            print('_ _ _ _ _ _')
        elif letter == 'k':
            correct.append(letter)
            print('  k')
            print('_ _ _ _ _ _')
        elif letter == 'y':
            correct.append(letter)
            print('    y')
            print('_ _ _ _ _ _')
        elif letter == 'r':
            correct.append(letter)
            print('      r')
            print('_ _ _ _ _ _')
        elif letter == 'i':
            correct.append(letter)
            print('        i')
            print('_ _ _ _ _ _')
        elif letter == 'm':
            correct.append(letter)
            print('          m')
            print('_ _ _ _ _ _')
        elif letter == r:
            print('You win!')
            break
        elif letter not in r:
            print('incorrect!')
            print(wrong.pop())
            print("tries")
    else:
        print('You Lose! The word is:')
        print(r)
        break
    
while r == 'civilization':
    if len(correct) == 12:
        print(r)
        print('You Win!')
        break
    if len(wrong) > 0:
        letter = input("guess a letter or word: ")
        if letter == 'c':
            correct.append(letter)
            print('c')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'i':
            for i in range(4):
                correct.append(letter)
            print('  i   i   i       i')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'v':
            correct.append(letter)
            print('    v')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'l':
            correct.append(letter)
            print('        l')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'z':
            correct.append(letter)
            print('            z')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'a':
            correct.append(letter)
            print('              a')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 't':
            correct.append(letter)
            print('                t')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'o':
            correct.append(letter)
            print('                    o')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'n':
            correct.append(letter)
            print('                      n')
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == r:
            print('You Win!')
            break
        elif letter not in r:
            print('incorrect')
            print(wrong.pop())
            print("tries")
    else:
        print('You Lose! The word is:')
        print(r)
        break

while r == 'fantasy':
    if len(correct) == 7:
        print(r)
        print('You Win')
        break
    if len(wrong) > 0:
        letter = input("Guess a letter or a word: ")
        if letter == 'f':
            correct.append(letter)
            print('f')
            print('_ _ _ _ _ _ _')
        elif letter == 'a':
            for i in range(2):
                correct.append(letter)
            print('  a     a')
            print('_ _ _ _ _ _ _')
        elif letter == 'n':
            correct.append(letter)
            print('    n')
            print('_ _ _ _ _ _ _')
        elif letter == 't':
            correct.append(letter)
            print('      t')
            print('_ _ _ _ _ _ _')
        elif letter == 's':
            correct.append(letter)
            print('          s')
            print('_ _ _ _ _ _ _')
        elif letter == 'r':
            correct.append(letter)
            print('            y')
            print('_ _ _ _ _ _ _')
        elif letter == r:
            print('You Win')
            break
        elif letter not in r:
            print('incorrect')
            print(wrong.pop())
            print('tries')
    else:
        print('You Lose! The word is: ')
        print(r)
        break
