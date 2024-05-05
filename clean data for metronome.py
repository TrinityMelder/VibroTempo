import pandas as pd

# Load the data
try:
    metronome_data = pd.read_csv('metronome_log.txt', delimiter=',', engine='python', names=['Timestamp', 'Command'], skiprows=1)
    print("Initial Data Loaded Successfully:")
    print(metronome_data.head())
except Exception as e:
    print("Failed to load data:", e)
    import sys
    sys.exit("Exiting: No data to process.")

# Ensure that all commands are strings and handle possible NaNs
metronome_data['Command'] = metronome_data['Command'].astype(str)

# Function to safely extract command components
def extract_command_parts(command):
    parts = command.split(',')
    # Ensure there are enough parts to unpack (add missing parts as None)
    while len(parts) < 6:
        parts.append(None)
    return parts

# Apply the function to each command
metronome_data[['Command_Type', 'BPM', 'Time_Signature_Top', 'Time_Signature_Bottom', 'Extra1', 'Extra2']] = pd.DataFrame(
    metronome_data['Command'].apply(extract_command_parts).tolist(), index=metronome_data.index)

# Drop unnecessary columns
metronome_data.drop(['Command', 'Extra1', 'Extra2'], axis=1, inplace=True)

# Convert new columns to appropriate types if necessary
metronome_data['BPM'] = pd.to_numeric(metronome_data['BPM'], errors='coerce')
metronome_data['Time_Signature_Top'] = pd.to_numeric(metronome_data['Time_Signature_Top'], errors='coerce')
metronome_data['Time_Signature_Bottom'] = pd.to_numeric(metronome_data['Time_Signature_Bottom'], errors='coerce')

# Print the processed data
print("Processed Data:")
print(metronome_data.head())
