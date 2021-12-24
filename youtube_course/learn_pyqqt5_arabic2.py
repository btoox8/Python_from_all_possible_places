from PyQt5 import QtCore, QtGui,QtWidgets
import sys  


app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.show()
w.setGeometry(50,50,1000,500)
w.setWindowTitle('btoo : v-1.0')
w.setStyleSheet('background-color:red;')

#make buttons
btn1 = QtWidgets.QPushButton('learn pyqt5', w)  # w = place where should be appear
btn1.resize(150,50)
btn1.move(100,100)
btn1.setStyleSheet('background-color:#58D3F7; color:white;font-size:20px;border:2px solid black;border-radius:3px;font-family:tajwal;')
# tooltip
#bittonname.setToolTip('our text')
btn1.setToolTip('first button')
##
btn2 = QtWidgets.QPushButton('learn tkinter',w)
btn2.resize(150,50)
btn2.move(100,150)
btn2.setStyleSheet('background-color:#58D3F7; color:white;font-size:20px;border:2px solid black;border-radius:3px 4px ppx 8px;font-family:tajwal;')

#make button to do certain job
btn3 = QtWidgets.QPushButton('exit' , w)
#buttonname.clicked.connect(our job)
btn3.clicked.connect(exit)
#لاحظ عند اضافه ايقونه لازم تتعدي السلاش بتديلها
#btn3.setIcon(QtGui.QIcon('c:\\users....png'))


app.exec_()  

