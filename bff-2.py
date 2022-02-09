import sys, os

M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
U = ('\x1b[1;95m')
O = ('\x1b[1;96m')

if sys.version[0:3] != "3.1":
  sys.exit("\n%s!%s anda harus menggunakan versi %spython 3.1%s,%s versi python anda sekarang%s:%s %s "%(U,O,H,M,O,M,H,sys.version[0:3]))

if __name__=='__main__':
    try:
        os.system('git pull')
        __import__("cracks").menu()
    except Exception as e:
        exit(str(e))
