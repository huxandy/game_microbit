def on_button_pressed_a():
    basic.pause(200)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.pause(200)
    basic.show_leds("""
        # # # # .
        # . . . #
        # # # # #
        # . . . #
        # # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
