import pandas as pd
import mido

def load_midi_data(midi_file):
    mid = mido.MidiFile(midi_file)
    midi_data = []
    time_elapsed = 0  # For accumulating delta times to get absolute times

    for track in mid.tracks:
        for msg in track:
            if not msg.is_meta:
                time_elapsed += msg.time
                if msg.type == 'note_on':
                    midi_data.append({'Timestamp': time_elapsed, 'Note': msg.note, 'Velocity': msg.velocity})

    return pd.DataFrame(midi_data), mid

# Load your MIDI file
midi_df, mid = load_midi_data('your_midi_file.mid')

# Assume the tempo is constant (usually the first set_tempo message in a MIDI file sets the tempo)
tempo = 500000  # Default MIDI tempo (microseconds per beat)
for i, track in enumerate(mid.tracks):
    for msg in track:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
            break  # Assuming only one tempo is set for simplicity

# Convert Timestamps to a uniform scale if necessary (assuming time is in ticks and needs conversion)
ticks_per_beat = mid.ticks_per_beat
midi_df['Timestamp'] = (midi_df['Timestamp'] * tempo / ticks_per_beat) / 1e6  # Convert to seconds

# Now you can proceed with merging and analyzing your data
print(midi_df.head())
