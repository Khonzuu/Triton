from playsound import playsound

def play_wav_file(file_path, repeat_count):
    for _ in range(repeat_count):
        playsound(file_path)

def main():
    file_path = "Broadcast.wav"
    repeat_count = 3
    play_wav_file(file_path, repeat_count)

if __name__ == "__main__":
    main()

