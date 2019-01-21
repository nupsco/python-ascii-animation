import os , time
files   = ["ascii1.txt", "ascii2.txt", "ascii3.txt", "ascii4.txt", "ascii5.txt", "ascii6.txt", "ascii7.txt", "ascii8.txt", "ascii9.txt", "ascii10.txt"]
frames  = []

os.system('cls') 
#os.system('clear) for linux
for name in files:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(1):
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        os.system('cls')
