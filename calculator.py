from tkinter import *
from base_operations import BaseOperations

# Window
window = Tk()
window.geometry('320x360')
window.title('Calculator')
window.resizable(False, False)
window.iconbitmap('image/calculator/cal_ico.ico')

# Function in classes
base = BaseOperations()


class Base_window:
    """The class is responsible for the window of the history of arithmetic operations"""

    def create_window(self):
        """Create pop-up operations"""
        self.window_base = Toplevel()
        self.window_base.geometry('200x225')
        self.window_base.resizable(False, False)
        self.window_base.title('Operations')

        self.operations = Listbox(self.window_base, width=30, height=10, justify=CENTER)
        self.info_window_base = Label(self.window_base, text='Operations go from new to old', fg='#4C0A79')
        self.operations.insert(END, *base.read_table()[::-1])
        self.frame_for_button = Frame(self.window_base, width=200, height=50)
        self.delete_base = Button(self.frame_for_button, text='clean', width=7,
                                  command=self.button_clean_table)
        self.button_update_base = Button(self.frame_for_button, text='update', width=7, command=self.update_window_base)
        self.quit_window_base = Button(self.frame_for_button, text='quit', width=7, command=self.window_base.destroy)

        self.info_window_base.pack(padx=2, pady=2)
        self.operations.pack(padx=2, pady=2)
        self.frame_for_button.pack(padx=2, pady=2)
        self.delete_base.grid(row=0, column=0, pady=2, padx=2)
        self.button_update_base.grid(row=0, column=1, pady=2, padx=2)
        self.quit_window_base.grid(row=0, column=2, pady=2, padx=2)

    def button_clean_table(self):
        """Clears the history of arithmetic operations"""
        base.clean_table()
        self.operations.delete(0, END)

    def update_window_base(self):
        """Updates the history of arithmetic operations"""
        self.operations.delete(0, END)
        self.operations.insert(END, *base.read_table()[::-1])


class Themes:
    """The class is responsible for color design and color window"""

    @staticmethod
    def window_change_theme():
        """Create pop-up color themes"""
        global window_theme
        # Settings window
        window_theme = Toplevel()
        window_theme.geometry('200x250')
        window_theme.resizable(False, False)
        window_theme.title('Theme')

        # Button
        info_theme = Label(window_theme, text='Choose a theme:', fg='#4C0A79')
        dark_mode = Button(window_theme, text='dark mode', width=25, command=Themes.dark_mode)
        light_mode = Button(window_theme, text='light mode', width=25, command=Themes.light_mode)
        rose_mode = Button(window_theme, text='rose mode', width=25, command=Themes.rose_mode)
        purple_mode = Button(window_theme, text='purple mode', width=25, command=Themes.purple_mode)
        green_mode = Button(window_theme, text='green mode', width=25, command=Themes.green_mode)
        orange_mode = Button(window_theme, text='orange mode', width=25, command=Themes.orange_mode)
        sky_mode = Button(window_theme, text='sky mode', width=25, command=Themes.sky_mode)
        yellow_mode = Button(window_theme, text='yellow mode', width=25, command=Themes.yellow_mode)

        # Pack

        info_theme.pack(padx=1, pady=1)
        dark_mode.pack(padx=1, pady=1)
        light_mode.pack(padx=1, pady=1)
        rose_mode.pack(padx=1, pady=1)
        purple_mode.pack(padx=1, pady=1)
        green_mode.pack(padx=1, pady=1)
        orange_mode.pack(padx=1, pady=1)
        sky_mode.pack(padx=1, pady=1)
        yellow_mode.pack(padx=1, pady=1)

    @staticmethod
    def dark_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('dark_mode')

    @staticmethod
    def light_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('light_mode')

    @staticmethod
    def rose_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('rose_mode')

    @staticmethod
    def purple_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('purple_mode')

    @staticmethod
    def green_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('green_mode')

    @staticmethod
    def orange_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('orange_mode')

    @staticmethod
    def sky_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('sky_mode')

    @staticmethod
    def yellow_mode():
        """Passes the name of the color theme to the generating function"""
        Themes.theme('yellow_mode')

    @staticmethod
    def theme(theme):
        """Generates a color for a theme"""
        themes = {
            'dark_mode': ['#000000', '#1F1F1F', '#FFFFFF', '#1F1F1F'],
            'light_mode': ['#F0F0F0', '#F0F0F0', '#000000', '#838996'],
            'rose_mode': ['#C86597', '#D387AE', '#FFFFFF', '#CC399D'],
            'purple_mode': ['#4C0A79', '#D42DF1', '#FFFFFF', '#9414FF'],
            'green_mode': ['#007B33', '#78E99E', '#000000', '#114721'],
            'orange_mode': ['#F07427', '#F2A85C', '#000000', '#FF7348'],
            'sky_mode': ['#0000FF', '#B3CCE9', '#000000', '#318CE7'],
            'yellow_mode': ['#F7CE46', '#F2FD78', '#000000', '#FFD000'],
        }
        Themes.change_theme(themes[theme])

    @staticmethod
    def change_theme(theme):
        """Changes the window theme"""
        window.config(bg=f'{theme[1]}')
        win_cal.config(bg=f'{theme[1]}', fg=f'{theme[2]}')
        frame_1.config(bg=f'{theme[1]}')
        frame_2.config(bg=f'{theme[1]}')
        win_cal_up.config(bg=f'{theme[1]}', fg=f'{theme[2]}')
        button_div.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_div_int.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_div_rem.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_mul.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_mul_double.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_plus.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_minus.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_del.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_sqrt.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_theme.config(bg=f'{theme[1]}')
        button_result.config(bg=f'{theme[1]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_off.config(bg=f'{theme[1]}')

        button_one.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_two.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_three.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_four.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_five.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_six.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_seven.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_eight.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_nine.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_zero.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_vir.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')
        button_operation.config(bg=f'{theme[0]}', fg=f'{theme[2]}', activebackground=f'{theme[3]}')

        window_theme.destroy()


class Calcul:
    """Calculator class, responsible for the functionality of the calculator"""
    __number_result = 0
    __number_increasing = 0
    __zero_error = False

    def __init__(self):
        """Clears arithmetic operations on startup"""
        base.clean_table()

    def num_1(self):
        """Adds to screen 1"""
        self.check_zero_division_error()
        win_cal.insert(END, '1')

    def num_2(self):
        """Adds to screen 2"""
        self.check_zero_division_error()
        win_cal.insert(END, '2')

    def num_3(self):
        """Adds to screen 3"""
        self.check_zero_division_error()
        win_cal.insert(END, '3')

    def num_4(self):
        """Adds to screen 4"""
        self.check_zero_division_error()
        win_cal.insert(END, '4')

    def num_5(self):
        """Adds to screen 5"""
        self.check_zero_division_error()
        win_cal.insert(END, '5')

    def num_6(self):
        """Adds to screen 6"""
        self.check_zero_division_error()
        win_cal.insert(END, '6')

    def num_7(self):
        """Adds to screen 7"""
        self.check_zero_division_error()
        win_cal.insert(END, '7')

    def num_8(self):
        """Adds to screen 8"""
        self.check_zero_division_error()
        win_cal.insert(END, '8')

    def num_9(self):
        """Adds to screen 9"""
        self.check_zero_division_error()
        win_cal.insert(END, '9')

    def num_0(self):
        """Adds to screen 0"""
        self.check_zero_division_error()
        win_cal.insert(END, '0')

    def sign_virgule(self):
        """Adds to screen point"""
        if win_cal.get().count('.') < 1:
            self.check_zero_division_error()
            win_cal.insert(END, '.')

    @staticmethod
    def round_num(number):
        """Responsible for rounding the number when displaying the result"""
        number_str = str(number).split('.')
        return round(number) if len(number_str) == 2 and number_str[1] == '0' else round(number, 2)

    @staticmethod
    def clear_windows():
        """Clears two windows"""
        win_cal.delete(0, END)
        win_cal_up.delete(0, END)

    def check_zero_division_error(self):
        """Checks for a ZeroDivisionError"""
        if self.__zero_error:
            base._BaseOperations__arithmetic_expression = ''
            self.sign_del()
            self.__zero_error = False

    def sign_del(self):
        """Clears the previously calculated result"""
        Calcul.clear_windows()
        self.__number_result = 0
        self.__number_increasing = 0

    def base_function(self):
        """Specifies numbers for an arithmetic expression"""
        text = win_cal_up.get().split()
        self.__number_increasing = float(win_cal.get())

        if len(text) == 0:
            self.__number_result = self.round_num(self.__number_increasing)
        elif len(text) == 2:
            self.operation(text[1], self.__number_increasing)
        Calcul.clear_windows()

    def operation(self, sign, num):
        """Finds the value of an arithmetic expression"""
        try:
            base.generate_operation(self.__number_result, sign, num)
            if sign == '+':
                self.__number_result += num
            elif sign == '-':
                self.__number_result -= num
            elif sign == '*':
                self.__number_result *= num
            elif sign == '/':
                self.__number_result /= num
            elif sign == '//':
                self.__number_result //= num
            elif sign == '%':
                self.__number_result %= num
            self.__number_result = self.round_num(self.__number_result)
            base.result_operation(self.__number_result)
        except ZeroDivisionError:
            self.__zero_error = True

    def generate_expression(self, sign):
        """Generates a mathematical arithmetic expression"""
        try:
            self.base_function()
            if not self.__zero_error:
                win_cal_up.insert(0, f'{self.__number_result} {sign}')
            else:
                win_cal.insert(0, 'Division by zero is not possible')
                self.__number_result = 0
                self.__number_increasing = 0
        except ValueError:
            text = win_cal_up.get()
            Calcul.clear_windows()
            win_cal_up.insert(0, f'{text[:-2].strip()} {sign}')

    def sign_plus(self):
        """Tells the program that the next arithmetic sign is +"""
        if not self.__zero_error:
            self.generate_expression('+')

    def sign_mul(self):
        """Tells the program that the next arithmetic sign is *"""
        if not self.__zero_error:
            self.generate_expression('*')

    def sign_minus(self):
        """Tells the program that the next arithmetic sign is -"""
        if not self.__zero_error:
            self.generate_expression('-')

    def sign_division(self):
        """Tells the program that the next arithmetic sign is /"""
        if not self.__zero_error:
            self.generate_expression('/')

    def sign_division_int(self):
        """Tells the program that the next arithmetic sign is //"""
        if not self.__zero_error:
            self.generate_expression('//')

    def sign_division_remainder(self):
        """Tells the program that the next arithmetic sign is %"""
        if not self.__zero_error:
            self.generate_expression('%')

    def sign_mul_double(self):
        """Responsible for counting the number squared"""
        if not self.__zero_error:
            try:
                self.base_function()
            except ValueError:
                Calcul.clear_windows()
            base.generate_sqr_mul_in_table(self.__number_result, '\u00B2')
            win_cal_up.insert(0, f'({self.__number_result})\u00B2')
            self.__number_result **= 2
            self.__number_result = self.round_num(self.__number_result)
            base.result_operation(self.__number_result)
            win_cal.insert(0, f'{self.__number_result}')

    def sign_sqrt(self):
        """Responsible for calculating the square root"""
        if not self.__zero_error:
            try:
                self.base_function()
            except ValueError:
                Calcul.clear_windows()
            base.generate_sqr_mul_in_table(self.__number_result, '\u221A')
            win_cal_up.insert(0, f'\u221A({self.__number_result})')
            self.__number_result **= 0.5
            self.__number_result = self.round_num(self.__number_result)
            base.result_operation(self.__number_result)
            win_cal.insert(0, f'{self.__number_result}')

    def sign_result(self):
        """Responsible for displaying the result when clicking on ="""
        if not self.__zero_error:
            try:
                self.base_function()
                if not self.__zero_error:
                    win_cal.insert(0, f'{self.__number_result}')
                else:
                    win_cal.insert(0, 'Division by zero is not possible')
            except ValueError:
                text = win_cal_up.get()
                Calcul.clear_windows()
                win_cal.insert(0, text[:-1].strip())


calculator = Calcul()
# Frame
frame_0 = Frame(width=200, height=10)
frame_1 = Frame(width=200, height=190)
frame_2 = Frame()

# Buttons
win_cal_up = Entry(frame_1, width=200, justify=RIGHT)
win_cal = Entry(frame_1, width=200, justify=RIGHT, font='12')

button_operation = Button(frame_0, text='operations', width=41, height=1, activebackground='#838996',
                          activeforeground='#FFFFFF',
                          command=Base_window().create_window)
button_one = Button(frame_2, text='1', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.num_1)
button_two = Button(frame_2, text='2', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.num_2)
button_three = Button(frame_2, text='3', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                      command=calculator.num_3)
button_four = Button(frame_2, text='4', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.num_4)
button_five = Button(frame_2, text='5', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.num_5)
button_six = Button(frame_2, text='6', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.num_6)
button_seven = Button(frame_2, text='7', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                      command=calculator.num_7)
button_eight = Button(frame_2, text='8', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                      command=calculator.num_8)
button_nine = Button(frame_2, text='9', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.num_9)
button_zero = Button(frame_2, text='0', width=20, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.num_0)
button_vir = Button(frame_2, text='.', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.sign_virgule)

button_plus = Button(frame_2, text='+', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.sign_plus)
button_minus = Button(frame_2, text='-', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                      command=calculator.sign_minus)
button_mul = Button(frame_2, text='*', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.sign_mul)
button_del = Button(frame_2, text='AC', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.sign_del)
button_div = Button(frame_2, text='/', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                    command=calculator.sign_division)
button_div_int = Button(frame_2, text='//', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                        command=calculator.sign_division_int)
button_div_rem = Button(frame_2, text='%', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                        command=calculator.sign_division_remainder)
button_theme = Button(frame_2, text='\u263D', width=9, height=2, fg='#F1CB2C', activebackground='#F1CB2C',
                      activeforeground='#FFFFFF',
                      command=Themes().window_change_theme)
button_result = Button(frame_2, text='=', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                       command=calculator.sign_result)
button_mul_double = Button(frame_2, text='x\u00B2', width=9, height=2, activebackground='#838996',
                           activeforeground='#FFFFFF',
                           command=calculator.sign_mul_double)
button_sqrt = Button(frame_2, text='\u221Ax', width=9, height=2, activebackground='#838996', activeforeground='#FFFFFF',
                     command=calculator.sign_sqrt)
button_off = Button(frame_2, text='OFF', width=9, height=2, fg='#FF0000', activebackground='#FF0000',
                    activeforeground='#FFFFFF', command=quit)

# Pack in window
frame_0.pack(padx=2, pady=3)
frame_1.pack(padx=10, pady=3)
frame_2.pack(padx=10, pady=3)
win_cal_up.pack(pady=2)
win_cal.pack()

button_operation.pack(padx=1, pady=1)

button_div_int.grid(row=0, column=0, padx=1, pady=1)
button_theme.grid(row=0, column=1, padx=1, pady=1)
button_del.grid(row=0, column=2, padx=1, pady=1)
button_off.grid(row=0, column=3, padx=1, pady=1)

button_div_rem.grid(row=1, column=0, padx=1, pady=1)
button_sqrt.grid(row=1, column=1, padx=1, pady=1)
button_mul_double.grid(row=1, column=2, padx=1, pady=1)
button_div.grid(row=1, column=3, padx=1, pady=1)

button_seven.grid(row=2, column=0, padx=1, pady=1)
button_eight.grid(row=2, column=1, padx=1, pady=1)
button_nine.grid(row=2, column=2, padx=1, pady=1)
button_mul.grid(row=2, column=3, padx=1, pady=1)

button_four.grid(row=3, column=0, padx=1, pady=1)
button_five.grid(row=3, column=1, padx=1, pady=1)
button_six.grid(row=3, column=2, padx=1, pady=1)
button_minus.grid(row=3, column=3, padx=1, pady=1)

button_one.grid(row=4, column=0, padx=1, pady=1)
button_two.grid(row=4, column=1, padx=1, pady=1)
button_three.grid(row=4, column=2, padx=1, pady=1)
button_plus.grid(row=4, column=3, padx=1, pady=1)

button_zero.grid(row=5, column=0, columnspan=2, padx=1, pady=1)
button_vir.grid(row=5, column=2, padx=1, pady=1)
button_result.grid(row=5, column=3, padx=1, pady=1)

# Mainloop
window.mainloop()
