from tkinter import EventType

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from vnpy_ctp.api import MdApi
from PySide6 import QtWidgets, QtCore
import simple_window
from vnpy.event import EventEngine, Event


class MainWindow(QWidget, simple_window.Ui_Form):
    signal = Signal(str)

    def __init__(self, ee: EventEngine):
        super().__init__()
        self.setupUi(self)

        self.ee: EventEngine = ee
        self.ee.register('log', self.update_log)

    def update_log(self, ee: Event):
        msg: str = ee.data
        self.txt_browser.append(msg)


class CtpMdApi(MdApi):
    def __init__(self, ee: EventEngine):
        super().__init__()
        self.ee: EventEngine = ee

    def write_log(self, msg: str):
        self.ee.put(Event('log', msg))

    def onFrontConnected(self):
        self.write_log('行情服务器连接成功！')
        ctp_req: dict = {
            "UserID": "abcdefg",
            "Password": "hijklmn",
            "BrokerID": "9999"
        }
        self.reqUserLogin(ctp_req, 1)

    def onFrontDisconnected(self, reason):
        self.write_log(f'行情服务器连接断开！{reason}')

    def onRspUserLogin(self, data, error, req_id, last):
        if not error['ErrorID']:
            self.write_log('行情服务器登录成功！')
        else:
            self.write_log(f'行情服务器登录失败！错误信息：{error}')

    def onRtnDepthMarketData(self, data: dict):
        self.write_log(str(data))


def main():
    ee: EventEngine = EventEngine()
    ee.start()

    app = QtWidgets.QApplication()
    window = MainWindow(ee)

    api = CtpMdApi(ee)

    window.btn_subscribe.clicked.connect(lambda: api.subscribeMarketData(window.txt_symbol.text()))

    api.createFtdcMdApi('./log')
    api.registerFront("tcp://180.168.146.187:10131")
    api.init()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()
