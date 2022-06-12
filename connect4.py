r="🔴"
y="🟡"
b="🔵"
bord = [
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["🔵","🔵","🔵","🔵","🔵","🔵","🔵"],
  ["","","","","","",""] # This row is to make sure they go to bottom
]
turn=r
def won():
  for i in bord: # Horizontal
    for j in range(4):
      if i[j]==i[j+1]==i[j+2]==i[j+3] and i[j]==turn: 
        return True

  for i in range(7): # Vertical
    for j in range(3):
      if bord[j][i]==bord[j+1][i]==bord[j+2][i]==bord[j+3][i] and bord[j][i]==turn:
        return True

  for i in range(6): # Diagonal
    for j in range(7):
      try:
        if bord[i][j]==bord[i+1][j+1]==bord[i+2][j+2]==bord[i+3][j+3] and bord[i][j]==turn:
          return True
        if bord[i][j]==bord[i+1][j-1]==bord[i+2][j-2]==bord[i+3][j-3] and bord[i][j]==turn:
          return True
      except:
        pass

while True:
  t="" # Checks for draws
  for i in bord: # Prints board
    t+="".join(i)
    print("".join(i))
  if not b in t:
    print("Draw!")
    break
  if won():
    print(f"{turn} won!")
    break
  if turn==r: # changes turn
    turn=y
  else:
    turn=r
  print(f"{turn}'s turn")
  full=False # detects for full column
  while not full:
    go=input("Where do you want to go? (1-7)\n")
    while True:# ensures proper input
      if go.isdigit() and int(go)>0 and int(go)<8:
        break
      go=input("Invalid input\n")
    go=int(go)-1
    for j in range(7):
      if bord[0][go]!=b:
        print("Can't go there, column full\n")
        break
      if bord[j][go]!=b: # Puts at lowest point  
        bord[j-1][go]=turn
        full=True
        break
