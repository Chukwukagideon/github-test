# car game
print("Welcome to car game, type start to start the car")
key = input(">>").lower()

car_started = False
car_stopped = True

button = ["start", "stop", "help"]
for keypad in button:
    """looping through prest commands, crosschecking with user input to give command to car"""
    if key == "start":
        if car_started is False:
            print("car started")
        else:
            car_started = True
            print("car already started")

    if key == "stop":
        if car_stopped:
            print("car stopped")
        else:
            print("car already stopped")
