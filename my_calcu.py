import tkinter as tk

#color and font for use
#------------------------------
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT = ("Arial,16")
LAEGE_FONT = ("Arial",40,"bold")
WHITE = "#FFFFFF"
BTN_FONT = ("Arial",24,"bold")
OFF_WHITE = "#F8FAFF"
DF_FOONT = ("Arial",20)
LIGHT_BLUE = "#CCEDFF"
#-------------------------------

class Calculator:
    def __init__(self):
        self.window = tk.Tk()

        #GIU wigth and hight
        self.window.geometry("375x667")

        #resize false
        self.window.resizable(0,0)
        self.window.title("My Calculator")

        #Initial display text None
        self.totalexp = ""
        self.currexp = ""

        #display part
        self.display_frame = self.creat_display()

        #button part
        self.button_frame = self.creat_btn()

        #Two part in dispay part 
        self.total_label,self.label = self.creat_display_label()

        #dictionary for digits 
        #use this dictionary by loop to set digit in button
        self.digit = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            ".":(4,1),0:(4,2)
        }

        #operatop dictionary 
        #keys are the operator and values are the unicode cherector 
        #for show the division and multiplication symbol
        self.operator = {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}

        #By this loop set the number of buton in column and row
        #range(1,5) set 4 rows and 4 column
        self.button_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        #func call
        self.creat_digit()
        self.creat_operator_btn()
        self.especialbtn()
        self.bind_key()

    def especialbtn(self):
        self.creat_clear_btn()
        self.creat_equal_btn()
        self.creat_sqr_btn()
        self.creat_sqrt_btn()

    #connecting keybord with GIU 
    def bind_key(self):
        self.window.bind("<Return>",lambda event: self.evaluate())
        self.window.bind("<BackSpace>",lambda event: self.clear())
        for key in self.digit:
            self.window.bind(str(key),lambda event,digit=key:self.add_To_Exp(digit))
        for key in self.operator:
            self.window.bind(key,lambda event,operator=key:self.append_operator(operator)) 

    #function to creat creat display
    def creat_display(self):
        frame = tk.Frame(self.window,height=221,bg="#F5F5F5")
        frame.pack(expand=True,fill="both")
        return frame

    #function to creat 2 label in display
    def creat_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.totalexp,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR,font=SMALL_FONT,padx=24)
        total_label.pack(expand=True,fill="both")

        label = tk.Label(self.display_frame, text=self.currexp,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR,font=LAEGE_FONT,padx=24)
        label.pack(expand=True,fill="both")

        return total_label,label
    
    #function to creat the frame of button
    def creat_btn(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    
    #give the value of the butoon and set row col in grid
    #By lamnda function we pass the input digit to the currexp
    def creat_digit(self):
        for digit,grid_valueOf in self.digit.items():
            button = tk.Button(self.button_frame,text=str(digit),bg=WHITE,fg=LABEL_COLOR,font=BTN_FONT,borderwidth=0,command=lambda x=digit:self.add_To_Exp(x))
            button.grid(row = grid_valueOf[0],column=grid_valueOf[1],sticky=tk.NSEW)

    #creat operator(+,-,*,/) button
    def creat_operator_btn(self):
        i = 0
        for operator,symbool in self.operator.items():
            button = tk.Button(self.button_frame,text=symbool,bg=OFF_WHITE,fg=LABEL_COLOR,font=DF_FOONT,borderwidth=0,command=lambda x=operator:self.append_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    #creat clear button
    def creat_clear_btn(self):
        button = tk.Button(self.button_frame,text="C",bg=OFF_WHITE,fg=LABEL_COLOR,font=DF_FOONT,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    #this function helps to store all enter value in currexp
    def add_To_Exp(self,value):
        self.currexp+=str(value)
        self.upgrade_label()

    #append the operator with currexp and add it to the totalexp
    def append_operator(self,operator):
        self.currexp+=operator
        self.totalexp+=self.currexp
        self.currexp = ""
        #after taking value update two function
        self.upgrade_total_label()
        self.upgrade_label()

    #clear the display
    def clear(self):
        self.currexp = ''
        self.totalexp = ''
        self.upgrade_label()
        self.upgrade_total_label()


    #function to squere a value 
    def squere(self):
        self.currexp = str(eval(f"{self.currexp}**2"))
        self.upgrade_label()

    #creat squere button 
    #\u00b2 this is a unicode to show X squere 
    def creat_sqr_btn(self):
        button = tk.Button(self.button_frame,text="x\u00b2",bg=OFF_WHITE,fg=LABEL_COLOR,font=DF_FOONT,borderwidth=0,command=self.squere)
        button.grid(row=0,column=2,sticky=tk.NSEW)
    
    #function to root a value
    def squert(self):
        self.currexp = str(eval(f"{self.currexp}**0.5"))
        self.upgrade_label()

    #creat squere root button 
    #\u00b2 this is a unicode to show root X     
    def creat_sqrt_btn(self):
        button = tk.Button(self.button_frame,text="\u221ax",bg=OFF_WHITE,fg=LABEL_COLOR,font=DF_FOONT,borderwidth=0,command=self.squert)
        button.grid(row=0,column=3,sticky=tk.NSEW)
    
    #function for make the result and show in display
    #eval() function evaluate the result
    def evaluate(self):
        self.totalexp+=self.currexp
        self.upgrade_total_label()
        try:
            self.currexp = str(eval(self.totalexp))
            self.totalexp=""
        #(1/0) show error in display label
        except Exception as e:
            self.currexp = "Error"
        finally:
            self.upgrade_label()

    #creat a equal button
    def creat_equal_btn(self):
        button = tk.Button(self.button_frame,text="=",bg=LIGHT_BLUE,fg=LABEL_COLOR,font=DF_FOONT,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    #show the value in the display label 2
    def upgrade_total_label(self):
        expretion = self.totalexp
        for operator,symbol in self.operator.items():
            expretion = expretion.replace(operator,f'{symbol}')
        self.total_label.config(text=expretion)

    #this is the label 1 display where show 1st 11 char
    def upgrade_label(self):
        self.label.config(text=self.currexp[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":

    calc = Calculator()
    calc.run()