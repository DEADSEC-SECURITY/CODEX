import colored
import time

from colored import fg, bg, attr

color = 1

while color != 256:
	time.sleep(0.1)
	print(fg(str(color)) + 'MY NAME IS ANTONIO AND IM GAY   ' + str(color))
	if color == 255:
		print('Finished color printing ...')
	color = color + 1
