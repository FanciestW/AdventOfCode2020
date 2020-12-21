import os
import sys
import collections as co
import itertools as it
import operator as op
import functools as ft

dat = co.defaultdict(list)
til = co.defaultdict(list)

def readf():
    data = open(os.path.join(os.path.dirname(__file__), 'input.txt')).read().split('\n\n')
    for b in data:
        b = b.split()
        if b == []:
            continue
        ## top, bottom, left, right
        edges = [ b[2], b[-1],
                ''.join([b[i][0] for i in range(2,len(b))]),
                ''.join([b[i][-1] for i in range(2,len(b))]),
                ]
        dat[b[1][:-1]] = edges

def match():
    ## a all pairs of tiles
    for i in it.permutations(dat.keys(), 2):
        ## match each pair (rotate if necessary)
        #print ('matching', i)
        for m,u in enumerate(dat[i[0]]):
            for n,v in enumerate(dat[i[1]]):
                ## x = rev(u), y = rev(v)
                ## compare (u,v), (u,y), (v,x) (x,y)
                x, y = u[::-1], v[::-1]
                if (u == v):
                    #print (u,v,m,n, 'uvmn')
                    til[i[0]].append(i[1])
                elif (u == y):
                    #print (u,y,m,-n, 'uym-n')
                    til[i[0]].append(i[1])
                elif (x == v):
                    #print (x,v,-m,n, 'xv-mn')
                    til[i[0]].append(i[1])
                elif (x == y):
                    #print (x,y,-m,-n, 'xy-m-n')
                    til[i[0]].append(i[1])

    ## corners have two tiles adjacent to them. rest have > 2
    return (ft.reduce ( op.mul, [int(a) for a in til if len(til[a]) == 2] )  )


readf()
print ('part 1:', match())