import random

def dice_roller():
    while True: 
        try:
            roll_quantity = int(input('How many rolls do you need-> #').strip())
        except:
                print('please try again')
        else:
                break
    for _ in range(roll_quantity):
        while True:
            try: 
                dice_size = int(input('Select a dice size-> d:').strip())
            except:
                print('please try again')
            else:
                break
        print(f'd{dice_size}: {random.randint(1, dice_size)}')

if __name__ == '__main__':
    dice_roller()