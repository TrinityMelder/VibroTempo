import serial
import ipywidgets as widgets
from IPython.display import display

# Connect to Arduino
ser = serial.Serial('COM8', 9600)  # Replace 'COM_PORT' with your actual COM port

def send_command(command):
    ser.write(f"{command}\n".encode())

def start_vibration():
    bpm = bpm_slider.value
    beats = beats_slider.value
    notes = notes_dropdown.value
    accent_pattern = accent_text.value
    send_command(f"start {bpm},{beats},{notes},{accent_pattern}")
    print(f"Vibration started at {bpm} BPM, {beats} beats, {notes} notes, accents on beats: {accent_pattern}")

def stop_vibration():
    send_command("stop")
    print("Vibration stopped.")

# BPM, Beats, and Notes controls
bpm_slider = widgets.IntSlider(value=120, min=60, max=360, step=1, description='Select BPM:', continuous_update=False)
beats_slider = widgets.IntSlider(value=4, min=1, max=16, step=1, description='Beats:', continuous_update=False)
notes_dropdown = widgets.Dropdown(
    options=[('1 Note', 1), ('4 Notes', 4), ('8 Notes', 8), ('16 Notes', 16), ('32 Notes', 32)],
    value=4,
    description='Notes:',
)

# Accent pattern input
accent_text = widgets.Text(
    value='',
    placeholder='Enter accented beats, e.g., 1,3',
    description='Accents:',
    continuous_update=False
)

# Start/Stop buttons
start_button = widgets.Button(description="Start Vibrations")
stop_button = widgets.Button(description="Stop Vibrations")
start_button.on_click(lambda x: start_vibration())
stop_button.on_click(lambda x: stop_vibration())

# Display controls
display(bpm_slider, beats_slider, notes_dropdown, accent_text, start_button, stop_button)
