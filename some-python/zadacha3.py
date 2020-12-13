class Robot:
    def __init__(self):
        self.control()

    def move(self):
        moves = input('Enter the move commands: ')
        x = 0
        y = 0
        z = 0
        for letter in moves:
            xMinus = '13579'
            xPlus = '02468'
            zMinus = '!#%&('
            zPlus = '@$^*)'
            if xMinus.find(letter) != -1:
                x -= 1
            elif xPlus.find(letter) != -1:
                x += 1
            elif zMinus.find(letter) != -1:
                z -= 1
            elif zPlus.find(letter) != -1:
                z += 1
            elif letter.isalpha() and letter.islower():
                y -= 1
            elif letter.isalpha() and letter.isupper():
                y += 1
            else:
                continue
        print(f'({x}, {y}, {z})')

    def reverse(self):
        word = input('You say a word: ')
        last_char = word[len(word)-1]
        punctuations = '!?.'
        if punctuations.find(last_char) != -1:
            word = word[:-1]
        else:
            last_char = ''
        print('Robot say a word:', word[::-1] + last_char)

    def control(self):
        action = input('Enter command (m, b, or e): ')
        if action == 'm':
            self.move()
            self.control()
        elif action == 'b':
            self.reverse()
            self.control()
        elif action == 'e':
            print('Good bye!')
        else:
            print('Wrong robot commands!')
            self.control()
    
Robot = Robot()