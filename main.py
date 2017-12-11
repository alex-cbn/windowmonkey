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


if __name__ == '__main__':
    print("Here it goes")
    app = wx.App()
    MenuFrameIcons(None)
    app.MainLoop()
