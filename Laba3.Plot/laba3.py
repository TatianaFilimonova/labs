from math import cos, sin, pi
import matplotlib.pyplot as plt
g = 1.61
M = 2150
U = 3660
a_max = 29.43
m = 1000
m_now = m

t = 0.1
X_0 = 0
Y_0 = 2
V_0 = 0

y = Y_0
x = 0
vy = 1
vx = 1
V_0X = 0
V_0Y = 0
tay = 0
Ax = 0
Ay = 0

T = []
X = []
Y = []
V = []
A = []

fig = plt.figure()
fig = plt.figure()
def auto(angle, d_m, t):
#    alpha = pi / 2 - angle * pi / 180 # в радианах
    alpha = angle * pi / 180
    ay = -1 * g + sin(alpha) / M * d_m * U
    ax = cos(alpha) / M * d_m * U
    vx = V_0X + ax * t
    vy = V_0Y + ay * t
    x = X_0 + vx * t
    y = Y_0 + vy * t + ay * pow(t, 2) / 2
    return vx, vy, x, y

while x < 250005 and m_now > 0:
    if y < 4505 and 0 <= x < 13000:
        angle = 45
        d_m = (M / U) * (a_max + g)
        m_now -= d_m * t
        vx, vy, x, y = auto(angle, d_m, t)
        Alpha = angle * pi / 180
        Ay = -1 * g + sin(Alpha) / M * d_m * U
        Ax = cos(Alpha) / M * d_m * U
    elif V_0X < 2:
        angle = 90
        d_m = (M / U) * (a_max * 0.7561 + g)
        m_now -= d_m * t
        vx, vy, x, y = auto(angle, d_m, t)
        Alpha = angle * pi / 180
        Ay = -1 * g + sin(Alpha) / M * d_m * U
        Ax = cos(Alpha) / M * d_m * U
        if 249995 < x < 250005 and  y == -2.890222920187778:
            V_0X, V_0Y, X_0, Y_0 = vx, vy, x, y
            Ay = -1 * g + sin(Alpha) / M * d_m * U
            Ax = cos(Alpha) / M * d_m * U
            print(f"Vx: {round(V_0X, 2)}, Vy: {round(V_0Y, 2)}, X: {round(X_0, 2)} Y: {round(Y_0, 2)}, alpha: {90 - angle}, dm: {round(d_m, 2)}, t: {t},")
            break
    elif y < 7400 and x > 244000:
        angle = 160
        d_m = (M / U) * (a_max * 0.95 + g)
        m_now -= d_m * t
        vx, vy, x, y = auto(angle, d_m, t)
        Alpha = angle * pi / 180
        Ay = -1 * g + sin(Alpha) / M * d_m * U
        Ax = cos(Alpha) / M * d_m * U
    elif y >= 4500:
        angle = 45
        d_m = 0
        m_now -= d_m * t
        vx, vy, x, y = auto(angle, d_m, t)
        Alpha = angle * pi / 180
        Ay = -1 * g + sin(Alpha) / M * d_m * U
        Ax = cos(Alpha) / M * d_m * U
    elif V_0X < 1 and V_0Y < -1:
        break

    V_0X, V_0Y, X_0, Y_0 = vx, vy, x, y
    tay += t
    Vz = pow((pow(V_0X, 2) + pow(V_0Y, 2)), 0.5)
    Az = pow((pow(Ax, 2) + pow(Ay, 2)), 0.5)
    T.append(tay)
    V.append(Vz)
    Y.append(Y_0)
    X.append(X_0)
    A.append(Az)
    print(f"Vx: {round(V_0X, 2)}, Vy: {round(V_0Y, 2)}, X: {round(X_0, 2)} Y: {round(Y_0, 2)}, alpha: {90 - angle}, dm: {round(d_m, 2)}, t: {t},")

print(f"Remaining fuel: {round(m_now, 1)}")

fig = plt.figure()
graf1 = plt.plot(T, V)
plt.xlabel("t")
plt.ylabel("V")
plt.title('V = f(t)', fontsize=20, fontname='Times New Roman')
plt.grid(True)
plt.show()
fig.savefig('fig v(t)')

fig = plt.figure()
graf2 = plt.plot(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Y = f(X)', fontsize=20, fontname='Times New Roman')
plt.grid(True)
plt.show()
fig.savefig('fig x(y)')

fig = plt.figure()
graf3 = plt.plot(T, A)
plt.xlabel("X")
plt.ylabel("Y")
plt.title('a = f(t)', fontsize=20, fontname='Times New Roman')
plt.grid(True)
plt.show()
fig.savefig('fig a(t)')