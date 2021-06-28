import matplotlib.pyplot as plt
import math
import numpy

# diketahui

m = 0.15
v0 = 50
teta = math.radians(35)
sin = math.sin(teta)
cos = math.cos(teta)
d = 0.0013
delta_t = 0.01
g = 9.806
t = 0

# analitik; mengabaikan hambatan udara

ax = 0
ay = -g

x_arr1 = []
y_arr1 = []

while (y >= 0):
    
    xtemp = x2+(cos*v0)*t+1/2*ax*t*t
    ytemp = y2+(sin*v0)*t+1/2*ay*t*t
    x_arr1.append(xtemp)
    y_arr1.append(ytemp)
    t = t + 0.01

# analitik; mempertimbangkan hambatan udara

vx = cos*v0
vy = sin*v0

ax = -(D/m)*v0*vx
ay = -g-(D/m)*v0*vy

x_arr2 = []
y_arr2 = []

while ( y >= 0 ):
    xtemp = x2+(cos*v0)*t+1/2*ax*t*t
    ytemp = y2+(sin*v0)*t+1/2*ay*t*t
    y_arr2.append(ytemp)
    x_arr2.append(xtemp)
    t = t + 0.01

# numerik; mengabaikan hambatan udara

t = 0
ax = 0
ay = -g

vx = cos*v0
vy = sin*v0

x_arr3 = []
y_arr3 = []

while (y >= 0):
    vy = vy+ay*delta_t
    vx = vx+ax*delta_t
    y = y+vy*delta_t
    x = x+vx*delta_t
    y_arr3.append(y)
    x_arr3.append(x)
    t = t+delta_t

fig, ax = plt.subplots(1,figsize=(8,6))
fig.suptitle('Parabolic')
ax.plot(x_arr1, y_arr1, c='b', label='analitik mengabaikan hambatan')
ax.plot(x_arr2, y_arr2, c='r', label='analitik dengan hambatan')
ax.plot(x_arr3,y_arr3, c = "g", label = "numerik mengabaikan hambatan")
plt.legend()
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()