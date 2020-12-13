num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
list = []
if num1 == num2:
    print(num2)
    print("Length: 1")
else:
    while True:
        if num2 % 2 == 0:
            num2 = num2 / 2
            print(int(num2), end=" ")
            list.append(num2)
            if num2 == num1:
                print('\nLength =', len(list)+1)
                break
            elif len(list) > 99:
                print('\nToo many length! Stop')
                break
        else:
            num2 = num2 * 5 + 3
            print(int(num2), end=" ")
            list.append(num2)
            if num2 == num1:
                print('\nLength =', len(list)+1)
                break
            elif len(list) > 99:
                print('\nToo many length! Stop')
                break
