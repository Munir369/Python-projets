print("enter how many values of your data are (max : 8)")
x = int(input("enter : "))
try:
  match x:
    case 2:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        ab = (a + b)/2
        print(ab)
    case 3:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        ab = (a + b + c)/3
        print(ab)
    case 4:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        d = int(input("enter value number 4 : "))
        ab = (a + b + c + d)/4
        print(ab)
    case 5:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        d = int(input("enter value number 4 : "))
        e = int(input("enter value number 5 : "))
        ab = (a + b + c + d + e)/5
        print(ab)
    case 6:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        d = int(input("enter value number 4 : "))
        e = int(input("enter value number 5 : "))
        f = int(input('enter value number 6 : '))
        ab = (a + b + c + d + e + f)/6
        print(ab)
    case 7:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        d = int(input("enter value number 4 : "))
        e = int(input("enter value number 5 : "))
        f = int(input('enter value number 6 : '))
        g = int(input("enter value number 7 : "))
        ab = (a + b + c + d + e + f + g)/7
        print(ab)
    case 8:
        a = int(input("enter value number 1 : "))
        b = int(input("enter value number 2 : "))
        c = int(input("enter value number 3 : "))
        d = int(input("enter value number 4 : "))
        e = int(input("enter value number 5 : "))
        f = int(input('enter value number 6 : '))
        g = int(input("enter value number 7 : "))
        h = int(input("enter value number 8 : "))
        ab = (a + b + c + d + e + f + g + h)/8    
        print(ab)
except:
        print("What! do you wan't!")
