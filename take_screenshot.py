#!/usr/bin/env python3
import tkinter as tk
import time
import subprocess
import os
import sys
from PIL import ImageGrab

def take_screenshot():
    """アプリケーションのスクリーンショットを撮影する"""
    # アプリを起動
    proc = subprocess.Popen([sys.executable, "easyeda2kicad_gui.py"])
    
    # GUIが表示されるまで待機
    time.sleep(2)
    
    # アクティブなウィンドウを特定
    if os.name == 'nt':  # Windows
        import win32gui
        window = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(window)
        screenshot = ImageGrab.grab(rect)
    else:  # その他のOS（MacOS, Linux）
        screenshot = ImageGrab.grab()
    
    # スクリーンショットを保存
    screenshot.save("screenshot.png")
    print("スクリーンショットを保存しました: screenshot.png")
    
    # アプリを終了
    proc.terminate()

if __name__ == "__main__":
    take_screenshot() 