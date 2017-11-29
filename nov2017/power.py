def pow(x,y):
    if y==0:
        return 1
    else:
        temp = pow(x,int(y/2))
        mult = x if y>0 else 1/x
        if y%2==1:
            return mult * temp * temp
        else:
            return temp * temp

if __name__ == "__main__":
    x = 2
    y = 5
    res = pow(x,y)
    print(res)

    x = 3
    y = -2
    res = pow(x,y)
    print(res)

    x = 1
    y = 0
    res = pow(x,y)
    print(res)