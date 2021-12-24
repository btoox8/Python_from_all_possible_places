# Whay is python
- is a general purpose programming language
- is a high level programming
- is portable
- is an interpreted language
- is strongly typed ( don't change from data type to another automatically )
- has huge set of libraries ( so you can access them and use their abillity without rewriting code again ) 

# to deal with properties
sudo apt install software-properties-common

# to add more release of one program
sudo add-apt-repository ppa:deadsnakes/ppa
then press [Enter]

# download python
sudo apt install python3.10

# what is tkinter
- python module use to GUI
- must imported into your python project to use it
- ttk ia a component of tkinter that has themed widget

# create project directory
- from command line == terminal : mkdir directoryname
- or just add new folder to certain place

# virtual env
- tool used to isolated python environments
- the environment it creates has it's own installaton directories and files
- does not share libraries with othe rvirtual environments

# installing python virtual environment
sudo pip install virtualenv

# create virtual env
virtualenv nameofVirtualEnvironment

# activate virtual env
source myenv/bin/activate

source Intro/bin/activate
الان سنجد اسم البيئه بين قوسين في بداية موجه الاوامر

# activate on windows
myenv\scripts\activate

# what is SQLite
- SLite is a software library that provides a relational database management system.
- The lite in SQLite means light weight in terms of setup database administration, and required resource.

# SLite features:
- self-contained : used in embedded devices like iphones, android ...
- serverless :
              - not need TCP/IP protocol to send and recive reuests (with server)
              - so does n't require a server to run
              - it's database is integrated with the application that accesses the database
- Zero-configuration
- transactional: are ACID- compliant Atomic,Consistent,Isolated,Durable
- use dynamin types for tables
- allows a single database connection to access multiple files simultaneously
اي بامكاننا استدعاء ايجزء من قاغدة البيانات ليتفاعل مع بقية العناصر او مع قواعد مختزنة اخري 

# install SQLite
- download what has command line with it
https://www.sqlite.org/download.html

- open file on terminal
./sqlite3
.help
.quot == ctrl + c

# Db browser for sqlite
- it come with linux system
- as GUI
https://sqlitebrowser.org/dl/

or
sudo apt-get install sqlitebrowser

# make db
sqlit3 name.db
.databases

then go to GUI, open database
excute SQL
- some to know:
                primary key : increase automatically
                VARCHAR     : varaible character
                NOT NULL    : not allow to be empty
                UNIQUE      : not allow repeate this value twice
- Ex:
CREATE TABLE contacts_list(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    number INTEGER NOT NULL UNIQUE
)

then press play/excute button

# we can use ccs style
ttk.style()
ttk.style.configure('our widget', css to change)