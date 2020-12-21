#!/usr/bin/env python3

import threading
import random
import os
import time

mutex = threading.Lock()
tree = list(open('tree.txt').read().rstrip())

def colored_dot(color):
    if color == 'red':
        return f'\033[91m●\033[0m' #mks  circle red and then clr of term
    if color == 'green':
        return f'\033[92m●\033[0m'
    if color == 'yellow':
        return f'\033[93m●\033[0m'
    if color == 'blue':
        return f'\033[94m●\033[0m'  
    pass

def lights(color, index):
    off = True
    while True:
        for idx in index:
            tree[idx] = colored_dot(color) if off else '●'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()
        
        off = not off

        time.sleep(random.uniform(.5, 1.5))

yellow = []
red = []
blue = []
green = []

for i, c in enumerate(tree):
    if c == 'Y':
        yellow.append(i)
        tree[i] = '●'
    if c == 'R':
        red.append(i)
        tree[i] = '●'
    if c == 'G':
        green.append(i)
        tree[i] = '●'
    if c == 'B':
        blue.append(i)
        tree[i] = '●'   

ty = threading.Thread(target=lights, args=('yellow', yellow))
tr = threading.Thread(target=lights, args=('red', red))
tb = threading.Thread(target=lights, args=('blue', blue))
tg = threading.Thread(target=lights, args=('green', green))

for t in [ ty, tr, tb, tg]:
    t.start()
for t in [ ty, tr, tb, tg]:
    t.join()


#print(''.join(tree), yellow, green, red, blue)
