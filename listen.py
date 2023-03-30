import sounddevice as sd
import numpy as np
import wavio

# Set the duration (in seconds) and the sample rate
duration = 60
sample_rate = 44100

# Record the audio
print("Recording audio for 60 seconds...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float64')
sd.wait()

# Save the audio as a WAV file
output_filename = "coded/listen.wav"
print(f"Saving audio to '{output_filename}'")
wavio.write(output_filename, audio, sample_rate, sampwidth=2)
print("Recording and saving complete.")

