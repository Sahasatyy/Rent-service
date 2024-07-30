import datetime as dt

def rb(un, kns, lds, tps):
    fn = un + "_" + dt.datetime.now().strftime('%Y%m%d') + ".txt"
    with open(fn, 'w') as f:
        f.write("********************** Techno Property Nepal **********************\n")
        f.write("                         RENTAL RECEIPT                           \n")
        f.write("Customer Name: " + un + "\n")
        f.write("Kitta Numbers: " + ', '.join(kns) + "\n")
        f.write("Rental Durations:\n")
        for d in lds:
            f.write("  - " + str(d) + " months\n") 
        ta = 0
        f.write("Costs:\n")
        for p in tps:
            f.write("  - Rs. " + str(p) + "\n")
            ta += int(p)
        f.write("Total Amount Due: Rs. " + str(ta) + "\n")
        f.write("Thank you for choosing Techno Property Nepal! Please come again.\n")
    print("Rental receipt generated successfully: ", fn)
    with open(fn, 'r') as f:
        print(f.read())



def rtb(un, kns, rds, tps, ards, lfs):
    fn = un + "_" + dt.datetime.now().strftime('%Y%m%d') + ".txt"
    with open(fn, 'w') as f:
        f.write("********************** Techno Property Nepal **********************\n")
        f.write("                         RETURN RECEIPT                          \n")      
        f.write("Customer Name: " + un + "\n")
        f.write("Kitta Numbers: " + ', '.join(kns) + "\n")
        f.write("Initial Rental Durations (in Contract):\n")
        for rd in rds:
            f.write("  - " + str(rd) + " months\n")
        f.write("Actual Return Durations:\n")
        
        for ard in ards:
            f.write("  - " + str(ard) + " months\n")
        lf_total = 0
        f.write("Late Fees (if any):\n")
        for lf in lfs:
            lf = int(lf)
            if lf > 0:
                lf_total += lf
                f.write("  - Rs. " + str(lf) + "\n")
        f.write("Cost:\n")
        gt = 0
        for lp in tps:
            f.write("  - Rs. " + lp + "\n")
            gt += int(lp)
        f.write("Total Amount: Rs. " + str(gt) + "\n")
        f.write("Thank you for choosing Techno Property Nepal! Please come again.\n")
    print("Return receipt generated successfully: ", fn)
    print()
    with open(fn, 'r') as f:
        print(f.read())
