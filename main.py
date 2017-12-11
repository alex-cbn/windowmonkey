import wx


class CenteredFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CenteredFrame, self).__init__(parent=parent, title=title, size=(350, 200))
        self.Center()
        self.Show()


if __name__ == '__main__':
    print("Here it goes")
    app = wx.App()
    CenteredFrame(None, "Op Germania")

    app.MainLoop()
