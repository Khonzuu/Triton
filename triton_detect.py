import os

if not os.path.exists("coded"):
    os.makedirs("coded")

import aubio

filename = input("Enter the path to the audio file: ")

win_s = 4096
hop_s = win_s // 2

samplerate = 0
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("Hz")
pitch_o.set_tolerance(0.8)

total_frames = 0

decimation_factor = 9  # Output only every 9th line

# Define pitch ranges
pitch_ranges = [(109, 113), (87, 90), (97, 100)]

def is_pitch_in_ranges(pitch, ranges):
    return any(lower <= pitch <= upper for lower, upper in ranges)

output_filename = os.path.join("coded", "output.txt")
with open(output_filename, "w") as output_file:
    with aubio.source(filename, samplerate, hop_s) as source:
        samplerate = source.samplerate
        line_count = 0
        while True:
            samples, read = source()
            pitch = pitch_o(samples)[0]
            confidence = pitch_o.get_confidence()
            if read < hop_s: break
            if line_count % decimation_factor == 0 and is_pitch_in_ranges(pitch, pitch_ranges):
                output_line = f"{total_frames / float(samplerate):.3f} {pitch:.3f} {confidence:.3f}\n"
                print(output_line.strip())
                output_file.write(output_line)
            total_frames += read
            line_count += 1

