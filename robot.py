# robot moves in a certain grid (9 x 9)
# cannot move to places it already visited 
# moves from top left to lower right 

# make a board structure 

def board():
  board = []
  for x in range(0,8):
    board.append([])
    for y in range(0,8):
      board[x].append(False)
  return board

# this function will count how many distinct ways the robot can find the lower right corner 
def robot(board):
  solutions = {"count": 0}
  #start in top left corner
  def traverse(i, j):
    # if out of bounds STOP  
    if i == len(board) or i < 0 or j == len(board[i]) or j < 0:
      return
    # if already visited STOP
    if board[i][j] == True:
      return
    # if we are in the lower right corner
    if i == len(board) - 1 and j == len(board[i]) - 1:
      # increment solutions
      solutions["count"] += 1
      return
    # set visited to true
    board[i][j] = True
    # make a call to go left, up, down and right
    traverse(i, j + 1)
    traverse(i, j - 1)
    traverse(i + 1, j)
    traverse(i - 1, j)
    # set current location back to false 
    board[i][j] = False
    return 
  traverse(0,0)
  return solutions["count"]

print robot(board())
