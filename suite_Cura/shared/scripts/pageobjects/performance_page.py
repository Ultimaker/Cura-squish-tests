# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import squish_module_helper
import squish
import time

class Performance(PageObject):
    main_window = names.mainWindow
    button_slice = names.sliceButton
    button_preview = names.previewButton
    
    def __init__(self):
        PageObject.__init__(self)
        squish_module_helper.import_squish_symbols()
        
    def trackBootTime(self):
        self.presetPreferences()
        start_time = time.time()
    
        startApplication("Cura -platformtheme none")
        waitForObjectExists(self.main_window)    
        
        t = time.time() - start_time
        return t
            
    @classmethod
    def trackFileloadTime(self):
        start_time = time.time()
        
        waitForObjectExists(self.button_slice).visible
        
        t = time.time() - start_time
        return t
    
    @classmethod
    def trackSliceTime(self):
        start_time = time.time()
        
        waitForObject(self.button_preview, 500000)
        
        t = time.time() - start_time
        return t
    
    def retrieveFromLog(self, action):
        f = '%s\cura.log' % self.windowsDir
        file = self.tail(f, 100)
                
        key = self.logLine(action)
        
        print("---- ENGINE TIMES ----")
        for lines in file:
            if key in lines:
                print(lines.split()[0] + ' ' + lines.split()[1] + ': ' + key + lines.split(key, 1)[1])
                
    def tail(self, file, n=1, bs=1024):
        f = open(file)
        f.seek(0,2)
        l = 1-f.read(1).count('\n')
        B = f.tell()
        while n >= l and B > 0:
                block = min(bs, B)
                B -= block
                f.seek(B, 0)
                l += f.read(block).count('\n')
        f.seek(B, 0)
        l = min(l,n)
        lines = f.readlines()[-l:]
        f.close()
        return lines
                 
    def logLine(self, action):
        switcher = {
                  'boot time':'Booting Cura took',
                  'file load time':'Loading file took',
                  'slice time':'Slicing took',
                  'writing time':'Writing file took'
        }
        
        return switcher.get(action)
