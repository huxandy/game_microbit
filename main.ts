input.onButtonPressed(Button.A, function () {
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.pause(200)
    basic.showLeds(`
        # # # # .
        # . . . #
        # # # # #
        # . . . #
        # # # # .
        `)
})
basic.forever(function () {
    basic.pause(randint(0, 10))
    led.plot(2, 2)
})
