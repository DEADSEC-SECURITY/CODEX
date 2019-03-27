import colored

from colored import fg, bg, attr

color = 1

while color != 256:
	print(fg(str(color)) + 'MY NAME IS ANTONIO AND IM GAY   ' + str(color))
	color = color + 1
