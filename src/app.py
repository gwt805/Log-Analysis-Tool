import sys
import glob
import json
import openpyxl
from ui import Mainui
from PyQt5.QtCore import QTimer
from easydict import EasyDict as edict
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMessageBox, QAbstractItemView


class Fun(Mainui):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.clean_result_uuid_list = []
        self.send_rcc_uuid_list = []
        self.same_list = []
        self.show()

        self.action_Log.triggered.connect(self.get_log_file_path)
        self.action.triggered.connect(self.get_save_result_path)
        self.pushButton.clicked.connect(self.save_result_file)
    
    def load_log_files(self):
        logfiles = glob.glob(f'{self.input_log.text()}/gs_console*.log')
        
        if len(logfiles) == 0:
            reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("该目录下没有 console 日志 , 请重选目录"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("重选"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.get_log_file_path()
            else:
                self.input_log.setText("")
        else:
            for item in logfiles:
                self.show_message(f"正在加载 {item} 文件")
                with open(item, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for l in lines:
                    if "[garbage_upload] send rcc" in l:
                        tmp = edict(json.loads(l.split(" ")[-1].replace("\n", "")))
                        t_l = [tmp.id, tmp.category]
                        if t_l not in self.send_rcc_uuid_list:
                            self.send_rcc_uuid_list.append(t_l)
                    
                    if "clean_result(0)" in l:
                        tmp = l.split(" ")[-2].replace("dirty_id(", "").replace(")", "")
                        if tmp not in self.clean_result_uuid_list:
                            self.clean_result_uuid_list.append(tmp)
            for item in self.send_rcc_uuid_list:
                if item[0] in self.clean_result_uuid_list:
                    self.same_list.append(item[0])
            QTimer.singleShot(1000, lambda:self.show_message("加载 log 文件完成"))
            
            QTimer.singleShot(2000, self.show_label)

            QTimer.singleShot(3000, self.create_table)
    
    def create_table(self):
        length_clean_result = len(self.clean_result_uuid_list)
        model = QStandardItemModel(self.tableView)
        model.setHorizontalHeaderLabels(['UUID'])
        model.setColumnCount(1)
        model.setRowCount(length_clean_result)
        for i in range(length_clean_result):
            item = QStandardItem(self.clean_result_uuid_list[i])
            model.setItem(i, 0, item)
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.show()

        # ===========================================================

        length_send_rcc = len(self.send_rcc_uuid_list)
        model_2 = QStandardItemModel(self.tableView_2)
        model_2.setColumnCount(3)
        model_2.setRowCount(length_send_rcc)
        model_2.setHorizontalHeaderLabels(['UUID', '标签', '中文标签'])
        
        for i in range(length_send_rcc):
            tmp = self.send_rcc_uuid_list[i]
            if tmp[-1] == "large_garbage" or tmp[-1] == "garbage":
                tmp.append("垃圾")
            if tmp[-1] == "sewage":
                tmp.append("脏污")
            item1 = QStandardItem(tmp[0])
            item2 = QStandardItem(tmp[1])
            item3 = QStandardItem(tmp[2])
            model_2.setItem(i, 0, item1)
            model_2.setItem(i, 1, item2)
            model_2.setItem(i, 2, item3)
        self.tableView_2.setModel(model_2)
        self.tableView_2.setColumnWidth(0, 300)
        self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_2.show()
        # ===================================================================
        length_same = len(self.same_list)
        model_3 = QStandardItemModel(self.tableView_3)
        model_3.setColumnCount(1)
        model_3.setRowCount(length_same)
        model_3.setHorizontalHeaderLabels(['UUID'])
        
        for i in range(length_same):
            item = QStandardItem(self.same_list[i])
            model_3.setItem(i, 0, item)
        self.tableView_3.setModel(model_3)
        self.tableView_3.setColumnWidth(0, 300)
        self.tableView_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_3.show()

    def show_message(self, msg):
        self.statusBar().showMessage(msg)
    
    def show_label(self):
        self.label_status = QLabel(f"clean_result:{len(self.clean_result_uuid_list)} 个 || send_rcc: {len(self.send_rcc_uuid_list)} 个 || same: {len(self.same_list)} 个")
        self.statusBar().addPermanentWidget(self.label_status)

    def get_log_file_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择 Log 所在文件夹")
        if path is not None:
            self.input_log.setText(path)

            QTimer.singleShot(1000, self.load_log_files)

    def get_save_result_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择保存文件夹")
        if path is not None:
            self.input_result.setText(path)
    
    def save_result_file(self):
        if self.input_result.text() == "":
            reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请选择结果保存目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("选择保存目录"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.get_save_result_path()
            else:
                self.input_result.setText("")
        else:
            workbook = openpyxl.Workbook()

            sheet = workbook.active
            sheet.title = "send rcc"

            sheet['A1'] = "UUID"
            sheet['B1'] = "标签"
            sheet['C1'] = "中文标签"

            sheet.column_dimensions['A'].width = 40
            sheet.column_dimensions['B'].width = 15

            for it in self.send_rcc_uuid_list:
                tmp = it
                if tmp[-1] == "large_garbage" or tmp[-1] == "garbage":
                    tmp.append("垃圾")
                if tmp[-1] == "sewage":
                    tmp.append("脏污")
                sheet.append(tmp)

            sheet2 = workbook.create_sheet("clean result")
            sheet2['A1'] = "UUID"
            sheet2.column_dimensions['A'].width = 40

            for it in self.clean_result_uuid_list:
                sheet2.append([it])

            try:
                workbook.save(f"{self.input_result.text()}/show.xlsx")
                reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("已保存到该目录下, 名为 show.xlsx !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()
            except PermissionError as pe:
                reply = QMessageBox(QMessageBox.Question, self.tr("警告"), self.tr(pe), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fun = Fun()
    sys.exit(app.exec_())