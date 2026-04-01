# ====================== 自动安装依赖 ======================
import subprocess
import sys

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"正在自动安装 {package} 库，请稍候...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])

# 自动安装 pyautogui 和 keyboard
install_package("pyautogui")
install_package("keyboard")
# ==========================================================

import pyautogui
import time
import keyboard

# 定义填充区域的起始和结束坐标
x = 63
y = 62
z = 63
x1 = -48
y1 = 62
z1 = -48
# 最低高度
min_y = -64

print("请在 5 秒内切换到《我的世界》窗口，程序将开始执行。")
time.sleep(5)

while y >= min_y and y1 >= min_y:
    # 构建填充指令
    command = f"fill {x} {y} {z} {x1} {y1} {z1} air"
    # 模拟按下斜杠键
    pyautogui.press('/')
    # 输入指令
    pyautogui.typewrite(command)

    # 模拟按下回车键
    pyautogui.press('enter')

    # 等待一段时间，避免指令发送过快
    time.sleep(1.5)
    # 检查是否按下ESC键退出
    if keyboard.is_pressed('esc'):
        print("检测到ESC键，按下退出。")
        break
    # 降低 y 和 y1 的值
    y -= 1
    y1 -= 1


