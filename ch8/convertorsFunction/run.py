def temp(c):
    c = float(c)
    f = 9/5 * c + 32
    return f

def hour(m, s):
    m = int(m)
    s = int(s)
    h = m/60 + s / 3600
    return h

c = input("Celcious: ")
f = temp(c)
print(f)

m = input("Enter minutes: ")
s = input("Enter seconds: ")
h = hour(m,s)
print(h)