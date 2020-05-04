# Author David Boga
# Gmail spoter49@gmail.com

from itertools import chain, product
import timeit
start = timeit.default_timer()

def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                     for i in range(1, maxlength + 1)))

special_charset = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"
lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_charset = '123456789'
total_charset = special_charset+lower_alpha+upper_alpha+num_charset
a = bruteforce(total_charset, 2)

file1 = open("passwordlist1.txt", "a")  # append mode
for i in a:
    file1.write(str(i)+'\n')
    # print(i)

file1.close()
stop = timeit.default_timer()
print('Time : ', stop - start)
