import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2023월 7월 7일 15시 30분 21초 -> _20230707_153021
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # image_20230707_153021.png

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc 를 누를 때까지 프로그램 수행