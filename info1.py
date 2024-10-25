def f(x):
    return x*x +1
def obliczenia():
    a = 0
    b = 4
    e=1000
    x = (b-a)/e
    for i in range(e):
        y=f(a+i*x)*x
    return y
print(obliczenia())