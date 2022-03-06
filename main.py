# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import os
from pynput import keyboard
#import keyboard
import tkinter as tk
from tkinter import *

from tkinter import simpledialog
from tkinter.filedialog import askdirectory
#자동완성 cmd shift space

def save_name():
    #input_path = r'/Users/jyoung/Downloads/'
    # filename = 'sample_merge'  # 파일명 고정값
    # file_ext = '.png'  # 파일 형식
    # output_path = '/Users/jyoung/Downloads/%s%s' % (filename, file_ext)
    global dir, filename, file_ext, output_path
    uniq = 1
    while os.path.exists(output_path):  # 동일한 파일명이 존재할 때
        output_path = '%s/%s%d%s' % (dir, filename, uniq, file_ext)  # 파일명(1) 파일명(2)...
        uniq += 1

def on_press(key):
    global startX, startY, endX, endY

    if key == keyboard.Key.f9:
        startX, startY = pyautogui.position()
        mouse_position1.configure(text="X=" + str(startX) + ", Y=" + str(startX))

    if key == keyboard.Key.f10:
        endX, endY = pyautogui.position()
        mouse_position2.configure(text="X=" + str(endX) + ", Y=" + str(endY))

    if key == keyboard.Key.f3:
        save_name()
        pyautogui.screenshot(output_path, region=(startX,startY,480*2.54,320*2.54))
        print(f'알파벳 \'{key}\' 캡처완료-----{output_path}')
    # try:
    #     print(f'알파벳 \'{key.char}\' 눌림')
    # except AttributeError:
    #     print(f'특수키 {key} 눌림')

def on_release(key):
    print(f'키보드 {key} 풀림')
    if key == keyboard.Key.f7:
        # esc 키에서 풀림
        window.destroy()
        return False

def mouse_drag(startX, startY, endX, endY, time):
    pyautogui.moveTo(startX, startY, 1) #시작 포인트
    pyautogui.dragTo(endX, endY, 1) #드래그 포인트

if __name__ == '__main__' :
    global filename, file_ext, output_path, dir
    global startX, startY, endX, endY
    filename = 'sample_merge'  # 파일명 고정값
    file_ext = '.png'  # 파일 형식
    dir = '/Users/jyoung/Downloads'
    output_path = '%s/%s%s' % (dir, filename, file_ext)

    window = Tk() # tkinter 객체 생성
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    # 파일명 변수 생성
    inputfield_filename = StringVar()

    def select_dir() :
        global dir, filename, output_path
        tmpdir = askdirectory(parent=window)
        if len(str(tmpdir)) >= 2 :
            dir = tmpdir
        output_path = '%s/%s%s' % (dir, filename, file_ext)
        selected_dir.configure(text=dir)
        output_label.configure(text=output_path)


    def input_filename():
        global dir, filename, output_path
        tmpfilename = str(inputfield_filename.get()).strip()
        if tmpfilename :
            filename = tmpfilename
        output_path = '%s/%s%s' % (dir, filename, file_ext)
        output_label.configure(text=output_path)

    def move(X,Y):
       # pyautogui.moveTo(X,Y)
        print(X,Y)

    def closing():
        window.destroy()

    def start():
        mouse_position1.configure(text="X=" + str(startX) + ", Y=" + str(startX))
        mouse_position2.configure(text="X=" + str(endX) + ", Y=" + str(endY))

        # while (1):
        #     startX, startY = pyautogui.position()
        #     startX, startY = pyautogui.position()
        #     pyautogui.sleep(1)
        #     statusbar.configure(text="X=" + str(startX) + ", Y=" + str(startX))
        #     print(startX, startY)
        #     if (startX == 10):
        #         break;

    # 경로와 파일명 입력 GUI
    window.title("forjs capture")
    window.geometry("480x320")
    Label(window, text="경로선택 : ").grid(row=0, column=0, padx=10, pady=10)
    selected_dir=Label(window, text=dir)
    selected_dir.grid(row=0, column=1, padx=10, pady=10)
    Button(window, text='경로', command=select_dir).grid(row=0, column=2, padx=10, pady=10)


    Label(window, text="파일명 : ").grid(row=1, column=0, padx=10, pady=10)
    Entry(window, text=filename, textvariable=inputfield_filename).grid(row=1, column=1, padx=10, pady=10)
    Button(window, text="확인", command=input_filename).grid(row=1, column=2, padx=10, pady=10)

    Label(window, text="저장예시 : ").grid(row=3, column=0, padx=10, pady=10)
    output_label=Label(window, text="없음")
    output_label.grid(row=3, column=1, padx=10, pady=10)

    Label(window, text="캡처 볌위 :").grid(row=4, column=0, padx=10, pady=10)
    Label(window, text="전체 "+str(pyautogui.size())).grid(row=4, column=1, padx=10, pady=10)

    startX,startY = 0,0
    endX,endY = pyautogui.size()
    mouse_position1 = Label(window, text="X="+str(startX)+", Y="+str(startY))
    mouse_position1.grid(row=6, column=1, padx=10, pady=10)
    Label(window, text="시작위치저장(F9)").grid(row=6, column=2, padx=10, pady=10)
    mouse_position2 = Label(window, text="X="+str(endX)+", Y="+str(endY))
    mouse_position2.grid(row=7, column=1, padx=10, pady=10)
    Label(window, text="종료위치저장(F10)").grid(row=7, column=2, padx=10, pady=10)

   # Button(window, text="현재위치", command=start).grid(row=8, column=1, padx=10, pady=10)
    Label(window, text="영역캡처: F3").grid(row=8, column=1, padx=10, pady=10)
    Button(window, text="종료(F7)", command=closing).grid(row=8, column=2, padx=10, pady=10)

    window.mainloop()


    # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.join()
