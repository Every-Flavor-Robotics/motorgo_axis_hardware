#https://opensource.org/licenses/MIT 

import os
import webbrowser
import shutil
import wx
import datetime
from threading import Thread
from .result_event import *
from .config import *
from .process import *


class PCBWayThread(Thread):
    def __init__(self, wxObject):
        Thread.__init__(self)
        self.process = PCBWayProcess()
        self.wxObject = wxObject
        self.start()

    def run(self):
        
        try:

            p_name = self.process.get_basedir()
            
            self.report(5)

            temp_dir = p_name + productionDir + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            
            self.report(15)

            os.makedirs(temp_dir)
            os.makedirs(temp_dir + "gerber")

            self.report(25)
            
            self.process.get_gerber_file(temp_dir + "gerber")

            self.report(35)

            self.process.get_netlist_file(temp_dir)

            self.report(45)

            self.process.get_components_file(temp_dir)

            self.report(55)

            temp_file = shutil.make_archive(self.process.get_basename() + "_gerber", 'zip', temp_dir + "gerber")

            self.report(60)

            shutil.move(temp_file, temp_dir)
            shutil.rmtree(temp_dir + "gerber")

            self.report(65)

            temp_file = os.path.join(temp_dir, os.path.basename(temp_file))

            self.report(75)

            readsofar = 0
            totalsize = os.path.getsize(temp_file)
            with open(temp_file, 'rb') as file:
                while True:
                    data = file.read(10)
                    if not data:
                        break
                    readsofar += len(data)
                    percent = readsofar * 1e2 / totalsize
                    self.report(75 + percent / 9)

            webbrowser.open("file://%s" % (temp_dir))

        except Exception as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            self.report(-1)
            return
       
        self.report(-1)

    def report(self, status):
        wx.PostEvent(self.wxObject, ResultEvent(status))
        



    