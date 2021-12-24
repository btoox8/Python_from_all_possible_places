#Our basic code

from PyQt5 import QtCore, QtGui,QtWidgets
import sys  # system to deal with cmd as terminal

#variable , our app use cmd
app = QtWidgets.QApplication(sys.argv)
# make screen
w = QtWidgets.QWidget()
#look QtW....QW...

#call our screen
w.show()
               # w, h #
#w.resize(500,500)
               #left,top #
#w.move(50,50)

# take both resize and move in one code
                         #l,    t,     w,    h#
w.setGeometry(50,50,500,500)
#windowname.setWindowTitle('title')
w.setWindowTitle('btoo : v-1.0')

#change window color
# take color by name ir rgb or hex , from web pages

#windowname.setStyleSheet('css codes')
w.setStyleSheet('background-color:red;')

#change icon
# تحصل عاي المسار المطلوب من cmd
#windoname.setWindowIcon(QtGui.QIcon('your_path.img_type'))
#w.setWindowIcon(QtGui.QIcon(c:\\..\\python.png))

#make our app work without closing
app.exec_()  #it equal to main loop

#####
#resize
# التحكم بحجم البرنامج
#move
#ظهور البرنامج علي اي بعد من زوايا الشاشه
# يكتبان داخل الكود الرئيسي