import TkGui

def DarkMode():
    WindowBg = "#252526"
    EditBG1 = "#1c1c1c"
    EditFg = "White"
    EditRelief = "groove"
    EditActivebackground = "#101010"
    EditHlt = "1"

    TkGui.Window.config(bg=WindowBg)

    TkGui.Title_Basic.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Statements.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Loops.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Storages.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Methods.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Mode.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Copy.config(bg=WindowBg,fg=EditFg)

    TkGui.Starting.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.WritingLine.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.PastingLine.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.IfStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.IfElseStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ElseIfStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.SwitchCase.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.WhileLooping.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ForLooping.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ForEach.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.ArrayStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.DictStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ListStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.MethodVoid.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.MethodInt.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.Darkmd.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.Lighmd.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.CopyNewText.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.CopyPreviousText.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)


#def LightMode():
def LightMode():
    WindowBg = "#ffffff"
    EditBG1 = "#ececec"
    EditFg = "Black"
    EditRelief = "groove"
    EditActivebackground = "#bcbcbc"
    EditHlt = "1"

    TkGui.Window.config(bg=WindowBg)

    TkGui.Title_Basic.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Statements.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Loops.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Storages.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Methods.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Mode.config(bg=WindowBg,fg=EditFg)
    TkGui.Title_Copy.config(bg=WindowBg,fg=EditFg)

    TkGui.Starting.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.WritingLine.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.PastingLine.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.IfStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.IfElseStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ElseIfStatement.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.SwitchCase.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.WhileLooping.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ForLooping.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ForEach.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.ArrayStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.DictStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.ListStorage.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.MethodVoid.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.MethodInt.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.Darkmd.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.Lighmd.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)

    TkGui.CopyNewText.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)
    TkGui.CopyPreviousText.config(bg=EditBG1,fg=EditFg,relief=EditRelief, activebackground=EditActivebackground,highlightthickness=EditHlt, activeforeground=EditFg)


