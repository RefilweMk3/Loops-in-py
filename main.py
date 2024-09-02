name="Refilwe"
for character in name:
    print(character)

for i in range(1,15):
    print("23*%d=%d" %(i,23*i))

n=int(input("Enter a number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()