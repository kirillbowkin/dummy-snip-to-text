import time

def show_timer(delay):
    for i in range(delay,0,-1):
        print(f"sinpping will start in {i}s", end="")
        print("\r", end="")
        time.sleep(1)
