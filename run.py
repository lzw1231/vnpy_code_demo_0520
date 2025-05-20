import sys

import qtpy
from vnpy_ctp.api import MdApi
from PySide6 import QtWidgets
import simple_window


class CtpMdApi(MdApi):
    def __init__(self, monitor) -> None:
        super().__init__()
        self.monitor = monitor

    def onFrontConnected(self):
        self.monitor.append('服务器连接成功！')
        ctp_req: dict = {
            "UserID": "luozhw",
            "Password": "bitCAN080*!@@%",
            "BrokerID": "9999"
        }
        self.reqUserLogin(ctp_req, 1)

    def onFrontDisconnected(self, reason):
        self.monitor.append(f'服务器连接断开！原因：{reason}')

    def onRspUserLogin(self, data, error, reqid, last):
        if not error['ErrorID']:
            self.monitor.append('行情服务器登录成功！')
        else:
            self.monitor.append(f'行情服务器登录失败！错误信息：{error}')

    def onRtnDepthMarketData(self, data: dict):
        self.monitor.append(str(data))


def main():
    app = QtWidgets.QApplication()
    main_window = QtWidgets.QWidget()
    widget = simple_window.Ui_Form()
    widget.setupUi(main_window)

    api = CtpMdApi(widget.txt_browser)

    widget.btn_subscribe.clicked.connect(lambda: api.subscribeMarketData(widget.txt_symbol.text()))

    api.createFtdcMdApi('.')
    api.registerFront("tcp://180.168.146.187:10211")
    api.init()

    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
