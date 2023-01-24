import random
from funciones.diccionarios import *


import pymysql
conn=pymysql.connect(host="20.86.76.157",user="proyecto", password="P@ssw0rd12345",database="sieteymedioDB")
cur = conn.cursor()
players = {
    "11115555A": {"name": "Arnau", "human": True, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 0, "cards": [], "roundPoints": 0},
    "22225555A": {"name": "Alex", "human": True, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 0, "cards": [], "roundPoints": 0},
    "22444555A": {"name": "Yahved", "human": True, "bank": False, "initialCard": "", "priority": 0
        , "type": 40, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
}

player_game = {'cardgame_id':{'id_jugador':{'initial_card_id':"", 'starting_points': "", 'ending_points':"",}}}

cardgame = {'cardgame_id': "", 'players': "Numero de jugadores",
'start_hour':"Hora de inicio de artida ( datetime)", 'rounds': "Número de rondas", 'end_hour': "hora final de partida ( datetime)" }

context_games = {'NumJugadores': 0}

player_game_round = {'round':{'id_jugaador':{'is_bank':"0 ó 1"",'bet_points': "",'starting_round_points':"",'cards_value':"",'endind_round_points':"""}}}

menu01 = "\n" + " " * 60 + "1) New Human Player".ljust(60) + "\n" + " " * 60 + \
         "2) New Boot".ljust(60) + "\n" + " " * 60 + \
         "3) Show/Remove Players".ljust(60) + "\n" + " " * 60 + \
         "4) Go Back".ljust(60)
menu02 = "\n" + " " * 60 + "1) Set Game Players".ljust(60) + "\n" + " " * 60+ \
         "2) Set Card's Deck (Default Spanish Deck)".ljust(60) + "\n" + " " * 60 + \
         "3) Set Max Rounds (Default 5 Rounds)".ljust(60) + "\n" + " " * 60 + \
         "4) Go Back".ljust(60)

menu03 = "\n" + " " * 63 + "1)View Stats".ljust(60) + "\n" + " " * 63 + \
         "2)View Game Stats".ljust(60) + "\n" + " " * 63 + \
         "3)Set Bet".ljust(60) + "\n" + " " * 63 + \
         "4)Order Card".ljust(60) + "\n" + " " * 63 + \
         "5)Automatic Play".ljust(60) + "\n" + " " * 63 + \
          "6)Stand"
menu04 = "\n" + " " * 63 + "1) Players With More Earnings".ljust(60) + "\n" + " " * 63 + \
         "2) Players With More Games Played".ljust(60) + "\n" + " " * 63 + \
         "3) Players With More Minutes Played".ljust(6) + "\n" + " " * 63 + \
          "4) Go Back"
menu05 = "\n" + " " * 60 + \
         "1) Initial card more repeated by each user,only users who have played a minimum of 3 games".ljust(60) + \
         "\n" + " " * 60+ \
         "2) Player who makes the highest bet per game, find the round with the highest bet".ljust(60) + \
         "\n" + " " * 60 + "3) Player who makes the lowest bet per game".ljust(60) + "\n" + " " * 60 + \
         "4) Percentage of rounds won per player in each game(%), as well as their average bet for the " \
         "game".ljust(60) + "\n" + " " * 60 + "5) List of games won by Bots".ljust(60) + "\n" + " " * 60 + \
         "6) Rounds won by the bank in each game".ljust(60) + "\n" + " " * 60 + \
         "7) Number of users have been the bank in each game".ljust(60) + "\n" + " " * 60 + \
         "8) Average bet per game".ljust(60) + "\n" + " " * 60 + \
         "9) Average bet of the first round of each game".ljust(60) + "\n" + " " * 60 + \
         "10) Average bet of the last round of each game".ljust(60) + "\n" + " " * 60 + \
         "11) Go Back"

def getOpt(textOpts,inputOptText,rangeList,exceptions):
 while True:
     print(textOpts)                 ### CON ESTA FUNCION LE PASAMOS UN TEXTO Y NOS PEDIRA QUE INTRODUZCAMOS UNA OPCIÓN QUE SI ESTA NO ESTA EN EL
                                      ##      RANGO QUE HEMOS DEFINIDO NOS DIRA QUE LA OPCIÓN ES INCORRECTA Y NOS MOSTRARÁ DE NUEVO EL TEXTO ##
     opc = input(inputOptText)
     if opc not in rangeList and opc not in exceptions:
         print("\n" + " " * 60 + "Invalid Option " + "\n" + " " * 60)
         input("\n" + " " * 60 + "Press enter to continue " + "\n" + " " * 60)
     else:
        return opc


def fill_player_game(player_game, gameID, *fields):
    #Asignar valores a las claves del diccionario
    player_game["game_id"] = gameID
    for field in fields:
        key, value = field.split(":")
        player_game[key.strip()] = value.strip()


def fill_player_game_round(player_game_round, round, *fields):
    player_game_round[round] = {}
    for i in range(0, len(fields), 6):
        id_player_1 = fields[i]
        is_bank = fields[i + 1]
        bet_points = fields[i + 2]
        starting_round_points = fields[i + 3]
        cards_value = fields[i + 4]
        endind_round_points = fields[i + 5]

        player_game_round[round][id_player_1] = {
            "is_bank": is_bank,
            "bet_points": bet_points,
            "starting_round_points": starting_round_points,
            "cards_value": cards_value,
            "endind_round_points": endind_round_points
        }
# def insertBBDD_player_game(player_game, cardgame_id):
#     #cur = conn.cursor()
#
#     # Insertar datos en la tabla player_game
#     sql = f"INSERT INTO player_game (cardgame_id, id_jugador, initial_card_id, starting_points, ending_points) VALUES (?,?,?,?)"
#
#     #cur.execute(sql)
#     #conn.commit()
#
# def insertBBDDCardgame(cardgame):
#     #cur = conn.cursor()
#
#     # Insertar datos en la tabla player_game
#     #sql = f"INSERT INTO cardgame (cardgame_id, players, rounds, start_hour, end_hour) VALUES (?,?,?,?)"
#         # (cardgame["cardgame_id"], 'players', 'rounds', ' start_hour', 'end_hour')
#     print("hola")
#     #cur.execute(sql)
#     #conn.commit()




def setGamePriority(mazo, contextGame=None):
    # Mezclar las cartas del mazo
    random.shuffle(mazo)
    # Repartir una carta a cada jugador
    cartas_repartidas = {}
    for jugador in contextGame["game"]:
        carta = mazo.pop()
        cartas_repartidas[jugador] = carta
        # Ordenar la lista de jugadores según la carta recibida
        contextGame["game"] = sorted(contextGame["game"], key=lambda x: cartas_repartidas[x])
    # Establecer las prioridades
    for i, jugador in enumerate(contextGame["game"]):
        contextGame["game"][i]["priority"] = i+1
    return contextGame["game"]


def resetPoints(contextGame=None):
    for jugador in contextGame["game"]:
     jugador["points"] = 20
    return contextGame["game"]


def Check2Players(players):
    player_with_points = 0
    for player in players:
        if player['points'] > 0:
            player_with_points += 1
    if player_with_points >= 2:
        return True
    else:
        return False


def maxRounds():
    rounds_ok = False
    while not rounds_ok:
        try:
            rounds = input("\n\n" + " " * 50 + "Select the max of rounds for the next game (5-30):\n" + " " * 50 + "Option --> ")
            if not rounds.isdigit():
                raise TypeError
            rounds = int(rounds)
            if rounds < 5 or rounds > 30:
                raise ValueError
            else:
                rounds_ok = True
                return rounds
        except ValueError:
            print("\n" + " " * 50 + "That's not a valid number")
            input(" " * 50 + "Press any key to continue...")
        except TypeError:
            print('\n' + " " * 50 + "That's not a number")
            input(" " * 50 + "Press any key to continue...")



def gameTitle():
    print("""     ********************************************************************************************************************************************
                                         _____                         ___              __   __  __      ______
                                        / ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/
                                        \__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /_  
                                       ___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/ 
                                      /____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/  
                             
    ********************************************************************************************************************************************""")


def gameover():
    print("*" * 120)
    print(" #####     ###    ##   ##  ######             #####   ###  ##  ####     ######")
    print("###       #####   ### ###  ##                ###  ##  ###  ##  ##       ###  ##")
    print("### ##    ## ##   #######  #####             ###  ##  ###  ##  #####    ###  ##")
    print("###  ##  ##   ##  #######  ##                ###  ##  ###  ##  ##       #######")
    print("###  ##  ##   ##  #######  ##                ###  ##  ###  ##  ##       ######")
    print("#######  ## ####  ###  ##  #######           #######   #####   #######  ### ###")
    print("#######  ## ####  ###  ##  #######           #######   #####   #######  ### ###")
    print(" #####   ## ####  ###  ##  #######            #####     ###    #######  ### ###")
    print("*" * 120)




def new_Nif():
    new = "yes"
    global letra

    try:
        nif = input("\n" + " " * 60 + "Enter Your Nif : " + "\n" + " " * 60)
        letra = nif[-1]
        validar_letra_nif(nif[:-1])     ### VALIDAMOS QUE LA LETRA SEA CORRECTA CON ESTA FUNCION ##
        while nif[-1] in num:
            print("")
            new_Nif()
        return nif
    except ValueError:    ### SIEMPRE QUE EL NIF NO TENGA  8 NUMEROS Y UNA LETRA MOSTARA EL ERROR DEL TIPO 'VALUE ERROR' ##
        print("\n" + " " * 60 + "The NIF must have 8 digits and a letter " + "\n" + " " * 60)
    new_Nif()
num = '0123456789 '

def validar_letra_nif(nif):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    valor = int(nif) % 23
    if letra.upper() == letras[valor]:
        pass
    else:
        print("Letra incorrecta")

def risk():
    txt = ("\n" + " " * 60 + "Select your profile:".ljust(60) + "\n" + " " * 60 + \
           "1) Cautious".ljust(60) + "\n" + " " * 60 + \
           "2) Moderated".ljust(60) + "\n" + " " * 60 + \
           "3) Bold".ljust(60) + "\n" + " " * 60)

    opt = "\n" + " " * 60 + "Choose Your Option: " + "\n" + " " * 60
    lista = ["1", "2", "3"]
    exc = []
    opc = getOpt(txt, opt, lista, exc)
    if opc == "1":
        return 50
    if opc == "2":
        return 40
    if opc == "3":
        return 30



def newName():
    nombre_ok = False
    while not nombre_ok:
        try:
            nombre = input("\n" + " " * 60 + "Insert Name : " + "\n" + " " * 60)
            if nombre.isspace() or nombre == "":
                raise TypeError("\n" + " " * 60 + "Incorrect  " + "\n" + " " * 60)
            else:
                return nombre

        except TypeError:
            print("Space-only or empty names are not allowed. Type Name Again.")



def createPlayer():
    nif = new_Nif()
    name = newName()
    riesgo = risk()


    sql = f"INSERT INTO jugadores VALUES ('{nif}','{name}',{1},{riesgo})"
    cur.execute(sql)
    conn.commit()
    players[nif] = {"name": name, "human": 1, "bank": False, "initialCard": "", "priority": 0
        , "type": riesgo, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
    input("\n" + " " * 60 + "Jugador creado correctamente\n" + "\n" + " " * 60 + "Pulsa enter para continuar" + "\n" + " " * 60)


def createPlayerBot():
    nif = newRandomDNI()
    print(f"\n" + " " * 60 + "NIF:"+ nif + "\n" + " " * 60 )
    name = newName()
    riesgo = risk()


    query = f"INSERT INTO jugadores VALUES ('{nif}','{name}',{0},{riesgo})"
    cur.execute(query)
    conn.commit()
    players[nif] = {"name": name, "human": 0, "bank": False, "initialCard": "", "priority": 0
        , "type": riesgo, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
    print("\n" + " " * 60 +"Player successfully created" + "\n" + " " * 60)
    input("\n" + " " * 60 +"Press any key to continue" + "\n" + " " * 60)


def TypeRisk(riesgo):
    if riesgo == 30:
        return "Prudente"
    elif riesgo == 40:
        return "Normal"
    elif riesgo == 50:
        return "Atrevido"
    else:
        return str(riesgo)


def ShowPlayers(PlayersList = []):
    HumanCur = conn.cursor()
    BotCur = conn.cursor()

    cadena = '\n           ' + 'Select Players'.center(140, '*') + '\n' + '\n           ' + 'Boot Player'.center(69, ' ') + '|' + 'Humans Player'.center(
        69, ' ') + '\n' + '\n           ' + '-' * 140 +  '\n            ' + "  ID".ljust(20) + "Name".ljust(25) + "Type Risk".ljust(24) + "|".ljust(
        1) + "ID".ljust(20) + "Name".ljust(25) + "Type Risk".ljust(25) + "\n" + '           ' +"*" * 140
    print(cadena)
    sqlBot = f"select * from jugadores where human = 0"

    sqlHuman = f"select * from jugadores where human = 1"

    HumanCur.execute(sqlHuman)
    HumanList = []
    BotList = []

    human = HumanCur.execute(sqlHuman)
    bot = BotCur.execute(sqlBot)

    for i in range(int(human)):
        h = HumanCur.fetchone()
        HumanList.append(h)
    for i in range(int(bot)):
        b = BotCur.fetchone()
        BotList.append(b)



    while True:
        string = ''

        if len(BotList) > 0:
            while True:
                if BotList[0][0] not in PlayersList :
                    string += '            ' + BotList[0][0].ljust(19) + " " + BotList[0][1].ljust(24) + " " + TypeRisk(BotList[0][3]).ljust(
                        24) + "|".ljust(1)
                    break
                else:
                    try:
                        if len(BotList) > 1:
                            BotList = BotList[1:]
                        else:
                            raise
                    except:
                        string += "".ljust(69) + "|".ljust(1)
                        break
        if len(HumanList) > 0:
            while True:
                if HumanList[0][0] not in PlayersList :
                    string += ' ' +HumanList[0][0].ljust(19) + " " + HumanList[0][1].ljust(24) + " " + TypeRisk(HumanList[0][3]).ljust(
                        25)
                    break
                else:
                        try:
                            if len(HumanList) > 1:
                                HumanList = HumanList[1:]
                            else:
                                raise
                        except:
                            break

        BotList, HumanList = BotList[1:], HumanList[1:]

        print(string)
        if len(HumanList) == 0 and len(BotList) == 0:
            break
    print('           ' +"*" * 140)



def DniExist(dni):
    query = f"select * from jugadores  where id_jugador = '{dni}'"
    cur.execute(query)
    if cur.fetchall():
        return False
    else:
        return True
def PlayersRemove():
    while True:
        ShowPlayers()
        print("-ID to remove player / -1 Go Back".center(160))
        while True:
            option = input(" " * 64 + "Option -> ")
            if option == "":
                print("   " * 60 + "Put a valid option")
            else:
                break


        if option[0] == "-" and not DniExist(option[1:]):
            sql = f"delete from jugadores where id_jugador = '{option[1:]}'"
            cur.execute(sql)
            conn.commit()
            Clear()
        elif option == "-1":

            Clear()
            gameTitle()
            break
        else:
            input(" " * 64 + "Put a valid option \n Enter to continue...")


def menu_01():    #### MENU ADD PLAYER.... ####
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            Clear()
            print(menu01)
            opc = input("\n" + " " * 60 + "Option: " + "\n" + " " * 60 )
            if not opc.isdigit():
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60 )
            elif int(opc) < 1 or int(opc) > 4:
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            print("\n" + " " * 60 + "**** New Human Player **** " + "\n" + " " * 60 )
            # nif = new_Nif()
            # name = crear_nombre()
            createPlayer()

            #InsertUser(nif,name,type)
            # players[nif] = {"name": name, "human": True, "bank": False, "initialCard": "", "priority": 0
            #     , "type": type, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
            #print(players)
            print("Player saved!")
        elif opc == 2:
            print("\n" + " " * 60 + "**** Boot **** " + "\n" + " " * 60)
            createPlayerBot()
        elif opc == 3:
            print("\n" + " " * 60 + "**** Show/Remove players ****" + "\n" + " " * 60)

            PlayersRemove()

        elif opc == 4:
            dejar_este_nivel = True
            Clear()




def newRandomDNI():
    # Generate random 8-digit number
    dni_number = str(random.randint(10000000, 99999999))

    # Calculate letter for DNI
    letter_list = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni_letter = letter_list[int(dni_number) % 23]

    return dni_number + dni_letter


deck = DeckEs
def setCardsDeck():

    txt = ("\n" + " " * 60 + "1)Spanish Deck".ljust(60) + "\n" + " " * 60 + \
           "2)Poker Deck".ljust(60) + "\n" + " " * 60 )
    opt = "\n" + " " * 60 + "Choose Your Option: " + "\n" + " " * 60
    lista = ["1", "2", "3", "4", "5", "6"]
    exc = []
    opc = getOpt(txt, opt, lista, exc)
    if opc == 1:
        deck = DeckEs
    if opc == 2:
        deck = DeckPok
    else:
        try:
            return context_games["deck"]
        except:
            return DeckEs
def Clear():
    print("\n" * 60)
def ShowDic(players_game):
    sql = f"select * from jugadores"
    cur.execute(sql)
    players = cur.fetchall()
    dict_players = {}
    for i in players_game:
        for x in players:
            if i == x[0]:
                if x[3] == 1:
                    dict_players[i] = {"name": x[1], "human": 1, "priority": 0, "type": x[2], "bank": False,
                                       "bet": 0, "points": 0, "cards": [], "initialCard": "", "roundPoints": 0}
                if x[3] == 0:
                    dict_players[i] = {"name": x[1], "human": 0, "priority": 0, "type": x[2], "bank": False,
                                       "bet": 0, "points": 0, "cards": [], "initialCard": "", "roundPoints": 0}
                #print(dict_players)
    return dict_players

def PlayersGame(players_game = []):
    sql = f"select * from jugadores"
    cur.execute(sql)
    players = cur.fetchall()
    jugadores = []
    for i in players:
        jugadores.append(i)
    #cadena = ' Jugadores Actuales en la Partida '.center(70, '*').center(140, ' ')
    #print(pjs)
    #print(cadena)

    if len(players_game) == 0:
        print("\n" + " " * 60 + "No Players Available " + "\n" + " " * 60 +"Press enterer to continue " + "\n" + " " * 60)

    else:
        sql = f"select * from jugadores"
        cur.execute(sql)
        players = cur.fetchall()

        jugadores = []
        for i in players:
            jugadores.append(i)
        cadena = "\n" + " " * 60 + "Id for player added " + "\n" + " " * 60 + str(players_game[0])

        for i in players_game:
            for j in jugadores:
                if j[0] == i:
                    if j[3] == 1:
                        cadena = (j[0].ljust(16) + " " + j[1].ljust(22) + " " + 'Humano'.ljust(16) + TypeRisk(
                            j[2]).ljust(23)).center(150, ' ')
                    if j[3] == 0:
                        cadena = (j[0].ljust(16) + " " + j[1].ljust(22) + " " + 'Boot'.ljust(16) + TypeRisk(
                            j[2]).ljust(23)).center(150, ' ')
                    print(cadena)
    input()

game = []

def setPlayersGame():
    Clear()
    players_game = []
    PlayersGame(players_game)
    opc = True
    while opc:
        ShowPlayers(PlayersList=players_game)

        while True:

            option = input("".ljust(36) + "Id to add player / -Id to remove player / ls to show players, -1 Go Back. Option ->")
            if option[0] == '-' and option[1:] in players_game:

                players_game.remove(option[1:])
                break
            if len(players_game) == 6:

                print("The maximum is 6 players")
                break
            elif not DniExist(option):
                if not option in players_game:
                    players_game.append(option)

                    print("\n" + " " * 60 + "Player saved correctly " + "\n" + " " * 60 )
                else:
                    input("\n" + " " * 60 + "ID incorrect\n Press any key to continue.. " + "\n" + " " * 60)
                break

            elif option == '-1':

                #player_in_game(players_in_game=players_in_game)
                opc = False
                Clear()
                break
            elif option == "ls":
                #print(players_in_game)
                PlayersGame(players_game)
            else:
                input("\n" + " " * 60 + "Invalid Id  " + "\n" + " " * 60 )

        if not opc:
            break
        PlayersGame(players_game=players_game)
    return ShowDic(players_game)



def menu_02():    #### MENU SETTINGS ####
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            Clear()
            print(menu02)
            opc = input("\n" + " " * 60 + "Option: " + "\n" + " " * 60 )
            if not opc.isdigit():
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            elif int(opc) < 1 or int(opc) > 4:
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            print("\n" + " " * 60 + "*** Set Players Game *** " + "\n" + " " * 60)

            players = setPlayersGame()
            context_games["NumJugadores"] = len(players)
            context_games["players"] = players
            #set_game_players()


        if opc == 2:
            print("\n" + " " * 60 + "*** Set Card's Deck (Default Spanish Deck) *** " + "\n" + " " * 60)

            cartas = setCardsDeck()
            context_games["deck"] = cartas
            input(" " * 60 + "Press enter to continue...")
            #limpiarTerminal()
        if opc == 3:
            print("\n" + " " * 60 + "*** Rounds *** " + "\n" + " " * 60)
            rounds = maxRounds()
            context_games["NumRondas"] = rounds
        if opc == 4:
            Clear()
            dejar_este_nivel = True



def menu_05():    #### MENU REPORTS ####
    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu05)
            opc = input("\n" + " " * 60 + "Option: " + "\n" + " " * 60 )
            if not opc.isdigit():
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            elif int(opc) < 1 or int(opc) > 11:
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            print("1")
        elif opc == 2:
            print("\n" + " " * 60 + "select cardgame_id, id_jugador, bet_points from player_game_round where bet_points = (select max(bet_points) from player_game_round) " + "\n" + " " * 60)

        elif opc == 3:
            print("\n" + " " * 60 + "select cardgame_id, id_jugador, bet_points from player_game_round where bet_points = (select min(bet_points) from player_game_round) " + "\n" + " " * 60)
        elif opc == 4:
            print("\n" + " " * 60 + "=== Query 4 === " + "\n" + " " * 60)
        elif opc == 5:
            print("\n" + " " * 60 + "=== Query 5 === " + "\n" + " " * 60)
        elif opc == 6:
            print("\n" + " " * 60 + "=== Query 6 === " + "\n" + " " * 60)
        elif opc == 7:
            print("\n" + " " * 60 + "select count(is_bank), pgr.cardgame_id from player_game_round pgr inner join player_game pg on pg.cardgame_id = pgr.cardgame_id where is_bank=1 group by cardgame_id" + "\n" + " " * 60)
        elif opc == 8:
            print("\n" + " " * 60 + "select avg(pgr.bet_points), pg.cardgame_id from player_game_round pgr inner join player_game pg on pg.cardgame_id = pgr.cardgame_id group by cardgame_id " + "\n" + " " * 60)

        elif opc == 9:
            print("\n" + " " * 60 + "=== Query 9 === " + "\n" + " " * 60)
        elif opc == 10:
            print("\n" + " " * 60 + "=== Query 10 === " + "\n" + " " * 60)
        elif opc == 11:
            dejar_este_nivel = True
            Clear()


def menu_04():    #### MENU RANKING  ####
    Clear()

    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu04)
            opc = input("\n" + " " * 60 + "    Option: " + "\n" + " " * 60 )
            if not opc.isdigit():
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            elif int(opc) < 1 or int(opc) > 6:
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            print("\n" + " " * 60 + "**** Players With More Earnings **** " + "\n" + " " * 60 )

        elif opc == 2:
            print("\n" + " " * 60 + "**** Players With More Games Played **** " + "\n" + " " * 60)
        elif opc == 3:
            print("\n" + " " * 60 + "**** Players With More Minutes Played **** " + "\n" + " " * 60)


        elif opc == 4:
            dejar_este_nivel = True
            Clear()


def menu_03():    #### MENU PLAY  ####
    Clear()

    dejar_este_nivel = False
    while not dejar_este_nivel:
        opcion_ok = False
        opc = ''
        while not opcion_ok:
            print(menu03)
            opc = input("\n" + " " * 60 + "  Option: " + "\n" + " " * 60 )
            if not opc.isdigit():
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            elif int(opc) < 1 or int(opc) > 6:
                print("\n" + " " * 60 + "=== Incorrect Option === " + "\n" + " " * 60)
            else:
                opcion_ok = True
                opc = int(opc)
        if opc == 1:
            print("\n" + " " * 60 + "**** View Stats **** " + "\n" + " " * 60 )

        elif opc == 2:
            print("\n" + " " * 60 + "**** View Game Stats **** " + "\n" + " " * 60)
        elif opc == 3:
            print("\n" + " " * 60 + "**** Set Bet **** " + "\n" + " " * 60)
        elif opc == 4:
            print("\n" + " " * 60 + "**** Order Card **** " + "\n" + " " * 60)
        elif opc == 5:
            print("\n" + " " * 60 + "**** Automatic Play **** " + "\n" + " " * 60)


        elif opc == 6:
            dejar_este_nivel = True
            Clear()

