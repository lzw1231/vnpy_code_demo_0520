from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from vnpy_ctp.api import MdApi
from PySide6 import QtWidgets, QtCore
import simple_window


class MainWindow(QWidget, simple_window.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 独立信号代理类
class SignalProxy(QtCore.QObject):
    proxy = Signal(str)

    def __init__(self):
        super().__init__()


class CtpMdApi(MdApi):
    def __init__(self) -> None:
        super().__init__()
        self.sig_msg = SignalProxy()

    def onFrontConnected(self):
        self.sig_msg.proxy.emit('行情服务器连接成功！')
        ctp_req: dict = {
            "UserID": "luozhw",
            "Password": "bitCAN080*!@@%",
            "BrokerID": "9999"
        }
        self.reqUserLogin(ctp_req, 1)

    def onFrontDisconnected(self, reason):
        self.sig_msg.proxy.emit(f'行情服务器连接断开！{reason}')

    def onRspUserLogin(self, data, error, req_id, last):
        if not error['ErrorID']:
            self.sig_msg.proxy.emit('行情服务器登录成功！')
        else:
            self.sig_msg.proxy.emit(f'行情服务器登录失败！错误信息：{error}')

    def onRtnDepthMarketData(self, data: dict):
        self.sig_msg.proxy.emit(str(data))


def main():
    app = QtWidgets.QApplication()
    window = MainWindow()

    api = CtpMdApi()

    window.btn_subscribe.clicked.connect(lambda: api.subscribeMarketData(window.txt_symbol.text()))
    api.sig_msg.proxy.connect(window.txt_browser.append)

    api.createFtdcMdApi('./log')
    api.registerFront("tcp://180.168.146.187:10131")
    api.init()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()
