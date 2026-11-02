# ENGR 1101 - Temperature-Controlled Incubator Prototype
# BBC micro:bit MakeCode Python (not standard desktop Python)
# Prototype/demo only: not a certified safety or sample-preservation device.

LOW_F = 85
HIGH_F = 90
FAILURE_SECONDS = 20  # Assignment demonstration; original design calls for 180 s
HEATER_PIN = DigitalPin.P0

mode = 0              # 0 = automatic, 1 = manual on, 2 = manual off
out_of_range_start = -1
sample_destroyed = False
last_state = ""

# Button A: manually switch heater ON.
def on_button_pressed_a():
    global mode
    mode = 1
    pins.digital_write_pin(HEATER_PIN, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Button B: manually switch heater OFF.
def on_button_pressed_b():
    global mode
    mode = 2
    pins.digital_write_pin(HEATER_PIN, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Press A+B together to resume automatic temperature control.
def on_button_pressed_ab():
    global mode
    mode = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def on_forever():
    global out_of_range_start, sample_destroyed, last_state

    now = input.running_time()
    temperature_f = input.temperature() * 1.8 + 32

    if temperature_f < LOW_F:
        state = "LOW"
    elif temperature_f > HIGH_F:
        state = "HIGH"
    else:
        state = "NORMAL"

    # Automatically heat only when temperature is below 85 F.
    # At 85 F or above, switch heater off; manual mode takes precedence.
    if mode == 1:
        pins.digital_write_pin(HEATER_PIN, 1)
    elif mode == 2:
        pins.digital_write_pin(HEATER_PIN, 0)
    elif temperature_f < LOW_F:
        pins.digital_write_pin(HEATER_PIN, 1)
    else:
        pins.digital_write_pin(HEATER_PIN, 0)

    # Count uninterrupted time outside the acceptable temperature band.
    if state == "NORMAL":
        out_of_range_start = -1
    else:
        if out_of_range_start < 0:
            out_of_range_start = now
        if now - out_of_range_start >= FAILURE_SECONDS * 1000:
            sample_destroyed = True

    # Short tones on state changes avoid long blocking pauses.
    if state != last_state:
        if state == "NORMAL":
            music.play_tone(349, 150)
        elif state == "HIGH":
            music.play_tone(262, 150)
        else:
            music.play_tone(294, 150)
        last_state = state

    if sample_destroyed:
        basic.show_icon(IconNames.SKULL)
    elif state == "NORMAL":
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)

    # Log elapsed time (ms), temperature (F), status, and heater mode.
    serial.write_line("" + str(now) + "," + str(temperature_f) + "," + state + "," + str(mode))
    basic.pause(1000)

basic.forever(on_forever)
