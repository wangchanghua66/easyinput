import tkinter as tk
from tkinter import simpledialog
import pyautogui
import time

def type_text_at_cursor_position():
    # 获取用户的文本输入
    text_to_type = text_input.get()
    delay = int(delay_input.get())

    # 获取光标位置
    try:
        cursor_pos = pyautogui.position()
        if cursor_pos is None:
            print("无法获取光标位置")
            return
    except Exception as e:
        print(f"获取光标位置时出错: {e}")
        return

    # 模拟键盘输入
    try:
        # 等待指定的延时时间
        time.sleep(delay)
        pyautogui.typewrite(text_to_type, 0)
    except Exception as e:
        print(f"模拟键盘输入时出错: {e}")

# 创建主窗口
root = tk.Tk()
root.title("文本输入与模拟键盘")

# 输入文本
text_input_label = tk.Label(root, text="请输入要输出的文本：")
text_input_label.pack()
text_input = tk.Entry(root, width=50)
text_input.pack()

# 输入延迟
delay_label = tk.Label(root, text="请输入延迟时间（秒）：")
delay_label.pack()
delay_input = tk.Entry(root, width=10)
delay_input.pack()

# 按钮触发输入
type_button = tk.Button(root, text="在光标位置输出文本", command=type_text_at_cursor_position)
type_button.pack()

# 运行主循环
root.mainloop()
