input.onPinPressed(TouchPin.P0, function () {
    hours += 1
})
input.onButtonPressed(Button.A, function () {
    if (degrees < 45) {
        basic.showString("N")
        basic.clearScreen()
    } else if (degrees < 135) {
        basic.showString("E")
        basic.clearScreen()
    } else if (degrees == 225) {
        basic.showString("S")
        basic.clearScreen()
    } else if (degrees == 315) {
        basic.showString("W")
        basic.clearScreen()
    } else {
        basic.showString("N")
        basic.clearScreen()
    }
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("C D E F G A B C5 ", 120)
    music.playMelody("C5 B A G F E D C ", 120)
})
input.onPinPressed(TouchPin.P1, function () {
    minutes += 1
})
input.onGesture(Gesture.Shake, function () {
    Step += 1
    basic.showString("" + (Step))
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showString("" + hours + ":" + minutes)
})
let degrees = 0
let Step = 0
let minutes = 0
let hours = 0
basic.showIcon(IconNames.Happy)
hours = 1
minutes = 0
let time = ""
Step = 0
degrees = 0
basic.forever(function () {
    degrees = input.compassHeading()
    for (let index = 0; index < 10; index++) {
        basic.pause(5000)
    }
    basic.pause(5000)
    basic.pause(5000)
    minutes += 1
    if (minutes == 60) {
        hours += 1
        minutes = 0
    } else if (hours == 12) {
        hours = 1
        minutes = 0
        time = ""
        degrees = 0
        Step = 0
    }
})
