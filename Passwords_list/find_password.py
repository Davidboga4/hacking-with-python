# a file named "geek", will be opened with the reading mode. 
file = open('passwordlist1.txt', 'r')
str1 = 'Boga'+'\n'
for i in file:
    if str1 == str(i):
        print('Found Password ', i)
        break
