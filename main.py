from sources.grid import *
import sys

thispath=sys.path[0]

grid=Grid(thispath+"\\utils\\Rosettas\\Level1.csv")
#grid.print()

tabellone=Tabellone(grid,thispath+"\\utils\\Backgrounds\\Bkgrnd11.png")
tabellone.Resize(4,4)
immagine=tabellone.immagine


immagine = cv2.cvtColor(immagine, cv2.COLOR_RGB2BGR)
cv2.imwrite("examples\\LVL1.png",immagine)


H,W=tabellone.GridBricks.shape[:2]
for y in range(H):
	for x in range(W):
		brick=tabellone.GridBricks[y,x]
		if brick!="":
			brick.print_properties()