import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import tkinter.font as tkFont
from PIL import Image, ImageTk
# import matplotlib.pyplot as plt_test
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


style = Style(theme='cerculean')
root = style.master
root.title('chart')
root.geometry('800x600')
font_style = tkFont.Font(family='SimHei', size=16)

a = tk.StringVar()  # 定義變數
a.set('')

label = tk.Label(root, textvariable=a,font=12)  # 建立標籤，內容為變數

box = ttk.Combobox(root,
                   width=15,
                   values=["3C", "家電", "美妝個清", "保健/食品", "服飾/內衣", "鞋包/精品", "母嬰用品", "圖書文具", "傢寢運動", "日用生活", "旅遊戶外"],
                   font=('', 12))

box1 = ttk.Combobox(root,
                    width=15,
                    values=["性別+年齡", "性別", "年齡", "表情"],font=('', 12),)

box.place(x=30,y=30)
box1.place(x=30,y=90)
label.place(x=30,y=180)

# def run_another_script():
#     process = subprocess.Popen(["python", "plt_test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error = process.communicate()
#
#     result_text.delete(1.0, tk.END)
#     result_text.insert(tk.END, f"输出结果：\n{output.decode('utf-8')}")
#     result_text.insert(tk.END, f"\n错误信息：\n{error.decode('utf-8')}")

def display_matplotlib_plot():
    #每次插圖時 在定義一個框框 相當於把舊的刪掉
    frame = tk.Frame(root, width=500, height=500, bd=1, relief=tk.SUNKEN)
    frame.place(x=200, y=30)

    #預防沒有選下拉選單就按繪圖的情況 可以在優化一下
    if(box1.current() != -1) and (box.current() != -1):
        #之後對應存的圖片用  zfill二位數補0
        temp = str(box1.current()) + str(box.current()).zfill(2)
        #a.set(temp1)  # 顯示索引值與內容
        a.set(f'{box.get()}' + '\n' f'{box1.get()}')  # 顯示索引值與內容 換行是字太長會被圖片擋住
    else:
        a.set('請選擇項目')
    img = Image.open('graph/'+temp+ ".png")
    img = img.resize((500, 500))  # 调整图片大小以适应 Frame
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=photo)
    label.image = photo
    label.pack()

# 创建一个框架

button = tk.Button(root, text="繪圖", command=display_matplotlib_plot,width=15,font=('Helvetica', 10))
button.place(x=30,y=270)

root.mainloop()