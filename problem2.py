def problem2(a):
    if a == 0:
        print(a)
    elif a == 1:
        print(a)
    elif a == 2:
        print("1, 3")
    else:
        for i in range(1, a+4, 2):
            print(f"{i}")
    
    
problem2(4)
    