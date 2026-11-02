# Temperature-Controlled Incubator Prototype | ENGR 1101

A BBC micro:bit–controlled incubator prototype developed for an introductory engineering design assignment. The project demonstrates temperature sensing, relay-based heater control, user feedback, serial logging, and an out-of-range sample-status alarm.

## Design targets

- Acceptable temperature band: **85–90 °F**.
- Temperature measured by the micro:bit's built-in sensor and converted from Celsius to Fahrenheit.
- Heater relay controlled through **pin P0**.
- Visual feedback on the micro:bit LED matrix, with audible alerts.
- Assignment demonstration uses a **20-second** out-of-range threshold; the design criterion described in the assignment is **three minutes**. This repository's improved demonstration code defaults to 20 seconds.

## Repository files

- `incubator_original.py` — original MakeCode Python code, preserved for reference.
- `incubator_improved.py` — revised, more maintainable MakeCode Python demonstration code; **not the code shown in the original submission video**.
- `docs/User_Manual_Original.pdf` — submitted user instructions and feedback definitions.
- `docs/Incubator_Data_Original.pdf` — PDF of the temperature-versus-time data and graph.
- `data/` — reserved for an original spreadsheet, if available. The PDF is not an editable `.xlsx` dataset.

## How it works (revised code)

| Condition | Heater in automatic mode | LED | Audio |
| --- | --- | --- | --- |
| Below 85 °F | On | X | Brief low-temperature tone on entry |
| 85–90 °F | Off | Check mark | Brief normal-temperature tone on entry |
| Above 90 °F | Off | X | Brief high-temperature tone on entry |
| Outside band for 20 uninterrupted seconds | Depends on temperature | Skull icon (latched) | Entry tone already sounded |

Buttons **A** and **B** manually turn the heater on and off; **A+B** resumes automatic mode. The original code's control behavior differs and is retained in its own file. The improved program writes time (milliseconds), temperature (°F), status, and control mode to the serial console once per second.

## Run the code

1. Open [Microsoft MakeCode for micro:bit](https://makecode.microbit.org/).
2. Create a new project and switch to **Python**.
3. Paste `incubator_improved.py` into the editor.
4. Check compatibility with your micro:bit and MakeCode version; then test in the simulator before flashing hardware.
5. Connect the relay input to P0 and wire the remaining circuit **according to the original hardware design**. Do not wire a mains-powered heater without appropriate isolation, electrical protection, and qualified supervision.
6. View serial output using MakeCode's serial monitor.

## Original deliverables and demonstration

The assignment required a user-feedback manual, a temperature-versus-time scatterplot in an Excel workbook, and a demonstration video under three minutes. The original submitted user manual and data-plot PDF are included. The original demonstration video is **not included in this ZIP** because the uploaded file is approximately 209 MB, exceeding GitHub's normal 100 MB per-file limit. Host it using GitHub Releases or another suitable video host and link it here after uploading.

The supplied PDF shows temperature readings plotted against time; it does not provide the original editable Excel workbook. The improved code has not been tested on the physical prototype, so its behavior should not be described as experimentally verified.

## Engineering considerations and limitations

The original program runs multiple `forever` handlers, includes a long `basic.pause(200000)` inside an interval callback, and uses a counter that can be reset unexpectedly. These choices make its timing and alerts difficult to reason about. The revised version uses a single control loop and elapsed-time tracking, but remains a **demonstration prototype**, not a validated incubator or certified temperature safety system. A production design would require independent temperature sensing, relay fail-safe design, thermal cutoff protection, and hardware testing.

The micro:bit's internal temperature sensor measures board temperature rather than directly measuring the air or sample; sensor placement and calibration matter.

## Skills demonstrated

Embedded systems • BBC micro:bit • MakeCode Python • Temperature monitoring • Relay control • Feedback systems • Serial data logging • Prototype testing • Technical documentation

## Attribution

ENGR 1101 group design project. Add collaborators' names and individual contributions before publication where appropriate. Original assignment materials and project deliverables remain attributed to their original authors.
