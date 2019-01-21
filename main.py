import os , time
files   = ["data/ascii1.txt", "data/ascii2.txt", "data/ascii3.txt", "data/ascii4.txt", "data/ascii5.txt", "data/ascii6.txt", "data/ascii7.txt", "data/ascii8.txt", "data/ascii9.txt", "data/ascii10.txt"]
frames  = []

os.system('cls')
for name in files:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(1):
    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)
        os.system('cls')
