import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from UI.MainWindow import Ui_MainWindow
from Settings import Settings
import Util
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis


class MainWindow(QMainWindow):
    myLinechart: QChart
    Setting = Settings()
    merits = ['ssim', 'psnr', 'mse']
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # 实例化 Ui_MainWindow
        self.ui.setupUi(self)  # 使用 setupUi 方法设置界面
        self.setup_import_modelpath()
        self.setup_import_filepath1()
        self.setup_import_filepath2()
        self.scene = QGraphicsScene()
        self.ui.Gv_inputimg.setScene(self.scene)
        self.setAcceptDrops(True)
        self.setup_showlinechart()

    def dragEnterEvent(self, event):
        # 检查拖入物品的类型并确定是否接受该事件
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        # 在拖放完成时执行操作
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.endswith(('.png', '.jpg', '.jpeg')):
                    pixmap = QPixmap(file_path)
                    if not pixmap.isNull():
                        pixmap_item = self.scene.addPixmap(pixmap)




    def setup_import_modelpath (self):
        self.ui.btn_importmodel.clicked.connect(self.on_importmodel_clicked)
    def on_importmodel_clicked(self):
        path =self.ui.Tb_Model.toPlainText()
        if(not Util.check_path_exists(path)):
            QMessageBox.information(None, "Title", "非法路径")
        else:
            if(os.path.isfile(path)):
                self.Setting.modelpath=path
            else:
                QMessageBox.information(None, "Title", "应该选择文件")

    def setup_import_filepath1(self):
        self.ui.btn_importcbdir.clicked.connect(self.on_import_filepath1_clicked)
    def on_import_filepath1_clicked(self):
        if (not Util.check_path_exists(self.ui.Tb_cbdir.toPlainText())):
            QMessageBox.information(None, "Title", "非法路径")
        else:
            self.Setting.inputDir1=self.ui.Tb_cbdir.toPlainText()
    def setup_import_filepath2(self):
        self.ui.btn_importctdir.clicked.connect(self.on_import_filepath2_clicked)
    def on_import_filepath2_clicked(self):
        if (not Util.check_path_exists(self.ui.Tb_ctdir.toPlainText())):
            QMessageBox.information(None, "Title", "非法路径")
        else:
            self.Setting.inputDir2=self.ui.Tb_ctdir.toPlainText()

    def setup_showlinechart(self):
        self.ui.btn_showlinechart.clicked.connect(self.on_showlinechart_clicked)
    def on_showlinechart_clicked(self):
        self.clear_Chart()
        merits = ['ssim', 'psnr', 'mse']
        if not self.ui.isShow_ssim.isChecked():
            merits.remove('ssim')
        if not self.ui.isShow_psnr.isChecked():
            merits.remove('psnr')
        if not self.ui.isShow_mse.isChecked():
            merits.remove('mse')
        if len(merits) ==0 :
            QMessageBox.information(None, "Title", "请至少勾选一个指标")
            return
        points=Util.getmeritslList(r'C:\Users\Tyang\Desktop\code\DataSets\Validation\trainA',r'C:\Users\Tyang\Desktop\code\DataSets\Validation\trainB',merits)
        self.showLineChart(points)
    def showLineChart(self,PointsList):
        seriesList = []
        x_axis = QValueAxis()
        x_axis.setTickCount(50)  # 设置 x 轴上的刻度数量
        for key, value in PointsList.items():
            series = QLineSeries()
            series.setName(key)
            series.attachAxis(x_axis)
            for i, y in enumerate(value):
                series.append(i, y)

            seriesList.append(series)

        self.myLinechart = QChart()
        self.myLinechart.addAxis(x_axis, Qt.AlignBottom)
        self.myLinechart.legend()
        for series in seriesList:
            self.myLinechart.addSeries(series)
        self.myLinechart.createDefaultAxes()

        # 将图表添加到图表视图
        chartView = QChartView(self.myLinechart)

        # 找到你在UI中放置QTabWidget的名称，例如tabWidget
        self.ui.LineChartLayout.addWidget(chartView)

    def clear_Chart(self):
        # 清除布局中的所有部件
        while self.ui.LineChartLayout.count():
            item = self.ui.LineChartLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
