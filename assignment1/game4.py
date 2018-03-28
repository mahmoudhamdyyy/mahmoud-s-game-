a=['1','2','3','4','5','6','7','8','9','10','11','l2','13','14','15','16','x','x','x','x']
print(a[0:4])
print(a[4:8])
print(a[8:12])
print(a[12:16])
player=0
y=0
k=4
print("lets start my friend")
print("Enter player 1 name : ")
name1=str(input())
print("Enter player 2 name : ")
name2=str(input())
while True:
    y+=1
    if player==0 or player==2 or player==1:
        if player==0:
            player+=1
        elif player==1 :
            player+=1
        elif player==2 :
            player-=1
        
        l=int(input("enter the first number"))
        m=int(input("enter the second number"))
        if (l-m == 4 or l-m == 1 or l-m == -1 or l-m == -4) and (l!=4 or m!=5) and (l!=5 or m!=4) and (l!=9 or m!=8) and (l!=8 or m!=9) and (l!=13 or m!=12) and (l!=12 or m!=13):
            a[l-1]="x"
            a[m-1]="x"
            print(a[0:4])
            print(a[4:8])
            print(a[8:12])
            print(a[12:16])
        else :
            print("UNKNOW NUMBER   please enter correct number")
            y-=1
            if player==1:
                player=0
            if player==2 :
                player=1    
    if a==["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]:
       print("the winner is :PLAYER 1")
       break;
    if y==7 :
        k=4
        for i in range(4,13,4):
            if a[i]!="x" and (a[i+1]=="x" and a[i+4] =="x" and a[i-4]=="x"):
                k-=1
        for i in range(5,14,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x" and a[i-4]=="x"):
                k-=1        
        for i in range(6,15,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x" and a[i-4]=="x"):
                k-=1               
        for i in range(7,16,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+4] =="x" and a[i-4]=="x"):
                k-=1
        for i in range(1,3):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x"):
                k-=1
    if a[0] !="x" and (a[1]=="x" and a[4]=="x"):
        k-=1
    if a[3] !="x" and (a[2]=="x" and a[7]=="x"):
        k-=1
    if k==3 or k==2 :
        print("the winner is :"+name1)
        keep=False
if y==6 :
    k=4
    for i in range(4,13,4):
            if a[i]!="x" and (a[i+1]=="x" and a[i+4] =="x" and a[i+4]=="x" and a[i-4]=="x"):
                k=k-1
    for i in range(5,14,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x" and a[i-4]=="x"):
                k=k-1
    for i in range(6,15,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x" and a[i-4]=="x"):
                k=k-1
    for i in range(7,16,4):
            if a[i]!="x" and (a[i-1]=="x" and a[i+4] =="x" and a[i-4]=="x"):
                k=k-1
    for i in range(1,3):
            if a[i]!="x" and (a[i-1]=="x" and a[i+1] =="x" and a[i+4]=="x"):
                k=k-1
    if a[0] !="x" and (a[1]=="x" and a[4]=="x"):
        k=k-1           
    if a[3] !="x" and (a[2]=="x" and a[7]=="x"):
        k=k-1
if k==1 or k==0 :
    print("the winner is : "+name2)
    keep=False

