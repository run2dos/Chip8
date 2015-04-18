from tkinter import *
from tkinter import ttk


class Debugger:
    def __init__(self, chip):

        self.chip = chip
        self.mainwindow = Tk()

        self.reg0 = StringVar()
        self.reg1 = StringVar() 
        self.reg2 = StringVar() 
        self.reg3 = StringVar() 
        self.reg4 = StringVar() 
        self.reg5 = StringVar() 
        self.reg6 = StringVar() 
        self.reg7 = StringVar() 
        self.reg8 = StringVar() 
        self.reg9 = StringVar() 
        self.regA = StringVar() 
        self.regB = StringVar() 
        self.regC = StringVar() 
        self.regD = StringVar() 
        self.regE = StringVar() 
        self.regF = StringVar()
        self.SP = StringVar()
        self.PC = StringVar()
        self.opcode = StringVar()
        self.cycle = StringVar()


        self.frame = Frame(self.mainwindow)
        self.frame.pack(padx =10, pady = 15)

        leftlabelframe = LabelFrame(self.frame, text="Registers")
        leftlabelframe.grid(row=0, column=0, rowspan=2, padx=20)

        rightlabelframe = LabelFrame(self.frame, text="Emu Values")
        rightlabelframe.grid(row=0, column=1, padx=10)

        bottomrightlabelframe = LabelFrame(self.frame, text="Timers")
        bottomrightlabelframe.grid(row=1, column=1, padx=10)

         
        inner_frame = Frame(leftlabelframe)
        inner_frame.pack(padx = 10, pady =15)

        label_reg0 = Label(inner_frame, text='V0')
        label_reg0.grid(row=0, column=0)

        label_reg1 = Label(inner_frame, text='V1')
        label_reg1.grid(row=1, column=0)

        label_reg2 = Label(inner_frame, text='V2')
        label_reg2.grid(row=2, column=0)

        label_reg3 = Label(inner_frame, text='V3')
        label_reg3.grid(row=3, column=0)

        label_reg4 = Label(inner_frame, text='V4')
        label_reg4.grid(row=4, column=0)

        label_reg5 = Label(inner_frame, text='V5')
        label_reg5.grid(row=5, column=0)

        label_reg6 = Label(inner_frame, text='V6')
        label_reg6.grid(row=6, column=0)

        label_reg7 = Label(inner_frame, text='V7')
        label_reg7.grid(row=7, column=0)

        label_reg8 = Label(inner_frame, text='V8')
        label_reg8.grid(row=8, column=0)

        label_reg9 = Label(inner_frame, text='V9')
        label_reg9.grid(row=9, column=0)

        label_regA = Label(inner_frame, text='VA')
        label_regA.grid(row=10, column=0)

        label_regB = Label(inner_frame, text='VB')
        label_regB.grid(row=11, column=0)

        label_regC = Label(inner_frame, text='VC')
        label_regC.grid(row=12, column=0)

        label_regD = Label(inner_frame, text='VD')
        label_regD.grid(row=13, column=0)

        label_regE = Label(inner_frame, text='VE')
        label_regE.grid(row=14, column=0)

        label_regF = Label(inner_frame, text='VF')
        label_regF.grid(row=15, column=0)


        label_value0 = Label(inner_frame, textvariable = self.reg0).grid(row=0, column=1)
        label_value1 = Label(inner_frame, text='0000').grid(row=1, column=1)
        label_value2 = Label(inner_frame, text='0000').grid(row=2, column=1)
        label_value3 = Label(inner_frame, text='0000').grid(row=3, column=1)
        label_value4 = Label(inner_frame, text='0000').grid(row=4, column=1)
        label_value5 = Label(inner_frame, text='0000').grid(row=5, column=1)
        label_value6 = Label(inner_frame, text='0000').grid(row=6, column=1)
        label_value7 = Label(inner_frame, text='0000').grid(row=7, column=1)
        label_value8 = Label(inner_frame, text='0000').grid(row=8, column=1)
        label_value9 = Label(inner_frame, text='0000').grid(row=9, column=1)
        label_valueA = Label(inner_frame, text='0000').grid(row=10, column=1)
        label_valueB = Label(inner_frame, text='0000').grid(row=11, column=1)
        label_valueC = Label(inner_frame, text='0000').grid(row=12, column=1)
        label_valueD = Label(inner_frame, text='0000').grid(row=13, column=1)
        label_valueE = Label(inner_frame, text='0000').grid(row=14, column=1)
        label_valueF = Label(inner_frame, text='0000').grid(row=15, column=1)


        rinner_frame = Frame(rightlabelframe)
        rinner_frame.pack(padx = 10, pady =15)

        label_SP = Label(rinner_frame, text='SP:')
        label_SP.grid(row=0, column=0)
        label_SP_value = Label(rinner_frame, text='0000').grid(row=0, column=1)

        label_PC = Label(rinner_frame, text='PC:')
        label_PC.grid(row=1, column=0)
        label_PC_value = Label(rinner_frame, text='0000').grid(row=1, column=1)

        label_opcode = Label(rinner_frame, text='Opcode:')
        label_opcode.grid(row=2, column=0)
        label_opdocd_value = Label(rinner_frame, text='0000').grid(row=2, column=1)

        label_cycle = Label(rinner_frame, text='Cycle:')
        label_cycle.grid(row=3, column=0)
        label_cycle_value = Label(rinner_frame, text='0000').grid(row=3, column=1)

        brinner_frame = Frame(bottomrightlabelframe)
        brinner_frame.pack(padx = 10, pady =15)


    def run(self):
        self.mainwindow.mainloop()

def Main():

    debugg = Debugger('hello').run()


if __name__ == '__main__':
    Main()