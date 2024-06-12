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
        pyautogui.typewrite(text_to_type)
    except Exception as e:
        print(f"模拟键盘输入时出错: {e}")

# 创建主窗口
root = tk.Tk()
root.title("EasyInput V0.1")
root.geometry("680x348")  # 设置窗口大小

# 设置字体和颜色
font_title = ('Arial', 14, 'bold')
font_entry = ('Arial', 12)
color_title = '#4CAF50'
color_entry = '#f2f2f2'

# 输入文本
text_input_label = tk.Label(root, text="请输入要输出的文本：", font=font_entry, bg=color_entry)
text_input_label.grid(row=0, column=0, padx=10, pady=10)
text_input = tk.Entry(root, font=font_entry, width=50, borderwidth=2, relief='solid', bg=color_entry)
text_input.grid(row=1, column=0, padx=10, pady=10)

# 输入延迟
delay_label = tk.Label(root, text="请输入延迟时间（秒）：", font=font_entry, bg=color_entry)
delay_label.grid(row=2, column=0, padx=10, pady=10)
delay_input = tk.Entry(root, font=font_entry, width=10, borderwidth=2, relief='solid', bg=color_entry)
delay_input.grid(row=3, column=0, padx=10, pady=10)

# 按钮触发输入
type_button = tk.Button(root, text="在光标位置输出文本", command=type_text_at_cursor_position, font=font_entry, bg='#008CBA', fg='white')
type_button.grid(row=4, column=0, padx=10, pady=10)

# 运行主循环
root.mainloop()
