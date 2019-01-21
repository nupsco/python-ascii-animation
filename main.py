import os
import time
import pyfiglet
frames = []

os.system('cls')
text = "Hello World"
for i in range(len(text) + 1):
    rendered_text = pyfiglet.figlet_format(text[:i], font='Big')
    frames.append(rendered_text)
for frame in frames:
    print("".join(frame))
    time.sleep(0.5)
    os.system('cls')
