import random



def main():
    while True:
        try:
            length = int(input('How many syllables do you want? ').strip())
            style = int(input('Select a region --> 1 - 2 - 3: ').strip())
        except ValueError:
            print('Both name # of syllables and region code need to be an integer.')
        else:
            break
    print(f'Your name is: {name_generator(length, style)}!')
    

def name_generator(len, sty):
    vowles = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    double_vowles = ['aa', 'ee', 'ii', 'oo', 'uu']
    syllables = range(len)
    name = []
    if sty == 1 or sty == 2:
        for _ in syllables:
            match sty:
                case 1: # cvcv
                    name.append(f'{random.choice(consonants)}{random.choice(vowles)}')
                case 2: # vcvc
                    name.append(f'{random.choice(vowles)}{random.choice(consonants)}')
    elif sty == 3:
            match sty:
                case 3: # cvcvvc
                    name.append(f'{random.choice(consonants)}{random.choice(vowles)}{random.choice(consonants)}{random.choice(double_vowles)}{random.choice(consonants)}')                 
                    print('Region 3 can only have 2 syllables.', end=" ")
    return ''.join(name).title()


if __name__ == '__main__':
    main()