import pretty_midi
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

midi_metronome = pretty_midi.PrettyMIDI('D:\\testing2.MID')  # With metronome
midi_no_metronome = pretty_midi.PrettyMIDI('D:\\testing1.MID')  # Without metronome

def analyze_performance(midi_file):
    onsets = []
    durations = []
    velocities = []
    for instrument in midi_file.instruments:
        for note in instrument.notes:
            onsets.append(note.start)
            durations.append(note.end - note.start)
            velocities.append(note.velocity)
    return np.array(onsets), np.array(durations), np.array(velocities)

onsets_metronome, durations_metronome, velocities_metronome = analyze_performance(midi_metronome)
onsets_no_metronome, durations_no_metronome, velocities_no_metronome = analyze_performance(midi_no_metronome)


tree = KDTree(onsets_metronome.reshape(-1, 1))


distances, indices = tree.query(onsets_no_metronome.reshape(-1, 1))

# Align the performances
aligned_onsets_metronome = onsets_metronome[indices]
aligned_durations_metronome = durations_metronome[indices]
aligned_velocities_metronome = velocities_metronome[indices]
timing_differences = onsets_no_metronome - aligned_onsets_metronome
duration_differences = durations_no_metronome - aligned_durations_metronome
velocity_differences = velocities_no_metronome - aligned_velocities_metronome

# Tempo Variability (Standard Deviation of time between notes)
tempo_variability_metronome = np.std(np.diff(onsets_metronome))
tempo_variability_no_metronome = np.std(np.diff(onsets_no_metronome))

# Plotting results
fig, ax = plt.subplots(4, 1, figsize=(10, 20))
ax[0].plot(timing_differences, label='Timing Differences')
ax[0].set_title('Note Onset Timing Differences')
ax[0].set_ylabel('Seconds')

ax[1].plot(duration_differences, label='Duration Differences')
ax[1].set_title('Note Duration Differences')
ax[1].set_ylabel('Seconds')

ax[2].plot(velocity_differences, label='Velocity Differences')
ax[2].set_title('Velocity Differences')
ax[2].set_ylabel('Velocity Units')

ax[3].bar(['With Metronome', 'Without Metronome'], [tempo_variability_metronome, tempo_variability_no_metronome])
ax[3].set_title('Tempo Variability')

plt.tight_layout()
plt.show()
