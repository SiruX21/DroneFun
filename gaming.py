import docker
import time
from codrone_edu.drone import *
client = docker.from_env()
container = client.containers.get('de1e72d5cb57')
previous_log = "test"
drone = Drone()
while True:
	last_log = container.logs(tail=1).decode('utf-8')
	if last_log in previous_log:
		pass
	else:
		print(last_log)	
		if "start" in last_log:
            print('\nStarting')
			drone.pair()
			drone.takeoff()
		elif "take off" in last_log:
            print('\nTaking Off')
			drone.takeoff()
		elif "takeoff" in last_log:
			print('\nTaking Off')
            drone.takeoff()
		elif "land" in last_log:
            print('\nLanding')
			drone.land()
		elif "stop" in last_log:
            print('\nStopping Motors')
			drone.stop_motors()
		elif "move forward" in last_log:
			print('\nMoving Forward')
            drone.move(1)
		elif "fifty percent" in last_log:
			print('\nFifty percent power')
            drone.set_pitch(50)
		elif "one hundred percent" in last_log:
			print('\nOne hundred percent power')
            drone.set_pitch(100)
		elif "full power" in last_log:
			print('\nOne hundred percent power')
            drone.set_pitch(100)
		elif "spiral" in last_log:
            print('\nSpiralling')
			drone.spiral()
		elif "square" in last_log:
			print('\nGoing in a square')
            drone.square()
		elif "left" in last_log:
			priint('\n Turning Left')
            drone.turn_left()
		elif "right" in last_log:
            print('\n Turning Right')
			drone.turn_right()
        elif "go into a wall" in last_log:
            print('\n Flying straight into a wall')
            drone.avoid_wall()
        elif "move backward" in last_log:
            print('\n Moving Backward')
            move_backward()
        elif "hover" in last_log:
            print('\n Hovering')
            drone.hover()
        elif "flip" in last_log:
            print('\n Flip!')
            drone.flip()
	previous_log=last_log
