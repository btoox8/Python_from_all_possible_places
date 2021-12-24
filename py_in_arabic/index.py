## importing things when call PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

## connect with DB
#import mysqldb
import mysql.connector
#import MySQLdb


## we need them to deal with path and files

import sys
import os
from os import path
import time 

## to open our design with it 

from PyQt5.uic import loadUiType
from mysql.connector.abstracts import MySQLCursorAbstract

## our ui (design file),path و look at man.ui

FROM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))

## main class 

class Main(QMainWindow,FROM_CLASS):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handel_DB_Connection()
        self.Handle_buttons()

        

## disapper def for certain things in the run time 

    def InitUI(self):
        ## changes in the run time
        self.setWindowTitle("برنامج ادارة السيارات")  #  our program title
        self.tabWidget.tabBar().setVisible(False) 
            # disappear object , here we deal with (tabWidget), 
            # we can bring it;s name from our qt designer 

## databaseconnection
    def Handel_DB_Connection(self):
        ## DB
        """
        db = MySQLdb.connect(host="localhost",user="btoo",passwd="1234", db="mydb")
        cur = db.cursor  ## it mean go with order and back with data
              ## db == our upper code 
        print('Connection done')
        """

        mydb = mysql.connector.connect(host="localhost",user="btoo",passwd="1234", db="mydb") # mayinstade db with database
        myCursor = mydb.cursor()
        myCursor.execute()

        for i in myCursor:
            print(i)

        ## now connect our data with this program

 
## dealing wuth btn

    def Handle_buttons(self):
        ## all buttons in the app
        ## connect button with methods , becarful delete method (
        ## you need to go to your qt designer toadjust objects_names

        self.pushButton.clicked.connect(self.Add_Car_info)
        self.pushButton_2.clicked.connect(self.Update_Car_info)
        self.pushButton_3.clicked.connect(self.Delete_Car_info)

        ## fuel
        self.btn_fuel_add.clicked.connect(self.Add_Fuel_info)
        self.btn_fuel_update.clicked.connect(self.Update_Fuel_info)

        ##maintenance
        self.btn_main_add.clicked.connect(self.Add_Main_info)
        self.btn_main_update.clicked.connect(self.Update_Main_info)
        self.btn_main_delete.clicked.connect(self.Delete_Main_info)


        ##licence
        self.btn_licence_add.clicked.connect(self.Add_Licence_info)
        self.btn_licence_update.clicked.connect(self.Update_Licence_info)

        ##revenu
        self.btn_revenu_add.clicked.connect(self.Add_Revenus_info)
        self.btn_revenu_update.clicked.connect(self.Revenus_info)

        ##rents
        self.btn_rents_add.clicked.connect(self.Add_Rents_info)
        self.btn_rents_update.clicked.connect(self.Update_Rents_info)

        ##ew
        self.btn_ew_add.clicked.connect(self.Add_ele_water_info)
        self.btn_ew_update.clicked.connect(self.Update_ele_water_info)

        ##search
        self.pushButton_6.clicked.connect(self.search)

        
    


    ##################################
    ##search
    def search(self):
        #print ('search')
        #print(self.listWidget.row(self.listWidget.currentItem()))

        if self.listWidget.row(self.listWidget.currentItem())  == 0:
            sql = ''' SELECT * FROM car_info WHERE car_number = %s '''
            car_number = self.lineEdit_70.text()

            self.cur.execute(sql , [(car_number)])
            data = self.cur.fetchall()

            for row in data:
                self.lineEdit.setText(str(row[1]))  # be carful with ()
                self.lineEdit_2.setText(row[2])
                self.lineEdit_3.setText(row[3])
                self.comboBox.setCurrentIndex(int(row[4]))
                self.lineEdit_8.setText(row[5])
                self.lineEdit_4.setText(row[6])
                self.comboBox_2.setCurrentIndex(int(row[7]))
                self.lineEdit_12.setText(row[8])
                self.lineEdit_6.setText(str(row[9]))
                self.lineEdit_11.setText(str(row[10]))
                self.lineEdit_9.setText(str(row[11]))
                self.lineEdit_10.setText(row[12])
                self.lineEdit_5.setText(row[13])






    ## Our tabs def
    ## now all tabels and it's sub

    ##Cars Info ##

    ## add car
    def Add_Car_info(self):
        ## on data  = self.object_from_designer_program()
        car_number = self.lineEdit.text()
        owner_company = self.lineEdit_2.text()
        branch = self.lineEdit_3.text()
        service_mode = self.comboBox.currentIndex()
        shaceh_number = self.lineEdit_8.text()
        motor_number = self.lineEdit_4.text()
        fuel_type = self.comboBox_2.currentIndex()
        car_type = self.lineEdit_12.text()
        car_model = self.lineEdit_6.text()
        car_load = self.lineEdit_11.text()
        car_weight = self.lineEdit_9.text()
        car_shape = self.lineEdit_10.text()
        car_color = self.lineEdit_5.text()

        ## test it
        # print(car_number)

        self.cur.execute(
            '''
            INSERT INTO
            car_info(car_number,owner_company,branch,service_mood,motor_number,fuel_type,car_type,car_model,car_load,car_weight,car_shape,car_color)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''' ,
            (car_number,owner_company,branch,service_mode,motor_number,fuel_type,car_type,car_model,car_load,car_weight,car_shape,car_color)

        )
        self.db.commit()  # to doing our edit inside database
        print('Done')  #to make sure it work

        ## create the other tabels
        # اربط هذه النافذع بعمود معين باخذ قيمتها المعطاه
        self.cur.execute(''' INSERT INTO fuel_info(car_number) VALUES(%s) ''' , (car_number,))
        self.cur.execute(''' INSERT INTO licence_info(car_number) VALUES(%s) ''' , (car_number,))
        self.cur.execute(''' INSERT INTO maintenance_info(car_number) VALUES(%s) ''' , (car_number,))
        self.cur.execute(''' INSERT INTO rents_info(car_number) VALUES(%s) ''' , (car_number,))
        self.cur.execute(''' INSERT INTO revenues_info(car_number) VALUES(%s) ''' , (car_number,))
        self.cur.execute(''' INSERT INTO WAEL_info(car_number) VALUES(%s) ''' , (car_number,))
        
        self.db.commit()

        ## لاتنسي الذهاب لقاعدةالبيانات وتعديل في خانه id 
        ## كل جدول بوضع صاح علي خانتين
        ## AI, UQ

        # التفريغ للحقول بعد ضغط الازرار
        #look at camelcase after setCamelCase('' or 0), as our default

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_8.setText('')
        self.lineEdit_4.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_12.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_5.setText('')

        # استخدام بار الحاله ، لمتابعه المعلومات
        self.statusBar.showMessage('تمت اضافة المعلومات بنجاح')
        time.sleep(10)  #  تنظيفهابعد 10 ثواني ، حيث تستمر لهذه المده ثم تظهر التي تليها فارغه
        self.statusBar.showMessage('')




    ## update car info
    def Update_Car_info(self):
        car_number = self.lineEdit.text()
        owner_company = self.lineEdit_2.text()
        branch = self.lineEdit_3.text()
        service_mode = self.comboBox.currentIndex()
        shaceh_number = self.lineEdit_8.text()
        motor_number = self.lineEdit_4.text()
        fuel_type = self.comboBox_2.currentIndex()
        car_type = self.lineEdit_12.text()
        car_model = self.lineEdit_6.text()
        car_load = self.lineEdit_11.text()
        car_weight = self.lineEdit_9.text()
        car_shape = self.lineEdit_10.text()
        car_color = self.lineEdit_5.text()

        ## test it
        # print(car_number)

        self.cur.execute(
            '''
            UPDATE
            car_info SET car_number = %s,owner_company = %s,branch = %s,service_mood = %s,motor_number = %s,fuel_type = %s,car_type = %s,car_model = %s,car_load = %s,car_weight = %s,car_shape = %s,car_color = %s
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''' ,
            (car_number,owner_company,branch,service_mode,motor_number,fuel_type,car_type,car_model,car_load,car_weight,car_shape,car_color)

        )
        self.db.commit()  # to doing our edit inside database
        print('Done')  #to make sure it work

        
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_8.setText('')
        self.lineEdit_4.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_12.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_5.setText('')

        # استخدام بار الحاله ، لمتابعه المعلومات
        self.statusBar.showMessage('تم تعديل المعلومات بنجاح')
        #time.sleep(10)  #  تنظيفهابعد 10 ثواني ، حيث تستمر لهذه المده ثم تظهر التي تليها فارغه
        #self.statusBar.showMessage('')


    ##delete car
    def Delete_Car_info(self):
        car_number = self.lineEdit_70.text()
        self.cur.execute(''' DELETE FROM car_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM fuel_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM licence_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM maintenance_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM rents_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM revenus_info WHERE car_number = %s ''', (car_number,)) 
        self.cur.execute(''' DELETE FROM WAEL_info WHERE car_number = %s ''', (car_number,)) 

        self.db.commit()
        self.statusbar.showMessage('تم مسح المعلومات بنجاح')


    ##################################
    ##fuel##

    ##add fuel info
    def Add_Fuel_info(self):
        pass

    ## Update fuel info
    def Update_Fuel_info(self):
        pass


    ## Maintenance##

    def Add_Maintenance_info(self):
        pass

    def Update_Maintenance_info(self):
        pass

    ##################################
    ##Licence##
    def Add_Licence_info(self):
        pass

    def Update_Licence_info(self):
        pass

    ##revenus##
    def Add_Revenus_info(self):
        pass

    def Update_Revenus_info(self):
        pass

    ##rents##
    def Add_Rents_info(self):
        pass

    def Update_Rents_info(self):
        pass


    #################################
    ##electricity & water
    def Add_ele_water_info(self):
        pass

    def Update_ele_water_info(self):
        pass


    ###########
    ## main ##
## it begin from start of our line
## take copy from our main
def main():
        app = QApplication(sys.argv)
        window = Main()   ## copy
        window.show()     ## show
        app.exec_()        ## run main loop

## to male it start from here == run index
if __name__ == '__main__':
        main() # we start from this method
    ###########




