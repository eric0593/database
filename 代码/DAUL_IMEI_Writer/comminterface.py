#!/usr/bin/env python
# -*- coding: GB2312 -*-

import serial
import time
import sys
import binascii

class CommInterface:
    def __init__(self, portnum, baudrate=115200, timeout=2, writeTimeout=0.5):
        #self.log = Log
        self.PORT = portnum
        self.BAUDRATE = baudrate
        self.TIMEOUT = timeout
        self.WRITETIMEOUT = writeTimeout
        self.workSerial = serial.Serial()
        
        
    def OpenPort(self, Log=None):      
        try:
            self.workSerial.port = self.PORT
            self.workSerial.baudrate = self.BAUDRATE
            self.workSerial.timeout = self.TIMEOUT
            self.workSerial.writeTimeout = self.WRITETIMEOUT
            self.workSerial.open()
            if not Log is None:
                Log.BeginTextColour((255, 255, 0))
                Log.AppendText('端口打开成功!')
                Log.Newline()
                Log.EndTextColour()
            return True
        
        except:
            if not Log is None:
                Log.BeginTextColour((255, 0, 0))
                Log.AppendText('错误：端口打开失败!')
                Log.Newline()
                Log.EndTextColour()
            return False
            
    
    def Write(self, cmd,Log=None):
        try:
            self.workSerial.write(cmd)
            return True
        except:
            if not Log is None:
                Log.BeginTextColour((255, 0, 0))
                Log.AppendText('错误：写IMEI失败!')
                Log.Newline()
                Log.EndTextColour()
            return False
        
    def Read(self,Log=None):
        try:
            n = self.workSerial.inWaiting()
            msg = self.workSerial.read(n)
            return msg
        except:
            if not Log is None:
                Log.BeginTextColour((255, 0, 0))
                Log.AppendText('错误：写IMEI失败!')
                Log.Newline()
                Log.EndTextColour()
            return False

    def Read_Ext(self,log=None):
            n = self.workSerial.inWaiting()
            msg = self.workSerial.read(n)
            pos = msg.find("OK")
            if pos == -1:
                return False
            else:
                return True
            
    def Read_Ext2(self,log=None):
            n = self.workSerial.inWaiting()
            msg = self.workSerial.read(n)
            return msg
            
    def Ask_Ext(self, cmd, Log=None, times=3):
        msg = ''
        for i in range(times):
            self.Write(cmd)
            time.sleep(0.1)
            if i==(times-1):
                if Log is None:
                    Log.BeginTextColour((255, 0, 0))
                    Log.AppendText('错误：手机无应答!')
                    Log.Newline()
                    Log.EndTextColour()
                    return False
                else:
                    pass
                
    def Ask(self, cmd, Log=None, times=3):
        msg = ''
        for i in range(times):
            self.Write(cmd)
            time.sleep(0.1)
            msg = self.Read()
            msg = binascii.b2a_hex(msg)
            if msg != False:
                if cmd=='\x41\x54\x2B\x45\x47\x4D\x52\x3D\x30\x2C\x37\x0A\x0D' \
                       and '\x4F\x4B' in msg:
                    if not Log is None:
                        Log.BeginTextColour((255, 255, 0))
                        Log.AppendText('写IMEI成功!')
                        Log.Newline()
                        Log.EndTextColour()
                    return True
                elif '\x4F\x4B' in msg:
                    return True
                else:
                    if i==(times-1):
                        if not Log is None:
                            Log.BeginTextColour((255, 0, 0))
                            Log.AppendText('错误：应答消息不匹配!')
                            Log.Newline()
                            Log.EndTextColour()
                        return False
                    else:
                        pass
            else:
                if i==(times-1):
                    if Log is None:
                        Log.BeginTextColour((255, 0, 0))
                        Log.AppendText('错误：手机无应答!')
                        Log.Newline()
                        Log.EndTextColour()
                    return False
                else:
                    pass
            
            
    def ClosePort(self,Log=None):
        try:
            self.workSerial.close()
            return True
        except:
            if not Log is None:
                Log.BeginTextColour((255, 0, 0))
                Log.AppendText('错误：端口关闭失败!')
                Log.Newline()
                Log.EndTextColour()
            return False

if __name__ == '__main__':
    test = CommInterface(11)
    test.OpenPort()
    msg = test.Ask("\x01",3)
    if msg:
        print binascii.b2a_hex(msg)
    else:
        print 'error'
