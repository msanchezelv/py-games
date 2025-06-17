import time
from math import remainder

import winsound

seconds = int(input("Enter the time you want in seconds: "))

while seconds > 0:
    hrs, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)

    print(f"{hrs:02}:{mins:02}:{secs:02}")
    time.sleep(1)
    seconds -=1

print("Time's up!")
winsound.Beep(1000, 1000)