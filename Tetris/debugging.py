from Game_State.activePiece import activePiece
testPiece = activePiece("L", "b", (4,4))
print(testPiece.shape)
testPiece.rotate()
print(testPiece.shape)
testPiece.rotate()
print(testPiece.shape)