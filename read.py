def rl():
    with open('data.txt', 'r') as f:
        d = f.read()
        return d

def cd():
    iv = False
    while not iv:
        uname = str(input("Enter your name: "))
        print()
        if not uname.isalpha():
            print()
            print("------------Please enter a valid name!------------\n")
        else:
            iv = True
    iv = False
    while not iv:
        unum = input("Enter your contact number: ")
        print()
        if not unum.isnumeric() or len(unum) != 10:
            print()
            print("------------Please enter a valid number------------\n")
            continue
        else:
            iv = True
    return uname, unum
