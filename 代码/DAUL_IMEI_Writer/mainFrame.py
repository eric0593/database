#Boa:Frame:imeiwriter
# -*- coding: gb2312 -*-

import wx
import wx.richtext
from comminterface import CommInterface
import binascii
import thread
import string
import time
from string import upper

def create(parent):
    return imeiwriter(parent)

[wxID_IMEIWRITER, wxID_IMEIWRITERAUTOADD1, wxID_IMEIWRITERCD_TC, 
 wxID_IMEIWRITERDAUL_IMEI, wxID_IMEIWRITERDAUL_IMEI_ESN, 
 wxID_IMEIWRITERDAUL_IMEI_MEID,wxID_IMEIWRITERONE_IMEI_ESN,wxID_IMEIWRITERONE_IMEI_MEID,
 wxID_WRITE_MEID,wxID_IMEIWRITERESN_CD, wxID_IMEIWRITERESN_TC, 
 wxID_IMEIWRITEREXIT_BTN, wxID_IMEIWRITERFIRSTIMEI, wxID_IMEIWRITERIMEI_1_CD, 
 wxID_IMEIWRITERIMEI_1_TC, wxID_IMEIWRITERIMEI_2_CD, wxID_IMEIWRITERIMEI_2_TC, 
 wxID_IMEIWRITERIMEI_TC, wxID_IMEIWRITERLED_1, wxID_IMEIWRITERLED_2, 
 wxID_IMEIWRITERLED_3, wxID_IMEIWRITERMODEL14, wxID_IMEIWRITERMODEL15, 
 wxID_IMEIWRITERPANEL, wxID_IMEIWRITERRESULT_SB, wxID_IMEIWRITERRESULT_ST, 
 wxID_IMEIWRITERSECONDIMEI, wxID_IMEIWRITERSTATICBOX1, 
 wxID_IMEIWRITERSTATICBOX2, wxID_IMEIWRITERSTATICLINE1, 
 wxID_IMEIWRITERSTATICTEXT1, wxID_IMEIWRITERSTATICTEXT2, 
 wxID_IMEIWRITERSTATUSBAR, wxID_IMEIWRITERWAITRSP, wxID_IMEIWRITERWRITE_BTN, 
] = [wx.NewId() for _init_ctrls in range(35)]

[wxID_IMEIWRITERSETTINGEXIT, wxID_IMEIWRITERSETTINGPORTSETTING, 
] = [wx.NewId() for _init_coll_Setting_Items in range(2)]

[wxID_IMEIWRITERABOUTABOUT] = [wx.NewId() for _init_coll_About_Items in range(1)]

class imeiwriter(wx.Frame):
    def _init_coll_menuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.Setting, title=u'\u8bbe\u7f6e(&S)')
        parent.Append(menu=self.About, title=u'\u5173\u4e8e(&A)')

    def _init_coll_About_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_IMEIWRITERABOUTABOUT,
              kind=wx.ITEM_NORMAL, text=u'\u5173\u4e8e(&A)...')
        self.Bind(wx.EVT_MENU, self.OnAboutAboutMenu,
              id=wxID_IMEIWRITERABOUTABOUT)

    def _init_coll_Setting_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_IMEIWRITERSETTINGPORTSETTING,
              kind=wx.ITEM_NORMAL, text=u'\u7aef\u53e3\u8bbe\u7f6e(&P)')
        parent.AppendSeparator()
        parent.Append(help=u'', id=wxID_IMEIWRITERSETTINGEXIT,
              kind=wx.ITEM_NORMAL, text=u'\u9000\u51fa(&X)')
        self.Bind(wx.EVT_MENU, self.OnSettingPortsettingMenu,
              id=wxID_IMEIWRITERSETTINGPORTSETTING)
        self.Bind(wx.EVT_MENU, self.OnSettingExitMenu,
              id=wxID_IMEIWRITERSETTINGEXIT)

    def _init_coll_statusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(2)

        parent.SetStatusText(number=0, text=u'\u72b6\u6001')
        parent.SetStatusText(number=1, text=u'Port:')

        parent.SetStatusWidths([-1, 80])

    def _init_utils(self):
        # generated method, don't edit
        self.Setting = wx.Menu(title='')

        self.About = wx.Menu(title='')

        self.menuBar = wx.MenuBar()

        self._init_coll_Setting_Items(self.Setting)
        self._init_coll_About_Items(self.About)
        self._init_coll_menuBar_Menus(self.menuBar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_IMEIWRITER, name=u'imeiwriter',
              parent=prnt, pos=wx.Point(578, 226), size=wx.Size(472, 468),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
              title=u'K组写号工具V3.1')
        self._init_utils()
        self.SetClientSize(wx.Size(464, 434))
        self.SetToolTipString(u'')
        self.Center(wx.BOTH)
        self.SetMenuBar(self.menuBar)

        self.statusBar = wx.StatusBar(id=wxID_IMEIWRITERSTATUSBAR,
              name=u'statusBar', parent=self, style=0)
        self._init_coll_statusBar_Fields(self.statusBar)
        self.SetStatusBar(self.statusBar)

        self.panel = wx.Panel(id=wxID_IMEIWRITERPANEL, name=u'panel',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(464, 332),
              style=wx.TAB_TRAVERSAL)
        self.panel.SetToolTipString(u'')
        self.panel.Enable(True)

        self.staticBox1 = wx.StaticBox(id=wxID_IMEIWRITERSTATICBOX1, label=u'',
              name='staticBox1', parent=self.panel, pos=wx.Point(8, 8),
              size=wx.Size(336, 212), style=0)

        self.staticText1 = wx.StaticText(id=wxID_IMEIWRITERSTATICTEXT1,
              label=u'IMEI\u53f7\uff1a', name='staticText1', parent=self.panel,
              pos=wx.Point(16, 24), size=wx.Size(87, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(64, 0, 64))

        self.staticBox2 = wx.StaticBox(id=wxID_IMEIWRITERSTATICBOX2, label=u'',
              name='staticBox2', parent=self.panel, pos=wx.Point(352, 8),
              size=wx.Size(104, 212), style=0)
        self.write_btn = wx.Button(id=wxID_IMEIWRITERWRITE_BTN, label=u'&Write',
              name=u'write_btn', parent=self.panel, pos=wx.Point(144, 358),
              size=wx.Size(75, 24), style=0)
        self.write_btn.SetToolTipString(u'')
        self.write_btn.Bind(wx.EVT_BUTTON, self.OnWrite_btnButton,
              id=wxID_IMEIWRITERWRITE_BTN)

        self.exit_btn = wx.Button(id=wxID_IMEIWRITEREXIT_BTN, label=u'E&xit',
              name=u'exit_btn', parent=self.panel, pos=wx.Point(256, 358),
              size=wx.Size(75, 24), style=0)
        self.exit_btn.SetToolTipString(u'')
        self.exit_btn.Bind(wx.EVT_BUTTON, self.OnExit_btnButton,
              id=wxID_IMEIWRITEREXIT_BTN)

        self.waitrsp = wx.CheckBox(id=wxID_IMEIWRITERWAITRSP,
              label=u'\u7b49\u5f85\u6d88\u606f\u5e94\u7b54', name=u'waitrsp',
              parent=self.panel, pos=wx.Point(360, 20), size=wx.Size(88, 14),
              style=0)
        self.waitrsp.SetValue(False)

        self.model14 = wx.CheckBox(id=wxID_IMEIWRITERMODEL14,
              label=u'14\u4f4d\u6a21\u5f0f', name=u'model14', parent=self.panel,
              pos=wx.Point(360, 38), size=wx.Size(79, 14), style=0)
        self.model14.SetValue(False)
        self.model14.Bind(wx.EVT_CHECKBOX, self.OnModel14Checkbox,
              id=wxID_IMEIWRITERMODEL14)

        self.autoadd1 = wx.CheckBox(id=wxID_IMEIWRITERAUTOADD1,
              label=u'\u53f7\u7801\u81ea\u52a8\u52a01', name=u'autoadd1',
              parent=self.panel, pos=wx.Point(360, 80), size=wx.Size(88, 14),
              style=0)
        self.autoadd1.SetValue(False)
        self.autoadd1.Enable(False)
        self.autoadd1.SetToolTipString(u'')

        self.imei_tc = wx.TextCtrl(id=wxID_IMEIWRITERIMEI_TC, name=u'imei_tc',
              parent=self.panel, pos=wx.Point(16, 64), size=wx.Size(280, 40),
              style=0, value=u'')
        self.imei_tc.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.imei_tc.SetMaxLength(15)
        self.imei_tc.SetToolTipString(u'')
        self.imei_tc.Bind(wx.EVT_TEXT_MAXLEN, self.OnImei_tcTextMaxlen,
              id=wxID_IMEIWRITERIMEI_TC)
        self.imei_tc.Bind(wx.EVT_TEXT_ENTER, self.OnImei_tcTextEnter,
              id=wxID_IMEIWRITERIMEI_TC)
        self.imei_tc.Bind(wx.EVT_TEXT, self.OnImei_tcText,
              id=wxID_IMEIWRITERIMEI_TC)

        self.cd_tc = wx.TextCtrl(id=wxID_IMEIWRITERCD_TC, name=u'cd_tc',
              parent=self.panel, pos=wx.Point(297, 64), size=wx.Size(40, 40),
              style=0, value=u'')
        self.cd_tc.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.cd_tc.SetMaxLength(1)
        self.cd_tc.SetEditable(False)
        self.cd_tc.Enable(False)
        self.cd_tc.SetToolTipString(u'')

        self.staticLine1 = wx.StaticLine(id=wxID_IMEIWRITERSTATICLINE1,
              name='staticLine1', parent=self.panel, pos=wx.Point(0, 345),
              size=wx.Size(466, 2), style=0)



        self.model15 = wx.CheckBox(id=wxID_IMEIWRITERMODEL15,
              label=u'15\u4f4d\u6a21\u5f0f', name=u'model15', parent=self.panel,
              pos=wx.Point(360, 59), size=wx.Size(79, 14), style=0)
        self.model15.SetValue(True)
        self.model15.Bind(wx.EVT_CHECKBOX, self.OnModel15Checkbox,
              id=wxID_IMEIWRITERMODEL15)

        self.Daul_Imei = wx.CheckBox(id=wxID_IMEIWRITERDAUL_IMEI,
              label=u'\u53ccIMEI\u53f7\u5199\u5165', name=u'Daul_Imei',
              parent=self.panel, pos=wx.Point(360, 101), size=wx.Size(88, 14),
              style=0)
        self.Daul_Imei.SetValue(False)
        self.Daul_Imei.Bind(wx.EVT_CHECKBOX, self.OnDaul_ImeiCheckbox,
              id=wxID_IMEIWRITERDAUL_IMEI)

        self.Result_sb = wx.StaticBox(id=wxID_IMEIWRITERRESULT_SB,
              label=u'结果', name=u'Result_sb', parent=self.panel,
              pos=wx.Point(8, 226), size=wx.Size(448, 112), style=0)
        self.Result_sb.SetToolTipString(u'')

        self.result_st = wx.StaticText(id=wxID_IMEIWRITERRESULT_ST, label=u'',
              name=u'result_st', parent=self.panel, pos=wx.Point(184, 252),
              size=wx.Size(0, 68), style=0)
        self.result_st.SetFont(wx.Font(42, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.result_st.SetToolTipString(u'')

        self.FirstIMEI = wx.StaticText(id=wxID_IMEIWRITERFIRSTIMEI,
              label=u'IMEI-1:', name='FirstIMEI', parent=self.panel,
              pos=wx.Point(16, 53), size=wx.Size(64, 23), style=0)
        self.FirstIMEI.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.FirstIMEI.Hide()

        self.SecondIMEI = wx.StaticText(id=wxID_IMEIWRITERSECONDIMEI,
              label=u'IMEI-2:', name=u'SecondIMEI', parent=self.panel,
              pos=wx.Point(16, 85), size=wx.Size(64, 23), style=0)
        self.SecondIMEI.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.SecondIMEI.Hide()

        self.Imei_1_cd = wx.TextCtrl(id=wxID_IMEIWRITERIMEI_1_CD,
              name=u'Imei_1_cd', parent=self.panel, pos=wx.Point(253, 50),
              size=wx.Size(30, 30), style=0, value=u'')
        self.Imei_1_cd.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.Imei_1_cd.SetMaxLength(1)
        self.Imei_1_cd.SetToolTipString(u'')
        self.Imei_1_cd.Enable(False)
        self.Imei_1_cd.Hide()

        self.Imei_2_cd = wx.TextCtrl(id=wxID_IMEIWRITERIMEI_2_CD,
              name=u'Imei_2_cd', parent=self.panel, pos=wx.Point(253, 83),
              size=wx.Size(30, 30), style=0, value=u'')
        self.Imei_2_cd.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.Imei_2_cd.SetMaxLength(1)
        self.Imei_2_cd.SetToolTipString(u'')
        self.Imei_2_cd.Enable(False)
        self.Imei_2_cd.Hide()

        self.led_1 = wx.Button(id=wxID_IMEIWRITERLED_1, label=u'',
              name=u'led_1', parent=self.panel, pos=wx.Point(295, 50),
              size=wx.Size(31, 31), style=0)
        self.led_1.SetToolTipString(u'')
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_1.Hide()

        self.led_2 = wx.Button(id=wxID_IMEIWRITERLED_2, label=u'',
              name=u'led_2', parent=self.panel, pos=wx.Point(295, 83),
              size=wx.Size(31, 31), style=0)
        self.led_2.SetToolTipString(u'')
        self.led_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_2.Hide()
        
        self.Daul_Imei_Esn = wx.CheckBox(id=wxID_IMEIWRITERDAUL_IMEI_ESN,
              label=u'\u53ccIMEI+ESN', name=u'Daul_Imei_Esn', parent=self.panel,
              pos=wx.Point(360, 121), size=wx.Size(88, 14), style=0)
        self.Daul_Imei_Esn.SetValue(False)
        self.Daul_Imei_Esn.Bind(wx.EVT_CHECKBOX, self.OnDaul_Imei_EsnCheckbox,
              id=wxID_IMEIWRITERDAUL_IMEI_ESN)
              
        self.One_IMEI_MEID = wx.CheckBox(id=wxID_IMEIWRITERONE_IMEI_MEID,
              label=u'IMEI+MEID', name=u'One_Imei_Meid', parent=self.panel,
              pos=wx.Point(360, 181), size=wx.Size(88, 14), style=0)
        self.One_IMEI_MEID.SetValue(False)
        self.One_IMEI_MEID.Bind(wx.EVT_CHECKBOX, self.OnIMEI_MEIDCheckbox,
              id=wxID_IMEIWRITERONE_IMEI_MEID)   
              
        self.One_Imei_Esn = wx.CheckBox(id=wxID_IMEIWRITERONE_IMEI_ESN,
              label=u'IMEI+ESN', name=u'One_Imei_Esn', parent=self.panel,
              pos=wx.Point(360, 161), size=wx.Size(88, 14), style=0)
        self.One_Imei_Esn.SetValue(False)
        self.One_Imei_Esn.Bind(wx.EVT_CHECKBOX, self.OnImei_EsnCheckbox,
              id=wxID_IMEIWRITERONE_IMEI_ESN)    

        self.One_MEID = wx.CheckBox(id=wxID_WRITE_MEID,
              label=u'MEID', name=u'One_MEID', parent=self.panel,
              pos=wx.Point(360, 201), size=wx.Size(88, 14), style=0)
        self.One_MEID.SetValue(False)
        self.One_MEID.Bind(wx.EVT_CHECKBOX, self.On_MEIDCheckbox,
              id=wxID_WRITE_MEID) 
               

        self.Daul_IMEI_MEID = wx.CheckBox(id=wxID_IMEIWRITERDAUL_IMEI_MEID,
              label=u'\u53ccIMEI+MEID', name=u'Daul_IMEI_MEID',
              parent=self.panel, pos=wx.Point(360, 141), size=wx.Size(88, 14),
              style=0)
        self.Daul_IMEI_MEID.SetValue(False)
        self.Daul_IMEI_MEID.Bind(wx.EVT_CHECKBOX, self.OnDaul_IMEI_MEIDCheckbox,
              id=wxID_IMEIWRITERDAUL_IMEI_MEID)

        self.staticText2 = wx.StaticText(id=wxID_IMEIWRITERSTATICTEXT2,
              label=u'ESN:', name='staticText2', parent=self.panel,
              pos=wx.Point(16, 118), size=wx.Size(42, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText2.Hide()

        self.esn_cd = wx.TextCtrl(id=wxID_IMEIWRITERESN_CD, name=u'esn_cd',
              parent=self.panel, pos=wx.Point(253, 116), size=wx.Size(30, 30),
              style=0, value=u'')
        self.esn_cd.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.esn_cd.SetMaxLength(1)
        self.esn_cd.SetToolTipString(u'')
        self.esn_cd.Enable(False)
        self.esn_cd.Hide()

        self.led_3 = wx.Button(id=wxID_IMEIWRITERLED_3, label=u'',
              name=u'led_3', parent=self.panel, pos=wx.Point(295, 116),
              size=wx.Size(31, 31), style=0)
        self.led_3.SetToolTipString(u'')
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_3.Hide()        

        self.Imei_1_tc = wx.TextCtrl(id=wxID_IMEIWRITERIMEI_1_TC,
              name=u'Imei_1_tc', parent=self.panel, pos=wx.Point(89, 50),
              size=wx.Size(162, 30), style=0, value=u'')
        self.Imei_1_tc.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.Imei_1_tc.SetToolTipString(u'')
        self.Imei_1_tc.SetMaxLength(15)
        self.Imei_1_tc.Bind(wx.EVT_TEXT_MAXLEN, self.OnImei_1_tcTextMaxlen,
              id=wxID_IMEIWRITERIMEI_1_TC)
        self.Imei_1_tc.Bind(wx.EVT_TEXT_ENTER, self.OnImei_1_tcTextEnter,
              id=wxID_IMEIWRITERIMEI_1_TC)
        self.Imei_1_tc.Bind(wx.EVT_TEXT, self.OnImei_1_tcText,
              id=wxID_IMEIWRITERIMEI_1_TC)
        self.Imei_1_tc.Hide()

        self.Imei_2_tc = wx.TextCtrl(id=wxID_IMEIWRITERIMEI_2_TC,
              name=u'Imei_2_tc', parent=self.panel, pos=wx.Point(89, 83),
              size=wx.Size(162, 30), style=0, value=u'')
        self.Imei_2_tc.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.Imei_2_tc.SetToolTipString(u'')
        self.Imei_2_tc.SetMaxLength(15)
        self.Imei_2_tc.Bind(wx.EVT_TEXT_MAXLEN, self.OnImei_2_tcTextMaxlen,
              id=wxID_IMEIWRITERIMEI_2_TC)
        self.Imei_2_tc.Bind(wx.EVT_TEXT_ENTER, self.OnImei_2_tcTextEnter,
              id=wxID_IMEIWRITERIMEI_2_TC)
        self.Imei_2_tc.Bind(wx.EVT_TEXT, self.OnImei_2_tcText,
              id=wxID_IMEIWRITERIMEI_2_TC)
        self.Imei_2_tc.Hide()

        self.esn_tc = wx.TextCtrl(id=wxID_IMEIWRITERESN_TC, name=u'esn_tc',
              parent=self.panel, pos=wx.Point(89, 116), size=wx.Size(162, 30),
              style=0, value=u'')
        self.esn_tc.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.esn_tc.SetToolTipString(u'')
        self.esn_tc.SetMaxLength(15)
        self.esn_tc.Bind(wx.EVT_TEXT_MAXLEN, self.OnEsn_tcTextMaxlen,
              id=wxID_IMEIWRITERESN_TC)
        self.esn_tc.Bind(wx.EVT_TEXT_ENTER, self.OnEsn_tcTextEnter,
              id=wxID_IMEIWRITERESN_TC)
        self.esn_tc.Bind(wx.EVT_TEXT, self.OnEsn_tcText,
              id=wxID_IMEIWRITERESN_TC)
        self.esn_tc.Hide()

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.ser = None
        try:
            fp = open("setting.ini","r")
            setting = fp.read()
            fp.close()
            exec setting in globals()
            portstr = globals()['port']
            self.baudrat = int(globals()['baud'])
            self.port = int(portstr[3:])-1
            self.SetStatusText('Port:COM%d'%(self.port+1),1)
            
        except:
            self.port = 0
            self.baudrat = 115200
            self.SetStatusText('Port:COM%d'%(self.port+1),1)

    def OnSettingPortsettingMenu(self, event):
        try:
            self.settingDlg.Destroy()
            self.settingDlg = None
        except:
            pass
        
        import settingDlg
        
        self.settingDlg = settingDlg.create(self)
        self.settingDlg.Show()

    def OnSettingExitMenu(self, event):
        self.Destroy()

    def OnAboutAboutMenu(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "K组写号工具V3.1"
        info.Version = "V3.1"
        info.Copyright = "waterworld Copyright(C) 2011-2012"
        info.WebSite = ("http://www.waterworld.com.cn", "waterworld home page")
        wx.AboutBox(info)

    def OnModel14Checkbox(self, event):
        if self.model14.IsChecked():
            self.imei_tc.SetValue('')
            self.Imei_1_tc.SetValue('')
            #self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            #self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.imei_tc.SetMaxLength(14)
            self.Imei_1_tc.SetMaxLength(14)
            self.Imei_2_tc.SetMaxLength(14)
            self.cd_tc.Enable(True)
            self.model15.SetValue(False)
            self.autoadd1.Enable(True)
            if self.Daul_Imei.IsChecked() or self.Daul_Imei_Esn.IsChecked() or self.Daul_IMEI_MEID.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(True)
            
        else:
            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.model15.SetValue(True)
            self.imei_tc.SetMaxLength(15)
            self.Imei_1_tc.SetMaxLength(15)
            self.Imei_2_tc.SetMaxLength(15)
            self.cd_tc.Enable(False)
            self.autoadd1.Enable(False)
            self.autoadd1.SetValue(False)
            self.Imei_1_cd.Enable(False)
            self.Imei_2_cd.Enable(False)        
        self.Refresh()
        self.SetFocus()
        
    def OnModel15Checkbox(self, event):
        if self.model15.IsChecked():
            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.imei_tc.SetMaxLength(15)
            self.Imei_1_tc.SetMaxLength(15)
            self.Imei_2_tc.SetMaxLength(15)
            self.cd_tc.Enable(False)
            self.model14.SetValue(False)
            self.autoadd1.Enable(False)
            self.autoadd1.SetValue(False)
            self.Imei_1_cd.Enable(False)
            self.Imei_2_cd.Enable(False)
        else:
            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.model14.SetValue(True)
            self.imei_tc.SetMaxLength(14)
            self.cd_tc.Enable(True)
            self.autoadd1.Enable(True)
            if self.Daul_Imei.IsChecked()or self.Daul_Imei_Esn.IsChecked() or self.Daul_IMEI_MEID.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                self.Imei_2_tc.SetMaxLength(14)
        self.Refresh()
        self.SetFocus()
        
    def OnImei_tcTextEnter(self, event):
        event.Skip()
        
    def OnImei_tcText(self, event):
        try:
            self.SetStatusText('请输入IMEI号...',0)
            int(self.imei_tc.GetValue())
        except:
            self.SetStatusText('输入错误数字！',0)
            self.imei_tc.SetSelection(-1,-1)
            
        if self.model14.IsChecked() and 14==self.imei_tc.GetLastPosition():
            imei14 = str(self.imei_tc.GetValue())
            self.cd_tc.SetValue(self.GetCD(imei14))
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
        else:
            if 15==self.imei_tc.GetLastPosition():
                self.SetStatusText('等待写入',0)
                self.SetFocus()
                self.write_btn.SetFocus()

    def OnImei_tcTextMaxlen(self, event):
        self.SetStatusText('等待写入',0)
        self.SetFocus()
        self.write_btn.SetFocus()
        
    def OnImei_1_tcTextMaxlen(self, event):    
        if self.One_Imei_Esn.IsChecked() or self.One_IMEI_MEID.IsChecked():
            self.SetFocus()
            self.esn_tc.SetFocus()
            self.esn_tc.SetSelection(-1,-1)
        else:
            self.SetFocus()
            self.Imei_2_tc.SetFocus()
            self.Imei_2_tc.SetSelection(-1,-1)
     

    def OnImei_1_tcTextEnter(self, event):
        event.Skip()

    def OnImei_1_tcText(self, event):
        try:
            self.SetStatusText('输入IMEI-1号...',0)
            int(self.Imei_1_tc.GetValue())
        except:
            self.SetStatusText('输入错误数字！',0)
            self.Imei_1_tc.SetSelection(-1,-1)
        """      
        if self.model14.IsChecked() and 14==self.Imei_1_tc.GetLastPosition():
            imei_1_14 = str(self.Imei_1_tc.GetValue())
            self.Imei_1_cd.SetValue(self.GetCD(imei_1_14))
            self.SetFocus()
            self.Imei_2_tc.SetFocus()
            self.Imei_2_tc.SetSelection(-1,-1)
        else:
            if 15==self.Imei_1_tc.GetLastPosition():
                self.SetFocus()
                self.Imei_2_tc.SetFocus()
                self.Imei_2_tc.SetSelection(-1,-1)
        """
    def OnImei_2_tcTextMaxlen(self, event):
        if self.Daul_Imei_Esn.IsChecked() or self.Daul_IMEI_MEID.IsChecked():
            self.SetFocus()
            self.esn_tc.SetFocus()
            self.esn_tc.SetSelection(-1,-1)
        else:
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()

    def OnImei_2_tcTextEnter(self, event):
        event.Skip()

    def OnImei_2_tcText(self, event):
        try:
            self.SetStatusText('输入IMEI-2号...',0)
            int(self.Imei_2_tc.GetValue())
        except:
            self.SetStatusText('输入错误数字！',0)
            self.Imei_2_tc.SetSelection(-1,-1)
        """    
        if self.model14.IsChecked() and 14==self.Imei_2_tc.GetLastPosition():
            imei_2_14 = str(self.Imei_2_tc.GetValue())
            self.Imei_2_cd.SetValue(self.GetCD(imei_2_14))
            if self.Daul_Imei_Esn.IsChecked() or self.Daul_IMEI_MEID.IsChecked():
                self.SetFocus()
                self.esn_tc.SetFocus()
                self.esn_tc.SetSelection(-1,-1)
            else:
                self.SetStatusText('等待写入',0)
                self.SetFocus()
                self.write_btn.SetFocus()
        else:
            if 15==self.Imei_2_tc.GetLastPosition():
                #print 'c'
                if self.Daul_Imei_Esn.IsChecked() or self.Daul_IMEI_MEID.IsChecked():
                    #print 'd'
                    self.SetFocus()
                    self.esn_tc.SetFocus()
                    self.esn_tc.SetSelection(-1,-1)
                else:
                    self.SetStatusText('等待写入',0)
                    self.SetFocus()
                    self.write_btn.SetFocus()        
        """
    def OnWrite_btnButton(self, event):
        if self.Daul_Imei.IsChecked():
            thread.start_new_thread(self.WriteDualIMEI,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)

        elif self.Daul_Imei_Esn.IsChecked():
            thread.start_new_thread(self.WriteDualIMEI_ESN,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)

        elif self.One_Imei_Esn.IsChecked():
            thread.start_new_thread(self.WriteOneIMEI_ESN,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)

        elif self.One_MEID.IsChecked():
            thread.start_new_thread(self.WriteOne_MEID,())
            self.SetFocus()
            self.esn_tc.SetFocus()
            self.esn_tc.SetSelection(-1,-1)

        elif self.One_IMEI_MEID.IsChecked():
            thread.start_new_thread(self.WriteOneIMEI_MEID,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)
            
        elif self.Daul_IMEI_MEID.IsChecked():
            thread.start_new_thread(self.WriteDualIMEI_MEID,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)
                        
            
        else:
            thread.start_new_thread(self.WriteIMEI,())
            self.SetFocus()
            self.Imei_1_tc.SetFocus()
            self.Imei_1_tc.SetSelection(-1,-1)
                
    def OnExit_btnButton(self, event):
        self.Destroy()
        
    def Connect2MT_ex(self):
        self.SetStatusText('开始连接...',0)
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetLabel('稍后')
        self.write_btn.Enable(False)
        self.exit_btn.Enable(False)
        self.ser = CommInterface(self.port,self.baudrat)
        result = self.ser.OpenPort()
        if result:
            return True
        else:
            return False
        
    def Connect2MT(self):
        failed = 0
        for i in range(10):
            result = self.Connect2MT_ex()
            if result:
                self.SetStatusText('已连接',0)
                failed = 0
                return True
            else:
                time.sleep(0.1)
                failed = 1
        if failed: 
            self.SetStatusText('连接失败',0)
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.exit_btn.Enable(True)
            self.write_btn.Enable(True)        
        return False
        
    def WriteDualIMEI(self):
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)
        imei1num = str(self.Imei_1_tc.GetValue())
        imei2num = str(self.Imei_2_tc.GetValue())
        cd1 = str(self.Imei_1_cd.GetValue())
        cd2 = str(self.Imei_2_cd.GetValue())
        if len(imei1num+cd1) != 15:
            self.SetStatusText('IMEI-1号码长度不够，写入失败。',0)
            self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        if len(imei2num+cd2) != 15:
            self.SetStatusText('IMEI-2号码长度不够，写入失败',0)
            self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.led_1.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-1号写入成功',0)
            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
            result = self.ser.Ask(temp)   
            if not result:
                self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_2.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-2号写入成功',0)
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()				
                if not b_ret:
                    self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                    self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_1.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('IMEI-1号写入成功',0)
                time.sleep(0.1)
            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                    #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_2.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('IMEI-2号写入成功',0)
                time.sleep(0.1)

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.autoadd1.GetValue():
                imei1str = self.AutoAdd(imei1num)
                self.Imei_1_tc.SetValue(imei1str)
                imei2str = self.AutoAdd(imei2num)
                self.Imei_2_tc.SetValue(imei2str)
                
                self.Imei_1_cd.SetValue(self.GetCD(imei1str))
                self.Imei_2_cd.SetValue(self.GetCD(imei2str))
            else:
                self.SetFocus()
                self.Imei_1_tc.SetFocus()
                self.Imei_1_tc.SetSelection(-1,-1)
        return
            
    def WriteIMEI(self):
        result = self.Connect2MT()
        if not result:
            return
        self.SetStatusText('写入中...',0)
        imeinum = str(self.imei_tc.GetValue())
        cd = str(self.cd_tc.GetValue())
        if len(imeinum+cd) != 15:
            self.SetStatusText('IMEI号码长度不够，写入失败。',0)
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imeinum+cd+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI号写入失败，请重新写入',0)
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.SetStatusText('IMEI号写入成功',0)
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imeinum+cd+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('IMEI号写入失败，请重新写入',0)
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.SetStatusText('IMEI-1号写入成功',0)
                time.sleep(0.1)

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.autoadd1.GetValue():
                imeistr = self.AutoAdd(imeinum)
                self.imei_tc.SetValue(imeistr)
                self.cd_tc.SetValue(self.GetCD(imeistr))

            else:
                self.SetFocus()
                self.imei_tc.SetFocus()
                self.imei_tc.SetSelection(-1,-1)
        return
        
    def AutoAdd(self,imei,times=1):
        imeistr = str(int(imei)+times)
        length = len(imeistr)
        if length>14:
            return imeistr[1:]
        elif length<14:
            return '0'*(14-length)+imeistr
        else:
            return imeistr         
        
    def GetCD(self, imei):
        evenstrtmp = ''
        oddstrtmp = ''
        for i in range((len(imei))/2):
            oddstrtmp += imei[2*i]
            evenstrtmp += imei[2*i+1]
        tmp = ''    
        for i in range(len(evenstrtmp)):
            tmp += str(int(evenstrtmp[i])*2)
            
        totalstr = oddstrtmp+tmp
        tmp = 0
        for i in range(len(totalstr)):
            tmp += int(totalstr[i])
            
        tmp = str(tmp)
        if len(tmp)>1:
            if tmp[-1]!='0':
                cd = str(int(str(int(tmp[:-1])+1)+'0')-int(tmp))
            else:
                cd = '0'
        else:
            if tmp != '0':
                cd = str(10-int(tmp))
            else:
                cd = '0'
        return cd
    
    def writeresultmsg(self,result,Log=None):
        if not Log is None:
            Log.BeginTextColour((255, 255, 0))
            Log.AppendText('='*48)
            Log.EndTextColour()
            Log.Newline()
            Log.BeginAlignment(wx.richtext.TEXT_ALIGNMENT_CENTRE)
            if result != 'SUCCESS':
                Log.BeginTextColour((255, 0, 0))
            else:
                Log.BeginTextColour("Dark Green")
            Log.BeginFontSize(30)
            Log.AppendText(result)
            Log.EndFontSize()
            Log.EndTextColour()
            Log.EndAlignment()
            Log.Newline()
            Log.BeginTextColour((255, 255, 0))
            Log.AppendText('='*48)
            Log.EndTextColour()
        else:
            pass

    def AutoSave(self,imei):
        try:
            fp = open('imei.txt','a+')
            fp.write('%s'%imei+'\n')
            fp.close()
        except:
            pass

    def OnDaul_ImeiCheckbox(self, event):  
        if self.Daul_Imei.IsChecked():
            self.Daul_Imei_Esn.SetValue(False)
            self.Daul_IMEI_MEID.SetValue(False)
            self.One_IMEI_MEID.SetValue(False)
            self.One_Imei_Esn.SetValue(False)
            self.One_MEID.SetValue(False)
            self.staticText2.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                self.Imei_2_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Enable(False)
                self.Imei_2_cd.Enable(False)
                self.Imei_1_tc.SetMaxLength(15)
                self.Imei_2_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Show()
            self.SecondIMEI.Show()
            self.Imei_1_tc.Show()
            self.Imei_2_tc.Show()
            self.Imei_1_cd.Show()
            self.Imei_2_cd.Show()
            self.led_1.Show()
            self.led_2.Show()
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
                      
        else:
            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.led_1.Hide()
            self.led_2.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
            
        self.Refresh()
        self.imei_tc.SetFocus()
        self.SetFocus()
        return

    def OnDaul_Imei_EsnCheckbox(self, event):
        if self.Daul_Imei_Esn.IsChecked():
            self.Daul_Imei.SetValue(False)
            self.Daul_IMEI_MEID.SetValue(False)
            self.One_Imei_Esn.SetValue(False)
            self.One_MEID.SetValue(False)
            self.One_IMEI_MEID.SetValue(False)
            self.staticText2.SetLabel("ESN:")
            self.Refresh()
            self.esn_tc.SetMaxLength(8)
            if self.model14.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(True)
                #self.esn_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                self.Imei_2_tc.SetMaxLength(14)
                #self.esn_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Enable(False)
                self.Imei_2_cd.Enable(False)
                self.esn_cd.Enable(False)
                self.Imei_1_tc.SetMaxLength(15)
                self.Imei_2_tc.SetMaxLength(15)
                #self.esn_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Show()
            self.SecondIMEI.Show()
            self.staticText2.Show()
            self.Imei_1_tc.Show()
            self.Imei_2_tc.Show()
            self.esn_tc.Show()
            self.Imei_1_cd.Show()
            self.Imei_2_cd.Show()
            self.esn_cd.Show()
            
            self.led_1.Show()
            self.led_2.Show()
            self.led_3.Show()
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.esn_cd.SetValue('')
                      
        else:
            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.staticText2.Hide()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_1.Hide()
            self.led_2.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
        
        self.Refresh()
        self.SetFocus()
        return
          
        
    def OnImei_EsnCheckbox(self, event):
        if self.One_Imei_Esn.IsChecked():
            self.Daul_Imei.SetValue(False)
            self.Daul_IMEI_MEID.SetValue(False)
            self.One_MEID.SetValue(False)
            self.Daul_Imei_Esn.SetValue(False)
            self.One_IMEI_MEID.SetValue(False)
            self.staticText2.SetLabel("ESN:")
            self.Refresh()
            self.esn_tc.SetMaxLength(8)
            if self.model14.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(False)
                #self.esn_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                #self.Imei_2_tc.SetMaxLength(14)
                #self.esn_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Enable(False)
                self.Imei_2_cd.Enable(True)
                self.esn_cd.Enable(False)
                self.Imei_1_tc.SetMaxLength(15)
                #self.Imei_2_tc.SetMaxLength(15)
                #self.esn_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Show()
            self.SecondIMEI.Hide()
            self.staticText2.Show()
            self.Imei_1_tc.Show()
            self.Imei_2_tc.Hide()
            self.esn_tc.Show()
            self.Imei_1_cd.Show()
            self.Imei_2_cd.Hide()
            self.esn_cd.Show()
            
            self.led_1.Show()
            self.led_2.Hide()
            self.led_3.Show()
            self.Imei_1_tc.SetValue('')
            #self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            #self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.esn_cd.SetValue('')
                      
        else:
            self.staticText2.SetLabel("ESN22222222:")
            self.FirstIMEI.Hide()
            #self.SecondIMEI.Hide()
            self.staticText2.Hide()
            self.Imei_1_tc.Hide()
            #self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            #self.Imei_2_cd.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_1.Hide()
            #self.led_2.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
        
        self.Refresh()
        self.SetFocus()
        return 

        
    def OnIMEI_MEIDCheckbox(self, event):
        if self.One_IMEI_MEID.IsChecked():           
            self.Daul_Imei.SetValue(False)
            self.Daul_Imei_Esn.SetValue(False)
            self.Daul_IMEI_MEID.SetValue(False)
            self.One_Imei_Esn.SetValue(False)
            self.One_MEID.SetValue(False)
            self.staticText2.SetLabel("MEID:")
            self.Refresh()
            self.esn_tc.SetMaxLength(14)            
            if self.model14.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Hide()
                #self.esn_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                #self.Imei_2_tc.SetMaxLength(14)
                #self.esn_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Enable(False)
                self.Imei_2_cd.Hide()
                self.esn_cd.Enable(False)
                self.Imei_1_tc.SetMaxLength(15)
                #self.Imei_2_tc.SetMaxLength(15)
                #self.esn_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Show()
            self.SecondIMEI.Hide()
            self.staticText2.Show()
            self.Imei_1_tc.Show()
            self.Imei_2_tc.Hide()
            self.esn_tc.Show()
            self.Imei_1_cd.Show()
            self.Imei_2_cd.Hide()
            self.esn_cd.Show()
            
            self.led_1.Show()
            self.led_2.Hide()
            self.led_3.Show()
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            #self.Imei_2_tc.SetValue('')
            #self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.esn_cd.SetValue('')
                      
        else:
                   
            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.staticText2.Hide()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_1.Hide()
            self.led_2.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
        
        self.Refresh()
        self.SetFocus()
        return

    def On_MEIDCheckbox(self, event):
        if self.One_MEID.IsChecked():
            self.One_IMEI_MEID.SetValue(False)
            self.Daul_Imei.SetValue(False)
            self.Daul_Imei_Esn.SetValue(False)
            self.Daul_IMEI_MEID.SetValue(False)
            self.One_Imei_Esn.SetValue(False)
            self.staticText2.SetLabel("MEID:")
            self.Refresh()
            self.esn_tc.SetMaxLength(14)            
            if self.model14.IsChecked():
                self.Imei_1_cd.Hide()
                self.Imei_2_cd.Hide()
                #self.esn_cd.Enable(True)
                #self.Imei_1_tc.SetMaxLength(14)
                #self.Imei_2_tc.SetMaxLength(14)
                #self.esn_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Hide()
                self.Imei_2_cd.Hide()
                self.esn_cd.Enable(False)
                #self.Imei_1_tc.SetMaxLength(15)
                #self.Imei_2_tc.SetMaxLength(15)
                #self.esn_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.staticText2.Show()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.esn_tc.Show()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.esn_cd.Show()
            
            self.led_1.Hide()
            self.led_2.Hide()
            self.led_3.Show()
            #self.Imei_1_tc.SetValue('')
            #self.Imei_1_cd.SetValue('')
            #self.Imei_2_tc.SetValue('')
            #self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.esn_cd.SetValue('')
                      
        else:
                   
            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.staticText2.Hide()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_1.Hide()
            self.led_2.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
        
        self.Refresh()
        self.SetFocus()
        return


    def OnDaul_IMEI_MEIDCheckbox(self, event):
        if self.Daul_IMEI_MEID.IsChecked():
            self.Daul_Imei.SetValue(False)
            self.Daul_Imei_Esn.SetValue(False)
            self.One_IMEI_MEID.SetValue(False)
            self.One_Imei_Esn.SetValue(False)
            self.One_MEID.SetValue(False)
            self.staticText2.SetLabel("MEID:")
            self.Refresh()
            self.esn_tc.SetMaxLength(14)
            
            if self.model14.IsChecked():
                self.Imei_1_cd.Enable(True)
                self.Imei_2_cd.Enable(True)
                #self.esn_cd.Enable(True)
                self.Imei_1_tc.SetMaxLength(14)
                self.Imei_2_tc.SetMaxLength(14)
                #self.esn_tc.SetMaxLength(14)
            else:
                self.Imei_1_cd.Enable(False)
                self.Imei_2_cd.Enable(False)
                self.esn_cd.Enable(False)
                self.Imei_1_tc.SetMaxLength(15)
                self.Imei_2_tc.SetMaxLength(15)
                #self.esn_tc.SetMaxLength(15)
            self.imei_tc.Hide()
            self.cd_tc.Hide()

            self.FirstIMEI.Show()
            self.SecondIMEI.Show()
            self.staticText2.Show()
            self.Imei_1_tc.Show()
            self.Imei_2_tc.Show()
            self.esn_tc.Show()
            self.Imei_1_cd.Show()
            self.Imei_2_cd.Show()
            self.esn_cd.Show()
            
            self.led_1.Show()
            self.led_2.Show()
            self.led_3.Show()
            self.Imei_1_tc.SetValue('')
            self.Imei_1_cd.SetValue('')
            self.Imei_2_tc.SetValue('')
            self.Imei_2_cd.SetValue('')
            self.esn_tc.SetValue('')
            self.esn_cd.SetValue('')
                      
        else:
            self.FirstIMEI.Hide()
            self.SecondIMEI.Hide()
            self.staticText2.Hide()
            self.Imei_1_tc.Hide()
            self.Imei_2_tc.Hide()
            self.Imei_1_cd.Hide()
            self.Imei_2_cd.Hide()
            self.esn_tc.Hide()
            self.esn_cd.Hide()
            self.led_1.Hide()
            self.led_2.Hide()
            self.led_3.Hide()
            if self.model14.IsChecked():
                self.cd_tc.Enable(True)
                self.imei_tc.SetMaxLength(14)

            else:
                self.cd_tc.Enable(False)
                self.imei_tc.SetMaxLength(15)

            self.imei_tc.Show()
            self.cd_tc.Show()

            self.imei_tc.SetValue('')
            self.cd_tc.SetValue('')
        
        self.Refresh()
        self.SetFocus()
        return

    def OnEsn_tcTextMaxlen(self, event):
        self.SetStatusText('等待写入',0)
        self.SetFocus()
        self.write_btn.SetFocus()

    def OnEsn_tcTextEnter(self, event):
        self.SetStatusText('输入111号...',0)
        event.Skip()

    def OnEsn_tcText(self, event):
        self.SetStatusText('输入ESN号...',0)
        t = self.esn_tc.GetValue().upper()
        for i in range(len(t)):            
            if not (t[i] in '0123456789ABCDEF'):
                self.SetStatusText('输入错误数字！',0)
                self.esn_tc.SetSelection(-1,-1)
                return
            
        
        if self.Daul_Imei_Esn.IsChecked() and 8==self.esn_tc.GetLastPosition():
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
        elif self.Daul_IMEI_MEID.IsChecked() and 14==self.esn_tc.GetLastPosition():
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
        elif self.One_Imei_Esn.IsChecked() and 8==self.esn_tc.GetLastPosition():
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
        elif self.One_IMEI_MEID.IsChecked() and 14==self.esn_tc.GetLastPosition():
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
            pass
        elif self.One_IMED.IsChecked() and 14==self.esn_tc.GetLastPosition():
            self.SetStatusText('等待写入',0)
            self.SetFocus()
            self.write_btn.SetFocus()
            pass			
        
        
    def WriteDualIMEI_MEID(self):
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)
        imei1num = str(self.Imei_1_tc.GetValue())
        imei2num = str(self.Imei_2_tc.GetValue())
        esnnum = str(self.esn_tc.GetValue())
        cd1 = str(self.Imei_1_cd.GetValue())
        cd2 = str(self.Imei_2_cd.GetValue())
        if len(imei1num+cd1) != 15:
            self.SetStatusText('IMEI-1号码长度不够，写入失败。',0)
            self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        if len(imei2num+cd2) != 15:
            self.SetStatusText('IMEI-2号码长度不够，写入失败',0)
            self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            #result = self.ser.Write('AT+ESLP=0\n\r')
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.led_1.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-1号写入成功',0)
            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
            result = self.ser.Ask(temp)   
            if not result:
                self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_2.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-2号写入成功',0)

            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('MEID号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_3.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('MEID号写入成功',0)
            
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                    self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_1.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('IMEI-1号写入成功',0)
                time.sleep(0.1)
            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                    #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_2.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('IMEI-2号写入成功',0)
                time.sleep(0.1)

            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('MEID号写入失败，请重新写入',0)
                    #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_3.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('MEID号写入成功',0)
                time.sleep(0.1)            

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.model14.GetValue():
                imei1str = self.AutoAdd(imei1num)
                self.Imei_1_tc.SetValue(imei1str)
                imei2str = self.AutoAdd(imei2num)
                self.Imei_2_tc.SetValue(imei2str)
                esnnumstr = self.AutoAdd(esnnum)
                self.esn_tc.SetValue(esnnumstr)
                
                self.Imei_1_cd.SetValue(self.GetCD(imei1str))
                self.Imei_2_cd.SetValue(self.GetCD(imei2str))
            else:
                self.SetFocus()
                self.Imei_1_tc.SetFocus()
                self.Imei_1_tc.SetSelection(-1,-1)
        return
    
 
    def WriteOneIMEI_MEID(self):
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)
        imei1num = str(self.Imei_1_tc.GetValue())
        esnnum = str(self.esn_tc.GetValue())
        cd1 = str(self.Imei_1_cd.GetValue())
        if len(imei1num+cd1) != 15:
            self.SetStatusText('IMEI-1号码长度不够，写入失败。',0)
            self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False

        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            #result = self.ser.Write('AT+ESLP=0\n\r')
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.led_1.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-1号写入成功',0)
                       
            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('MEID号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_3.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('MEID号写入成功',0)
            
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                    self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_1.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('IMEI-1号写入成功',0)
                time.sleep(0.1)
                        
            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('MEID号写入失败，请重新写入',0)
                    #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_3.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('MEID号写入成功',0)
                time.sleep(0.1)            

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.model14.GetValue():
                imei1str = self.AutoAdd(imei1num)
                self.Imei_1_tc.SetValue(imei1str)
                esnnumstr = self.AutoAdd(esnnum)
                self.esn_tc.SetValue(esnnumstr)                
                self.Imei_1_cd.SetValue(self.GetCD(imei1str))

            else:
                self.SetFocus()
                self.Imei_1_tc.SetFocus()
                self.Imei_1_tc.SetSelection(-1,-1)
        return

    def WriteOne_MEID(self):
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)        
        esnnum = str(self.esn_tc.GetValue())

        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            #result = self.ser.Write('AT+ESLP=0\n\r')
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
                        
            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('MEID号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_3.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('MEID号写入成功',0)
            
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)
            
                        
            temp = 'AT^MEID=1,1,"'+esnnum+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                b_ret=self.ser.Read_Ext()
                if not b_ret:
                    self.SetStatusText('MEID号写入失败，请重新写入',0)
                    #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                    self.result_st.SetLabel('失败')
                    self.write_btn.Enable(True)
                    self.exit_btn.Enable(True)
                    return b_ret
                else:
                    if i==2:
                        self.led_3.SetBackgroundColour('FOREST GREEN')
                        self.SetStatusText('MEID号写入成功',0)
                time.sleep(0.1)            

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.model14.GetValue():
                esnnumstr = self.AutoAdd(esnnum)
                self.esn_tc.SetValue(esnnumstr)                
                self.esn_cd.SetValue(self.GetCD(esnnumstr))

            else:
                self.SetFocus()
                self.esn_tc.SetFocus()
                self.esn_tc.SetSelection(-1,-1)
        return            
    
    def WriteDualIMEI_ESN(self):
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)
        imei1num = str(self.Imei_1_tc.GetValue())
        imei2num = str(self.Imei_2_tc.GetValue())
        esnnum = str(self.esn_tc.GetValue())
        cd1 = str(self.Imei_1_cd.GetValue())
        cd2 = str(self.Imei_2_cd.GetValue())
        if len(imei1num+cd1) != 15:
            self.SetStatusText('IMEI-1号码长度不够，写入失败。',0)
            self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        if len(imei2num+cd2) != 15:
            self.SetStatusText('IMEI-2号码长度不够，写入失败',0)
            self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            #result = self.ser.Write('AT+ESLP=0\n\r')
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.led_1.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-1号写入成功',0)
            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
            result = self.ser.Ask(temp)   
            if not result:
                self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_2.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-2号写入成功',0)

            temp = 'AT^MEID=1,0,"'+esnnum+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('ESN号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_3.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('ESN号写入成功',0)
            
                    
        else:
            for i in range(10):
                result = self.ser.Write('AT+ESLP=0\n\r')
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
       ###########################
            for i in range(3):
                result = self.ser.Write(temp)
                #time.sleep(0.1)
                b_ret=self.ser.Read_Ext()
                #mxm='hexing %s' %data
                #self.SetStatusText(mxm,0)
                if not b_ret:
                    failed=1
                    #return b_ret
                else:
                    failed=0
                    self.led_1.SetBackgroundColour('FOREST GREEN')
                    self.SetStatusText('IMEI-1号写入成功',0)
                    break
                time.sleep(0.1)            
            if failed == 1:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.ser.ClosePort()
                return

            
            temp = 'AT+EGMR=1,10,"'+imei2num+cd2+'"\n\r'
         ###########################
            for i in range(3):
                result = self.ser.Write(temp)
                #time.sleep(0.1)
                b_ret=self.ser.Read_Ext()
                #mxm='hexing %s' %data
                #self.SetStatusText(mxm,0)
                if not b_ret:
                    failed=1
                    #return b_ret
                else:
                    failed=0
                    self.led_2.SetBackgroundColour('FOREST GREEN')
                    self.SetStatusText('IMEI-2号写入成功',0)
                    break
                time.sleep(0.1)            
            if failed == 1:
                self.SetStatusText('IMEI-2号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.ser.ClosePort()
                return

            temp = 'AT^MEID=1,0,"'+esnnum+'"\n\r'            
            ###########################
            for i in range(3):
                result = self.ser.Write(temp)
                #time.sleep(0.1)
                b_ret=self.ser.Read_Ext()
                #mxm='hexing %s' %data
                #self.SetStatusText(mxm,0)
                if not b_ret:
                    failed=1
                    #return b_ret
                else:
                    failed=0
                    self.led_3.SetBackgroundColour('FOREST GREEN')
                    self.SetStatusText('ESN号写入成功',0)
                    break
                time.sleep(0.1)            
            if failed == 1:
                self.SetStatusText('ESN号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.ser.ClosePort()
                return
            

        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        #self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.autoadd1.GetValue():
                imei1str = self.AutoAdd(imei1num)
                self.Imei_1_tc.SetValue(imei1str)
                imei2str = self.AutoAdd(imei2num)
                self.Imei_2_tc.SetValue(imei2str)
                esnnumstr = self.AutoAdd(esnnum)
                self.esn_tc.SetValue(esnnumstr)
                
                self.Imei_1_cd.SetValue(self.GetCD(imei1str))
                self.Imei_2_cd.SetValue(self.GetCD(imei2str))
            else:
                self.SetFocus()
                self.Imei_1_tc.SetFocus()
                self.Imei_1_tc.SetSelection(-1,-1)
        return
    
    def WriteOneIMEI_ESN(self):
        self.led_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        #self.led_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.led_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.result_st.SetForegroundColour(wx.Colour(255, 255, 0))
        result = self.Connect2MT()
        if not result:
            return

        self.SetStatusText('写入中...',0)
        imei1num = str(self.Imei_1_tc.GetValue())
        #imei2num = str(self.Imei_2_tc.GetValue())
        esnnum = str(self.esn_tc.GetValue())
        cd1 = str(self.Imei_1_cd.GetValue())
        #cd2 = str(self.Imei_2_cd.GetValue())
        if len(imei1num+cd1) != 15:
            self.SetStatusText('IMEI-1号码长度不够，写入失败。',0)
            self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
            self.result_st.SetLabel('失败')
            self.write_btn.Enable(True)
            self.exit_btn.Enable(True)
            return False
        
        if  self.waitrsp.GetValue():
            result = self.ser.Ask('AT+ESLP=0\n\r', times=5)
            #result = self.ser.Write('AT+ESLP=0\n\r')
            if not result:
                self.SetStatusText('Disable睡眠模式失败，写入失败',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            
            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('IMEI-1号写入失败，请重新写入',0)
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                #self.led_2.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                return result
            else:
                self.led_1.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('IMEI-1号写入成功',0)
                       
            temp = 'AT^MEID=1,0,"'+esnnum+'"\n\r'
            result = self.ser.Ask(temp)
            if not result:
                self.SetStatusText('ESN号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.result_st.SetLabel('失败')
                return result
            else:
                self.led_3.SetBackgroundColour('FOREST GREEN')
                self.SetStatusText('ESN号写入成功',0)
            
                    
        else:
            for i in range(6):
                result = self.ser.Write('AT+ESLP=0\n\r')				
                time.sleep(0.1)

            temp = 'AT+EGMR=1,7,"'+imei1num+cd1+'"\n\r'                     
            for i in range(3):
                result = self.ser.Write(temp)
                #time.sleep(0.1)
                b_ret=self.ser.Read_Ext()
                #mxm='hexing %s' %data
                #self.SetStatusText(mxm,0)
                if not b_ret:
                    failed=1
                    #return b_ret
                else:
                    failed=0
                    self.led_1.SetBackgroundColour('FOREST GREEN')
                    self.SetStatusText('IMEI-1号写入成功',0)
                    break
                time.sleep(0.1)            
            if failed == 1:
                self.SetStatusText('IMEI-1号写入失败，请重新写入1',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.ser.ClosePort()
                return 


            
            temp = 'AT^MEID=1,0,"'+esnnum+'"\n\r'
            for i in range(3):
                result = self.ser.Write(temp)
                #time.sleep(0.1)
                b_ret=self.ser.Read_Ext()
                #mxm='hexing %s' %data
                #self.SetStatusText(mxm,0)
                if not b_ret:
                    failed=1
                    #return b_ret
                else:
                    failed=0
                    self.led_3.SetBackgroundColour('FOREST GREEN')
                    self.SetStatusText('ESN号写入成功',0)
                    break
                time.sleep(0.1)            
            if failed == 1:
                self.SetStatusText('ESN号写入失败，请重新写入',0)
                #self.led_1.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.led_3.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetForegroundColour(wx.Colour(255, 0, 0))
                self.result_st.SetLabel('失败')
                self.write_btn.Enable(True)
                self.exit_btn.Enable(True)
                self.ser.ClosePort()
                return
            
        self.result_st.SetForegroundColour('FOREST GREEN')
        self.result_st.SetLabel('成功')
        self.write_btn.Enable(True)
        self.exit_btn.Enable(True)
        self.SetStatusText('状态',0)
        self.ser.ClosePort()
        if self.model14.IsChecked():
            if self.autoadd1.GetValue():
                imei1str = self.AutoAdd(imei1num)
                self.Imei_1_tc.SetValue(imei1str)
                esnnumstr = self.AutoAdd(esnnum)
                self.esn_tc.SetValue(esnnumstr)                
                self.Imei_1_cd.SetValue(self.GetCD(imei1str))
            else:
                self.SetFocus()
                self.Imei_1_tc.SetFocus()
                self.Imei_1_tc.SetSelection(-1,-1)
        return
    
    
 

