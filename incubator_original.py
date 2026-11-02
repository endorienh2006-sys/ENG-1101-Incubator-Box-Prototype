# Original ENGR 1101 submission code, transcribed from the user-provided text.
# This is MakeCode Python, not standard desktop Python.
# Known issues are documented in README.md; retained for project provenance.

temperature = 0
counter = 0

def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval():
    serial.write_line("" + str((temperature)))
loops.every_interval(1000, on_every_interval)

def on_every_interval2():
    for index in range(1):
        while temperature >= 85 and temperature <= 90:
            music.play(music.tone_playable(349, music.beat(BeatFraction.BREVE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.pause(200000)
loops.every_interval(1000, on_every_interval2)

def on_forever():
    global temperature
    temperature = input.temperature() * 1.8 + 32
    basic.show_number(temperature)
basic.forever(on_forever)

def on_forever2():
    global counter
    if temperature < 85:
        pins.digital_write_pin(DigitalPin.P0, 1)
    elif temperature > 90:
        pins.digital_write_pin(DigitalPin.P0, 0)
    else:
        if temperature >= 85 and temperature <= 90:
            basic.show_icon(IconNames.YES)
            counter = 0
    if temperature > 90:
        basic.show_icon(IconNames.NO)
    counter = 1
basic.forever(on_forever2)

def on_forever3():
    global counter
    music.set_volume(255)
    if temperature >= 90 and counter >= 20:
        counter = 1
        music.play(music.tone_playable(330, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever3)

def on_forever4():
    global counter
    if temperature > 90:
        music.play(music.tone_playable(262, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
        for index2 in range(20):
            counter += 1
            basic.pause(1000)
basic.forever(on_forever4)
