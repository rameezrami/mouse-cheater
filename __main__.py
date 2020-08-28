from autopilot.input import Mouse
import time
import sys
args = sys.argv

sleeper = 600
if(len(args)>1):
	sleeper = int(args[1])

position = '1*1'
if(len(args)>1):
	position = args[2]
positions = position.split('*')



mouse = Mouse.create()

x = int(positions[0])
y = int(positions[1])
counter = 1;
while True:
	
	currentPostion = mouse.position()
	x = currentPostion[0]
	y = currentPostion[1]
	counter = counter +1
	xx = x-10 if counter%2==0 else x+10
	mouse.move(xx,y)
	#mouse.click()
	time.sleep(sleeper)
