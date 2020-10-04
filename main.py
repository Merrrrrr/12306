import tkinter as tk
import train
from tkinter import ttk
from tkinter import messagebox, Label
import city

window = tk.Tk()

window.title("12306火车票直达查询")
window.resizable(height=False, width=False)

window.geometry("965x550")

label1 = Label(window, text="出发地")
label2 = Label(window, text="目的地")
label3 = Label(window, text="出发时间")

e1 = tk.Entry(window, font=('Arial', 14))
e2 = tk.Entry(window, font=('Arial', 14))
e3 = tk.Entry(window, font=('Arial', 14))

label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)

e1.grid(row=0, column=1, pady=5)
e2.grid(row=1, column=1, pady=5)
e3.grid(row=2, column=1, pady=5)


def deleteTree(Tree):
    x = Tree.get_children()
    for item in x:
        Tree.delete(item)


def command():
    deleteTree(tree)
    from_station = e1.get().strip()
    to_station = e2.get().strip()
    if city.getCityCode(from_station) is None:
        messagebox.showinfo('提示', '出发地输入错误')
        return
    if city.getCityCode(to_station) is None:
        messagebox.showinfo('提示', '目的地输入错误')
        return

    train_date = e3.get().strip()
    # trainList = []
    try:

        trainList = train.getAll(from_station, to_station, train_date)
        if len(trainList) == 0:
            messagebox.showinfo('提示', '无直达车次')
    except Exception as e:
        messagebox.showinfo("提示", "查询超时，请稍后再试")
        raise e

    for i in range(0, len(trainList)):
        tree.insert("", i, values=trainList[i])


button = tk.Button(window, text='点击查询', command=command)
button.grid(row=3, column=9, pady=10)

tree = ttk.Treeview(window, show="headings", height=16)
tree['columns'] = (
    "车次", "出发站", "到达站", "出发时间", "到达时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座")
width = 60
tree.column("车次", width=width)
tree.column("出发站", width=width)
tree.column("到达站", width=width)
tree.column("出发时间", width=width)
tree.column("到达时间", width=width)
tree.column("历时", width=width)
tree.column("商务座", width=width)
tree.column("一等座", width=width)
tree.column("二等座", width=width)
tree.column("高级软卧", width=width)
tree.column("软卧", width=width)
tree.column("动卧", width=width)
tree.column("硬卧", width=width)
tree.column("软座", width=width)
tree.column("硬座", width=width)
tree.column("无座", width=width)

for name in tree['columns']:
    tree.heading(name, text=name)

tree.grid(row=5, columnspan=10)

messagebox.showinfo('提示', '只能查询直达车次')

window.mainloop()
