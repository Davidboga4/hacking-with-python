import pikepdf as p
import itertools
import threading
import timeit
import os

start = timeit.default_timer()
special_charset = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"
lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_charset = '123456789'
multi_alpha = lower_alpha + upper_alpha
lower_num = lower_alpha + num_charset
upper_num = upper_alpha + num_charset
spec_low = special_charset + lower_alpha
spec_upper = special_charset + upper_alpha
spec_num = special_charset + num_charset
total_charset = special_charset + lower_alpha + upper_alpha + num_charset
cnt = 0


def crack(charset='a', length=1):
    global cnt
    for item in itertools.product(charset, repeat=length):
        cnt += 1
        if os.path.exists('one5.pdf'):
            exit()
        try:
            m = p.open('nature-converted-protected.pdf', item[0])  # nature-converted
            print('Password found :', item[0])
            print('Total password :', cnt)
            m.save('one5.pdf')
            return 'cracked'
        except:
            pass


class myThread(threading.Thread):
    def __init__(self, charset, num):
        threading.Thread.__init__(self)
        self.charset = charset
        self.num = num

    def run(self):
        if os.path.exists('one5.pdf'):
            exit()
        result = crack(self.charset, self.num)
        if result == 'cracked':
            exit()


for i in range(5, 6):
    thread1 = myThread(total_charset, i)
    thread1.start()
    thread1.join()
    print('thread', i)

stop = timeit.default_timer()
print('Time : ', stop - start)
