#-*- coding: utf-8 -*-
from log import logger
from ui.AppIcons import *
from SockTreeItem import SockTreeItem
import config
from PyQt4.QtGui import (
    QTreeWidget,
    QIcon )

class SockTreeWidget(QTreeWidget):
    
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)
    
    def addTcpServer(self, address):
        curItem = self.currentItem()
        if not curItem:
            logger.error("currentItem is None")
            return
            
        item = SockTreeItem()
        item.setText(0, address)
        item.setIcon(0, QIcon(config.TCP_SERVER_ICON))
        curItem.addChild(item)
        self.setItemExpanded(curItem, True)
        self.setCurrentItem(item)
        