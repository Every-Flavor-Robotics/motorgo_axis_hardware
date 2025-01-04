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
## Class Archive3DModelsSettingsGui
###########################################################################

class Archive3DModelsSettingsGui ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Archive 3D models settings", pos = wx.DefaultPosition, size = wx.Size( 343,248 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"3D model path:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetHelpText( u"3D model path relative to project folder" )

        bSizer2.Add( self.m_staticText2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.txt_path = wx.TextCtrl( self, wx.ID_ANY, u"/packages3d", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer2.Add( self.txt_path, 2, wx.ALL|wx.EXPAND, 5 )


        bSizer4.Add( bSizer2, 0, 0, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Allow missing models", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.cb_amm = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.cb_amm, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer3, 0, wx.EXPAND, 0 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Debug Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer41.Add( self.m_staticText4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        cb_debug_levelChoices = [ u"debug", u"info" ]
        self.cb_debug_level = wx.ComboBox( self, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, cb_debug_levelChoices, wx.CB_READONLY )
        bSizer41.Add( self.cb_debug_level, 2, wx.ALL, 5 )


        bSizer4.Add( bSizer41, 0, wx.EXPAND, 5 )


        bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.bnt_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.bnt_ok, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.btn_cancel.Bind( wx.EVT_BUTTON, self.on_cancel )
        self.bnt_ok.Bind( wx.EVT_BUTTON, self.on_ok )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def on_cancel( self, event ):
        event.Skip()

    def on_ok( self, event ):
        event.Skip()


