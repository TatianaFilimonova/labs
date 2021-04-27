from math import cos, pi, fabs
g = 1.61
M = 2150
U = 3660
a_max = 29.43
m_now = 200

H_0 = 1186
V_0 = 53
alpha = 0
t = 0.001

v = V_0
h = H_0
h_min = -1
M += m_now

def auto(angle, dm, t):
    if angle == 180:
        angle = pi
    else:
        angle = 0
    a = -1 * g - cos(angle) / M * dm * U
    v = V_0 + a * t
    h = H_0 + V_0 * t + a * pow(t, 2) / 2
    return v, h

while h > 0 and m_now > 0:
    if v > 0:
            angle = 0
            dm = (M/U) * (a_max - g)
            m_now -= dm * t
            v, h = auto(angle, dm, t)
    elif v < 0 and h < h_min:
        angle = 180
        dm = (M / U) * (a_max + g)
        m_now -= dm * t
        v, h = auto(angle, dm, t)
    else:
        angle = 180
        dm = 0
        m_now -= dm * t
        v, h = auto(angle, dm, t)
        h_min = pow(v, 2) / (2 * a_max)
    print(
        f"V: {V_0}, H: {H_0}, alpha: {180 - angle}, dm: {dm}, t: {t}")
    V_0, H_0 = v, h
print(f"оставшееся топливо: {m_now}")
