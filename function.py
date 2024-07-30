import read
import write

def dsp():
    sl = read.rl()
    print()
    print("-" * 80)
    print("Kitta".ljust(10, ' '), "City".ljust(13, ' '), "Anna".ljust(12, ' '), "Price".ljust(9, ' '), "Availability Status")
    print("-" * 80)
    for itm in sl.split('\n'):
        dt = itm.strip().split(',')
        if len(dt) == 6:
            print(f"{dt[0]: <10}{dt[1]:<13} {dt[3]:<9}  {dt[4]:<12}  {dt[5]}")
    print("-" * 80)

def rd(data):
    while True:
        rd = input("Enter the duration of rent: ")
        if not rd.isdigit():
            print("------------Invalid input. Please enter a valid duration.------------\n")
            continue
        data.append(rd)
        tp = int(rd) * int(data[4])
        data.append(tp)
        print()
        print("Your total is: Rs.", tp)

        with open('data.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                ld = line.strip().split(',')
                if ld[0] == data[0]:
                    ld[5] = "Unavailable"
                    line = ','.join(ld) + '\n'
                f.write(line)
            f.truncate()
        break
    return data

def rlnd():
    while True:
        print()
        kn = input("Enter the kitta number: ")
        if not kn.isdigit() or int(kn) < 100 or int(kn) > 999:
            print("Invalid Kitta number. Please enter a valid number")
            continue
        with open('data.txt', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                kn = int(kn)
                if int(data[0]) == kn:
                    if data[5].strip().lower() == "available":
                        print()
                        print("Land available for renting, please continue")
                        name, num = read.cd()
                        data.append(name)
                        data.append(num)
                        return data
                    else:
                        print("Land not available for renting. Try again!")
                        break

def rdur(data):
    while True:
        ird = input("Enter the initial duration of rent: ")
        if not ird.isdigit():
            print("Invalid duration.")
            continue

        ard = input("Enter the actual return duration: ")
        if not ard.isdigit():
            print("Invalid return duration")
            continue

        ird = int(ird)
        ard = int(ard)

        data.append(ird)
        data.append(ard)

        tp = ird * int(data[4])
        data.append(tp)

        if ard > ird:
            ld = ard - ird
            lf = ld * (int(data[4]) * 0.1)
            tp += lf
            print()
            print("Your total price is: Rs.", tp)
            print("Your late fee is: Rs.", lf)
            print()
        else:
            print()
            print("Your total price is: Rs.", tp)
            print()

        with open('data.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                ld = line.strip().split(',')
                if ld[0] == data[0]:
                    ld[5] = "Available"
                    line = ','.join(ld) + '\n'
                f.write(line)
            f.truncate()
        break
    return data

def rtnd():
    while True:
        kn = input("Enter the kitta number: ")
        if not kn.isdigit():
            print("Invalid Kitta number")
            continue
        with open('data.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for i, line in enumerate(lines):
                data = line.strip().split(',')
                if int(data[0]) == int(kn):
                    if data[5].strip().lower() == "unavailable":
                        print("The land is available for renting.")
                        name, num = read.cd()
                        data.append(name)
                        data.append(num)
                        return data
                    else:
                        print("The kitta number entered is not rented.")
                        break
            else:
                print("Invalid Kitta number.")
