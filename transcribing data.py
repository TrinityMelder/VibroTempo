import speech_recognition as sr
from pydub import AudioSegment
import math

def split_audio(file_path, chunk_length_ms=60000):  # default to 1 minute chunks
    audio = AudioSegment.from_wav(file_path)
    chunk_length = len(audio) / chunk_length_ms  # Number of chunks
    chunks = []
    
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunks.append(chunk)
    return chunks

def transcribe_chunks(chunks):
    recognizer = sr.Recognizer()
    full_transcript = ""
    
    for i, chunk in enumerate(chunks):
        chunk.export(f"temp_chunk_{i}.wav", format="wav")
        with sr.AudioFile(f"temp_chunk_{i}.wav") as source:
            audio = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio)
            full_transcript += " " + text
        except sr.UnknownValueError:
            full_transcript += " [Unintelligible]"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        
    return full_transcript

# Usage
file_path = r"C:\Users\Trinity's Laptop\Documents\Sound recordings\user 1 and 2.wav"
audio_chunks = split_audio(file_path)
transcription = transcribe_chunks(audio_chunks)
print(transcription)
