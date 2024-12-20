import pyautogui
import random
import time
import threading
import pygetwindow as gw

active = False
target_window = "Fortnite  "
lock = threading.Lock()

# def window_res():s
#     while True:
#         print(gw.getActiveWindow())


def auto_click():
    while True:
        with lock:
            if not active or target_window != gw.getActiveWindow().title:
                continue
            pyautogui.click()
            print("click")

            delay = random.uniform(120, 260)
            time.sleep(delay)

def auto_move():
    while True:
        with lock:
            if not active or target_window != gw.getActiveWindow().title:
                continue
            movement = random.randint(1, 8)
            # move_time = random.randint(6, 30)
            move_time = random.randint(1, 2)

            if movement == 1:
                pyautogui.keyDown("w")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                # print("w")
            elif movement == 2:
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("a")
                # print("a")
            elif movement == 3:
                pyautogui.keyDown("s")
                time.sleep(move_time)
                pyautogui.keyUp("s")
                # print("s")
            elif movement == 4:
                pyautogui.keyDown("d")
                time.sleep(move_time)
                pyautogui.keyUp("d")
                # print("d")
            elif movement == 5:
                pyautogui.keyDown("w")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                pyautogui.keyUp("a")
                # print("wa")
            elif movement == 6:
                pyautogui.keyDown("w")
                pyautogui.keyDown("d")
                time.sleep(move_time)
                pyautogui.keyUp("w")
                pyautogui.keyUp("d")
                # print("wd")
            elif movement == 7:
                pyautogui.keyDown("d")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("d")
                pyautogui.keyUp("a")
                # print("da")
            elif movement == 8:
                pyautogui.keyDown("s")
                pyautogui.keyDown("a")
                time.sleep(move_time)
                pyautogui.keyUp("s")
                pyautogui.keyUp("a")
                # print("sa")

            # list, jump table


            delay = random.uniform(30, 150)
            time.sleep(delay)

def check_input():
    is_checking = True
    global active
    while is_checking:
        is_active = input()
        with lock:
            if is_active == "stop":
                active = False
            elif is_active == "start":
                active = True
            elif is_active == "terminate":
                is_checking = False
                is_active = False


def main():
    print("Commands:\n - 'start'\n - 'stop'\n - 'terminate': Kill all threads\nHappy XP Farming, remember to stay tabbed into Fortnite!")
    thread1=threading.Thread(target=auto_click, daemon=True)
    thread2=threading.Thread(target=auto_move, daemon=True)
    # thread4=threading.Thread(target=window_res, daemon=True)
    thread3=threading.Thread(target=check_input)
    thread1.start()
    thread2.start()
    thread3.start()
    # thread4.start()


    thread3.join()

    

if __name__ == "__main__":
    main()
    
