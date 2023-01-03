import time

def num(seconds):
    while seconds>0:
         mins=int(seconds/60)
         s=int(seconds%60)
         timer=f'{mins}:{s}'
         print(timer)
         seconds-=1
    print('timeup')


seconds=input("enter the time in seconds")
num(int(seconds))      