import re

import wx
import wx.lib.scrolledpanel as LibScrolledPanel

APP_EXIT = 1


#
#
# class CenteredFrame(wx.Frame):
#     def __init__(self, parent, title):
#         super(CenteredFrame, self).__init__(parent=parent, title=title, size=(350, 200))
#         self.Center()
#         self.Show()
#
#
# class MenuFrame(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(MenuFrame, self).__init__(*args, **kwargs)
#         self.InitUi()
#
#     def InitUi(self):
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         file_menu_exit = wx.MenuItem(wx.ID_EXIT, 'Eject', 'Ankide acola')
#         menu_bar.Append(file_menu, '&File')
#         self.SetMenuBar(menu_bar)
#         self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
#         self.SetSize((300, 200))
#         self.SetTitle('Frame with menu')
#         self.Center()
#         self.Show()
#
#     def OnQuit(self, e):
#         self.Close()
#
#
# class MenuFrameIcons(MenuFrame):
#     def __init__(self, *args, **kwargs):
#         super(MenuFrameIcons, self).__init__(*args, **kwargs)
#         self.InitUi()
#
#     def InitUi(self):
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         file_menu_exit = wx.MenuItem(file_menu, APP_EXIT, '&Eject\tCtrl+C')
#         file_menu_exit.SetBitmap(wx.Bitmap('exit.bmp'))
#         file_menu.Append(file_menu_exit)
#         self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
#         menu_bar.Append(file_menu, '&File')
#         self.SetMenuBar(menu_bar)
#         self.SetSize((350, 300))
#         self.SetTitle('Icons and shortcuts')
#         self.Center()
#         self.Show(True)
#
#     def OnQuit(self, e):
#         self.Close()
#
#
# class SubMenuFrame(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(SubMenuFrame, self).__init__(*args, *kwargs)
#         self.Initialize()
#
#     def Initialize(self):
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         file_menu_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New')
#         file_menu_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open')
#         file_menu_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save')
#         file_menu.Append(file_menu_new)
#         file_menu.Append(file_menu_open)
#         file_menu.Append(file_menu_save)
#         file_menu.AppendSeparator()
#         import_menu = wx.Menu()
#         import_menu.Append(wx.ID_ANY, 'Import newsfeed list...')
#         import_menu.Append(wx.ID_ANY, 'Import bookmarks...')
#         import_menu.Append(wx.ID_ANY, 'Import mail...')
#         file_menu.Append(wx.ID_ANY, 'I&mport', import_menu)
#         file_menu.AppendSeparator()
#         file_menu_exit = wx.MenuItem(file_menu, wx.ID_EXIT, '&Ankide\tCtrl+A')
#         file_menu.Append(file_menu_exit)
#         self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
#         menu_bar.Append(file_menu, '&File')
#         self.SetMenuBar(menu_bar)
#         self.SetSize((350, 250))
#         self.SetTitle('Submenus')
#         self.Center()
#         self.Show(True)
#
#     def OnQuit(self, e):
#         self.Close()
#
#
# class MenuItemTypes(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(MenuItemTypes, self).__init__(*args, **kwargs)
#         self.OnInit()
#
#     def OnInit(self):
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         view_menu = wx.Menu()
#         self.view_menu_show_toolbar = wx.MenuItem(view_menu, wx.ID_ANY, 'Show toolbar', 'Show Toolbar',
#                                                   kind=wx.ITEM_CHECK)
#         self.view_menu_show_statubar = wx.MenuItem(view_menu, wx.ID_ANY, 'Show statusbar', 'Show Statusbar',
#                                                    kind=wx.ITEM_CHECK)
#         view_menu.Append(self.view_menu_show_toolbar)
#         view_menu.Append(self.view_menu_show_statubar)
#         self.view_menu_show_statubar.Check(True)
#         self.view_menu_show_toolbar.Check(True)
#         self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.view_menu_show_toolbar)
#         self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.view_menu_show_statubar)
#         menu_bar.Append(file_menu, '&File')
#         menu_bar.Append(view_menu, '&View')
#         self.SetMenuBar(menu_bar)
#
#         self.toolbar = self.CreateToolBar()
#         self.toolbar.AddTool(1, '', wx.Bitmap('exit.bmp'))
#         self.toolbar.Realize()
#
#         self.statusbar = self.CreateStatusBar()
#         self.statusbar.SetStatusText('Ready')
#
#         self.SetSize((350, 250))
#         self.SetTitle('Check Menu Item')
#         self.Center()
#         self.Show(True)
#
#         self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
#
#     def ToggleStatusBar(self, e):
#         if self.view_menu_show_statubar.IsChecked():
#             self.statusbar.Show()
#         else:
#             self.statusbar.Hide()
#
#     def ToggleToolBar(self, e):
#         if self.view_menu_show_toolbar.IsChecked():
#             self.toolbar.Show()
#         else:
#             self.toolbar.Hide()
#
#     def OnRightDown(self, e):
#         self.PopupMenu(PopUpMenu(self), e.GetPosition())
#
#
# class PopUpMenu(wx.Menu):
#
#     def __init__(self, parent):
#         super(PopUpMenu, self).__init__()
#         self.parent = parent
#
#         menu_minimize = wx.MenuItem(self, wx.NewId(), 'Minimize')
#         self.Append(menu_minimize)
#         self.Bind(wx.EVT_MENU, self.OnMinimize, menu_minimize)
#
#         menu_close = wx.MenuItem(self, wx.NewId(), 'Close')
#         self.Append(menu_close)
#         self.Bind(wx.EVT_MENU, self.OnClose, menu_close)
#
#     def OnMinimize(self, e):
#         self.parent.Iconize()
#
#     def OnClose(self, e):
#         self.parent.Close()
#
#
# class PanelTextFrame(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(PanelTextFrame, self).__init__(parent, title=title, size=(260, 180))
#         panel = wx.Panel(self, wx.ID_ANY)
#         menu_bar = wx.MenuBar()
#         menu_cyka = wx.Menu()
#         menu_blyat = wx.Menu()
#         menu_bar.Append(menu_cyka, '&Cyka')
#         menu_bar.Append(menu_blyat, '&Blyat')
#         self.SetMenuBar(menu_bar)
#         wx.TextCtrl(panel, pos=(3, 3), size=(50, 50))
#         self.Center()
#         self.Show()
#
#
# class BoxSizerFrame(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(BoxSizerFrame, self).__init__(parent, title=title, size=(260, 160))
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         edit_menu = wx.Menu()
#         help_menu = wx.Menu()
#         menu_bar.Append(file_menu, '&File')
#         menu_bar.Append(edit_menu, '&Edit')
#         menu_bar.Append(help_menu, '&Help')
#         self.SetMenuBar(menu_bar)
#         wx.TextCtrl(self)
#         self.Center()
#         self.Show()
#
#
# class BoxFrame(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(BoxFrame, self).__init__(parent, title=title, size=(350, 250))
#         panel = wx.Panel(self)
#         panel.SetBackgroundColour('#ff0000')
#         vertical_box = wx.BoxSizer(wx.VERTICAL)
#         median_panel = wx.Panel(panel)
#         median_panel.SetBackgroundColour('#00ff00')
#         vertical_box.Add(median_panel, 1, wx.EXPAND | wx.ALL, 20)
#         panel.SetSizer(vertical_box)
#         self.Center()
#         self.Show()
#
#
# class GoToClass(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(GoToClass, self).__init__(parent, title=title, size=(540, 420))
#         panel = wx.Panel(self)
#
#         font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
#         font.SetPointSize(9)
#
#         vertical_box = wx.BoxSizer(wx.VERTICAL)
#
#         horizontal_box = wx.BoxSizer(wx.HORIZONTAL)
#         label = wx.StaticText(panel, label='Class Name')
#         label.SetFont(font)
#         horizontal_box.Add(label, flag=wx.RIGHT, border=8)
#         text_control = wx.TextCtrl(panel)
#         horizontal_box.Add(text_control, proportion=1)
#         vertical_box.Add(horizontal_box, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
#
#         vertical_box.Add((-1, 10))
#
#         horizontal_box_2 = wx.BoxSizer(wx.HORIZONTAL)
#         label2 = wx.StaticText(panel, label='Matching Classes')
#         label2.SetFont(font)
#         horizontal_box_2.Add(label2)
#         vertical_box.Add(horizontal_box_2, flag=wx.LEFT | wx.TOP, border=10)
#
#         vertical_box.Add((-1, 10))
#
#         horizontal_box_3 = wx.BoxSizer(wx.HORIZONTAL)
#         text_control_2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
#         horizontal_box_3.Add(text_control_2, proportion=1, flag=wx.EXPAND)
#         vertical_box.Add(horizontal_box_3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
#                          border=10)
#
#         vertical_box.Add((-1, 25))
#
#         horizontal_box_4 = wx.BoxSizer(wx.HORIZONTAL)
#         checkbox_1 = wx.CheckBox(panel, label='Case Sensitive')
#         checkbox_1.SetFont(font)
#         horizontal_box_4.Add(checkbox_1, flag=wx.LEFT, border=10)
#         check_box_2 = wx.CheckBox(panel, label='Nested Classes')
#         check_box_2.SetFont(font)
#         horizontal_box_4.Add(check_box_2, flag=wx.LEFT, border=10)
#         check_box_3 = wx.CheckBox(panel, label='Non-Project classes')
#         check_box_3.SetFont(font)
#         horizontal_box_4.Add(check_box_3, flag=wx.LEFT, border=10)
#         vertical_box.Add(horizontal_box_4, flag=wx.LEFT, border=10)
#
#         vertical_box.Add((-1, 25))
#
#         horizontal_box_5 = wx.BoxSizer(wx.HORIZONTAL)
#         button_1 = wx.Button(panel, label='Ok', size=(70, 30))
#         horizontal_box_5.Add(button_1, flag=wx.LEFT | wx.BOTTOM)
#         button_2 = wx.Button(panel, label='Close', size=(70, 30))
#         horizontal_box_5.Add(button_2, flag=wx.LEFT | wx.BOTTOM, border=5)
#         vertical_box.Add(horizontal_box_5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
#
#         panel.SetSizer(vertical_box)
#         self.Center()
#         self.Show()
#
#
# class Calculator(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(Calculator, self).__init__(parent, title=title, size=(300, 250))
#         menu_bar = wx.MenuBar()
#         file_menu = wx.Menu()
#         menu_bar.Append(file_menu, '&File')
#         self.SetMenuBar(menu_bar)
#         vertical_box = wx.BoxSizer(wx.VERTICAL)
#         self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
#         vertical_box.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
#         grid_sizer = wx.GridSizer(5, 4, 5, 5)
#
#         grid_sizer.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
#                             (wx.Button(self, label='Bck'), 0, wx.EXPAND),
#                             (wx.StaticText(self), wx.EXPAND),
#                             (wx.Button(self, label='Close'), 0, wx.EXPAND),
#                             (wx.Button(self, label='7'), 0, wx.EXPAND),
#                             (wx.Button(self, label='8'), 0, wx.EXPAND),
#                             (wx.Button(self, label='9'), 0, wx.EXPAND),
#                             (wx.Button(self, label='/'), 0, wx.EXPAND),
#                             (wx.Button(self, label='4'), 0, wx.EXPAND),
#                             (wx.Button(self, label='5'), 0, wx.EXPAND),
#                             (wx.Button(self, label='6'), 0, wx.EXPAND),
#                             (wx.Button(self, label='*'), 0, wx.EXPAND),
#                             (wx.Button(self, label='1'), 0, wx.EXPAND),
#                             (wx.Button(self, label='2'), 0, wx.EXPAND),
#                             (wx.Button(self, label='3'), 0, wx.EXPAND),
#                             (wx.Button(self, label='-'), 0, wx.EXPAND),
#                             (wx.Button(self, label='0'), 0, wx.EXPAND),
#                             (wx.Button(self, label='.'), 0, wx.EXPAND),
#                             (wx.Button(self, label='='), 0, wx.EXPAND),
#                             (wx.Button(self, label='+'), 0, wx.EXPAND)])
#
#         vertical_box.Add(grid_sizer, proportion=1, flag=wx.EXPAND)
#         self.SetSizer(vertical_box)
#         self.Center()
#         self.Show()
#
#
# class ReviewFrame(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(ReviewFrame, self).__init__(parent, title=title, size=(300, 250))
#
#         panel = wx.Panel(self)
#         horizontal_box = wx.BoxSizer(wx.HORIZONTAL)
#         flex_grid_sizer = wx.FlexGridSizer(3, 2, 9, 25)
#         title = wx.StaticText(panel, label="Title")
#         author = wx.StaticText(panel, label="Author")
#         review = wx.StaticText(panel, label="Review")
#
#         text_control_1 = wx.TextCtrl(panel)
#         text_control_2 = wx.TextCtrl(panel)
#         text_control_3 = wx.TextCtrl(panel)
#
#         flex_grid_sizer.AddMany(
#             [title, (text_control_1, 1, wx.EXPAND), author, (text_control_2, 1, wx.EXPAND), (review, 1, wx.EXPAND),
#              (text_control_3, 1, wx.EXPAND)])
#         flex_grid_sizer.AddGrowableRow(2, 1)
#         flex_grid_sizer.AddGrowableCol(1, 1)
#
#         horizontal_box.Add(flex_grid_sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
#         panel.SetSizer(horizontal_box)
#
#         self.Center()
#         self.Show()
#
#
# class Example(wx.Frame):
#
#     def __init__(self, parent, title):
#         super(Example, self).__init__(parent, title=title,
#                                       size=(320, 130))
#
#         self.InitUI()
#         self.Centre()
#         self.Show()
#
#     def InitUI(self):
#         panel = wx.Panel(self)
#         sizer = wx.GridBagSizer(4, 4)
#
#         text = wx.StaticText(panel, label="Rename To")
#         sizer.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
#
#         tc = wx.TextCtrl(panel)
#         sizer.Add(tc, pos=(1, 0), span=(1, 5),
#                   flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
#
#         buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
#         buttonClose = wx.Button(panel, label="Close", size=(90, 28))
#         sizer.Add(buttonOk, pos=(3, 3))
#         sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)
#
#         sizer.AddGrowableCol(1)
#         sizer.AddGrowableRow(2)
#         panel.SetSizerAndFit(sizer)

class ConfigurationTab(wx.lib.scrolledpanel.ScrolledPanel):

    def list_to_string(self, list):
        result = ""
        for element in list:
            result = result + '\"' + element + '\"' + ", "
        result = result[:len(result) - 2]
        result = '[' + result + ']'
        result = result.replace('\\', "\\\\")
        return result

    def add_field_parent(self, name, parent):  # syntactic sugar here
        name = name.replace(' ', '_')
        setattr(self, 'label_' + name.lower(), wx.StaticText(self, label=name.replace('_', ' ')))
        setattr(self, 'text_' + name.lower(), wx.TextCtrl(self))
        cmd = parent + ".Add(self.label_" + name.lower() + ", pos=(" + \
              str(self.counter) + ", 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)"
        exec(cmd)
        cmd = parent + ".Add(self.text_" + name.lower() + ', pos=(' + str(
            self.counter) + ', 1), span=(1, 4), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)'
        exec(cmd)
        self.ConfigurationDictionary.update({name.replace('_', ' '): ''})
        self.counter = self.counter + 1

    def add_simple_field(self, name):  # syntactic sugar here
        name = name.replace(' ', '_')
        setattr(self, 'label_' + name.lower(), wx.StaticText(self, label=name.replace('_', ' ')))
        setattr(self, 'text_' + name.lower(), wx.TextCtrl(self))
        exec(
            "self.sizer.Add(self.label_" + name.lower() + ", pos=(" + str(self.counter) +
            ", 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)")
        exec(
            'self.sizer.Add(self.text_' + name.lower() + ', pos=(' + str(self.counter) +
            ', 1), span=(1, 4), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)')
        self.ConfigurationDictionary.update({name.replace('_', ' '): ''})
        self.counter = self.counter + 1

    def InitStarter(self):
        self.StarterOptionBox = wx.StaticBox(self, label="Starter Options")
        self.StarterOptionBoxSizer = wx.StaticBoxSizer(self.StarterOptionBox, wx.VERTICAL)
        self.StarterGrid = wx.GridBagSizer(5, 5)
        self.counter = 0

        self.add_field_parent('Timeout', 'self.StarterGrid')

        self.StarterGrid.AddGrowableCol(1)
        self.StarterOptionBoxSizer.Add(self.StarterGrid, flag=wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT | wx.BOTTOM)
        self.sizer.Add(self.StarterOptionBoxSizer, pos=(0, 0), span=(1, 5),
                       flag=wx.TOP | wx.LEFT | wx.EXPAND | wx.RIGHT | wx.BOTTOM, border=5)

    def InitEmail(self):
        self.EmailOptionBox = wx.StaticBox(self, label="Email Options")
        self.EmailOptionBoxSizer = wx.StaticBoxSizer(self.EmailOptionBox, wx.VERTICAL)
        self.EmailGrid = wx.GridBagSizer(5, 5)
        self.counter = 0

        self.add_field_parent('Email Address', 'self.EmailGrid')

        self.label_password = wx.StaticText(self, label="Password")
        self.EmailGrid.Add(self.label_password, pos=(self.counter, 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                           border=5)
        self.text_password = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.EmailGrid.Add(self.text_password, pos=(self.counter, 1), span=(1, 4),
                           flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP,
                           border=5)
        self.ConfigurationDictionary.update({'Password': ''})
        self.counter = self.counter + 1

        self.add_field_parent('Email Server Address', 'self.EmailGrid')
        self.add_field_parent('Email Server Port', 'self.EmailGrid')
        self.add_field_parent('Imap Server Address', 'self.EmailGrid')
        self.add_field_parent('Subject', 'self.EmailGrid')
        self.add_field_parent('Zip Format', 'self.EmailGrid')
        self.add_field_parent('Grade Email Subject', 'self.EmailGrid')
        self.add_field_parent('Grade Email Body', 'self.EmailGrid')

        self.EmailGrid.AddGrowableCol(1)
        self.EmailOptionBoxSizer.Add(self.EmailGrid, flag=wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT | wx.BOTTOM)
        self.sizer.Add(self.EmailOptionBoxSizer, pos=(1, 0), span=(1, 5),
                       flag=wx.TOP | wx.LEFT | wx.EXPAND | wx.BOTTOM, border=5)

    def InitSheets(self):
        self.SheetsOptionBox = wx.StaticBox(self, label="Sheets Options")
        self.SheetsOptionBoxSizer = wx.StaticBoxSizer(self.SheetsOptionBox, wx.VERTICAL)
        self.SheetsGrid = wx.GridBagSizer(5, 5)
        self.counter = 0

        self.add_field_parent('Sheets Secret File', 'self.SheetsGrid')
        self.button_secret_file = wx.Button(self, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSecretFileBrowser, self.button_secret_file)
        self.SheetsGrid.Add(self.button_secret_file, pos=(self.counter, 4), span=(1, 1), flag=wx.EXPAND | wx.RIGHT,
                            border=5)
        self.counter = self.counter + 1

        self.add_field_parent('Sheets Scopes', 'self.SheetsGrid')
        self.add_field_parent('Sheets Application Name', 'self.SheetsGrid')
        self.add_field_parent('Sheets Key', 'self.SheetsGrid')
        self.add_field_parent('Sheets Id', 'self.SheetsGrid')

        self.SheetsGrid.AddGrowableCol(1)
        self.SheetsOptionBoxSizer.Add(self.SheetsGrid, flag=wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT)
        self.sizer.Add(self.SheetsOptionBoxSizer, pos=(2, 0), span=(1, 5),
                       flag=wx.TOP | wx.LEFT | wx.EXPAND | wx.BOTTOM, border=5)

    def InitHomework(self):
        self.HomeworkOptionBox = wx.StaticBox(self, label="Homework Options")
        self.HomeworkOptionBoxSizer = wx.StaticBoxSizer(self.HomeworkOptionBox, wx.VERTICAL)
        self.HomeworkGrid = wx.GridBagSizer(5, 5)
        self.counter = 0

        self.add_field_parent('Build String', 'self.HomeworkGrid')
        self.add_field_parent('Exe Filename', 'self.HomeworkGrid')
        self.add_field_parent('Homework', 'self.HomeworkGrid')
        self.add_field_parent('Absolute Path', 'self.HomeworkGrid')

        self.button_checker_path = wx.Button(self, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnCheckerPathBrowse, self.button_checker_path)
        self.HomeworkGrid.Add(self.button_checker_path, pos=(self.counter, 4), span=(1, 1), flag=wx.RIGHT | wx.EXPAND,
                              border=5)
        self.counter = self.counter + 1

        self.add_field_parent('Relative Download Path', 'self.HomeworkGrid')
        self.add_field_parent('Relative Checker Path', 'self.HomeworkGrid')

        self.HomeworkGrid.AddGrowableCol(1)
        self.HomeworkOptionBoxSizer.Add(self.HomeworkGrid, flag=wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT)
        self.sizer.Add(self.HomeworkOptionBoxSizer, pos=(3, 0), span=(1, 5),
                       flag=wx.TOP | wx.LEFT | wx.EXPAND | wx.BOTTOM, border=5)

    def InitTest(self):
        self.TestOptionBox = wx.StaticBox(self, label="Tests Options")
        self.TestOptionBoxSizer = wx.StaticBoxSizer(self.TestOptionBox, wx.VERTICAL)
        self.TestGrid = wx.GridBagSizer(5, 5)
        self.counter = 0

        self.add_field_parent('In Files', 'self.TestGrid')
        self.button_in_files = wx.Button(self, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnInFilesBrowser, self.button_in_files)
        self.TestGrid.Add(self.button_in_files, pos=(self.counter, 4), span=(1, 1), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_field_parent('Out Files', 'self.TestGrid')
        self.button_out_files = wx.Button(self, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnOutFilesBrowser, self.button_out_files)
        self.TestGrid.Add(self.button_out_files, pos=(self.counter, 4), span=(1, 1), flag=wx.EXPAND | wx.RIGHT,
                          border=5)
        self.counter = self.counter + 1

        self.add_field_parent('Reference Files', 'self.TestGrid')
        self.button_reference_files = wx.Button(self, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnReferenceFilesBrowser, self.button_reference_files)
        self.TestGrid.Add(self.button_reference_files, pos=(self.counter, 4), span=(1, 1), flag=wx.EXPAND | wx.RIGHT,
                          border=5)
        self.counter = self.counter + 1

        self.TestGrid.AddGrowableCol(1)
        self.TestOptionBoxSizer.Add(self.TestGrid, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM)
        self.sizer.Add(self.TestOptionBoxSizer, pos=(4, 0), span=(1, 5),
                       flag=wx.TOP | wx.LEFT | wx.EXPAND | wx.BOTTOM, border=5)

    def __init__(self, parent):
        super(ConfigurationTab, self).__init__(parent, -1, style=wx.TAB_TRAVERSAL, name='Panel')

        self.ConfigurationDictionary = dict()
        self.OpenedConfigPath = ""

        self.SetAutoLayout(1)
        self.SetupScrolling()
        self.sizer = wx.GridBagSizer(5, 5)

        self.InitStarter()
        self.InitEmail()
        self.InitSheets()
        self.InitHomework()
        self.InitTest()

        self.sizer.AddGrowableCol(1)
        self.SetSizerAndFit(self.sizer)

    def OnCheckerPathBrowse(self, e):
        dialog_checker_path = wx.DirDialog(self, "Choose Checker Path", "",
                                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dialog_checker_path.ShowModal() == wx.ID_OK:
            chosen_path = dialog_checker_path.GetPath()
            self.text_absolute_path.SetValue(chosen_path)

    def OnSecretFileBrowser(self, e):
        dialog_secret_file = wx.FileDialog(self, "Choose Secret File", "", "", "Json file (*.json)|*.json",
                                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog_secret_file.ShowModal() == wx.ID_OK:
            secret_path = dialog_secret_file.GetPath()
            self.text_sheets_secret_file.SetValue(secret_path)

    def OnInFilesBrowser(self, e):
        dialog_in_files = wx.FileDialog(self, "Choose Input Files", "", "", "All files (*.*)|*.*",
                                        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_in_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_in_files.GetPaths()
            self.text_in_files.SetValue(self.list_to_string(all_files_path))

    def OnOutFilesBrowser(self, e):
        dialog_out_files = wx.FileDialog(self, "Choose Output Files", "", "", "All files (*.*)|*.*",
                                         wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_out_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_out_files.GetPaths()
            self.text_out_files.SetValue(self.list_to_string(all_files_path))

    def OnReferenceFilesBrowser(self, e):
        dialog_reference_files = wx.FileDialog(self, "Choose Reference Files", "", "", "All files (*.*)|*.*",
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if dialog_reference_files.ShowModal() == wx.ID_OK:
            all_files_path = dialog_reference_files.GetPaths()
            self.text_reference_files.SetValue(self.list_to_string(all_files_path))

    def UpdateConfiguration(self):
        for item in self.ConfigurationDictionary.keys():
            var_name = item
            var_name = var_name.replace(' ', '_')
            var_name = var_name.lower()
            var_name = 'self.text_' + var_name
            command = 'self.ConfigurationDictionary.update({\'' + item + '\':' + var_name + '.GetValue()})'
            exec(command)

    def WriteConfiguration(self, filename):
        try:
            with open(filename, 'w') as file:
                for item in self.ConfigurationDictionary.keys():
                    if item == "In Files" or item == "Out Files" or item == "Reference Files":
                        line = item.replace(' ', '') + ' = '
                        right = self.ConfigurationDictionary[item]
                        right = right.replace('[', '')
                        right = right.replace(']', '')
                        line = line + "[" + right + "]\n"
                    else:
                        line = item.replace(' ', '') + ' = ' + '\'' + self.ConfigurationDictionary[item] + '\'\n'
                    line = line.replace('\\', '\\\\')
                    file.write(line)
        except IOError:
            wx.LogError('Fak')
            print('Fakk')

    def LoadConfiguration(self):
        for item in self.ConfigurationDictionary.keys():
            var_name = item
            var_name = var_name.replace(' ', '_')
            var_name = var_name.lower()
            var_name = 'self.text_' + var_name
            itemvalue = self.ConfigurationDictionary[item]
            if itemvalue == " ":
                itemvalue = ""
            command = var_name + '.SetValue(\'' + itemvalue + '\')'
            exec(command)

    def ReadConfiguration(self, filename):
        try:
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    if line != "":
                        left = line.split('=')[0]
                        right = line.split('=')[1]
                        left = left.strip()
                        right = right.strip()
                        if left == "InFiles" or left == "OutFiles" or left == "ReferenceFiles":
                            right = right
                        else:
                            right = right.replace('\'', "")
                        left = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", left)
                        self.ConfigurationDictionary.update({left: right})
                    line = file.readline()
        except IOError:
            wx.LogError('Fak')


class MainWindowTabbed(wx.Frame):

    def __init__(self, parent, title):
        super(MainWindowTabbed, self).__init__(parent, title=title, size=(550, 400))

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New')
        file_menu_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open')
        file_menu_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save')
        file_menu_save_as = wx.MenuItem(file_menu, wx.ID_SAVEAS, 'Save &As')
        file_menu.Append(file_menu_new)
        file_menu.Append(file_menu_open)
        file_menu.Append(file_menu_save)
        file_menu.Append(file_menu_save_as)
        file_menu_exit = wx.MenuItem(file_menu, wx.ID_EXIT, 'E&xit\tCtrl+X')
        file_menu.Append(file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnNew, file_menu_new)
        self.Bind(wx.EVT_MENU, self.OnOpen, file_menu_open)
        self.Bind(wx.EVT_MENU, self.OnSave, file_menu_save)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, file_menu_save_as)
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)

        self.main_panel = wx.Panel(self)
        self.notebook = wx.Notebook(self.main_panel)
        self.tab_1 = ConfigurationTab(self.notebook)
        self.notebook.AddPage(self.tab_1, "Configuration")

        sizer = wx.BoxSizer()
        sizer.Add(self.notebook, 1, wx.EXPAND)
        self.main_panel.SetSizer(sizer)

        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icon)

        self.Center()
        self.Show()

    def OnQuit(self, e):
        self.Close()

    def OnNew(self, e):
        self.tab_1.OpenedConfigPath = ""
        for item in self.tab_1.ConfigurationDictionary:
            self.tab_1.ConfigurationDictionary.update({item: ' '})
        self.tab_1.LoadConfiguration()

    def OnOpen(self, e):
        dialog_open = wx.FileDialog(self.tab_1, "Import Configuration", "", "", "Python Configuration (*.py)|*.py",
                                    wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog_open.ShowModal() == wx.ID_OK:
            self.tab_1.OpenedConfigPath = dialog_open.GetPath()
            self.tab_1.ReadConfiguration(self.tab_1.OpenedConfigPath)
            self.tab_1.LoadConfiguration()

    def OnSave(self, e):
        if self.tab_1.OpenedConfigPath == "":
            self.OnSaveAs(e)
        else:
            self.tab_1.UpdateConfiguration()
            self.tab_1.WriteConfiguration(self.tab_1.OpenedConfigPath)

    def OnSaveAs(self, e):
        dialog_save = wx.FileDialog(self.tab_1, "Save Configuration", wildcard=".py files (*.py)|*.py",
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dialog_save.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog_save.GetPath()
        self.tab_1.UpdateConfiguration()
        self.tab_1.WriteConfiguration(pathname)
        self.tab_1.OpenedConfigPath = pathname


class MainWindow(wx.Frame):

    def list_to_string(self, list):
        result = ""
        for element in list:
            result = result + '\'' + element + '\'' + ", "
        result = result[:len(result) - 2]
        result = '[' + result + ']'
        result = result.replace('\\', "\\\\")
        return result

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
        self.ConfigurationDictionary.update({name.replace('_', ' '): ''})
        self.counter = self.counter + 1

    def add_line(self, label, text, position):
        self.sizer.Add(label, pos=(position, 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        self.sizer.Add(text, pos=(position, 1), span=(1, 1), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=5)

    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(550, 400))

        self.ConfigurationDictionary = dict()
        self.OpenedConfigPath = ""

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New')
        file_menu_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open')
        file_menu_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save')
        file_menu_save_as = wx.MenuItem(file_menu, wx.ID_SAVEAS, 'Save &As')
        file_menu.Append(file_menu_new)
        file_menu.Append(file_menu_open)
        file_menu.Append(file_menu_save)
        file_menu.Append(file_menu_save_as)
        file_menu_exit = wx.MenuItem(file_menu, wx.ID_EXIT, 'E&xit\tCtrl+X')
        file_menu.Append(file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnQuit, file_menu_exit)
        self.Bind(wx.EVT_MENU, self.OnNew, file_menu_new)
        self.Bind(wx.EVT_MENU, self.OnOpen, file_menu_open)
        self.Bind(wx.EVT_MENU, self.OnSave, file_menu_save)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, file_menu_save_as)
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

        self.label_password = wx.StaticText(self.panel, label="Password")
        self.sizer.Add(self.label_password, pos=(3, 0), span=(1, 1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        self.text_password = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        self.sizer.Add(self.text_password, pos=(3, 1), span=(1, 4), flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP,
                       border=5)
        self.counter = self.counter + 1  # password field
        self.ConfigurationDictionary.update({'Password': ''})

        self.add_simple_field('Email Server Address')
        self.add_simple_field('Email Server Port')
        self.add_simple_field('Imap Server Address')
        self.add_simple_field('Subject')
        self.add_simple_field('Zip Format')
        self.add_simple_field('Grade Email Subject')
        self.add_simple_field('Grade Email Body')

        self.add_simple_field('Sheets Secret File')
        self.button_secret_file = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSecretFileBrowser, self.button_secret_file)
        self.sizer.Add(self.button_secret_file, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_simple_field('Sheets Scopes')
        self.add_simple_field('Sheets Application Name')
        self.add_simple_field('Sheets Key')
        self.add_simple_field('Sheets Id')
        self.add_simple_field('Build String')
        self.add_simple_field('Exe Filename')
        self.add_simple_field('Absolute Path')

        self.button_checker_path = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnCheckerPathBrowse, self.button_checker_path)
        self.sizer.Add(self.button_checker_path, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_simple_field('Relative Download Path')
        self.add_simple_field('Relative Checker Path')

        self.add_simple_field('In Files')
        self.button_in_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnInFilesBrowser, self.button_in_files)
        self.sizer.Add(self.button_in_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_simple_field('Out Files')
        self.button_out_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnOutFilesBrowser, self.button_out_files)
        self.sizer.Add(self.button_out_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.add_simple_field('Reference Files')
        self.button_reference_files = wx.Button(self.panel, label="Browse...", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnReferenceFilesBrowser, self.button_reference_files)
        self.sizer.Add(self.button_reference_files, pos=(self.counter, 4), flag=wx.EXPAND | wx.RIGHT, border=5)
        self.counter = self.counter + 1

        self.sizer.AddGrowableCol(1)

        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icon)

        self.panel.SetSizerAndFit(self.sizer)
        self.Center()
        self.Show()

    def OnCheckerPathBrowse(self, e):
        dialog_checker_path = wx.DirDialog(self.panel, "Choose Checker Path", "",
                                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dialog_checker_path.ShowModal() == wx.ID_OK:
            chosen_path = dialog_checker_path.GetPath()
            self.text_absolute_path.SetValue(chosen_path)

    def OnSecretFileBrowser(self, e):
        dialog_secret_file = wx.FileDialog(self.panel, "Choose Secret File", "", "", "Json file (*.json)|*.json",
                                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog_secret_file.ShowModal() == wx.ID_OK:
            secret_path = dialog_secret_file.GetPath()
            self.text_sheets_secret.SetValue(secret_path)

    def OnInFilesBrowser(self, e):
        dialog_in_files = wx.FileDialog(self.panel, "Choose Input Files", "", "", "All files (*.*)|*.*",
                                        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_in_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_in_files.GetPaths()
            self.text_input_files.SetValue(self.list_to_string(all_files_path))

    def OnOutFilesBrowser(self, e):
        dialog_out_files = wx.FileDialog(self.panel, "Choose Output Files", "", "", "All files (*.*)|*.*",
                                         wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if (dialog_out_files.ShowModal() == wx.ID_OK):
            all_files_path = dialog_out_files.GetPaths()
            self.text_output_files.SetValue(self.list_to_string(all_files_path))

    def OnReferenceFilesBrowser(self, e):
        dialog_reference_files = wx.FileDialog(self.panel, "Choose Reference Files", "", "", "All files (*.*)|*.*",
                                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
        if dialog_reference_files.ShowModal() == wx.ID_OK:
            all_files_path = dialog_reference_files.GetPaths()
            self.text_reference_files.SetValue(self.list_to_string(all_files_path))

    def OnQuit(self, e):
        self.Close()

    def OnNew(self, e):
        self.OpenedConfigPath = ""
        for item in self.ConfigurationDictionary:
            self.ConfigurationDictionary.update({item: ' '})
        self.LoadConfiguration()

    def OnOpen(self, e):
        dialog_open = wx.FileDialog(self.panel, "Import Configuration", "", "", "Python Configuration (*.py)|*.py",
                                    wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog_open.ShowModal() == wx.ID_OK:
            self.OpenedConfigPath = dialog_open.GetPath()
            self.ReadConfiguration(self.OpenedConfigPath)
            self.LoadConfiguration()

    def OnSave(self, e):
        if self.OpenedConfigPath == "":
            self.OnSaveAs(e)
        else:
            self.UpdateConfiguration()
            self.WriteConfiguration(self.OpenedConfigPath)

    def OnSaveAs(self, e):
        dialog_save = wx.FileDialog(self.panel, "Save Configuration", wildcard=".py files (*.py)|*.py",
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dialog_save.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog_save.GetPath()
        self.UpdateConfiguration()
        self.WriteConfiguration(pathname)
        self.OpenedConfigPath = pathname

    def UpdateConfiguration(self):
        for item in self.ConfigurationDictionary.keys():
            var_name = item
            var_name = var_name.replace(' ', '_')
            var_name = var_name.lower()
            var_name = 'self.text_' + var_name
            command = 'self.ConfigurationDictionary.update({\'' + item + '\':' + var_name + '.GetValue()})'
            exec(command)

    def WriteConfiguration(self, filename):
        try:
            with open(filename, 'w') as file:
                for item in self.ConfigurationDictionary.keys():
                    line = item.replace(' ', '') + ' = ' + '\"' + self.ConfigurationDictionary[item] + '\"\n'
                    file.write(line)
        except IOError:
            wx.LogError('Fak')

    def LoadConfiguration(self):
        for item in self.ConfigurationDictionary.keys():
            var_name = item
            var_name = var_name.replace(' ', '_')
            var_name = var_name.lower()
            var_name = 'self.text_' + var_name
            itemvalue = self.ConfigurationDictionary[item]
            if itemvalue == " ":
                itemvalue = ""
            command = var_name + '.SetValue(\'' + itemvalue + '\')'
            exec(command)

    def ReadConfiguration(self, filename):
        try:
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    if line != "":
                        left = line.split('=')[0]
                        right = line.split('=')[1]
                        left = left.strip()
                        right = right.strip()
                        right = right.replace('\"', "")
                        left = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", left)
                        self.ConfigurationDictionary.update({left: right})
                    line = file.readline()
        except IOError:
            wx.LogError('Fak')


if __name__ == '__main__':
    print("Here it goes")
    app = wx.App()
    MainWindowTabbed(None, 'Checker Configurator')
    app.MainLoop()
