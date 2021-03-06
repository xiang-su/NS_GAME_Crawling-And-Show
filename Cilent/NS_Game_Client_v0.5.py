import pymysql.cursors
from PyQt5 import QtWidgets
from PyQt5.Qt import QApplication, QMessageBox, QTableWidgetItem, QWidget

from main import Ui_Form

#配置数据库连接
connect = pymysql.Connect(
 #   host='',
 #   port=3306,
  #  user='root',
  #  passwd='',
  #  db='',
  #  charset='utf8'
  host='45.77.11.232',
    port=3306,
    user='root',
    passwd='Inspur@871',
    db='NS_Game',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
now_show_num = 0


class mywindow ( QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load)   #槽函数不用加括号
        self.pushButton_2.clicked.connect(self.last)
        self.pushButton_3.clicked.connect(self.next)

    def load(self):
        #print("helloWorld")
        #查询数据
        sql = "SELECT Game_Name, Game_Name_ZH, Release_date_order, On_sale, Recent_release, Coming_soon, Has_demo, Image_url,Best_Price,Best_Price_CHN,Best_Price_country FROM NS_Game_Index LIMIT 0,20 "
        #data = ('13512345678')
        print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        row = cursor.rowcount
        vol = len(rows[0])
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        for i in range(row):
            for j in range(vol):
                temp_data=rows[i][j]  #临时记录，不能直接插入表格
                data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                self.tableWidget.setItem(i,j,data)
        print('共查找出', cursor.rowcount, '条数据')
        # newItem = QTableWidgetItem("松鼠")
        # self.tableWidget.setItem(0, 0, newItem)


    def next(self):
        #print("helloWorld")
        #查询数据
        global now_show_num
        now_show_num = now_show_num + 20
        sql = "SELECT Game_Name, Game_Name_ZH, Release_date_order, On_sale, Recent_release, Coming_soon, Has_demo, Image_url,Best_Price,Best_Price_CHN,Best_Price_country FROM NS_Game_Index LIMIT "+str( now_show_num)+" ,20 "
        print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        row = cursor.rowcount
        vol = len(rows[0])
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        self.tableWidget.setVerticalHeaderLabels([str(now_show_num + 1), str(now_show_num + 2), str(now_show_num + 3),
                                                 str(now_show_num + 4), str(now_show_num + 5), str(now_show_num + 6),
                                                 str(now_show_num + 7), str(now_show_num + 8), str(now_show_num + 9),
                                                 str(now_show_num + 10), str(now_show_num + 11), str(now_show_num + 12),
                                                 str(now_show_num + 13), str(now_show_num + 14), str(now_show_num + 15),
                                                 str(now_show_num + 16), str(now_show_num + 17), str(now_show_num + 18),
                                                 str(now_show_num + 19), str(now_show_num + 20)])
        for i in range(row):
            for j in range(vol):
                temp_data=rows[i][j]  #临时记录，不能直接插入表格
                data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                self.tableWidget.setItem(i,j,data)
        print('共查找出', cursor.rowcount, '条数据')
        # newItem = QTableWidgetItem("松鼠")
        # self.tableWidget.setItem(0, 0, newItem)

    def last(self):
        #print("helloWorld")
        #查询数据
        global now_show_num
        if now_show_num< 20:
            reply = QMessageBox.information(self, "提醒", "已到首页！", QMessageBox.Yes | QMessageBox.No)
            now_show_num = 0
        else:
            now_show_num = now_show_num - 20

        sql = "SELECT Game_Name, Game_Name_ZH, Release_date_order, On_sale, Recent_release, Coming_soon, Has_demo, Image_url,Best_Price,Best_Price_CHN,Best_Price_country FROM NS_Game_Index LIMIT "+str( now_show_num)+" ,20 "
        print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        row = cursor.rowcount
        vol = len(rows[0])
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        self.tableWidget.setVerticalHeaderLabels([str(now_show_num + 1), str(now_show_num + 2), str(now_show_num + 3),
                                                 str(now_show_num + 4), str(now_show_num + 5), str(now_show_num + 6),
                                                 str(now_show_num + 7), str(now_show_num + 8), str(now_show_num + 9),
                                                 str(now_show_num + 10), str(now_show_num + 11), str(now_show_num + 12),
                                                 str(now_show_num + 13), str(now_show_num + 14), str(now_show_num + 15),
                                                 str(now_show_num + 16), str(now_show_num + 17), str(now_show_num + 18),
                                                 str(now_show_num + 19), str(now_show_num + 20)])
        for i in range(row):
            for j in range(vol):
                temp_data=rows[i][j]  #临时记录，不能直接插入表格
                data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                self.tableWidget.setItem(i,j,data)
        print('共查找出', cursor.rowcount, '条数据')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
