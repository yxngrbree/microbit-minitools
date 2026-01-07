reading = 0
degrees = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global reading
    reading = input.light_level()
    led.plot_bar_graph(reading, 255)
    if input.button_is_pressed(Button.A):
        basic.show_number(reading)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    elif degrees < 315:
        basic.show_string("W")
    else:
        basic.show_string("N")
input.on_button_pressed(Button.B, on_button_pressed_b)
