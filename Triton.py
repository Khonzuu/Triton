import subprocess
import tkinter as tk
import os
from pydub import AudioSegment
from pydub.playback import play

def run_script_1():
    script_path = '/home/khonsu/Triton/triton_writer.py'  # Replace with the path to your first script
    subprocess.call(['python3', script_path])

def run_script_2():
    script_path = '/home/khonsu/Triton/triton_output.py'  # Replace with the path to your second script
    subprocess.call(['python3', script_path])

def run_script_3():
    script_path = '/home/khonsu/Triton/triton_broadcast.py'  # Replace with the path to your third script
    subprocess.call(['python3', script_path])

def run_script_4():
    script_path = '/home/khonsu/Triton/listen.py'  # Replace with the path to your fourth script
    subprocess.call(['python3', script_path])

def run_script_5():
    script_path = '/home/khonsu/Triton/triton_detect.py'  # Replace with the path to your fifth script
    subprocess.call(['python3', script_path])

def run_script_6():
    script_path = '/home/khonsu/Triton/triton_decode.py'  # Replace with the path to your fifth script
    subprocess.call(['python3', script_path])

root = tk.Tk()

button1 = tk.Button(root, text='Write_Text', command=run_script_1)
button1.pack()

button2 = tk.Button(root, text='Text_To_Audio', command=run_script_2)
button2.pack()

button3 = tk.Button(root, text='Broadcast_Audio', command=run_script_3)
button3.pack()

button4 = tk.Button(root, text='Listen_For_Audio', command=run_script_4)
button4.pack()

button5 = tk.Button(root, text='Process_Audio', command=run_script_5)
button5.pack()

button6 = tk.Button(root, text='Decode_Message', command=run_script_6)
button6.pack()

root.mainloop()
