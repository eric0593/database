#Boa:Dialog:setting
# -*- coding: GB2312 -*-

import wx
import serial

def create(parent):
    return setting(parent)

[wxID_SETTING, wxID_SETTINGBAUD_COMBOBOX, wxID_SETTINGBAUD_ST, 
 wxID_SETTINGOKBTN, wxID_SETTINGPORT_COMBOBOX, wxID_SETTINGPORT_SB, 
 wxID_SETTINGPORT_ST, wxID_SETTINGSTATICLINE1, 
] = [wx.NewId() for _init_ctrls in range(8)]

#BAUDRATE = ['2400','4800','9600','19200','38400','57600','115200']

class setting(wx.Dialog):
    def _init_ctrls(self, prnt, port):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_SETTING, name=u'setting', parent=prnt,
              pos=wx.Point(701, 390), size=wx.Size(209, 193),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Config')
        self.SetClientSize(wx.Size(201, 159))
        self.Center(wx.BOTH)

        self.port_sb = wx.StaticBox(id=wxID_SETTINGPORT_SB,
              label=u'Port Setting', name=u'port_sb', parent=self,
              pos=wx.Point(8, 1), size=wx.Size(184, 96), style=0)

        self.port_st = wx.StaticText(id=wxID_SETTINGPORT_ST, label=u'Port:',
              name=u'port_st', parent=self, pos=wx.Point(18, 28),
              size=wx.Size(48, 14), style=0)
        self.port_st.SetToolTipString(u'')

        self.port_comboBox = wx.ComboBox(choices=port,
              id=wxID_SETTINGPORT_COMBOBOX, name=u'port_comboBox', parent=self,
              pos=wx.Point(79, 24), size=wx.Size(99, 22), style=0, value=u'')
        self.port_comboBox.SetLabel(u'')
        self.port_comboBox.SetToolTipString(u'')
        self.port_comboBox.Bind(wx.EVT_COMBOBOX, self.OnPort_comboBoxCombobox,
              id=wxID_SETTINGPORT_COMBOBOX)

        self.baud_st = wx.StaticText(id=wxID_SETTINGBAUD_ST, label=u'baudrate:',
              name=u'baud_st', parent=self, pos=wx.Point(18, 59),
              size=wx.Size(55, 14), style=0)
        self.baud_st.SetToolTipString(u'')

        self.baud_ComboBox = wx.ComboBox(choices=['2400', '4800', '9600',
              '19200', '38400', '57600', '115200'],
              id=wxID_SETTINGBAUD_COMBOBOX, name=u'baud_ComboBox', parent=self,
              pos=wx.Point(79, 55), size=wx.Size(99, 22), style=0, value=u'')
        self.baud_ComboBox.SetLabel(u'')
        self.baud_ComboBox.SetToolTipString(u'')
        self.baud_ComboBox.Bind(wx.EVT_COMBOBOX, self.OnBaud_ComboBoxCombobox,
              id=wxID_SETTINGBAUD_COMBOBOX)

        self.staticLine1 = wx.StaticLine(id=wxID_SETTINGSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(2, 104),
              size=wx.Size(202, 2), style=0)

        self.okbtn = wx.Button(id=wxID_SETTINGOKBTN, label=u'OK', name=u'okbtn',
              parent=self, pos=wx.Point(61, 120), size=wx.Size(75, 24),
              style=0)
        self.okbtn.Bind(wx.EVT_BUTTON, self.OnOkbtnButton, id=wxID_SETTINGOKBTN)

    def __init__(self, parent):
        portlist = []
        self.portlistdic = {}
        for i in range(256):
            try:
                ser = serial.Serial(i)

                portname = ser.portstr
                portname = portname[portname.find('COM'):]

                portlist.append(portname)
                self.portlistdic[portname] = i
                ser.close()
            except:
                pass
        
        self._init_ctrls(parent,portlist)
        
        try:
            fp = open("setting.ini","r")
            setting = fp.read()
            fp.close()
            exec setting in globals()
            self.portstr = globals()['port']
            self.baudratestr = globals()['baud']
            
            if self.portstr in self.portlistdic.keys():
                self.port_comboBox.SetValue(self.portstr)
                self.baud_ComboBox.SetValue(self.baudratestr)
            else:
                self.portstr = 'COM1'
                self.port_comboBox.SetValue('COM1')
                self.baud_ComboBox.SetValue('115200')
        except:
            self.spc = '000000'
            self.portstr = 'COM1'
            self.baudratestr = '115200'
            self.port_comboBox.SetValue('COM1')
            self.baud_ComboBox.SetValue('115200')

    def OnOkbtnButton(self, event):
        if self.portstr == 'COM1':
            self.Parent.port = 0
            
        else:
            self.Parent.port = self.portlistdic[self.portstr]
        
        self.Parent.SetStatusText('',0)
        self.Parent.SetStatusText('Port:%s'%self.portstr,1)   
        self.Parent.baudrat = int(self.baudratestr)
        self.savesetting()
        self.Destroy()
        
    def savesetting(self):
        try:
            fp = open('setting.ini','w')
            fp.write("#Port:\n")
            fp.write("port = '"+ self.portstr + "'\n\n")
            fp.write("#baudrate:\n")
            fp.write("baud = '"+ self.baudratestr + "'\n\n")
            fp.close()    
        except:
            pass

    def OnSpc_tcText(self, event):
        self.spc = event.GetString()

    def OnPort_comboBoxCombobox(self, event):
        self.portstr = self.port_comboBox.GetValue()

    def OnBaud_ComboBoxCombobox(self, event):
        self.baudratestr = self.baud_ComboBox.GetValue()
        
