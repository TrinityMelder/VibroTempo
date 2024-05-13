from mido import MidiFile
import numpy as np

def extract_note_onsets(midi_path):
    """
    Extracts note onset times from a MIDI file.
    """
    mid = MidiFile(midi_path)
    times = []
    current_time = 0
    
    for msg in mid:
        current_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            times.append(current_time)
    
    return np.array(times)

def calculate_tempo_variability(onsets):
    """
    Calculates the tempo variability as the standard deviation of inter-onset intervals.
    """
    intervals = np.diff(onsets)
    return np.std(intervals)

# Paths to MIDI files for one user, replace these with the correct paths for your files
user1_with_metro_path = r"C:\Users\Trinity's Laptop\Desktop\Desktop\Files_In_Desktop\Media\With Metronomes\user1 with vibro.MID"
user1_without_metro_path =  r"C:\Users\Trinity's Laptop\Desktop\Desktop\Files_In_Desktop\Media\Without Metronomes\User 1 without the Mteronome.MID"

# Extract note onsets
user1_with_metro_onsets = extract_note_onsets(user1_with_metro_path)
user1_without_metro_onsets = extract_note_onsets(user1_without_metro_path)

# Calculate tempo variability
tempo_var_with = calculate_tempo_variability(user1_with_metro_onsets)
tempo_var_without = calculate_tempo_variability(user1_without_metro_onsets)

print(f"Tempo Variability With Metronome: {tempo_var_with}")
print(f"Tempo Variability Without Metronome: {tempo_var_without}")
