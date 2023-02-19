tic = [[1,2,3,],
       [4,5,6],
       [7,8,9]]
p=[0,2,3]
p[1] = input("Enter player 1 name = ")
p[2] = input("Enter player 2 name = ")


print("Tic Tac Toe Board:")
for i in tic:
    print(i)


#insertion function
def insertAt(place,i):
    for j in range(len(tic)):
        for k in range(len(tic[j])):
            if tic[j][k] == place:
                if i == 1:
                    tic[j][k] = "X"
                else:
                    tic[j][k] = "O"
                    

#verification of places
def verify(i):
    #horizantal lines
    if tic[0][0] == tic[0][1] == tic[0][2]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    elif tic[1][0] == tic[1][1] == tic[1][2]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    elif tic[2][0] == tic[2][1] == tic[2][2]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    #Diagonal lines
    elif tic[0][0] == tic[1][1] == tic[2][2]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    elif tic[0][2] == tic[1][1] == tic[2][0]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    #vertical lines
    elif tic[0][0] == tic[1][0] == tic[1][0]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    elif tic[0][1] == tic[1][1] == tic[2][1]:
        print(f"Hurrah! player {p[i]} won the match")
        exit(0)
    elif tic[0][2] == tic[1][2] == tic[2][2]:
        print(f"Hurrah! {p[i]} won the match")
        exit(0)

#Displaying the tic-tac-toe panel
def disp():
    for i in tic:
        print(i)

i=1
for itr in range(9):
    place = int(input(f"{p[i]},Enter a position = "))
    if i == 1:
        insertAt(place,i)
        disp()
        verify(i)
        i=2
    else:
        insertAt(place,i)
        disp()
        verify(i)
        i=1
