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

def a2():
    print('____')
    print('|   |')
    print('|  \O/')
    print('|   |')
    print('|  / ')
    print('|_____')

def n2():
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
    print('A popular RPG game')
    if len(correct) == 6:
            print(r)
            print('You Win!')
            break
    if len(wrong) > 0:
        letter = input("guess a letter or word: ")
        if letter == 's':
            if letter not in correct:
                correct.append(letter)
                print('s')
                print('_ _ _ _ _ _')
        elif letter == 'k':
            if letter not in correct:
                correct.append(letter)
                print('  k')
                print('_ _ _ _ _ _')
        elif letter == 'y':
            if letter not in correct:
                correct.append(letter)
                print('    y')
                print('_ _ _ _ _ _')
        elif letter == 'r':
            if letter not in correct:
                correct.append(letter)
                print('      r')
                print('_ _ _ _ _ _')
        elif letter == 'i':
            if letter not in correct:
                correct.append(letter)
                print('        i')
                print('_ _ _ _ _ _')
        elif letter == 'm':
            if letter not in correct:
                correct.append(letter)
                print('          m')
                print('_ _ _ _ _ _')
        elif letter == r:
            print('You win!')
            break
        elif letter not in r:
            print('incorrect!')
            wrong.pop()
            if len(wrong) == 6:
                print(n())
            elif len(wrong) == 5:
                print(a())
            elif len(wrong) == 4:
                print(m())
            elif len(wrong) == 3:
                print(g())
            elif len(wrong) == 2:
                print(n2())
            elif len(wrong) == 1:
                print(a2())            
    else:
        print(h())
        print('You Lose! The word is:')
        print(r)
        break
    
while r == 'civilization':
    print('where people reside')
    if len(correct) == 12:
        print(r)
        print('You Win!')
        break
    if len(wrong) > 0:
        letter = input("guess a letter or word: ")
        if letter == 'c':
            if letter not in correct:
                correct.append(letter)
                print('c')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'i':
            if letter not in correct:
                for i in range(4):
                    correct.append(letter)
                print('  i   i   i       i')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'v':
            if letter not in correct:
                correct.append(letter)
                print('    v')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'l':
            if letter not in correct:
                correct.append(letter)
                print('        l')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'z':
            if letter not in correct:
                correct.append(letter)
                print('            z')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'a':
            if letter not in correct:
                correct.append(letter)
                print('              a')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 't':
            if letter not in correct:
                correct.append(letter)
                print('                t')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'o':
            if letter not in correct:
                correct.append(letter)
                print('                    o')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == 'n':
            if letter not in correct:
                correct.append(letter)
                print('                      n')
                print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif letter == r:
            print('You Win!')
            break
        elif letter not in r:
            print('incorrect')
            wrong.pop()
            if len(wrong) == 6:
                print(n())
            elif len(wrong) == 5:
                print(a())
            elif len(wrong) == 4:
                print(m())
            elif len(wrong) == 3:
                print(g())
            elif len(wrong) == 2:
                print(n2())
            elif len(wrong) == 1:
                print(a2())
    else:
        print(h())
        print('You Lose! The word is:')
        print(r)
        break

while r == 'fantasy':
    print('popular category in literature and other popular media')
    if len(correct) == 7:
        print(r)
        print('You Win')
        break
    if len(wrong) > 0:
        letter = input("Guess a letter or a word: ")
        if letter == 'f':
            if letter not in correct:
                correct.append(letter)
                print('f')
                print('_ _ _ _ _ _ _')
        elif letter == 'a':
            if letter not in correct:
                for i in range(2):
                    correct.append(letter)
                print('  a     a')
                print('_ _ _ _ _ _ _')
        elif letter == 'n':
            if letter not in correct:
                correct.append(letter)
                print('    n')
                print('_ _ _ _ _ _ _')
        elif letter == 't':
            if letter not in correct:
                correct.append(letter)
                print('      t')
                print('_ _ _ _ _ _ _')
        elif letter == 's':
            if letter not in correct:
                correct.append(letter)
                print('          s')
                print('_ _ _ _ _ _ _')
        elif letter == 'y':
            if letter not in correct:
                correct.append(letter)
                print('            y')
                print('_ _ _ _ _ _ _')
        elif letter == r:
            print('You Win')
            break
        elif letter not in r:
            print('incorrect')
            wrong.pop()
            if len(wrong) == 6:
                print(n())
            elif len(wrong) == 5:
                print(a())
            elif len(wrong) == 4:
                print(m())
            elif len(wrong) == 3:
                print(g())
            elif len(wrong) == 2:
                print(n2())
            elif len(wrong) == 1:
                print(a2())
    else:
        print(h())
        print('You Lose! The word is: ')
        print(r)
        break
