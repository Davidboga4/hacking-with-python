# Author is David Boga
# Gmail : spoter49@gmail.com

import threading
from itertools import chain, product
import timeit

start = timeit.default_timer()


class myThread(threading.Thread):
    def __init__(self, charset, num):
        threading.Thread.__init__(self)
        self.charset = charset
        self.num = num

    def run(self):
        a = bruteforce(self.charset, self.num)
        file1 = open("passwordlist2.txt", "a")  # append mode
        for i in a:
            file1.write(str(i) + '\n')
            # print(i)

        file1.close()


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(1, maxlength + 1)))


special_charset = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"
lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_charset = '123456789'
total_charset = special_charset + lower_alpha + upper_alpha + num_charset
# a = bruteforce(total_charset, 12)


# Create new threads
thread1 = myThread(special_charset, 24)
thread2 = myThread(lower_alpha, 24)
thread3 = myThread(upper_alpha, 24)
thread4 = myThread(num_charset, 24)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

stop = timeit.default_timer()
print('Time : ', stop - start)
