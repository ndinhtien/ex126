from PyQt6.QtWidgets import QInputDialog,QTableWidgetItem
from UiFile import Ui_MainWindow
from Practice import *

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
       self.data = load_data()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.refresh_data(load_data())
        self.pushButton.clicked.connect(lambda: self.refresh_data(self.data))
        self.pushButton_2.clicked.connect(self.filter_by_close)
        self.pushButton_3.clicked.connect(self.extract_selected_columns)
        self.pushButton_4.clicked.connect(self.export_transaction_date)
        self.pushButton_5.clicked.connect(self.filter_multi_dates)

    def refresh_data(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.tableWidget.setItem(row, col, item)

    def filter_by_close(self):
        user_input, ok = QInputDialog.getText(self.MainWindow, "Input Value", "Enter value to filter (',' for 2 value):")
        if ok and user_input:
            user_input = user_input.strip().split(",")
            result = filter_by_close(self.data, float(user_input[0]), float(user_input[1]))
            self.refresh_data(result)

    def extract_selected_columns(self):
        user_input, ok = QInputDialog.getText(self.MainWindow, "Input Value",
                                              "Enter value to filter (',' for 2 value):")
        if ok and user_input:
            user_input = user_input.strip().split(",")
            result = extract_selected_columns(self.data, float(user_input[0]), float(user_input[1]))
            self.refresh_data(result)

    def export_transaction_date(self):
        user_input, ok = QInputDialog.getText(self.MainWindow, "Input Value",
                                              "Enter value to filter:")
        if ok and user_input:
            result = export_transaction_date(self.data, user_input)
            self.refresh_data(result)

    def filter_multi_dates(self):
        user_input, ok = QInputDialog.getText(self.MainWindow, "Input Value",
                                              "Enter value to filter (',' for multi days):")
        if ok and user_input:
            user_input = user_input.split(",")
            result = filter_by_dates(self.data, user_input)
            self.refresh_data(result)

    def show(self):
        self.MainWindow.show()




