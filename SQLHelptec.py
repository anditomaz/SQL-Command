import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextDocument, QFont, QTextOption, QSyntaxHighlighter, QTextCharFormat, QColor
import pyodbc
import sqlparse

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

    def highlightBlock(self, text):
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#F92672"))
        keywordFormat.setFontWeight(QFont.Bold)

        keywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "FROM", "SET", "WHERE", "ORDER BY", "DESC", "HAVING", "INNER JOIN", "OUTER JOIN", "LEFT JOIN", "GROUP BY", "IF", "ELSE", "MAX", "AVG", "COUNT", "MIN", "GROUP BY", "ON", "IN", "GRANT", "TO", "REVOKE"]

        for word in keywords:
            index = text.upper().find(word)
            while index >= 0:
                length = len(word)
                self.setFormat(index, length, keywordFormat)
                index = text.upper().find(word, index + length)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EdtServer = QtWidgets.QLineEdit(self.centralwidget)
        self.EdtServer.setGeometry(QtCore.QRect(20, 40, 221, 20))
        self.EdtServer.setObjectName("EdtServer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 21, 41, 16))
        self.label.setObjectName("label")
        self.EdtDatabase = QtWidgets.QLineEdit(self.centralwidget)
        self.EdtDatabase.setGeometry(QtCore.QRect(20, 90, 221, 20))
        self.EdtDatabase.setObjectName("EdtDatabase")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 72, 61, 16))
        self.label_2.setObjectName("label_2")
        self.EdtUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.EdtUserName.setGeometry(QtCore.QRect(20, 140, 221, 20))
        self.EdtUserName.setObjectName("EdtUserName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 122, 51, 16))
        self.label_3.setObjectName("label_3")
        self.EdtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.EdtPassword.setGeometry(QtCore.QRect(20, 190, 221, 20))
        self.EdtPassword.setObjectName("EdtPassword")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 172, 61, 16))
        self.label_4.setObjectName("label_4")
        self.BtnConectar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConectar.setGeometry(QtCore.QRect(167, 220, 75, 23))
        self.BtnConectar.setObjectName("BtnConectar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 260, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(272, -3, 20, 271))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 8, 621, 260))
        self.textEdit.setObjectName("textEdit")
        self.BtnExecutar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnExecutar.setGeometry(QtCore.QRect(810, 280, 101, 31))
        self.BtnExecutar.setObjectName("BtnExecutar")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 320, 1001, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(11, 345, 891, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-20, 602, 1011, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(173, 216, 230))  # Definindo a cor azul claro
        MainWindow.setPalette(palette)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BtnConectar.clicked.connect(self.connect_to_database)
        self.BtnExecutar.clicked.connect(self.execute_query)

        self.textEdit.textChanged.connect(self.convert_to_upper)

        self.EdtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 8, 621, 260))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: #272822; color: #F8F8F2;")

        self.highlighter = SyntaxHighlighter(self.textEdit.document())

        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

    def convert_to_upper(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setPlainText(text.upper())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SQL HelpTec", "SQL-Command"))
        self.label.setText(_translate("MainWindow", "Server"))
        self.label_2.setText(_translate("MainWindow", "Database"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.BtnConectar.setText(_translate("MainWindow", "Conectar"))
        self.BtnExecutar.setText(_translate("MainWindow", "Executar"))
        item = self.tableWidget.horizontalHeaderItem(0)

    def connect_to_database(self):
        server = self.EdtServer.text()
        database = self.EdtDatabase.text()
        username = self.EdtUserName.text()
        password = self.EdtPassword.text()

        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            QMessageBox.information(None, "Connection", "Connected to the database!")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error connecting to the database: {e}")

    def execute_query(self):
        try:
            if not hasattr(self, 'conn') or not self.conn:
                QMessageBox.critical(None, "Error", "Connection not established!")
                return

            textCursor = self.textEdit.textCursor()
            selected_text = textCursor.selectedText().strip()

            if selected_text:
                query = selected_text
            else:
                query = self.textEdit.toPlainText().strip()

            if not query:
                QMessageBox.warning(None, "Warning", "No query to execute!")
                return

            query_type = query.split(' ', 1)[0].upper()

            if query_type in ["SELECT", "SHOW", "DESCRIBE", "EXPLAIN"]:
                cursor = self.conn.cursor()
                formatted_query = sqlparse.format(query, reindent=True)
                cursor.execute(formatted_query)
                cursor.execute(query)
                result = cursor.fetchall()

                if len(result) > 0:
                    col_count = len(cursor.description)
                    self.tableWidget.setColumnCount(col_count)

                    for i in range(col_count):
                        header = cursor.description[i][0]
                        self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(header))

                    self.tableWidget.setRowCount(len(result))
                    for i, row in enumerate(result):
                        for j, val in enumerate(row):
                            item = QTableWidgetItem(str(val))
                            self.tableWidget.setItem(i, j, item)
            else:
                cursor = self.conn.cursor()
                formatted_query = sqlparse.format(query, reindent=True)
                cursor.execute(formatted_query)
                cursor.execute(query)
                self.conn.commit()
                QMessageBox.information(None, "Success", "Query executed successfully!")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error executing query: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)
    MainWindow.setFixedSize(914, 637)
    MainWindow.show()
    sys.exit(app.exec_())