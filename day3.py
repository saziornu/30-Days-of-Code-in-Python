n = int(input())

if(n%2!=0):
    print("Weird")
else:
    if(n>20):
        print("Not Weird")
    elif n in range(2,5):
        print("Not Weird")
    else:
        print("Weird")