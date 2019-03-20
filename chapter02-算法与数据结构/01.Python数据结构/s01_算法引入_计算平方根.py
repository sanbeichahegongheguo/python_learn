def sqrt(x):
    y = 1.0
    while abs(y*y-x) > 1e-6:
        y = (y + x/y)/2
    return y

if __name__ == '__main__':
    m = sqrt(16)
    print(m)
