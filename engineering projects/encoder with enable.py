enable = int(input("enter the enable value:"))
number = input("enter a input value between 0 to 3:")
print(bin(int(number)))
if enable == 0:
    print("output is not enabled,so output y3,y2,y1,y0=000")
else:
    if number == '0':
        y3 = "0001"
        print("output is y3,y2,y1,y0=", y3)
    elif number == '1':
        y2 = "0010"
        print("output is y3,y2,y1,y0=", y2)
    elif number == '2':
        y1 = "0100"
        print("output is y3,y2,y1,y0=", y1)

    elif number == '3':
        y0 = "1000"
        print("output is y3,y2,y1,y0=", y0)