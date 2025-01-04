# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Archive3DModelsMainGui
###########################################################################

class Archive3DModelsMainGui ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Archive 3D models", pos = wx.DefaultPosition, size = wx.Size( 213,81 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_settings = wx.Button( self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn_settings, 0, wx.ALL, 5 )

        self.btn_run = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.btn_run.SetDefault()
        bSizer4.Add( self.btn_run, 0, wx.ALL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.btn_settings.Bind( wx.EVT_BUTTON, self.on_settings )
        self.btn_run.Bind( wx.EVT_BUTTON, self.on_run )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def on_settings( self, event ):
        event.Skip()

    def on_run( self, event ):
        event.Skip()


