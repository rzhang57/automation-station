import pyautogui
import random
import time
import threading
import pygetwindow as gw
from datetime import datetime

active = False
target_window = "Fortnite  "
lock = threading.Lock()
is_terminated = False

# def window_res():s
#     while True:
#         print(gw.getActiveWindow())

def log_with_time(message):
    print(f"{datetime.now().strftime('[(%Y-%m-%d) %H:%M:%S]')} {message}")

def auto_click():
    global is_terminated
    while not is_terminated:
        with lock:
            active_window = gw.getActiveWindow()
            if not active or active_window is None or target_window != active_window.title:
                continue
            pyautogui.click()
            log_with_time("Click")

            delay = random.uniform(120, 260)
            time.sleep(delay)

def auto_move():
    global is_terminated
    while not is_terminated:
        with lock:
            active_window = gw.getActiveWindow()
            if not active or active_window is None or target_window != active_window.title:
                continue
            movement = random.randint(1, 8)
            move_time = random.randint(6, 30)
            # move_time = random.randint(1, 2)

            if movement == 1:
                pyautogui.keyDown("w")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                log_with_time("w")
            elif movement == 2:
                pyautogui.move
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("a")
                log_with_time("a")
            elif movement == 3:
                pyautogui.keyDown("s")
                time.sleep(move_time)
                pyautogui.keyUp("s")
                log_with_time("s")
            elif movement == 4:
                pyautogui.keyDown("d")
                time.sleep(move_time)
                pyautogui.keyUp("d")
                log_with_time("d")
            elif movement == 5:
                pyautogui.keyDown("w")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                pyautogui.keyUp("a")
                log_with_time("wa")
            elif movement == 6:
                pyautogui.keyDown("w")
                pyautogui.keyDown("d")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                pyautogui.keyUp("d")
                log_with_time("wd")
            elif movement == 7:
                pyautogui.keyDown("d")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("d")
                pyautogui.keyUp("a")
                log_with_time("da")
            elif movement == 8:
                pyautogui.keyDown("s")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("s")
                pyautogui.keyUp("a")
                log_with_time("sa")

            # list, jump table
            delay = random.uniform(30, 150)
            time.sleep(delay)

def check_input():
    global active, is_terminated
    while True:
        is_active = input()
        with lock:
            if is_active == "stop":
                active = False
                print("End of session\nCommands:\n - 'start'\n - 'stop'\n - 'terminate': Kill all threads\nHappy XP Farming, remember to stay tabbed into Fortnite (fullscreened please)!")
            elif is_active == "start":
                active = True
                print("Key log:")
            elif is_active == "terminate":
                print("Terminating all threads")
                is_active = False
                is_terminated = True
                break


def main():
    print("Commands:\n - 'start'\n - 'stop'\n - 'terminate': Kill all threads\nHappy XP Farming, remember to stay tabbed into Fortnite (fullscreened please)!")


    thread1=threading.Thread(target=auto_click, daemon=True)
    thread2=threading.Thread(target=auto_move, daemon=True)
    # thread4=threading.Thread(target=window_res, daemon=True)

    # thread3=threading.Thread(target=check_input)
    thread1.start()
    thread2.start()
    # thread3.start()
    # # thread4.start()

    # thread3.join()

    check_input()

    

if __name__ == "__main__":
    main()
    
