import wx
import wx.lib.scrolledpanel as LibScrolledPanel

APP_EXIT = 1


class CenteredFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CenteredFrame, self).__init__(parent=parent, title=title, size=(350, 200))
        self.Center()
        self.Show()


class MenuFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MenuFrame, self).__init__(*args, **kwargs)
        self.InitUi()

    def InitUi(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_exit = wx.MenuItem(wx.ID_EXIT, 'Eject', 'Ankide acola')
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
        self.SetSize((300, 200))
        self.SetTitle('Frame with menu')
        self.Center()
        self.Show()

    def OnQuit(self, e):
        self.Close()


class MenuFrameIcons(MenuFrame):
    def __init__(self, *args, **kwargs):
        super(MenuFrameIcons, self).__init__(*args, **kwargs)
        self.InitUi()

    def InitUi(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_exit = wx.MenuItem(file_menu, APP_EXIT, '&Eject\tCtrl+C')
        file_menu_exit.SetBitmap(wx.Bitmap('exit.bmp'))
        file_menu.Append(file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)
        self.SetSize((350, 300))
        self.SetTitle('Icons and shortcuts')
        self.Center()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


class SubMenuFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SubMenuFrame, self).__init__(*args, *kwargs)
        self.Initialize()

    def Initialize(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New')
        file_menu_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open')
        file_menu_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save')
        file_menu.Append(file_menu_new)
        file_menu.Append(file_menu_open)
        file_menu.Append(file_menu_save)
        file_menu.AppendSeparator()
        import_menu = wx.Menu()
        import_menu.Append(wx.ID_ANY, 'Import newsfeed list...')
        import_menu.Append(wx.ID_ANY, 'Import bookmarks...')
        import_menu.Append(wx.ID_ANY, 'Import mail...')
        file_menu.Append(wx.ID_ANY, 'I&mport', import_menu)
        file_menu.AppendSeparator()
        file_menu_exit = wx.MenuItem(file_menu, wx.ID_EXIT, '&Ankide\tCtrl+A')
        file_menu.Append(file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)
        self.SetSize((350, 250))
        self.SetTitle('Submenus')
        self.Center()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


class MenuItemTypes(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MenuItemTypes, self).__init__(*args, **kwargs)
        self.OnInit()

    def OnInit(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        view_menu = wx.Menu()
        self.view_menu_show_toolbar = wx.MenuItem(view_menu, wx.ID_ANY, 'Show toolbar', 'Show Toolbar',
                                                  kind=wx.ITEM_CHECK)
        self.view_menu_show_statubar = wx.MenuItem(view_menu, wx.ID_ANY, 'Show statusbar', 'Show Statusbar',
                                                   kind=wx.ITEM_CHECK)
        view_menu.Append(self.view_menu_show_toolbar)
        view_menu.Append(self.view_menu_show_statubar)
        self.view_menu_show_statubar.Check(True)
        self.view_menu_show_toolbar.Check(True)

        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.view_menu_show_toolbar)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.view_menu_show_statubar)
        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(view_menu, '&View')
        self.SetMenuBar(menu_bar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, '', wx.Bitmap('exit.bmp'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((350, 250))
        self.SetTitle('Check Menu Item')
        self.Center()
        self.Show(True)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    def ToggleStatusBar(self, e):
        if self.view_menu_show_statubar.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):
        if self.view_menu_show_toolbar.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def OnRightDown(self, e):
        self.PopupMenu(PopUpMenu(self), e.GetPosition())


class PopUpMenu(wx.Menu):

    def __init__(self, parent):
        super(PopUpMenu, self).__init__()
        self.parent = parent

        menu_minimize = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(menu_minimize)
        self.Bind(wx.EVT_MENU, self.OnMinimize, menu_minimize)

        menu_close = wx.MenuItem(self, wx.NewId(), 'Close')
        self.Append(menu_close)
        self.Bind(wx.EVT_MENU, self.OnClose, menu_close)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


class PanelTextFrame(wx.Frame):

    def __init__(self, parent, title):
        super(PanelTextFrame, self).__init__(parent, title=title, size=(260, 180))
        panel = wx.Panel(self, wx.ID_ANY)
        menu_bar = wx.MenuBar()
        menu_cyka = wx.Menu()
        menu_blyat = wx.Menu()
        menu_bar.Append(menu_cyka, '&Cyka')
        menu_bar.Append(menu_blyat, '&Blyat')
        self.SetMenuBar(menu_bar)
        wx.TextCtrl(panel, pos=(3, 3), size=(50, 50))
        self.Center()
        self.Show()


class BoxSizerFrame(wx.Frame):

    def __init__(self, parent, title):
        super(BoxSizerFrame, self).__init__(parent, title=title, size=(260, 160))
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        edit_menu = wx.Menu()
        help_menu = wx.Menu()
        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(edit_menu, '&Edit')
        menu_bar.Append(help_menu, '&Help')
        self.SetMenuBar(menu_bar)
        wx.TextCtrl(self)
        self.Center()
        self.Show()


class BoxFrame(wx.Frame):

    def __init__(self, parent, title):
        super(BoxFrame, self).__init__(parent, title=title, size=(350, 250))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#ff0000')
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        median_panel = wx.Panel(panel)
        median_panel.SetBackgroundColour('#00ff00')
        vertical_box.Add(median_panel, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vertical_box)
        self.Center()
        self.Show()


class GoToClass(wx.Frame):

    def __init__(self, parent, title):
        super(GoToClass, self).__init__(parent, title=title, size=(540, 420))
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vertical_box = wx.BoxSizer(wx.VERTICAL)

        horizontal_box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(panel, label='Class Name')
        label.SetFont(font)
        horizontal_box.Add(label, flag=wx.RIGHT, border=8)
        text_control = wx.TextCtrl(panel)
        horizontal_box.Add(text_control, proportion=1)
        vertical_box.Add(horizontal_box, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vertical_box.Add((-1, 10))

        horizontal_box_2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panel, label='Matching Classes')
        label2.SetFont(font)
        horizontal_box_2.Add(label2)
        vertical_box.Add(horizontal_box_2, flag=wx.LEFT | wx.TOP, border=10)

        vertical_box.Add((-1, 10))

        horizontal_box_3 = wx.BoxSizer(wx.HORIZONTAL)
        text_control_2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        horizontal_box_3.Add(text_control_2, proportion=1, flag=wx.EXPAND)
        vertical_box.Add(horizontal_box_3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
                         border=10)

        vertical_box.Add((-1, 25))

        horizontal_box_4 = wx.BoxSizer(wx.HORIZONTAL)
        checkbox_1 = wx.CheckBox(panel, label='Case Sensitive')
        checkbox_1.SetFont(font)
        horizontal_box_4.Add(checkbox_1, flag=wx.LEFT, border=10)
        check_box_2 = wx.CheckBox(panel, label='Nested Classes')
        check_box_2.SetFont(font)
        horizontal_box_4.Add(check_box_2, flag=wx.LEFT, border=10)
        check_box_3 = wx.CheckBox(panel, label='Non-Project classes')
        check_box_3.SetFont(font)
        horizontal_box_4.Add(check_box_3, flag=wx.LEFT, border=10)
        vertical_box.Add(horizontal_box_4, flag=wx.LEFT, border=10)

        vertical_box.Add((-1, 25))

        horizontal_box_5 = wx.BoxSizer(wx.HORIZONTAL)
        button_1 = wx.Button(panel, label='Ok', size=(70, 30))
        horizontal_box_5.Add(button_1, flag=wx.LEFT | wx.BOTTOM)
        button_2 = wx.Button(panel, label='Close', size=(70, 30))
        horizontal_box_5.Add(button_2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vertical_box.Add(horizontal_box_5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        panel.SetSizer(vertical_box)
        self.Center()
        self.Show()


class Calculator(wx.Frame):

    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title, size=(300, 250))
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vertical_box.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        grid_sizer = wx.GridSizer(5, 4, 5, 5)

        grid_sizer.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
                            (wx.Button(self, label='Bck'), 0, wx.EXPAND),
                            (wx.StaticText(self), wx.EXPAND),
                            (wx.Button(self, label='Close'), 0, wx.EXPAND),
                            (wx.Button(self, label='7'), 0, wx.EXPAND),
                            (wx.Button(self, label='8'), 0, wx.EXPAND),
                            (wx.Button(self, label='9'), 0, wx.EXPAND),
                            (wx.Button(self, label='/'), 0, wx.EXPAND),
                            (wx.Button(self, label='4'), 0, wx.EXPAND),
                            (wx.Button(self, label='5'), 0, wx.EXPAND),
                            (wx.Button(self, label='6'), 0, wx.EXPAND),
                            (wx.Button(self, label='*'), 0, wx.EXPAND),
                            (wx.Button(self, label='1'), 0, wx.EXPAND),
                            (wx.Button(self, label='2'), 0, wx.EXPAND),
                            (wx.Button(self, label='3'), 0, wx.EXPAND),
                            (wx.Button(self, label='-'), 0, wx.EXPAND),
                            (wx.Button(self, label='0'), 0, wx.EXPAND),
                            (wx.Button(self, label='.'), 0, wx.EXPAND),
                            (wx.Button(self, label='='), 0, wx.EXPAND),
                            (wx.Button(self, label='+'), 0, wx.EXPAND)])

        vertical_box.Add(grid_sizer, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vertical_box)
        self.Center()
        self.Show()


class ReviewFrame(wx.Frame):

    def __init__(self, parent, title):
        super(ReviewFrame, self).__init__(parent, title=title, size=(300, 250))

        panel = wx.Panel(self)
        horizontal_box = wx.BoxSizer(wx.HORIZONTAL)
        flex_grid_sizer = wx.FlexGridSizer(3, 2, 9, 25)
        title = wx.StaticText(panel, label="Title")
        author = wx.StaticText(panel, label="Author")
        review = wx.StaticText(panel, label="Review")

        text_control_1 = wx.TextCtrl(panel)
        text_control_2 = wx.TextCtrl(panel)
        text_control_3 = wx.TextCtrl(panel)

        flex_grid_sizer.AddMany(
            [title, (text_control_1, 1, wx.EXPAND), author, (text_control_2, 1, wx.EXPAND), (review, 1, wx.EXPAND),
             (text_control_3, 1, wx.EXPAND)])
        flex_grid_sizer.AddGrowableRow(2, 1)
        flex_grid_sizer.AddGrowableCol(1, 1)

        horizontal_box.Add(flex_grid_sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(horizontal_box)

        self.Center()
        self.Show()


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(320, 130))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(panel, label="Rename To")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3))
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)


class Proof(wx.Frame):

    def list_to_string(self, list):
        result = ""
        for element in list:
            result = result + element + ", "
        return result[:len(result) - 2]

    def add_simple_field(self, name):  # syntactic sugar here
        name = name.replace(' ', '_')
        setattr(self, 'label_' + name.lower(), wx.StaticText(self.panel, label=name.replace('_', ' ')))
        setattr(self, 'text_' + name.lower(), wx.TextCtrl(self.panel))
        exec(
            "self.sizer.Add(self.label_" + name.lower() + ", pos=(" + str(self.counter) +
            ", 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)")
        exec(
            'self.sizer.Add(self.text_' + name.lower() + ', pos=(' + str(self.counter) +
            ', 1), span=(1, 4), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)')
        self.counter = self.counter + 1

    def add_line(self, label, text, position):
        self.sizer.Add(label, pos=(position, 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        self.sizer.Add(text, pos=(position, 1), span=(1, 1), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)

    def __init__(self, parent, title):
        super(Proof, self).__init__(parent, title=title, size=(550, 400))

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New')
        file_menu_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open')
        file_menu_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save')
        file_menu.Append(file_menu_new)
        file_menu.Append(file_menu_open)
        file_menu.Append(file_menu_save)
        file_menu_exit = wx.MenuItem(file_menu, wx.ID_EXIT, '&Ankide\tCtrl+A')
        file_menu.Append(file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)

        self.panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, style=wx.TAB_TRAVERSAL, name='Panel')
        self.panel.SetAutoLayout(1)
        self.panel.SetupScrolling()
        self.sizer = wx.GridBagSizer(5, 5)

        self.counter = 0

        self.add_simple_field('Timeout')
        self.add_simple_field('Homework')
        self.add_simple_field('Email Address')

        label_password = wx.StaticText(self.panel, label="Password")
        self.sizer.Add(label_password, pos=(3, 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        text_password = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        self.sizer.Add(text_password, pos=(3, 1), span=(1, 4), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)
        self.counter = self.counter + 1  # password field

        self.add_simple_field('Email Server')
        self.add_simple_field('Email Server Port')
        self.add_simple_field('Imap Server Address')
        self.add_simple_field('Subject')
        self.add_simple_field('Zip Format')
        self.add_simple_field('Grade Email Subject')
        self.add_simple_field('Grade Email Body')
        self.add_simple_field('SheetsScopes')
        self.add_simple_field('Sheets Application Name')
        self.add_simple_field('Sheets Key')
        self.add_simple_field('Sheets Id')
        self.add_simple_field('Build String')
        self.add_simple_field('Exe Filename')
        self.add_simple_field('Checker Path')

        self.button_checker_path = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnCheckerPathBrowse, self.button_checker_path)
        self.sizer.Add(self.button_checker_path, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_simple_field('Relative Download Path')
        self.add_simple_field('Relative Checker Path')
        self.add_simple_field('Input Files')
        self.button_in_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnInFilesBrowser, self.button_in_files)
        self.sizer.Add(self.button_in_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1
        self.add_simple_field('Output Files')
        self.button_out_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnOutFilesBrowser, self.button_out_files)
        self.sizer.Add(self.button_out_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1
        self.add_simple_field('Reference Files')
        self.button_refrence_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnOutFilesBrowser, self.button_refrence_files)
        self.sizer.Add(self.button_refrence_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.sizer.AddGrowableCol(1)

        self.panel.SetSizerAndFit(self.sizer)
        self.Center()
        self.Show()

    def OnCheckerPathBrowse(self, e):
        dialog_checker_path = wx.DirDialog(self.panel, "Choose Checker Path", "",
                                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if (dialog_checker_path.ShowModal() == wx.ID_OK):
            chosen_path = dialog_checker_path.GetPath()
            self.text_checker_path.SetValue(chosen_path)

    def OnInFilesBrowser(self, e):
        dialog_in_files = wx.FileDialog(self.panel, "Choose Input Files", "", "", "All files (*.*)|*.*",
                                        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_in_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_in_files.GetPaths()
            all_files_names = dialog_in_files.GetFilenames()
            self.text_input_files.SetValue(self.list_to_string(all_files_names))

    def OnOutFilesBrowser(self, e):
        dialog_out_files = wx.FileDialog(self.panel, "Choose Output Files", "", "", "All files (*.*)|*.*",
                                         wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_out_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_out_files.GetPaths()
            all_files_names = dialog_out_files.GetFilenames()
            self.text_output_files.SetValue(self.list_to_string(all_files_names))

    def OnReferenceFilesBrowser(self, e):
        dialog_reference_files = wx.FileDialog(self.panel, "Choose Reference Files", "", "", "All files (*.*)|*.*",
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_reference_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_reference_files.GetPaths()
            all_files_names = dialog_reference_files.GetFilenames()
            self.text_reference_files.SetValue(self.list_to_string(all_files_names))

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    print("Here it goes")
    app = wx.App()
    Proof(None, 'ConfMe')
    app.MainLoop()
