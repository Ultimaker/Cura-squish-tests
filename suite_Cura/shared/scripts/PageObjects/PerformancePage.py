# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper
import time


class Performance(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()

    def trackBootTime(self):
        self.presetPreferences()
        start_time = time.time()

        startApplication("Cura -platformtheme none")
        waitForObjectExists(names.mwi)

        t = time.time() - start_time
        return t

    @classmethod
    def trackFileloadTime(self):
        start_time = time.time()

        waitForObjectExists(names.mwi_btn_slice).visible

        t = time.time() - start_time
        return t

    @classmethod
    def trackSliceTime(self):
        start_time = time.time()

        waitForObject(names.mwi_btn_preview, 50000)

        t = time.time() - start_time
        return t

    def retrieveFromLog(self, action):
        f = f'{self.windows_dir}\cura.log'
        file = self.tail(f, 100)

        key = self.logLine(action)

        for lines in file:
            if key in lines:
                if key == 'TranslateOp':
                    print(lines.split()[-1])
                else:
                    print(lines.split()[0] + ' ' + lines.split()[1] + ': ' + key + lines.split(key, 1)[1])

    def tail(self, file, n=1, bs=1024):
        f = open(file)
        f.seek(0, 2)
        l = 1 - f.read(1).count('\n')
        B = f.tell()
        while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
        f.seek(B, 0)
        l = min(l, n)
        lines = f.readlines()[-l:]
        f.close()
        return lines

    def logLine(self, action):
        switcher = {
            'boot time': 'Booting Cura took',
            'file load time': 'Loading file took',
            'slice time': 'Slicing took',
            'writing time': 'Writing file took',
            'movement time': 'TranslateOp'
        }

        return switcher.get(action)
