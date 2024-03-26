import serial
import time

ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  

# Define the metronome function
def metronome(bpm, beats_per_measure):
    interval = 60 / bpm  
    for _ in range(beats_per_measure):
        ser.write(b'1')  
        time.sleep(interval)

# Test the metronome
try:
    while True:
        metronome(100, 4)  # 100 BPM, 4 beats per measure
except KeyboardInterrupt:
    ser.close() 
