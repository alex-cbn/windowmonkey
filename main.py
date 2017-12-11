import wx

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


if __name__ == '__main__':
    print("Here it goes")
    app = wx.App()
    MenuItemTypes(None)
    app.MainLoop()
