def on_pin_pressed_p0():
    global hours
    hours += 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    if degrees < 45:
        basic.show_string("N")
        basic.clear_screen()
    elif degrees < 135:
        basic.show_string("E")
        basic.clear_screen()
    elif degrees == 225:
        basic.show_string("S")
        basic.clear_screen()
    elif degrees == 315:
        basic.show_string("W")
        basic.clear_screen()
    else:
        basic.show_string("N")
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.show_icon(IconNames.HAPPY)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    music.play_melody("- - - - - - - - ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global minutes
    minutes += 1
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global Step
    Step += 1
    basic.show_string("" + str((Step)))
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    basic.show_string("" + str(hours) + ":" + str(minutes))
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

degrees = 0
Step = 0
minutes = 0
hours = 0
basic.show_icon(IconNames.HAPPY)
hours = 1
minutes = 0
time = ""
Step = 0
degrees = 0

def on_forever():
    global degrees, minutes, hours, time, Step
    degrees = input.compass_heading()
    for index in range(10):
        basic.pause(5000)
    basic.pause(5000)
    basic.pause(5000)
    minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
    elif hours == 12:
        hours = 1
        minutes = 0
        time = ""
        degrees = 0
        Step = 0
basic.forever(on_forever)
