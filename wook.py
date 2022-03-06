from pynput import keyboard
from pynput import mouse
import pyautogui

def mouse_move():
    pyautogui.FAILSAFE = False
    print('현재 마우스 인식 : {0}'.format(pyautogui.position()))
    print('전체 사이즈 : {0}'.format(pyautogui.size()))
    pyautogui.moveTo(596, 676)  # 화면 해상도의 가로 200, 세로 200 픽셀 위치로 마우스 이동
    pyautogui.click(660, 185)  # 특정 위치에 마우스 클릭 (순간이동하여 클릭함)
    print('이동?')

def check_mouse_position(key):
    print('마우스 클릭이다 : {0}'.format(key))
    # if key == mouse.
    #     print('Left-Clicked')  # 메시지 출력
    #     pos = mouse.get_position()  # 현재 마우스 포인터 좌표
    #     print(pos)

def on_release(key):
    print('키 뗐다: {0}'.format(key))
    if key == keyboard.Key.f1:
        print('프로그램을 시작하자')


    if key == keyboard.Key.f2:
        print('프로그램을 종료하자')
        return False

    if key == keyboard.Key.f3:
        print('캡쳐 하자')
        pyautogui.screenshot('/Users/burningsweetpotato/Downloads/test.png', region=(0, 0, 1000, 1000))
        mouse_move()

if __name__ == '__main__':
    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()

    with mouse.Listener(
            on_release=check_mouse_position) as mlistener:
        mlistener.join()