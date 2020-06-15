# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:12:30 2020

@author: USER
"""



def init(color,ball):
    for _ in range(len(ball)):
        c=ball.pop()
        if c!=color:
            ball.append(c)
            break
    return ball

def play(color,ball):

    ball=init(color,ball)

    
    return ball.count(color)
    

n=int(input())

ball=list(input())


print(min(play('R',ball[:]),play('R',ball[::-1]),play('B',ball[:]),play('B',ball[::-1])))
