from game_state.gridState import gridState

grid = gridState([10,20], 20)
grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
for i in range(18,20):
    grid.solidArray[i] = ['R' for x in range(grid.gridShape[0])]
for i in range(9):
    grid.solidArray[17][i] = 'R'


#for row in grid.solidArray:
 #   print(row)

print(grid.checkRowClear())