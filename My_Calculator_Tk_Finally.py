"""My Calculator. Calculator from 90s. Калькулятор из 90х"""

import tkinter as tk
from tkinter import *
from sys import exit
from os import getpid, kill
import win32com.client


# Исключим мультипроцессинг

proc_name = 'calculator_from_90s.exe'
my_pid = getpid()
wmi = win32com.client.GetObject('winmgmts:')
all_procs = wmi.InstancesOf('Win32_Process')

for proc in all_procs:
    if proc.Properties_("Name").Value == proc_name:
        proc_pid = proc.Properties_("ProcessID").Value
        if proc_pid != my_pid:
            kill(proc_pid, 9)

# Создадим окно калькулятора

root = Tk()
root.title('Калькулятор из девяностых')
root.geometry('430x550')
root.eval('tk::PlaceWindow . center')
photo = tk.PhotoImage(file='icon_calc.png')
root.iconphoto(False, photo)
root.resizable(False, False)
root['bg'] = '#dfdfdf'
root.wm_attributes('-alpha', 0.99)

# Создадим фон, область и дисплей для цифр

background_image = tk.PhotoImage(file='calculator_bg.png')
background_label = tk.Label(root, image=background_image)
frame = background_label
frame.place(relx=0.005, rely=0.005, relheight=0.99, relwidth=0.99)
frame.focus_set()

label_disp = tk.Label(background_label, bg='#dbdbdb')
label_disp.place(relx=0.015, rely=0.1060, relheight=0.149, relwidth=0.97)
label_but = tk.Label(background_label, bg='#d7d7d7')
label_but.place(relx=0.01, rely=0.34, relheight=0.68, relwidth=1)

display_text = tk.StringVar()  # Отображение информации на дисплее
text_field = tk.Label(label_disp, font=('Agency FB', 44, 'bold'), textvariable=display_text, bg='#9f9f2e', fg='black',
                      width=16, height=0, anchor='e', padx=11, pady=2, relief=tk.RAISED, bd=0.25).grid(row=0, column=0)

# Создадим переменные, учавствующие в вычислениях

a = float(0)  # переменная a
b = float(0)  # переменная b
a1 = float(0)  # переменная a1
b1 = float(0)  # переменная b1
m = float(0)   # переменная m, число в памяти
opi = ''  # задействованный на момент вычисления знак (оператор)

display_text.set(str(f'{a :g}'))
op = ('/', '*', '-', '+', '^')


# Создадим функции для цифр, знаков и других клавиш

def num_func(x):
    """Универсальная ф-ия для отображения введенных цифр"""
    global a, b
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list == '0' and len(calc_list) == 1:
            calc_list += str(x)
            return display_text.set(calc_list.lstrip('0'))
        else:
            calc_list += str(x)
            return display_text.set(calc_list)


def zero(*args):
    """Ввод 0"""
    global a, b
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list == '0' and len(calc_list) == 1:
            calc_list += str(0)
            return display_text.set(calc_list)
        else:
            calc_list += str(0)
            return display_text.set(calc_list)


def one(*args):
    """Ввод 1"""
    return num_func(1)


def two(*args):
    """Ввод 2"""
    return num_func(2)


def three(*args):
    """Ввод 3"""
    return num_func(3)


def four(*args):
    """Ввод 4"""
    return num_func(4)


def five(*args):
    """Ввод 5"""
    return num_func(5)


def six(*args):
    """Ввод 6"""
    return num_func(6)


def seven(*args):
    """Ввод 7"""
    return num_func(7)


def eight(*args):
    """Ввод 8"""
    return num_func(8)


def nine(*args):
    """Ввод 9"""
    return num_func(9)


def point(*args):
    """Ввод и отображение точки"""
    global a, b
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    elif calc_list == '0' and len(calc_list) == 1:
        calc_list += str('.')
        return display_text.set(calc_list)
    else:
        calc_list += str('.')
        return display_text.set(calc_list)


def plus(*args):
    """Ввод и отображение плюса"""
    enter()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list[-1] in op:
            calc_list = calc_list[:-1]
            calc_list += '+'
        else:
            calc_list += '+'
        return display_text.set(calc_list)


def minus(*args):
    """Ввод и отображение минуса"""
    enter()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list[-1] in op:
            calc_list = calc_list[:-1]
            calc_list += '-'
        else:
            calc_list += '-'
        return display_text.set(calc_list)


def split(*args):
    """Ввод и отображение деления"""
    enter()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list[-1] in op:
            calc_list = calc_list[:-1]
            calc_list += '/'
        else:
            calc_list += '/'
        return display_text.set(calc_list)


def multiply(*args):
    """Ввод и отображение умножения"""
    enter()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list[-1] in op:
            calc_list = calc_list[:-1]
            calc_list += '*'
        else:
            calc_list += '*'
        return display_text.set(calc_list)


def square(*args):
    """Ввод и отображение степени"""
    enter()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if calc_list[-1] in op:
            calc_list = calc_list[:-1]
            calc_list += '^'
        else:
            calc_list += '^'
        return display_text.set(calc_list)


def square_root(*args):
    """Ввод и отображение корня"""
    global a, b
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        logic_a_b()
        if b == 0:
            if a == 0:
                a = float(calc_list) ** 0.5
            else:
                a = a ** 0.5
            display_text.set(str(round(a, 6)))
            return a
        else:
            b = b ** 0.5
            display_text.set(str(b))
            return b


def percent(*args):
    """Ввод и отображение процента"""
    global a, b, a1, b1, opi
    a1 = a
    b1 = b
    calc_list = display_text.get()
    logic_a_b()
    enter()
    if calc_list.isalpha():
        pass
    else:
        if b1 == 0:
            a = 0
            calc_list = a
        else:
            b1 = a1 / 100 * b1
            result = str(f'{a1 :g}') + opi + str(f'{b1 :g}')
            return display_text.set(result)


def mem_plus(*args):
    """Работа памяти М+"""
    global a, b, m, opi
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        logic_a_b()
        if b == 0:
            if a == 0:
                m = calc_list
                if calc_list == '0':
                    m = 0
            else:
                m = f'{a}'
            return m
        else:
            m = f'{b}'
            return m


def mem_minus(*args):
    """Работа памяти М-"""
    global a, b, m, opi
    logic_a_b()
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if b == 0:
            if a == 0:
                if calc_list[0] == '-':
                    m = calc_list[1:]
                elif calc_list[0] != '-':
                    m = '-' + calc_list
                if calc_list == '0':
                    m = 0
            elif a != 0:
                m = f'{float(a) * (-1)}'
        if b != 0:
            m = f'{float(b) * (-1)}'
        return m


def mem_ms(*args):
    """Сброс числа в памяти"""
    global a, b, m
    if display_text.get() == 'Error':
        pass
    m = 0
    return m


def mem_mr(*args):
    """Вывод числа из памяти"""
    global a, b, m, opi
    calc_list = display_text.get()
    logic_a_b()
    if calc_list == 'Error':
        pass
    else:
        if m == 0:
            pass
        else:
            if str(m)[0] == '-':
                if b == 0 and calc_list.count('-') >= 1 or '+' in calc_list or '*' in calc_list or '/' in calc_list:
                    if calc_list[-1] == '-':
                        calc_list = calc_list[:-1] + '+' + f'{m}'[1:]
                    elif calc_list[-1] == '+':
                        calc_list = calc_list[:-1] + '-' + f'{m}'[1:]
                    elif calc_list[-1] == '*':
                        if calc_list[0] == '-':
                            calc_list = calc_list[1:-1] + '*' + f'{m}'[1:]
                        else:
                            calc_list = '-' + calc_list[:-1] + '*' + f'{m}'[1:]
                    elif calc_list[-1] == '/':
                        if calc_list[0] == '-':
                            calc_list = calc_list[1:-1] + '*' + f'{m}'[1:]
                        else:
                            calc_list = '-' + calc_list[:-1] + '/' + f'{m}'[1:]
                return display_text.set(calc_list)
            elif b == 0 and calc_list.count('-') >= 1 or '+' in calc_list or '*' in calc_list or '/' in calc_list:
                calc_list = str(f'{a}' + opi + f'{m}')
                return display_text.set(calc_list)
            elif b == 0:
                a = m
                return display_text.set(str(m))
            elif a == 0:
                return display_text.set(str(m))


def c(*args):
    """Сброс"""
    global a, b, a1, b1, opi
    a = 0
    b = 0
    a1 = 0
    b1 = 0
    opi = ''
    return display_text.set('0')


def bsp(*args):
    """Стереть"""
    if display_text.get() == 'Error':
        c()
    else:
        calc_list = display_text.get()[:-1]
        if len(calc_list) == 0:
            calc_list = '0'
        return display_text.set(calc_list)


def negative(*args):
    """Ввод и отображение отрицательного числа"""
    global a, b, opi
    calc_list = display_text.get()
    if calc_list == 'Error':
        pass
    else:
        if calc_list[0] == '-':
            calc_list = calc_list[1:]
            return display_text.set(calc_list)
        elif calc_list[0] != '0':
            calc_list = '-' + calc_list
            return display_text.set(calc_list)


# Создаём функции для работы логики и подсчёта выражений

def logic_a_b(*args):
    """Логика работы калькулятора, операции с числами"""
    global a, b, opi
    calc_list = display_text.get()
    if calc_list.isalpha():
        pass
    else:
        if '/' in calc_list:
            opi = '/'
            if calc_list[-1] in op:
                a = calc_list[:-1]
                return display_text.set(calc_list)
            else:
                result1 = [float(i) for i in calc_list.split('/')]
                a = result1[0]
                b = result1[1]
        elif '*' in calc_list:
            opi = '*'
            if calc_list[-1] in op:
                a = calc_list[:-1]
                return display_text.set(calc_list)
            else:
                result1 = [float(i) for i in calc_list.split('*')]
                a = result1[0]
                b = result1[1]
        elif '+' in calc_list:
            opi = '+'
            if calc_list[-1] in op:
                a = calc_list[:-1]
                return display_text.set(calc_list)
            else:
                result1 = [float(i) for i in calc_list.split('+')]
                a = result1[0]
                b = result1[1]
        elif '-' in calc_list:
            opi = '-'
            if calc_list[-1] in op:
                a = calc_list[:-1]
                return display_text.set(calc_list)
            else:
                if '-' == calc_list[0]:
                    if calc_list.count('-') > 1 or '+' in calc_list or '*' in calc_list or '/' in calc_list:
                        calc_list2 = calc_list[1:]
                        result1 = [float(i) for i in calc_list2.split('-')]
                        a = result1[0] * (-1)
                        b = result1[1]
                        if result1[-1] == '':
                            return display_text.set(calc_list)
                        return display_text.set(calc_list)
                    elif calc_list.count('-') == 1 or '+' not in calc_list or '*' not in calc_list \
                            or '/' not in calc_list:
                        a = float(calc_list)
                    else:
                        return display_text.set(calc_list)
                else:
                    result1 = [float(i) for i in calc_list.split('-')]
                    a = result1[0]
                    b = result1[1]
                    if result1[-1] == '':
                        return display_text.set(calc_list)
        elif '^' in calc_list:
            opi = '^'
            if calc_list[-1] in op:
                a = calc_list[:-1]
                return display_text.set(calc_list)
            else:
                result1 = [float(i) for i in calc_list.split('^')]
                a = result1[0]
                b = result1[1]


def enter(*args):
    """Нажатие на Enter, либо автоматический итог вычисления перед вводом следующего оператора"""
    calc_list = display_text.get()
    global a, b, a1, b1
    logic_a_b()
    per = 0
    if calc_list.isalpha():
        pass
    else:
        if '/' in calc_list:
            try:
                if calc_list[-1] in op:
                    a = calc_list[:-1]
                    # if calc_list[-1] == '/':
                    #     a = float(a)
                    #     a /= a
                    return display_text.set(f'{round(a, 8) :g}')
                result = a / b
                a1 = a
                b1 = b
                a = result
                b = 0
                return display_text.set(f'{round(result, 8) :g}')
            except ZeroDivisionError:
                return display_text.set('Error')
        elif '*' in calc_list:
            if calc_list[-1] in op:
                a = calc_list[:-1]
                # if calc_list[-1] == '*':
                #     a = float(a)
                #     a *= a
                return display_text.set(f'{round(a, 8) :g}')
            result = a * b
            a1 = a
            b1 = b
            a = result
            b = 0
            return display_text.set(f'{round(result, 8) :g}')
        elif '+' in calc_list:
            if calc_list[-1] in op:
                a = calc_list[:-1]
                # if calc_list[-1] == '+':
                #     a = float(a)
                #     a += a
                return display_text.set(f'{round(a, 8) :g}')
            result = a + b
            a1 = a
            b1 = b
            a = result
            b = 0
            return display_text.set(f'{round(result, 8) :g}')
        elif '-' in calc_list:
            if calc_list[-1] in op:
                a = calc_list[:-1]
                # if calc_list[-1] == '-':
                #     a = float(a)
                #     a += a
                return display_text.set(f'{round(a, 8) :g}')
            result = a - b
            a1 = a
            b1 = b
            a = result
            b = 0
            return display_text.set(f'{round(result, 8) :g}')
        elif '^' in calc_list:
            if calc_list[-1] in op:
                a = calc_list[:-1]
                # if calc_list[-1] == '^':
                #     a = float(a)
                #     a = a ** a
                return display_text.set(f'{round(a, 8) :g}')
            result = a ** b
            a1 = a
            b1 = b
            a = result
            b = 0
            return display_text.set(f'{round(result, 8) :g}')


def close(*args):
    """Выход"""
    return exit()


# Забиндим клавиши на клавиатуре

frame.bind('1', one)
frame.bind('2', two)
frame.bind('3', three)
frame.bind('4', four)
frame.bind('5', five)
frame.bind('6', six)
frame.bind('7', seven)
frame.bind('8', eight)
frame.bind('9', nine)
frame.bind('0', zero)
frame.bind('.', point)

frame.bind('/', split)
frame.bind('*', multiply)
frame.bind('+', plus)
frame.bind('-', minus)
frame.bind('<Return>', enter)
frame.bind('<Escape>', c)
frame.bind('<BackSpace>', bsp)
frame.bind('`', negative)
frame.bind('%', percent)
frame.bind('^', square)
frame.bind('@', square_root)
frame.bind('<Prior>', mem_plus)
frame.bind('<Next>', mem_minus)
frame.bind('<End>', mem_mr)
frame.bind('<Home>', mem_ms)

# Создадим кнопки калькулятора и разместим их на условной сетке

bt_neg = Button(label_but, text='+/-', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
                activebackground='#4e4e4e',
                command=negative).grid(row=5, column=0)
btp = Button(label_but, text='.', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=point).grid(row=5, column=2)
bt0 = Button(label_but, text='0', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=zero).grid(row=5, column=1)
bt1 = Button(label_but, text='1', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=one).grid(row=4, column=0)
bt2 = Button(label_but, text='2', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=two).grid(row=4, column=1)
bt3 = Button(label_but, text='3', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=three).grid(row=4, column=2)
bt4 = Button(label_but, text='4', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=four).grid(row=3, column=0)
bt5 = Button(label_but, text='5', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=five).grid(row=3, column=1)
bt6 = Button(label_but, text='6', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=six).grid(row=3, column=2)
bt7 = Button(label_but, text='7', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=seven).grid(row=2, column=0)
bt8 = Button(label_but, text='8', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=eight).grid(row=2, column=1)
bt9 = Button(label_but, text='9', font=('Arial', 12, 'bold'), fg='white', height=2, width=6, bg='#3e3e3e',
             activebackground='#4e4e4e',
             command=nine).grid(row=2, column=2)

bt_enter = Button(label_but, text='=', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                  activebackground='#bebebe',
                  command=enter).grid(row=5, column=4)
bt_plus = Button(label_but, text='+', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                 activebackground='#bebebe',
                 command=plus).grid(row=4, column=3, rowspan=2, pady=2.9, stick='ns')
bt_minus = Button(label_but, text='-', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                  activebackground='#bebebe',
                  command=minus).grid(row=4, column=4)
bt_multy = Button(label_but, text='x', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                  activebackground='#bebebe',
                  command=multiply).grid(row=3, column=3)
bt_split = Button(label_but, text='÷', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                  activebackground='#bebebe',
                  command=split).grid(row=3, column=4)
bt_square = Button(label_but, text='x²', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                   activebackground='#bebebe',
                   command=square).grid(row=2, column=3)
bt_square_root = Button(label_but, text='√', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                        activebackground='#bebebe',
                        command=square_root).grid(row=2, column=4)

bt_percent = Button(label_but, text='%', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                    activebackground='#bebebe',
                    command=percent).grid(row=1, column=4)
bt_mem_mn = Button(label_but, text='M-', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                   activebackground='#bebebe',
                   command=mem_minus).grid(row=1, column=3)
bt_mem_pl = Button(label_but, text='M+', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                   activebackground='#bebebe',
                   command=mem_plus).grid(row=1, column=2)
bt_mem_ms = Button(label_but, text='MS', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                   activebackground='#bebebe',
                   command=mem_ms).grid(row=1, column=1)
bt_mem_mr = Button(label_but, text='MR', font=('Arial', 12, 'bold'), height=2, width=6, bg='#ababab',
                   activebackground='#bebebe',
                   command=mem_mr).grid(row=1, column=0)

bt_ce = Button(label_but, text='ON/C', font=('Arial', 12, 'bold'), fg='white', height=1, width=6, bg='#bc412d',
               activebackground='#d24c36',
               command=c).grid(row=0, column=0)
bt_bsp = Button(label_but, text='←', font=('Arial', 12, 'bold'), fg='white', height=1, width=6, bg='#bc412d',
                activebackground='#d24c36',
                command=bsp).grid(row=0, column=1)
bt_off = Button(label_but, text='OFF', font=('Arial', 12, 'bold'), fg='white', height=1, width=6, bg='#bc412d',
                activebackground='#d24c36',
                command=close).grid(row=0, column=2)

label_but.grid_rowconfigure(0, minsize=58)
label_but.grid_rowconfigure(1, minsize=58)
label_but.grid_rowconfigure(2, minsize=58)
label_but.grid_rowconfigure(3, minsize=58)
label_but.grid_rowconfigure(4, minsize=58)
label_but.grid_rowconfigure(5, minsize=58)

label_but.grid_columnconfigure(0, minsize=82)
label_but.grid_columnconfigure(1, minsize=82)
label_but.grid_columnconfigure(2, minsize=82)
label_but.grid_columnconfigure(3, minsize=82)
label_but.grid_columnconfigure(4, minsize=82)

root.mainloop()
