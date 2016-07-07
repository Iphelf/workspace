import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 0, "My Frame", size = (300, 300))
        panel = wx.Panel(self, 0)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, 0, "Pos:", pos = (10, 12))
        self.posCtrl = wx.TextCtrl(panel, 0, "", pos = (40, 10))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" %(pos.x, pos.y))
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()