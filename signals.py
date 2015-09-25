#-*- coding: utf-8 -*-
from PyQt4.QtCore import SIGNAL

SIG_CREATE_TCP_SERVER    = SIGNAL("SIG_CREATE_TCP_SERVER")
SIG_CREATE_TCP_CLIENT    = SIGNAL("SIG_CREATE_TCP_CLIENT")
SIG_SERVER_CLOSED        = SIGNAL("SIG_SERVER_CLOSED")
SIG_REMOTE_CLOSED        = SIGNAL("SIG_REMOTE_CLOSED")
SIG_SERVER_CREATE_ERROR  = SIGNAL("SIG_SERVER_CREATE_ERROR")
SIG_SERVER_CREATE_OK     = SIGNAL("SIG_SERVER_CREATE_OK")
SIG_DATA_RECVED          = SIGNAL("SIG_DATA_RECVED")
SIG_SEND_DATA            = SIGNAL("SIG_SEND_DATA")

SIG_REMOTE_TCP_CLIENT_CONNECTED = SIGNAL("SIG_REMOTE_TCP_CLIENT_CONNECTED")
