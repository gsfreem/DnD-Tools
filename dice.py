import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)
dice_case = [4, 6, 8, 10, 12, 20, 100,]

def main():
    print('Pick a dice to roll. When you are done type 0 to exit.')
    while True:
        try:
            selected_dice = int(input('d: ').strip().lower())
            if selected_dice == 0:
                raise SyntaxError
            elif selected_dice not in dice_case:
                raise ValueError
        except ValueError:
            print('Dice not available')
        except SyntaxError:
            break
        else:
            match selected_dice:
                case 4:
                    print(d4.roll())
                case 6:
                    print(d6.roll())                       
                case 8:
                    print(d8.roll())                     
                case 10:
                    print(d10.roll())                    
                case 12:
                    print(d12.roll())                    
                case 20:
                    print(d20.roll()) 
                case 100:
                    print(d100.roll())

if __name__ == "__main__":
    main()