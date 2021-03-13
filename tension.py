# -*- coding: utf-8 -*- 
import os
from visual import *
from math import *

scene.range = (15,10,10)
scene.center = (0,0,0)
scene.width = 800
scene.height = 300
 
# Generate Elements (Block, Floor, Wall, Spring)
block1 = box(pos=(-2.5,0,0), size=(2,2,2), color=color.red, opacity=0.8)
bottom_wall = box(pos=(0,-1.25,0), size=(15.5,0.5,7))
wall1 = box(pos=(-7.5,1,0), size=(.5,4,7))
spring1 = helix(pos=(-7.5,0,0), axis=7, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))

x1 = -2  # 초기 위치
v1 = 0.  # 초기 속도
 
k = 20.  # 용수철상수
m = 2.   # 질량
 
#------------------------------------------------------------------
# 애니메이션 코드
#------------------------------------------------------------------
t = 0
dt = 0.01
 
# 데이터 표시할 라벨
label1 = label()
label2 = label()
label3 = label()
label4 = label()
label5 = label()
label6 = label()
label6.pos = bottom_wall.pos + vector (-4, -2.5, 0)
label6.text = "Calculating.."
label7 = label()

 
while True:
    rate(100) # 100 Hz, 초당 100번씩 루프를 돌고 dt=0.01이므로 시간 t는 실제 시간과 일치
    t += dt

    # 운동방정식을 통해 a1을 구하고 v,x로 적분
    a1 = k/m * (0.01-x1)
 
    v1 += a1*dt
 
    x1 += v1*dt
 
    # 블럭 실시간 위치 업데이트
    block1.pos.x = x1 - 2.5
    
    # pos : 스프링 좌측의 좌표
    # axis : 스프링 우측의 좌표

    # 스프링 실시간 위치 업데이트
    spring1.axis = block1.pos.x - wall1.pos.x
 
    label1.pos = bottom_wall.pos + vector(0,-0.5,0)
    label1.text = 't = %.2f s' % t
    label2.pos = bottom_wall.pos + vector(0,-1.5,0)
    label2.text = 'm = %.2f kg' % m
    label3.pos = bottom_wall.pos + vector(0,-2.5,0)
    label3.text = 'k = %.2f N/m' % k
    label4.pos = bottom_wall.pos + vector(5,-2.5, 0)
    label4.text = 'x = %.2f m' % x1
    label5.pos = bottom_wall.pos + vector(9, -2.5, 0)
    Ep = (k * (x1**2))/2

    label5.text = 'Ep = %.2f J' % Ep

    if (Ep >= -0.0001 and Ep <= 0.0001):
        O = x1
        label6.text = "O: %.2f m" % O
    label7.pos = bottom_wall.pos + vector(9, -1.5, 0)
    label7.text = "Ek = %.2f J" % (40-Ep)
    
   