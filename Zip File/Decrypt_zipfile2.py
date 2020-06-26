from zipfile import ZipFile
import itertools
import timeit

start = timeit.default_timer()
cnt = 0


def crack(charset='a', length=1):
    chars = charset
    global cnt
    for item in itertools.product(chars, repeat=length):
        cnt += 1
        try:
            ZipFile('myzip.zip').extractall(pwd=bytes(item[0], 'utf-8'))
            return 'cracked'
        except:
            pass


special_charset = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"
lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_charset = '123456789'
multi_alpha = upper_alpha + lower_alpha
lower_num = lower_alpha + num_charset
upper_num = upper_alpha + num_charset
spec_low = special_charset + lower_alpha
spec_upper = special_charset + upper_alpha
spec_num = special_charset + num_charset
total_charset = special_charset + lower_alpha + upper_alpha + num_charset

for i in range(1, 6):
    result = crack(lower_alpha, i)
    print(i)
    if result == 'cracked':
        break

stop = timeit.default_timer()
print('Time : ', stop - start)
