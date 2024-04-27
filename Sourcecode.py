from tkinter.constants import W
import plotly.graph_objects as go
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk
import csv



pd.set_option('future.no_silent_downcasting', True)

win = tb.Window(themename = "darkly")
# Load the background image

background_image = tk.PhotoImage(file="stockm.png")


background_image = background_image.zoom(3)
# Resize the background image
# You can adjust the size by changing the parameters of subsample method
background_image = background_image.subsample(1,1)  # Resize by a factor of 2 in both dimensions


# Create a label with the background image
background_label = tk.Label(win, image=background_image)
background_label.place(relwidth= 1, relheight=1)

L1 = tb.Label(win,text='       TITAN\n STOCK ANALYSIS',font=("batmanforeveralternate",80,""),bootstyle='cosmo').pack(pady=20 )

c = None

def im():
    top = tk.Toplevel()
    L1 = tb.Label(top, text='       TITAN \n STOCK ANALYSIS', font=("batmanforeveralternate", 50, "bold"),bootstyle='cosmo').pack(pady=20)
    e = tb.Entry(top)
    def d():
        try:
            r = e.get()
            cs = pd.read_csv(r)
        except FileNotFoundError:
            tb.Label(top, text="file not found", bootstyle='cosmo').pack(pady=2)

        frame = tb.Frame(top)
        # code for table
        tree = ttk.Treeview(top)
        # defining columns

        tree['columns'] = cs.columns
        he = [i for i in cs.columns]
        # formate our columns
        tree.column('#0', width=90)  # this part is for phonthom column
        num = 1
        for i in cs.columns:
            tree.column(num, anchor=W, width=90)
            num = num + 1




        # create headings
        tree.heading('#0', text="")  # phonthom column
        num2 = 0
        for i in cs.columns:
            tree.heading(num2, text=he[num2], anchor=W)
            num2 = num2 + 1

        c = cs.to_numpy().tolist()

        # add data
        for i in c:
            tree.insert(parent="", index='end', iid=i, text="", value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        # pack on the screen
        tree.pack(pady=20)



    def exit():
        top.destroy()


    b1 = tb.Label(top,text="Read CSV File to create and Display DataFrame",bootstyle='cosmo').pack(pady=20)

    t = tb.Label(top, text="Enter the file name with extension .CSV:").pack()
    e.pack()
    b3 = tb.Button(top, text='submit', command=d, bootstyle='cosmo').pack(pady=20)
    b2 = tb.Button(top,text='Exit',command=exit,bootstyle='cosmo').pack(pady=20)



clicks1 = 0
def ins():

    top = tk.Toplevel()
   
    e = tb.Entry(top)
    c = None
    def d():
        try:
            r = e.get()
            cs = pd.read_csv(r)
        except FileNotFoundError:
            tb.Label(top,text="file not found", bootstyle='cosmo').pack(pady=2)


        frame = tb.Frame(top)
        # code for table
        tree = ttk.Treeview(top)
        # defining columns

        tree['columns'] = cs.columns
        he = [i for i in cs.columns]
        num = 1
        saves = []


        for i in he:
            tb.Label(top,text=i,bootstyle='cosmo').pack()
            o = tb.Entry(top)
            o.pack()
            saves.append(o)


        # formate our columns
        tree.column('#0', width=90)  # this part is for phonthom column
        num = 1
        for i in cs.columns:
            tree.column(num, anchor=W, width=90)
            num = num + 1

        c = cs.to_numpy().tolist()
        # create headings
        tree.heading('#0', text="")  # phonthom column
        num2 = 0
        for i in cs.columns:
            tree.heading(num2, text=he[num2], anchor=W)
            num2 = num2 + 1
        tt = 0
        save2 = []

        def save():
            global clicks1
            if clicks1 == 0:
                clicks1 += 1
                for i in saves:
                    save2.append(i.get())
                with open(r,'a',newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(save2)
                tb.Label(top,text="Row inserted successfully").pack()
            else:
                tb.Label(top,text="you have already submitted").pack()




        tb.Button(top, text="save", command=save).pack()





    def exit():
        top.destroy()
        num_t = 0

    b1 = tb.Label(top, text="insert data into DataFrame", bootstyle='cosmo').pack(pady=20)

    t = tb.Label(top, text="Enter the file name with extension .CSV:").pack()
    e.pack()
    b3 = tb.Button(top, text='submit', command=d, bootstyle='cosmo').pack(pady=20)
    b2 = tb.Button(top, text='Exit', command=exit, bootstyle='cosmo').pack(pady=20)

    return c




def da():
    #window for stock file
    top = tk.Toplevel()
    L1 = tb.Label(top, text='       TITAN \n STOCK ANALYSIS', font=("batmanforeveralternate", 50, "bold"),bootstyle='cosmo').pack(pady=20)
    e = tb.Entry(top)


    def da_menu():
        #stored file :
        r = e.get()
        cs = pd.read_csv(r)
        #--------
        da_win = tk.Toplevel()
        top.destroy()
        tb.Label(da_win,text="DATA ANALYTICS MENU",font=("batmanforeveralternate", 30, "bold"),bootstyle='cosmo').pack(pady=20)

        def exiting():
            top.destroy()


        def top_rec():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)
            def crea():
                a = re.get()
                a = int(a)
                fa = cs.head(a)
                tree['columns'] = fa.columns
                he = [i for i in fa.columns]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.columns:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings
                tree.heading('#0', text="")  # phonthom column
                num2 = 0
                for i in fa.columns:
                    tree.heading(num2, text=he[num2], anchor=W)
                    num2 = num2 + 1

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                for i in li:

                    tree.insert(parent="", index='end', iid=i, text="",value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                # pack on the screen
                tree.pack(pady=20)


                def exiting():

                    top_rec_win.destroy()
                tb.Button(top_rec_win,text="exit", command=exiting).pack()

            tb.Label(top_rec_win,text="Enter the number of records to be displayed:").pack()
            re.pack()
            tb.Button(top_rec_win,text='submit',command=crea).pack()


        def exit():
            da_win.destroy()

        def bot_rec():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = re.get()
                a = int(a)
                fa = cs.tail(a)
                tree['columns'] = fa.columns
                he = [i for i in fa.columns]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.columns:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings
                tree.heading('#0', text="")  # phonthom column
                num2 = 0
                for i in fa.columns:
                    tree.heading(num2, text=he[num2], anchor=W)
                    num2 = num2 + 1

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                num = 0
                for i in li:

                    if num < a:
                        tree.insert(parent="", index='end', iid=i, text="",
                                    value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                    num += 1
                # pack on the screen
                tree.pack(pady=20)

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win, text="Enter the number of records to be displayed:").pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()

        def one_col():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = re.get()
                fa = cs[[a]]
                tree['columns'] = fa.columns
                he = [i for i in fa.columns]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.columns:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings
                tree.heading('#0', text="")  # phonthom column
                num2 = 0
                for i in fa.columns:
                    tree.heading(num2, text=he[num2], anchor=W)
                    num2 = num2 + 1

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                num = 0
                for i in li:
                    o = li[num]
                    tree.insert(parent="", index='end', text="",value=o)
                    num = num + 1
                # pack on the screen

                tree.pack(pady=20)

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win, text="Enter the column name be displayed:").pack()
            ev = [i+',' for i in cs.columns]
            tb.Label(top_rec_win, text=ev).pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()

        def mul_cols():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = eval(re.get())
                fa = cs[a]
                tree['columns'] = fa.columns
                tb.Label(top_rec_win,text=fa.columns).pack()
                he = [i for i in fa.columns]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.columns:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings
                tree.heading('#0', text="")  # phonthom column
                num2 = 0
                for i in fa.columns:
                    tree.heading(num2, text=he[num2], anchor=W)
                    num2 = num2 + 1

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                num = 0
                for i in li:
                    o = li[num]
                    tree.insert(parent="", index='end', text="", value=o)
                    num = num + 1
                # pack on the screen

                tree.pack(pady=20)

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win, text="Enter the column names as list in square bracket:").pack()
            ev = [i+',' for i in cs.columns]
            tb.Label(top_rec_win, text=ev).pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()

        def stat():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)
            fa = cs.describe()
            tree['columns'] = fa.columns

            he = [i for i in fa.columns]
            # formate our columns
            tree.column('#0', width=90)  # this part is for phonthom column
            num = 1
            for i in fa.columns:
                tree.column(num, anchor=W, width=90)
                num = num + 1

            # create headings
            tree.heading('#0', text="")  # phonthom column
            num2 = 0
            for i in fa.columns:
                tree.heading(num2, text=he[num2], anchor=W)
                num2 = num2 + 1

            li = fa.to_numpy().tolist()
            # add data
            num = 0
            for i in li:
                o = li[num]
                tree.insert(parent="", index='end', text="", value=o)
                num = num + 1
            # pack on the screen

            tree.pack(pady=20)

            def exiting():
                top_rec_win.destroy()

            tb.Button(top_rec_win, text="exit", command=exiting).pack()

        def com_in():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)

            fa = cs.describe()
            print(fa)
            fi = cs.describe().index
            fc = cs.describe().columns

            he = [i for i in fc]
            # formate our columns

            tree['columns'] = he
            tree.column('#0', width=90)  # this part is for phonthom column
            num = 1
            for i in he:
                tree.column(i, anchor=W, width=90)
                num = num + 1

            # create headings
            tree.heading('#0', text="")  # phonthom column
            num2 = 0
            for i in he:
                tree.heading(num2, text=he[num2], anchor=W)
                num2 = num2 + 1

            li = cs.describe().to_numpy().tolist()
            # add data
            num = 0
            for i in li:
                tree.insert(parent="", index='end', text=fi[num], value=(i[0],i[1],i[2]))
                num = num + 1
            # pack on the screen

            tree.pack(pady=20)



                # pack on the screen

            def exiting():
                top_rec_win.destroy()

            tb.Button(top_rec_win, text="exit", command=exiting).pack()




        def uni():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = re.get()
                fa = cs[a].unique()
                nm = 1
                for i in fa:
                    frame = tb.Frame(top_rec_win)
                    tb.Label(frame,text=i).grid(row=nm,column=nm)
                    frame.pack()
                    nm += 1

                # pack on the screen

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win, text="Displaying unique values of any columns:").pack()
            ev = [i+',' for i in cs.columns]
            tb.Label(top_rec_win, text=ev).pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()

        def ap():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = eval(re.get())
                fa = cs[a]
                tree['columns'] = fa.columns
                tb.Label(top_rec_win, text=fa.columns).pack()
                he = [i for i in fa.columns]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.columns:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings
                tree.heading('#0', text="")  # phonthom column
                num2 = 0
                for i in fa.columns:
                    tree.heading(num2, text=he[num2], anchor=W)
                    num2 = num2 + 1

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                num = 0
                for i in li:
                    o = li[num]
                    tree.insert(parent="", index='end', text="", value=o)
                    num = num + 1
                # pack on the screen

                tree.pack(pady=20)
                ba = tb.Entry(top_rec_win)

                def baa():

                    tree2 = ttk.Treeview(top_rec_win)
                    b = ba.get()
                    loo = [a[0], b]
                    ga = cs[a].groupby(b).count()
                    print(ga)
                    tree2['columns'] = [" ", a, b]

                    he = [i for i in loo]
                    # formate our columns
                    tree2.column('#0', width=90)  # this part is for phonthom column
                    num = 1
                    for i in loo:
                        tree2.column(num, anchor=W, width=90)
                        num = num + 1

                    # create headings
                    tree2.heading('#0', text="")  # phonthom column
                    num2 = 0
                    for i in loo:
                        tree2.heading(num2, text=he[num2], anchor=W)
                        num2 = num2 + 1
                    li = ga.to_numpy().tolist()

                    # add data
                    num = 0
                    for i in cs[a].groupby(b).count().index:
                        u = cs[a].groupby(b).count().index
                        tree2.insert(parent="", index='end', text="", value=(u[num], li[num]))
                        num = num + 1
                    # pack on the screen

                    tree2.pack(pady=20)

                tb.Label(top_rec_win, text="Enter the column name to be displayed:").pack()
                ba.pack()
                tb.Button(top_rec_win, text='submit', command=baa).pack()

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win,
                     text="Name of the columns \n Enter the column names as list in square bracket:").pack()
            ev = [i + ',' for i in cs.columns]
            tb.Label(top_rec_win, text=ev).pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()

        def agma():
            top_rec_win = tk.Toplevel()
            tree = ttk.Treeview(top_rec_win)
            # defining columns
            re = tb.Entry(top_rec_win)

            def crea():
                a = eval(re.get())
                fa = cs[a].max()
                print(fa)
                fi = fa.index
                tree['columns'] = fa.index
                tb.Label(top_rec_win, text=fa.index).pack()
                he = [i for i in fa.index]
                # formate our columns
                tree.column('#0', width=90)  # this part is for phonthom column
                num = 1
                for i in fa.index:
                    tree.column(num, anchor=W, width=90)
                    num = num + 1

                # create headings

                li = fa.to_numpy().tolist()
                tb.Label(top_rec_win, text="top records").pack()
                # add data
                print(li)
                print(fi)
                num = 0
                for i in li:
                    o = li[num]
                    tree.insert(parent="", index='end', text="", value=(fi[num],li[num]))
                    num = num + 1
                # pack on the screen

                tree.pack(pady=20)

                def exiting():
                    top_rec_win.destroy()

                tb.Button(top_rec_win, text="exit", command=exiting).pack()

            tb.Label(top_rec_win, text="Enter the column names as list in square bracket:").pack()
            ev = [i + ',' for i in cs.columns]
            tb.Label(top_rec_win, text=ev).pack()
            re.pack()
            tb.Button(top_rec_win, text='submit', command=crea).pack()







        tb.Button(da_win, text="Top record", bootstyle="cosmo", width=70, command=top_rec).pack(pady=10)
        tb.Button(da_win, text="Bottom Records", bootstyle="cosmo",command=bot_rec, width=70).pack(pady=10)
        tb.Button(da_win, text="To print particular column", bootstyle="cosmo",command=one_col, width=70).pack(pady=10)
        tb.Button(da_win, text="To print multiple columns", bootstyle="cosmo",command=mul_cols, width=70).pack(pady=10)
        tb.Button(da_win, text="To display complete statitics of the dataframe",command=stat, bootstyle="cosmo", width=70).pack(pady=10)
        tb.Button(da_win, text="To display complte information about dataframe",command=com_in, bootstyle="cosmo", width=70).pack(pady=10)
        tb.Button(da_win, text="To display the unique values of the columns", bootstyle="cosmo",command=uni, width=70).pack(pady=10)
        tb.Button(da_win, text="To apply and display the data group by with count function",command=ap, bootstyle="cosmo",width=70).pack(pady=10)
        tb.Button(da_win, text="To applying aggregate function(max)", bootstyle="cosmo",command=agma, width=70).pack(pady=10)
        tb.Button(da_win, text="exit", bootstyle="cosmo", command=exit, width=70).pack(pady=10)








    b1 = tb.Label(top,text="Read CSV File to create and Display DataFrame",bootstyle='cosmo').pack(pady=20)

    t = tb.Label(top, text="Enter the file name with extension .CSV:").pack()
    e.pack()
    b3 = tb.Button(top, text='submit', command=da_menu, bootstyle='cosmo').pack(pady=20)
    b2 = tb.Button(top,text='Exit',command=exit,bootstyle='cosmo').pack(pady=20)














def gr():
    top = tk.Toplevel()
    L1 = tb.Label(top, text='       TITAN \n STOCK ANALYSIS', font=("batmanforeveralternate", 50, "bold"),
                  bootstyle='cosmo').pack(pady=20)
    e = tb.Entry(top)

    def d():
        try:
            r = e.get()
            cs = pd.read_csv(r)
            top.destroy()

            top2 = tk.Toplevel()
            l1 = tb.Label(top2, text='       TITAN \n STOCK ANALYSIS', font=("batmanforeveralternate", 50, "bold"),
                          bootstyle='cosmo').pack(pady=20)



            def his():
                plt.hist(cs['Current_price'], bins=[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],
                         facecolor='m', edgecolor='k')
                plt.xlabel("Ticker")
                plt.ylabel('Frequency')
                plt.show()

            def bar():
                plt.figure().set_figwidth(15)
                plt.bar(cs['Ticker'], cs['Current_price'], color='c', edgecolor='k')
                plt.xlabel('Ticker')
                plt.ylabel('Current price')
                plt.show()

            def hori():
                df2 = cs.head(2)
                plt.barh(cs['Ticker'], cs['Current_price'], color='m', edgecolor='k')
                plt.xlabel('Current Price')
                plt.ylabel('Ticker')
                plt.show()

            def candle():
                df = pd.read_csv('New Text Document.csv')
                fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])
                fig.show()
            def ohlc():
                df = pd.read_csv('ohlc.csv')
                fig = go.Figure(data=[go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])
                fig.show()
            def line():
                df = pd.read_csv('ohlc.csv')

                fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
                fig.show()
                
                fig.show()

            
                
            tb.Button(top2, text="Candlestick Chart", bootstyle="cosmo", command=candle).pack(pady=20)
            tb.Button(top2, text="OHLC Chart", bootstyle="cosmo", command=ohlc).pack(pady=20)
            tb.Button(top2, text="Line Series Chart", bootstyle="cosmo", command=line).pack(pady=20)
            tb.Button(top2, text="Histogram", bootstyle="cosmo", command=his).pack(pady=20)
            tb.Button(top2, text="Bar Chart", bootstyle="cosmo", command=bar).pack(pady=20)
            tb.Button(top2, text="Horizontal Bar Chart", bootstyle="cosmo", command=hori).pack(pady=20)
            tb.Button(top2, text="Exit", bootstyle="cosmo", command=top2.destroy).pack(pady=20)
            

        except FileNotFoundError:
            tb.Label(top, text="file not found",bootstyle='cosmo').pack(pady=2)




    def ex():
        top.destroy()
        num_t = 0


    b1 = tb.Label(top, text="Read CSV File to create and Display DataFrame", bootstyle='cosmo').pack(pady=20)

    t = tb.Label(top, text="Enter the file name with extension .CSV:").pack()
    e.pack()
    b3 = tb.Button(top, text='submit', command=d, bootstyle='cosmo').pack(pady=20)
    b2 = tb.Button(top, text='Exit', command=ex, bootstyle='cosmo').pack(pady=20)




def exe():
    win.destroy()


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 18))

# Create buttons
b1 = tb.Button(text='IMPORT STOCK DATA', bootstyle='cosmo', command=im) 
b1.pack(pady=20)

b2 = tb.Button(text='INSERT DATA / EXPORT', bootstyle='cosmo', command=ins)
b2.pack(pady=20)

b3 = tb.Button(text='DATA ANALYSIS', bootstyle='cosmo', command=da)
b3.pack(pady=20)

b4 = tb.Button(text='GRAPH', bootstyle='cosmo', command=gr)
b4.pack(pady=20)

b5 = tb.Button(text='EXIT', bootstyle='cosmo', command=exe)
b5.pack(pady=20)






win.mainloop()
