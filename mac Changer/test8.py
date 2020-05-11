import os
from elevate import elevate


def is_root():

    def remove_newlines(fname):
        flist = open(fname).readlines()
        return [s.rstrip('\n') for s in flist]

    a = remove_newlines("mac.txt")
    v1 = a[0]
    v2 = a[1]
    print(os.system(f'py win_mac_changer_1.py set {v1} {v2}'))
    print(os.system('getmac > getmac.txt'))
    return 1

elevate(show_console=False)
print(" ", is_root())
