#!/usr/bin/env python3
import pygame
import simpleaudio as sa
import os
from pydub import AudioSegment
from pydub.playback import play

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '---', 'B': '--.', 'C': '--*', 'D': '-.-', 'E': '-..', 'F': '-.*',
    'G': '-*-', 'H': '-*.', 'I': '-**', 'J': '.--', 'K': '.-.', 'L': '.-*',
    'M': '..-', 'N': '...', 'O': '..*', 'P': '.*-', 'Q': '.*.', 'R': '.**',
    'S': '*--', 'T': '*-.', 'U': '*-*', 'V': '*. -', 'W': '*..', 'X': '*.*',
    'Y': '**-', 'Z': '**.', '/': '***'
}


def txt_to_morse(file_path):
    with open(file_path, 'r') as f:
        text = f.read().upper()

    morse_code = ''
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '  '
    return morse_code

def morse_to_audio(morse_code):
    unit = 100 // 5  # Duration of a single dot in milliseconds divided by 5
    
    dot = AudioSegment.from_file("tones/beep.wav", format="wav")
    dash = AudioSegment.from_file("tones/boop.wav", format="wav")
    slash = AudioSegment.from_file("tones/slash.wav", format="wav")
    
    # Adjust the frame rate to change the duration
    dot = dot.set_frame_rate(int(dot.frame_rate * (dot.duration_seconds / (unit / 1000))))
    dash = dash.set_frame_rate(int(dash.frame_rate * (dash.duration_seconds / (unit / 1000))))
    slash = slash.set_frame_rate(int(slash.frame_rate * (slash.duration_seconds / (unit / 1000))))
    
    gap = AudioSegment.silent(duration=unit)
    audio_sequence = AudioSegment.silent(duration=0)

    for symbol in morse_code:
        if symbol == '.':
            audio_sequence += dot + gap
        elif symbol == '-':
            audio_sequence += dash + gap
        elif symbol == '*':
            audio_sequence += slash + gap
        elif symbol == ' ':
            audio_sequence += gap + gap

    return audio_sequence

def main():
    file_path = input("Enter the path to the text file: ")
    morse_code = txt_to_morse(file_path)
    print("Morse code:", morse_code)

    audio_sequence = morse_to_audio(morse_code)

  

    # Play the audio sequence using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_sequence.export("Broadcast.wav", format="wav"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Save the audio sequence as a .wav file
    output_file = "coded/Broadcast.wav"
    audio_sequence.export(output_file, format="wav")
    print("Audio file saved as: {}".format(output_file))



if __name__ == '__main__':
    main()
