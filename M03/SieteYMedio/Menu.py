
import pymysql
from funciones.funciones import *
from funciones.diccionarios import *
##############################################################################################################
conn=pymysql.connect(host="20.86.76.157",user="proyecto", password="P@ssw0rd12345",database="sieteymedioDB") #
cur = conn.cursor()                                                                                          #
##############################################################################################################



###########################    MENU PRINCIPAL    ####################################################

opcio = '0'

while opcio != '':
    gameTitle()
    txt = ("\n" + " " * 60 + "1) Add/Remove/Show Players".ljust(60) + "\n" + " " * 60 + \
         "2) Settings".ljust(60) + "\n" + " " * 60 + \
         "3) Play Game".ljust(60) + "\n" + " " * 60 + \
         "4) Ranking".ljust(60) + "\n" + " " * 60 + \
         "5) Reports".ljust(60) + "\n" + " " * 60 + \
         "6) Exit".ljust(60))
    opt = "\n" + " " * 60 + "Choose Your Option: " + "\n" + " " * 60
    lista = ["1", "2", "3", "4", "5","6"]
    exc = []
    opc = getOpt(txt, opt, lista, exc)


    if opc == '1':       ### MENU ADD/REMOVE/SHOW ###

        menu_01()
    elif opc == '2':     ###### MENU SETTINGS #######
        menu_02()
    elif opc == '3':     ###### MENU PLAY ###########
        menu_03()
    elif opc == '4':     ###### MENU RANKING #######
        menu_04()
    elif opc == '5':     ###### MENU REPORTS #######
        menu_05()
    elif opc == '6':
        break
    elif opc != '':
        input("\n" + " " * 60 + "Invalid Option " + "\n" + " " * 60)