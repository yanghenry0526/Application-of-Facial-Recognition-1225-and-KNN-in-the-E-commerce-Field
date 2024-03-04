import tkinter as tk
from ttkbootstrap import Style
import tkinter.font as tkFont
import subprocess
import os


def user():
    try:
        # 使用subprocess模块运行其他Python文
        p = subprocess.Popen(["python", "shopping_website.py"],stdin=subprocess.PIPE,shell=True)
        string = str(radioValue.get())
        p.communicate(input=string.encode())
    except subprocess.CalledProcessError:
        print("执行其他Python文件时出错")
def host():
    try:
        # 使用subprocess模块运行其他Python文件
        # os.system('plt_test.py')
        subprocess.Popen(["python", "host.py"])
        subprocess.Popen(["python", "plt_test.py"])
    except subprocess.CalledProcessError:
        print("执行其他Python文件时出错")

# 创建主窗口
style = Style(theme='cerculean')
root = style.master

# root = tk.Tk()
root.title("HomePage")
root.geometry("700x600")
font_style = tkFont.Font(family='SimHei', size=16)


# 按钮
button = tk.Button(root, font=16 ,text="User", command=lambda: user(),width=16, height=2).pack(side='left', padx=50)
button2 = tk.Button(root,font=16 ,text="Host", command=lambda: host(),width=16, height=2).pack(side='right', padx=50)

radioValue = tk.IntVar()
rdioOne = tk.Radiobutton(root, font=16, text="momo", variable=radioValue, value=0).pack(side='bottom',pady=50)
rdioTwo = tk.Radiobutton(root, font=16, text="露天", variable=radioValue, value=1).pack(side='bottom',pady=50)
#標題
font_style = tkFont.Font(family='SimHei', size=12)
label = tk.Label(root, text='網路使用習慣', font=font_style)
label.pack()

#subprocess.Popen(["python", "KNN.py"])
# main loop
root.mainloop()
