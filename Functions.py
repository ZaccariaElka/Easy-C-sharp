from tkinter import *
import pyperclip

previous_data = ""
#timer = 1

def Start():
    code = (
        "using System;\n"
        "public class Program\n"
        "{"
        "\tpublic static void Main()\n"
        "\t{\n\t\n\t\n\t\n"
        "\t}\n"
        "}"
                    )

    pyperclip.copy(code)

    #time.sleep(timer)
    #pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    #pyperclip.copy(previous_data)


def Writeline():
    #global previous_data
    #previous_data = pyperclip.paste()
    #---
    code = "Console.WriteLine();"
    pyperclip.copy(code)

    #time.sleep(timer)
    #pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    #pyperclip.copy(previous_data)
    #---

    #pyautogui.typewrite(code, interval=0.01)


def Readline():
    code = "string rlname = Console.ReadLine();"
    pyperclip.copy(code)


def If():
    code = (
        "if ()\n"
        "{\n\t\n"
        "}"
                    )
    pyperclip.copy(code)


def IfElse():
    code = (
        "if ()\n"
        "{\n\t\n"
        "}\n"
        "else\n"
        "{\n\t\n"
        "}"
                    )
    pyperclip.copy(code)

    
def ElseIf():
    code = (
        "else if ()\n"
        "{\n\t\n"
        "}"
                    )
    pyperclip.copy(code)


def Switch():
    code = (
        "switch ()\n"
        "{\n"
        "\tcase 1:\n"
        "\t\t\n"
        "\t\tbreak;\n"
        "\tcase 2:\n"
        "\t\t\n"
        "\t\tbreak;\n"
        "\tcase 3:\n"
        "\t\t\n"
        "\t\tbreak;\n"
        "\tdefault: break;\n"
        "}"
                    )
    pyperclip.copy(code)


def WhileLoop():
    code = (
        "int i = 0;\n"
        "while (i < 10)\n"
        "{\n\n"
        "i++;\n"
        "}"
                    )
    pyperclip.copy(code)


def ForLoop():
    code = (
        "for (int x = 0; x <= 0; x++)\n"
        "{\n\n"
        "}"
                    )
    pyperclip.copy(code)

def ForEachLoop():
    code = (
        "foreach (var i in name)\n"
        "{\n\t\n"
        "}"
                    )
    pyperclip.copy(code)

def Array():
    code = (
        "string[] arraystring = {\"\", \"\", \"\"};\n"
        "int[] arrayint = {0, 0, 0};"
                    )
    pyperclip.copy(code)

def Dictionary():
    code = (
        "var DictName = new Dictionary< , >();\n"
        "DictName.Add( , );          //? Key 1 | Value 2"
                    )
    pyperclip.copy(code)

def List():
    code = (
        "var ListName = new List< >();\n"
        "ListName.Add();"
                    )
    pyperclip.copy(code)

def VoidMethod():
    code = (
       "static void Methodname() \n"
        "{\n\t\n"
        "}"
                    )
    pyperclip.copy(code)

def IntMethod():
    code = (
       "static int Methodname()\n"
        "{\n\t\n\treturn x;\n"
        "}"
                    )
    pyperclip.copy(code)


def SaveText():
    global previous_data
    previous_data = pyperclip.paste()


def PreviousText():
    global previous_data
    pyperclip.copy(previous_data)