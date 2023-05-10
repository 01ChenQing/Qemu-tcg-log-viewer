# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem,QAbstractItemView
from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt
from ui_form import Ui_Widget


class Trans_block:
    def __init__(self,tb_log_text):
        self.asm_in = []
        self.asm_tcg = []
        self.asm_out = []
        self.asm_data = []
        self.tb_name = 'NULL'
        self.format_text(tb_log_text)
        self.tb_address = '--> ' + self.asm_in[0].split(':')[0]   #get first insn in tb and keep address
        self.format_asm_lists()

    def format_text(self,text):
        asm_list = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith('IN:'):
                asm_list = self.asm_in
                self.tb_name = line   #get tb name from IN:name
                continue
            elif line.startswith('OP:'):
                asm_list = self.asm_tcg
                continue
            elif line.startswith('OUT:'):
                asm_list = self.asm_out
                continue
            elif line.startswith('data:'):
                continue
                asm_list = self.asm_data

            line = self.nop_hex_code(line)
            asm_list.append(line)

    def format_asm_lists(self):
        new_asm_in = []
        new_asm_tcg = []
        new_asm_out = []

        for line in self.asm_in:
            ad,asm = line.split(':')
            new_asm_in.append('--> ' + ad)
            new_asm_in.append(asm)

        for line in self.asm_tcg:
            if '----' in line:
                ad = line.split()[1] #get guest ad
                new_asm_tcg.append('--> ' + '0x' + ad)
                continue
            new_asm_tcg.append(line)

        for line in self.asm_out:
            if '-- guest addr' in line:
                line_list = line.split()
                ad = line_list[line_list.index('addr') + 1] #get guest ad
                new_asm_out.append('--> ' + ad)
                continue
            new_asm_out.append(line)

        self.asm_in = new_asm_in
        self.asm_tcg = new_asm_tcg
        self.asm_out = new_asm_out


    def nop_hex_code(self,line):
        line_list = line.split('  ')
        if len(line_list) > 2:
            line_list[1] = '' #delete insn hex code
            line_list = [x for x in line_list if x != '']
            line = ' '.join(line_list)
        return line


class Qemu_log:

    def __init__(self,log_path):
        self.tb_list = []
        self.format_file(log_path)
        self.t = []
        self.t.append("a")

    def format_file(self,file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        for tb_log_text in text.split('----------------')[1:]: #delete PROLOGUE:
            self.tb_list.append(Trans_block(tb_log_text))


class Widget(QWidget):
    def __init__(self,qemu_log_path,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.qemu_log = Qemu_log(qemu_log_path)
        self.init_tb_table()
        self.ui.tb_table.itemClicked.connect(self.tb_item_clicked)
        self.ui.t_asm_in.itemClicked.connect(self.on_item_clicked)
        self.ui.t_asm_tcg.itemClicked.connect(self.on_item_clicked)
        self.ui.t_asm_out.itemClicked.connect(self.on_item_clicked)
        self.setStyleSheet("QWidget { background-color: rgb(144, 238, 144); }")
        self.setWindowFlags(Qt.FramelessWindowHint)

    def init_tb_table(self):
        tb_ad_list = [tb.tb_address for tb in self.qemu_log.tb_list]
        self.flash_table(self.ui.tb_table,tb_ad_list)

    def tb_item_clicked(self, item):
        tb_index = item.row()
        tb = self.qemu_log.tb_list[tb_index]
        self.flash_table(self.ui.t_asm_in,tb.asm_in)
        self.flash_table(self.ui.t_asm_tcg,tb.asm_tcg)
        self.flash_table(self.ui.t_asm_out,tb.asm_out)

    def flash_table(self,table,list):
        table.setRowCount(0)
        for line in list:
            self.add_row(table,line)
        table.resizeColumnsToContents()

    def add_row(self,table,line):
        row_position = table.rowCount()
        table.insertRow(row_position)
        item = QTableWidgetItem(line)

        if '-->' in line:
            item.setBackground(QBrush(QColor(144, 255, 144)))
        table.setItem(row_position, 0, item)

    def on_item_clicked(self, item):
        search_item = item.text()
        self.select_and_scroll_to_item(self.ui.t_asm_in, search_item)
        self.select_and_scroll_to_item(self.ui.t_asm_tcg, search_item)
        self.select_and_scroll_to_item(self.ui.t_asm_out, search_item)

    def select_and_scroll_to_item(self, table, search_item):
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and item.text() == search_item:
                table.setCurrentItem(item)
                table.scrollToItem(item)
                table.scrollToItem(item, QAbstractItemView.PositionAtTop)
                return

if __name__ == "__main__":
    current_dir = os.getcwd()
    relative_path = 'log_jit'
    file_path = os.path.join(current_dir, relative_path)

    app = QApplication(sys.argv)
    widget = Widget(file_path)
    widget.show()
    sys.exit(app.exec())
