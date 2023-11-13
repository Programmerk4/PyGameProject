import time

time1 = time.time()

while True:
    time2 = time.time()
    if time2 % time1 == 0:
        print("yes")
