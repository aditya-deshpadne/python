def gcd(no1,no2):
    max=1
    while(no1!= no2):
        if(no1>no2):
            no1=no1-no2
        elif(no2>no1):    
            no2=no2-no1
    return no1;



def main():
    no1,no2=eval(input("Enter two nos:"))
    gd=gcd(no1,no2)
    print("GCD %d,%d = %d"%(no1,no2,gd))


main()