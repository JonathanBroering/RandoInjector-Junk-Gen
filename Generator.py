import random
print('This is a free Project by Jonathan B. (jnthn-b). It is licenced under the MIT License.')
amount = input('Enter the Amount of Junk Blocks: ')
count = 0

while int(float(amount)) > count:
    randomint = random.randint(1,99)
    if randomint <= 9:
        randomint = str(randomint)
        randomint = '0' + randomint
    print('__asm _emit 0x' + str(randomint) + ' \\')
    count = count + 1

print("done.")
input()
