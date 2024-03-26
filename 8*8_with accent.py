import serial
import time

# Set up serial connection
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

# Define the metronome function
def metronome(bpm, beats_per_measure):
    interval = 60 / bpm
    for beat in range(1, beats_per_measure + 1):
        if beat == 2:
            ser.write(b'2')  # Intensified beat
        else:
            ser.write(b'1')  # Standard beat
        time.sleep(interval)

# Test the metronome
try:
    while True:
        metronome(100, 8)  # 100 BPM, 8 beats per measure
except KeyboardInterrupt:
    ser.close()
