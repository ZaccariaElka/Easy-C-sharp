from tkinter import *
from Functions import *
from EditGUI import *

Window = Tk()
Window.title("Easy C#")
Window.resizable(False,True)

button_size = 5
width_size = button_size * 2
titleheight = 2
rownum = 0


rownum = 1 #ROW 1
Title_Basic = Label(Window,text="Basic",height=titleheight)
Title_Basic.grid(row=rownum,column=1,columnspan=3)


rownum = 2 #ROW 2
Starting = Button(Window,height=button_size,width=width_size,command=Start,text="Start")
Starting.grid(column=1,row=rownum)

WritingLine = Button(Window,height=button_size,width=width_size,command=Writeline,text="Write Line")
WritingLine.grid(column=2,row=rownum)

PastingLine = Button(Window,height=button_size,width=width_size,command=Readline, text="Read Line")
PastingLine.grid(column=3,row=rownum)


rownum = 3 #ROW 3
Title_Statements = Label(Window,text="If Statements",height=titleheight)
Title_Statements.grid(row=rownum,column=1,columnspan=3)


rownum = 4 #ROW 4
IfStatement = Button(Window,height=button_size,width=width_size,command=If, text="If")
IfStatement.grid(column=1,row=rownum)

IfElseStatement = Button(Window,height=button_size,width=width_size,command=IfElse, text="If, Else")
IfElseStatement.grid(column=2,row=rownum)

ElseIfStatement = Button(Window,height=button_size,width=width_size,command=ElseIf, text="Else If")
ElseIfStatement.grid(column=3,row=rownum)


rownum = 5 #ROW 5
Title_Loops = Label(Window,text="Loops",height=titleheight)
Title_Loops.grid(row=rownum,column=1,columnspan=3)


rownum = 6 #ROW 6
SwitchCase = Button(Window,height=button_size,width=width_size,command=Switch, text="Switch")
SwitchCase.grid(column=1,row=rownum)

WhileLooping = Button(Window,height=button_size,width=width_size,command=WhileLoop, text="While Loop")
WhileLooping.grid(column=2,row=rownum)

ForLooping = Button(Window,height=button_size,width=width_size,command=ForLoop, text="For Loop")
ForLooping.grid(column=3,row=rownum)


rownum = 7 #ROW 7
ForEach = Button(Window,height=button_size,width=width_size,command=ForEachLoop, text="For Each")
ForEach.grid(column=1,row=rownum)


rownum =  8 #ROW 8
Title_Storages = Label(Window,text="Storages",height=titleheight)
Title_Storages.grid(row=rownum,column=1,columnspan=3)


rownum = 9 #ROW 9
ArrayStorage = Button(Window,height=button_size,width=width_size,command=Array, text="Array")
ArrayStorage.grid(column=1,row=rownum)

DictStorage = Button(Window,height=button_size,width=width_size,command=Dictionary, text="Dictionary")
DictStorage.grid(column=2,row=rownum)

ListStorage = Button(Window,height=button_size,width=width_size,command=List, text="List")
ListStorage.grid(column=3,row=rownum)


rownum = 10 #ROW 10
Title_Methods = Label(Window,text="Methods",height=titleheight)
Title_Methods.grid(row=rownum,column=1,columnspan=3)


rownum = 11 #ROW 11
MethodVoid = Button(Window,height=button_size,width=width_size,command=VoidMethod, text="Void Method")
MethodVoid.grid(column=1,row=rownum)

MethodInt = Button(Window,height=button_size,width=width_size,command=IntMethod, text="Int Method")
MethodInt.grid(column=2,row=rownum)


rownum = 15 #ROW 15
Title_Mode = Label(Window,text="Settings",height=titleheight)
Title_Mode.grid(row=rownum,column=1,columnspan=3)


rownum = 16 #ROW 16
Darkmd = Button(Window,height=2,width=33,command=DarkMode, text="Dark Mode")
Darkmd.grid(row=rownum,column=1,columnspan=3)


rownum = 17 #ROW 17
Lighmd = Button(Window,height=2,width=33,command=LightMode, text="Light Mode")
Lighmd.grid(row=rownum,column=1,columnspan=3)


rownum =  20 #ROW 20
Title_Copy = Label(Window,text="Copy",height=titleheight)
Title_Copy.grid(row=rownum,column=1,columnspan=3)


rownum =  21 #ROW 21
CopyNewText = Button(Window,height=2,width=33,command=SaveText, text="Save Text")
CopyNewText.grid(row=rownum,column=1,columnspan=3)


rownum = 22 #ROW 22
CopyPreviousText = Button(Window,height=2,width=33,command=PreviousText, text="Copy Previous Text")
CopyPreviousText.grid(row=rownum,column=1,columnspan=3)

LightMode()

Window.mainloop()