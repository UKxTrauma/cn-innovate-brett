light = False

def light_switch():
    global light
    if light:
        print("Whoa! It's bright in here")
        light = False
    else:
        print("Who turned out the lights?")
        light = False

light_switch()
light_switch()