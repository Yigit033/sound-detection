import numpy as np
import wave
import struct
from IPython.display import Audio

# Sample data and rate
sample_rate = 16000
wav_data = np.random.randn(75200)  # Example data

# Ensure the data is in the correct format
wav_data = np.int16(wav_data / np.max(np.abs(wav_data)) * 32767)  # Normalize and convert to int16

# Write the data to a WAV file
with wave.open('output.wav', 'w') as wave_file:
    n_channels = 1
    sampwidth = 2  # Number of bytes per sample (16-bit audio)
    n_frames = len(wav_data)
    comptype = 'NONE'
    compname = 'not compressed'

    wave_file.setparams((n_channels, sampwidth, sample_rate, n_frames, comptype, compname))
    wave_file.writeframes(wav_data.tobytes())

# Load the WAV file for playback
Audio('Kayıt.wav')
