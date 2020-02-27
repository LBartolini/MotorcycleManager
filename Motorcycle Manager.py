import time as t
import random as r
import os.path
##############################
'''
Patch - 1.3

Modifiche :
-Aggiunto Laboratorio
-
-
-
'''
##############################

def decrescente(numeri):
    m = 0
    n = 0
    for i in range(len(numeri)):
        x = 0
        while x <= len(numeri):
            y = x+1
            if y != len(numeri):
                if numeri[x] < numeri[y]:
                    m = numeri[x]
                    n = numeri[y]
                    numeri[x] = n
                    numeri[y] = m
                    x += 1
                else:
                    x += 1
            else:
                break
    return numeri

def crescente(numeri):
    m = 0
    n = 0
    for i in range(len(numeri)):
        x = 0
        while x <= len(numeri):
            y = x+1
            if y != len(numeri):
                if numeri[x] > numeri[y]:
                    m = numeri[x]
                    n = numeri[y]
                    numeri[x] = n
                    numeri[y] = m
                    x += 1
                else:
                    x += 1
            else:
                break
    return numeri

##############################

squadre = {
           'Yamaha' : [8, 9, 12, 12],
           'Honda' : [12, 10, 11, 8],
           'Ducati': [9, 9, 11, 11],  #c, m, g, a
           'Suzuki' : [8, 7, 6, 10],         
           'KTM' : [8, 9, 11, 8],
           'Aprilia' : [10, 6, 5, 8],
           'Piaggio' : [9, 4, 5, 8],
           'BMW' : [10, 8, 12, 8], #32
           }

piloti = {
           'Yamaha' : ['Rossi', 'Vinales'], #16
           'Honda' : ['Marquez', 'Pedrosa'],
           'Ducati': ['Dovizioso', 'Jorge L.'],
           'Suzuki' : ['Iannone', 'Rins'],
           'KTM' : ['Smith', 'Espargaro'],
           'Aprilia' : ['Bautista', 'Redding'],
           'Piaggio' : ['Morbidelli', 'Zarco'],
           'BMW' : ['Petrucci', 'Rabat'],
            }

##############################

assetto_campionato = ['Yamaha', 'Honda', 'Ducati', 'Suzuki', 'KTM', 'Aprilia', 'Piaggio', 'BMW']
assetto_tutorial = ['Suzuki', 'KTM', 'Piaggio', 'Aprilia']

##############################

circuiti = {
            'Mugello' : [1, 2, 0.5],  #ciclistica, motore, aerodinamica
            'Misano' : [1, -1, 3],
            'FranciaCorta' : [1, 2, 0.5],
            'Le Mans' : [0.25, 3, 3],
            'Catalunya' : [3, 1, 1],
            'Quatar' : [1, 1, 1],
            'Twin Ring Motegi' : [-1, 2, 2],
            'Termas de Rio Hondo' : [1.25, 4, -2],
            'Sachsenring' : [3, 2, 2],
            'Silverstone' : [2, -1.25, 0.75],
            'Sepang' : [-1, 4, 1],
            'Phillip Island' : [1.25, -1, 4],
            }

t_circuito = {
            'Mugello' : ['Al Mugello il Motore conta molto mentre l\'Aerodinamica non è così importante', 'Conta molto la bravura del Pilota in curva e in rettilineo!'],
            'Misano' : ['L\'Aerodinamica lo fa da padrone mentre il Motore non è il primo dei problemi', 'Il team dovrà fare un ottimo lavoro per far vincere il Pilota!'],
            'FranciaCorta' : ['A FranciaCorta il Motore conta molto mentre l\'Aerodinamica non è così importante', 'Conta molto la bravura del Pilota in curva e in rettilineo!'],
            'Le Mans' : ['Motore e Aerodinamica sono il fulcro della gara', 'Il team che eseguirà un buon assetto riuscirà a portare a casa la vittoria!'],
            'Catalunya' : ['In Spagna la Ciclistica ha un importanza vitale', 'Al contrario Motore e Aerodinamica passano in secondo piano!'],
            'Quatar' : ['La migliore pista per far sfoggiare il talento del Pilota', 'Se riuscirà in una buona partenza il gioco è fatto!'],
            'Twin Ring Motegi' : ['Una tappa piena di curve', 'Il Pilota, insieme alla Ciclistica, devono lavorare molto!'],
            'Termas de Rio Hondo' : ['Una pista spettacolare dove si raggiungono velocità altissime', 'L\'Aerodinamica non è particolarmente sollecitata!'],
            'Sachsenring' : ['Una pista in cui le moto possono correre al meglio', 'Nessun punto debole qui ci si gioca il Mondiale!'],
            'Silverstone' : ['Tappa estremamente tecnica', 'La Ciclistica deve aiutare il pilota in tutte le fasi di Gara!'],
            'Sepang' : ['Una pista spettacolare dove si raggiungono velocità altissime', 'La Ciclistica non è particolarmente sollecitata!'],
            'Phillip Island' : ['Pista in cui i cambi di direzione sforzano il Pilota', 'Una buona Ciclistica lo aiuterà nel guidare la Moto!'],
            }

classifica_mondiale = {
           'Yamaha' : [0, 0], #37
           'Honda' : [0, 0],
           'Ducati': [0, 0],
           'Suzuki' : [0, 0],
           'KTM' : [0, 0],
           'Aprilia' : [0, 0],
           'Piaggio' : [0, 0],
           'BMW' : [0, 0],
                        }

##############################

ts = 0             #Team scelto
ciclistica = 0     #1-10 Default
motore = 0         #1-10 Default
gomme = 0          #1-10 Default
aerodinamica = 0   #1-10 Default
fm = 0             #feeling con la moto
mondiale = 1
num_miglioramenti = 0
soldi = 150 #milioni
nome = ''
n_gara = 1
all_pa = False
all_pi = False
energia = False
tutorial = False
assetto = [1, 1, 1]  # 1-Manubrio>0=chiuso, 1=normale, 2=aperto, 2-Sella>0=Bassa, 1=Media, 2=Alta, 3-Sospensioni>0=Dure, 1=Medie, 2=Morbide
inge = [0, 0, 0]
diff = 0
t_guasto = ''
c_guasto = False
sviluppatore = False
p_meteo = ['Piovoso', 'Soleggiato', 'Nuvoloso', 'Ventoso']
versione = '1.3'
svil_versione = '13'
mondiali_vinti = 0
caduta = False
cost_caduta = False
t_cost_caduta = '\nLa Moto non è al pieno delle sue condizioni a causa di una caduta. provvedi a ripararla al più presto.'
sponsor = 'No-Sponsor'
n_sponsor = 0
l_sponsor ={
    'PxF-Esport' : [20, 3],
    'PxF-Music' : [17, 4],
    'Zamsung' : [15, 6],
    'Adisas' : [10, 7],
    'pinApple' : [8, 8],
    'Minisoft' : [6, 10],
    'Niche' : [4, 13],
    'WannemaWay' : [2, 16]
    }
lf_sponsor = ['False','False','False','False','False','False','False','False']
ex_sponsor = ''
costo_1 = 10
c_1 = 2
costo_2 = 20
c_2 = 4
costo_3 = 30
c_3 = 6

##############################

def invio():
    input('\nPremi INVIO per continuare.')

def spazio():
    for d in range(40):
            print('\n\n\n\n\n\n')

def maiuscola(n):
    nome = ''
    for i, l in enumerate(n):
        if i == 0:
            nome += l.upper()
        else:
            nome += l
    return nome

def full_maiuscola(n):
    nome = ''
    for i, l in enumerate(n):
        nome += l.upper()
    return nome

def modalità_sviluppatore():
    global sviluppatore, motore, aerodinamica, gomme, ciclistica, soldi, diff, fm, nome, mondiale, sponsor, n_sponsor
    while True:
        x = input('\nPassword: (Ricorda, non potrai salvare la partita se entri nella modalità Sviluppatore!)\nPer uscire scrivi : \'esc\'\n\n>>>')
        if x == 'mmms'+svil_versione:
            sviluppatore = True
            break
        elif x.lower() == 'esc':
            break
        else:
            print('\nPassword Errata!')
            input('\nPremi INVIO per continuare.')
            continue
    while sviluppatore:
        print('\nLa modalità sviluppatore, se usata male, può causare crash del gioco.')
        print('\nN1 - Motore')
        print('N2 - Ciclistica')
        print('N3 - Aerodinamica')
        print('N4 - Gomme')
        print('N5 - Soldi')
        print('N6 - Fm')
        print('N7 - Nome')
        print('N8 - Mondiale')
        print('N9 - Difficoltà')
        print('N10 - Reset Sponsor')
        print('N11 - Esci')
        y = input('\n\n>>>')
        
        if y == '1' or y.lower() == 'n1':
            motore = int(input('\nMotore ->'))
            continue
        elif y == '2' or y.lower() == 'n2':
            ciclistica = int(input('\nCiclistica ->'))
            continue
        elif y == '3' or y.lower() == 'n3':
            aerodinamica = int(input('\nAerodinamica ->'))
            continue
        elif y == '4' or y.lower() == 'n4':
            gomme = int(input('\nGomme ->'))
            continue
        elif y == '5' or y.lower() == 'n5':
            soldi = int(input('\nSoldi ->'))
            continue
        elif y == '6' or y.lower() == 'n6':
            fm = int(input('\nFm ->'))
            continue
        elif y == '7' or y.lower() == 'n7':
            nome = maiuscola(input('\nNome ->'))
            piloti[ts][1] = nome
            continue
        elif y == '8' or y.lower() == 'n8':
            mondiale = int(input('\nMondiale ->'))
            continue
        elif y == '9' or y.lower() == 'n9':
            diff = int(input('\nDifficoltà(2=Difficile, 3=Media, 4=Facile) ->'))
            continue
        elif y == '10' or y.lower() == 'n10':
            reset_sponsor()
            continue
        elif y == '11' or y.lower() == 'n11':
            break
        else:
            print('\nCarattere non valido.')
            input('\nPremi INVIO per continuare.')
            continue
            

def salva():
    salvataggio = open('data.mm', 'w')
    salvataggio.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|' % (ts, ciclistica, motore, gomme, aerodinamica, fm, mondiale, num_miglioramenti, soldi, nome, n_gara, all_pa, all_pi, energia, costo_1, c_1, costo_2, c_2, costo_3, c_3, classifica_mondiale['Yamaha'][0], classifica_mondiale['Yamaha'][1], classifica_mondiale['Honda'][0], classifica_mondiale['Honda'][1], classifica_mondiale['Ducati'][0], classifica_mondiale['Ducati'][1], classifica_mondiale['Suzuki'][0], classifica_mondiale['Suzuki'][1], classifica_mondiale['KTM'][0], classifica_mondiale['KTM'][1], classifica_mondiale['Aprilia'][0], classifica_mondiale['Aprilia'][1], classifica_mondiale['Piaggio'][0], classifica_mondiale['Piaggio'][1], classifica_mondiale['BMW'][0], classifica_mondiale['BMW'][1], piloti['Yamaha'][0], piloti['Yamaha'][1], piloti['Honda'][0], piloti['Honda'][1], piloti['Ducati'][0], piloti['Ducati'][1], piloti['Suzuki'][0], piloti['Suzuki'][1], piloti['KTM'][0], piloti['KTM'][1], piloti['Aprilia'][0], piloti['Aprilia'][1], piloti['Piaggio'][0], piloti['Piaggio'][1], piloti['BMW'][0], piloti['BMW'][1], squadre['Yamaha'][0], squadre['Yamaha'][1], squadre['Yamaha'][2], squadre['Yamaha'][3], squadre['Honda'][0], squadre['Honda'][1], squadre['Honda'][2], squadre['Honda'][3], squadre['Ducati'][0], squadre['Ducati'][1], squadre['Ducati'][2], squadre['Ducati'][3], squadre['Suzuki'][0], squadre['Suzuki'][1], squadre['Suzuki'][2], squadre['Suzuki'][3], squadre['KTM'][0], squadre['KTM'][1], squadre['KTM'][2], squadre['KTM'][3], squadre['Aprilia'][0], squadre['Aprilia'][1], squadre['Aprilia'][2], squadre['Aprilia'][3], squadre['Piaggio'][0], squadre['Piaggio'][1], squadre['Piaggio'][2], squadre['Piaggio'][3], squadre['BMW'][0], squadre['BMW'][1], squadre['BMW'][2], squadre['BMW'][3], diff, mondiali_vinti, n_sponsor, sponsor, lf_sponsor[0],lf_sponsor[1],lf_sponsor[2],lf_sponsor[3],lf_sponsor[4],lf_sponsor[5],lf_sponsor[6],lf_sponsor[7], caduta, cost_caduta, assetto[0], assetto[1], assetto[2], inge[0], inge[1], inge[2]))
    salvataggio.close()
def carica():
    global ts, ciclistica, motore, cost_caduta, caduta, gomme, aerodinamica, fm, mondiale, num_miglioramenti, soldi, nome, n_gara, all_pa, all_pi, energia, costo_1, c_1, costo_2, c_2, costo_3, c_3, piloti, classifica_mondiale, squadre, diff, mondiali_vinti, sponsor, n_sponsor, inge
    dati = []
    var = ''
    if os.path.exists('data.mm'):
        caricamento = open('data.mm', 'r')
        for l in caricamento.read():
            if l == '|':
                dati.append(var)
                var = ''
            else:
                var += l
        caricamento.close()
        for i, p in enumerate(dati):
            if i == 0:
                ts = p
            elif i == 1:
                ciclistica = int(p)
            elif i == 2:
                motore = int(p)
            elif i == 3:
                gomme = int(p)
            elif i == 4:
                aerodinamica = int(p)
            elif i == 5:
                fm = float(p)
            elif i == 6:
                mondiale = int(p)
            elif i == 7:
                num_miglioramenti = int(p)
            elif i == 8:
                soldi = int(p)
            elif i == 9:
                nome = p
            elif i == 10:
                n_gara = int(p)
            elif i == 11:
                all_pa = p
            elif i == 12:
                all_pi = p
            elif i == 13:
                energia = p
            elif i == 14:
                costo_1 = int(p)
            elif i == 15:
                c_1 = int(p)
            elif i == 16:
                costo_2 = int(p)
            elif i == 17:
                c_2 = int(p)
            elif i == 18:
                costo_3 = int(p)
            elif i == 19:
                c_3 = int(p)
            elif i == 20:
                classifica_mondiale['Yamaha'][0] = int(p)
            elif i == 21:
                classifica_mondiale['Yamaha'][1] = int(p)
            elif i == 22:
                classifica_mondiale['Honda'][0] = int(p)
            elif i == 23:
                classifica_mondiale['Honda'][1] = int(p)
            elif i == 24:
                classifica_mondiale['Ducati'][0] = int(p)
            elif i == 25:
                classifica_mondiale['Ducati'][1] = int(p)
            elif i == 26:
                classifica_mondiale['Suzuki'][0] = int(p)
            elif i == 27:
                classifica_mondiale['Suzuki'][1] = int(p)
            elif i == 28:
                classifica_mondiale['KTM'][0] = int(p)
            elif i == 29:
                classifica_mondiale['KTM'][1] = int(p)
            elif i == 30:
                classifica_mondiale['Aprilia'][0] = int(p)
            elif i == 31:
                classifica_mondiale['Aprilia'][1] = int(p)
            elif i == 32:
                classifica_mondiale['Piaggio'][0] = int(p)
            elif i == 33:
                classifica_mondiale['Piaggio'][1] = int(p)
            elif i == 34:
                classifica_mondiale['BMW'][0] = int(p)
            elif i == 35:
                classifica_mondiale['BMW'][1] = int(p)
            elif i == 36:
                piloti['Yamaha'][0] = p
            elif i == 37:
                piloti['Yamaha'][1] = p
            elif i == 38:
                piloti['Honda'][0] = p
            elif i == 39:
                piloti['Honda'][1] = p
            elif i == 40:
                piloti['Ducati'][0] = p
            elif i == 41:
                piloti['Ducati'][1] = p
            elif i == 42:
                piloti['Suzuki'][0] = p
            elif i == 43:
                piloti['Suzuki'][1] = p
            elif i == 44:
                piloti['KTM'][0] = p
            elif i == 45:
                piloti['KTM'][1] = p
            elif i == 46:
                piloti['Aprilia'][0] = p
            elif i == 47:
                piloti['Aprilia'][1] = p
            elif i == 48:
                piloti['Piaggio'][0] = p
            elif i == 49:
                piloti['Piaggio'][1] = p
            elif i == 50:
                piloti['BMW'][0] = p
            elif i == 51:
                piloti['BMW'][1] = p
            elif i == 52:
                squadre['Yamaha'][0] = int(p)
            elif i == 53:
                squadre['Yamaha'][1] = int(p)
            elif i == 54:
                squadre['Yamaha'][2] = int(p)
            elif i == 55:
                squadre['Yamaha'][3] = int(p)
            elif i == 56:
                squadre['Honda'][0] = int(p)
            elif i == 57:
                squadre['Honda'][1] = int(p)
            elif i == 58:
                squadre['Honda'][2] = int(p)
            elif i == 59:
                squadre['Honda'][3] = int(p)
            elif i == 60:
                squadre['Ducati'][0] = int(p)
            elif i == 61:
                squadre['Ducati'][1] = int(p)
            elif i == 62:
                squadre['Ducati'][2] = int(p)
            elif i == 63:
                squadre['Ducati'][3] = int(p)
            elif i == 64:
                squadre['Suzuki'][0] = int(p)
            elif i == 65:
                squadre['Suzuki'][1] = int(p)
            elif i == 66:
                squadre['Suzuki'][2] = int(p)
            elif i == 67:
                squadre['Suzuki'][3] = int(p)
            elif i == 68:
                squadre['KTM'][0] = int(p)
            elif i == 69:
                squadre['KTM'][1] = int(p)
            elif i == 70:
                squadre['KTM'][2] = int(p)
            elif i == 71:
                squadre['KTM'][3] = int(p)
            elif i == 72:
                squadre['Aprilia'][0] = int(p)
            elif i == 73:
                squadre['Aprilia'][1] = int(p)
            elif i == 74:
                squadre['Aprilia'][2] = int(p)
            elif i == 75:
                squadre['Aprilia'][3] = int(p)
            elif i == 76:
                squadre['Piaggio'][0] = int(p)
            elif i == 77:
                squadre['Piaggio'][1] = int(p)
            elif i == 78:
                squadre['Piaggio'][2] = int(p)
            elif i == 79:
                squadre['Piaggio'][3] = int(p)
            elif i == 80:
                squadre['BMW'][0] = int(p)
            elif i == 81:
                squadre['BMW'][1] = int(p)
            elif i == 82:
                squadre['BMW'][2] = int(p)
            elif i == 83:
                squadre['BMW'][3] = int(p)
            elif i == 84:
                diff = int(p)
            elif i == 85:
                mondiali_vinti = int(p)
            elif i == 86:
                n_sponsor = int(p)
            elif i == 87:
                sponsor = p
            elif i == 88:
                lf_sponsor[0] = p
            elif i == 89:
                lf_sponsor[1] = p
            elif i == 90:
                lf_sponsor[2] = p
            elif i == 91:
                lf_sponsor[3] = p
            elif i == 92:
                lf_sponsor[4] = p
            elif i == 93:
                lf_sponsor[5] = p
            elif i == 94:
                lf_sponsor[6] = p
            elif i == 95:
                lf_sponsor[7] = p
            elif i == 96:
                caduta = bool(p)
            elif i == 97:
                cost_caduta = bool(p)
            elif i == 98:
                assetto[0] = int(p)
            elif i == 99:
                assetto[1] = int(p)
            elif i == 100:
                assetto[2] = int(p)
            elif i == 101:
                inge[0] = int(p)
            elif i == 102:
                inge[1] = int(p)
            elif i == 103:
                inge[2] = int(p)
        return True
    else:
        print('\n\nNon è presente nessun salvataggio!')
        invio()
        return False

def cm(cl_md):
    co_classifica = 0
    cla_mond = []
    for i in cl_md:
        for c in cl_md[i]:
            cla_mond.append(c)
    cla_mond = decrescente(cla_mond)
    print('Classifica Mondiale : ')
    for j in range(20):
        for i, c in enumerate(cl_md):
            for co, s in enumerate(cl_md[c]):
                if co_classifica < 16:
                    if s == cla_mond[co_classifica]:
                        pl_mnd = piloti[c][co]
                        print('N%s - %s(%s) - Punti : %s' % (co_classifica+1, pl_mnd, c, s))
                        co_classifica += 1

def clm(cl_md):
    co_classifica = 0
    cla_mond = []

    for i in cl_md:
        for c in cl_md[i]:
            cla_mond.append(c)

    cla_mond = decrescente(cla_mond)
    for j in range(20):
        for i, c in enumerate(cl_md):
            for co, s in enumerate(cl_md[c]):
                if co_classifica < 16:
                    if s == cla_mond[co_classifica]:
                        pl_mnd = piloti[c][co]
                        co_classifica += 1
                        if pl_mnd == nome:
                            return co_classifica


def assetto_moto():
    global assetto
    t.sleep(0.5)  # 1-Manubrio>0=chiuso, 1=normale, 2=aperto, 2-Sella>0=Bassa, 1=Media, 2=Alta, 3-Sospensioni>0=Dure, 1=Medie, 2=Morbide
    man = ''
    sella = ''
    sosp = ''
    stile = ''
    print('\nScegli l\'Assetto della Moto in vista della Gara')
    print('\n$-- SELLA')
    print('\n1-Alta')
    print('2-Media')
    print('3-Bassa')
    while True:
        x = input('\n\n>>>')
        if x == '1':
            sella = 2
            break
        elif x == '2':
            sella = 1
            break
        elif x == '3':
            sella = 0
            break
        else:
            print('\nHai sbagliato carattere. Riprova!')
            invio()
            continue
    print('\n$-- MANUBRIO')
    print('\n1-Aperto')
    print('2-Normale')
    print('3-Chiuso')
    while True:
        x = input('\n\n>>>')
        if x == '1':
            man = 2
            break
        elif x == '2':
            man = 1
            break
        elif x == '3':
            man = 0
            break
        else:
            print('\nHai sbagliato carattere. Riprova!')
            invio()
            continue
    print('\n$-- SOSPENSIONI')
    print('\n1-Morbide')
    print('2-Medie')
    print('3-Dure')
    while True:
        x = input('\n\n>>>')
        if x == '1':
            sosp = 2
            break
        elif x == '2':
            sosp = 1
            break
        elif x == '3':
            sosp = 0
            break
        else:
            print('\nHai sbagliato carattere. Riprova!')
            invio()
            continue
    print('\n$-- STILE DI GUIDA')
    print('\n1-Aggressivo')
    print('2-Normale')
    print('3-Conservativo')
    while True:
        x = input('\n\n>>>')
        if x == '1':
            stile = 2
            break
        elif x == '2':
            stile = 1
            break
        elif x == '3':
            stile = 0
            break
        else:
            print('\nHai sbagliato carattere. Riprova!')
            invio()
            continue
    return man, sella, sosp, stile


def gara(circ, partecipanti):
    global fm, soldi
    global mondiale, mondiali_vinti
    global num_miglioramenti, all_pi, all_pa, energia, assetto
    global n_gara, n_sponsor, sponsor, l_sponsor, ex_sponsor
    global p_meteo
    global caduta, t_caduta, c_guasto, cost_caduta, t_cost_caduta
    
    temp_g = []
    ris = {
                'Yamaha' : [],
                'Honda' : [],
                'Ducati': [],
                'Suzuki' : [],
                'KTM' : [],
                'Aprilia' : [],
                'Piaggio' : [],
                'BMW' : [],
                }
    c_ris = {
                'Yamaha' : [],
                'Honda' : [],
                'Ducati': [],
                'Suzuki' : [],
                'KTM' : [],
                'Aprilia' : [],
                'Piaggio' : [],
                'BMW' : [],
                }
    ris_gara = []
    c_piloti = 0
    c_class = 1
    meteo = p_meteo[r.randint(0, 3)]
    t_caduta = '\n%s è caduto!\nSarà necessaria la riparazione della Moto.' % nome
    if cost_caduta:
        temp_caduta = 0.9
    else:
        temp_caduta = 1
    if not cost_caduta:
        c_evento = r.randint(0, 100)
    else:
        c_evento = 100
    print('\nStai per entrare in Pista...')
    t.sleep(1.5)
    print('\n\n\nCircuito : %s\nCondizioni meteo : %s\n' % (circ, meteo))
    for h in t_circuito[circ]:
        print(h)
    temp_manubrio, temp_sella, temp_sospensioni, temp_stile = assetto_moto()
    input('\n\nPremi INVIO per continuare.')    
    spazio()
    print('Gara in Corso...')
    t.sleep(2)
    print('\n\n\n\nGara finita!\n\n\n\n')
    for i, p in enumerate(partecipanti):
        if ts == p:
            for c, pi in enumerate(piloti[p]):
                if c == 0:
                    t_ciclistica = squadre[p][0] * circuiti[circ][0]
                    t_motore = squadre[p][1] * circuiti[circ][1]
                    t_aerodinamica = squadre[p][3] * circuiti[circ][2]
                    t_gomme = squadre[p][2]
                    if meteo == 'Nuvoloso':
                        t_ciclistica *= 0.9
                    elif meteo == 'Soleggiato':
                        t_motore *= 0.9
                    elif meteo == 'Piovoso':
                        t_gomme *= 0.95
                    elif meteo == 'Ventoso':
                        t_aerodinamica *= 0.9
                    s = ((t_ciclistica + t_motore + t_aerodinamica + r.randint(n_gara, 12)) * t_gomme) + r.randint(-15,
                                                                                                                   15)
                    if r.randint(0, 100) >= 20:
                        ris[p].append(max(0, int(s)))
                    else:
                        ris[p].append(int(s / 10))
                else:
                    tmp_ass = 1.0
                    tmp_bonus = 1.0
                    rischio_caduta = 20
                    t_ciclistica = (ciclistica * circuiti[circ][0]) * 0.75
                    t_motore = (motore * circuiti[circ][1]) * 0.75
                    t_aerodinamica = (aerodinamica * circuiti[circ][2]) * 0.75
                    if diff == 2 and mondiale <= 3:
                        t_gomme = (gomme * diff) / mondiale
                        t_fm = (fm * diff) / mondiale
                    elif diff == 2 and mondiale > 3:
                        t_gomme = gomme * 0.7
                        t_fm = fm * 0.65
                    elif diff == 3 and mondiale <= 4:
                        t_gomme = (gomme * diff) / mondiale
                        t_fm = (fm * diff) / mondiale
                    elif diff == 3 and mondiale > 4:
                        t_gomme = gomme * 0.75
                        t_fm = fm * 0.62
                    elif diff == 4 and mondiale <= 6:
                        t_gomme = (gomme * diff) / mondiale
                        t_fm = (fm * diff) / mondiale
                    elif diff == 4 and mondiale > 6:
                        t_gomme = gomme * 0.72
                        t_fm = fm * 0.6
                    if meteo == 'Nuvoloso':
                        t_ciclistica *= 0.9
                    elif meteo == 'Soleggiato':
                        t_motore *= 0.9
                    elif meteo == 'Piovoso':
                        t_gomme *= 0.95
                    elif meteo == 'Ventoso':
                        t_aerodinamica *= 0.9
                    if temp_manubrio == assetto[0]:
                        tmp_ass += 0.05
                    else:
                        tmp_ass -= 0.05
                    if temp_sella == assetto[1]:
                        tmp_ass += 0.05
                    else:
                        tmp_ass -= 0.05
                    if temp_sospensioni == assetto[2]:
                        tmp_ass += 0.05
                    else:
                        tmp_ass -= 0.05
                    if temp_stile == 2:
                        tmp_bonus += 0.1
                        rischio_caduta += 5
                    elif temp_stile == 0:
                        tmp_bonus -= 0.1
                        rischio_caduta -= 5
                    s = (((((t_ciclistica + t_motore + t_aerodinamica + r.randint(n_gara,
                                                                                12)) * t_gomme) + t_fm) * temp_caduta) * tmp_ass) * tmp_bonus
                    if c_evento >= 0 and c_evento <= 15:
                        ris[p].append(int(s / 10))
                        guasto()
                    elif c_evento > 15 and c_evento <= rischio_caduta:
                        ris[p].append((int(s / 10)))
                        caduta = True
                        cost_caduta = False
                    else:
                        ris[p].append(max(0, int(s)))
                c_piloti += 1
        else:
            for c, pi in enumerate(piloti[p]):
                t_ciclistica = squadre[p][0] * circuiti[circ][0]
                t_motore = squadre[p][1] * circuiti[circ][1]
                t_aerodinamica = squadre[p][3] * circuiti[circ][2]
                t_gomme = squadre[p][2]
                if meteo == 'Nuvoloso':
                    t_ciclistica *= 0.9
                elif meteo == 'Soleggiato':
                    t_motore *= 0.9
                elif meteo == 'Piovoso':
                    t_gomme *= 0.95
                elif meteo == 'Ventoso':
                    t_aerodinamica *= 0.9
                s = ((t_ciclistica + t_motore + t_aerodinamica + r.randint(n_gara, 12)) * t_gomme) + r.randint(-15, 15)
                if r.randint(0, 100) >= 20:
                    ris[p].append(max(0, int(s)))
                else:
                    ris[p].append(int(s / 10))
                c_piloti += 1
    for i, p in enumerate(partecipanti):
        for v in ris[p]:
            ris_gara.append(v)
            ris_gara.sort()
            temp_g.append(v)
            temp_g.sort()

    for i, p in enumerate(partecipanti):
        for ind, v in enumerate(ris[p]):
            c_ris[p].append(c_piloti - (ris_gara.index(v)))
            temp = ris_gara.index(v)
            ris_gara[temp] = 0
            if p == ts and ind == 1:
                if temp > 5:
                    fm += temp
                elif temp > 10:
                    fm += temp + 2
                else:
                    fm += 16 - temp
    t.sleep(1)
    print('Classifica: (%s)\n' % (circ))
    t.sleep(1)
    if len(partecipanti) == 8:
        for j in range(20):
            for i, p in enumerate(partecipanti):
                for ind, v in enumerate(c_ris[p]):
                    if v == c_class:
                        if v == 1:
                            classifica_mondiale[p][ind] += 20
                        if v == 2:
                            classifica_mondiale[p][ind] += 19
                        if v == 3:
                            classifica_mondiale[p][ind] += 18
                        if v == 4:
                            classifica_mondiale[p][ind] += 17
                        if v == 5:
                            classifica_mondiale[p][ind] += 16
                        if v == 6:
                            classifica_mondiale[p][ind] += 15
                        if v == 7:
                            classifica_mondiale[p][ind] += 14
                        if v == 8:
                            classifica_mondiale[p][ind] += 13
                        if v == 9:
                            classifica_mondiale[p][ind] += 12
                        if v == 10:
                            classifica_mondiale[p][ind] += 11
                        if v == 11:
                            classifica_mondiale[p][ind] += 10
                        if v == 12:
                            classifica_mondiale[p][ind] += 10
                        if v == 13:
                            classifica_mondiale[p][ind] += 10
                        if v == 14:
                            classifica_mondiale[p][ind] += 0
                        if v == 15:
                            classifica_mondiale[p][ind] += 0
                        if v == 16:
                            classifica_mondiale[p][ind] += 0
                        pl = piloti[p][ind]
                        print('N%s - %s(%s) con un punteggio di %s\n' % (v, pl, p, ris[p][ind]))
                        if pl == nome:
                            temp_posizione = v
                        c_class += 1
                        t.sleep(0.35)
    else:
        for j in range(20):
            for i, p in enumerate(partecipanti):
                for ind, v in enumerate(c_ris[p]):
                    if v == c_class:
                        pl = piloti[p][ind]
                        print('N%s - %s(%s) con un punteggio di %s\n' % (v, pl, p, ris[p][ind]))
                        c_class += 1
                        t.sleep(0.35)
    #if n_gara % (mondiale+2) == 0:
        #for i, c in enumerate(squadre):
            #for b, v in enumerate(squadre[c]):
                #squadre[c][b] += r.randint(-mondiale, mondiale)
                #if squadre[c][b] <= 0:
                    #squadre[c][b] = 1

    if n_gara % mondiale == 0:
        for i, c in enumerate(squadre):
            f = r.randint(0, 3)
            for b, v in enumerate(squadre[c]):
                if b == f:
                    squadre[c][b] += r.randint(-1, 2)
                if squadre[c][b] <= 0:
                    squadre[c][b] = 1
    num_miglioramenti = 0
    if n_gara % 3 == 0:
        all_pi = False
        all_pa = False
        energia = False
    if n_sponsor != 0:
        if temp_posizione <= l_sponsor[sponsor][1]:
            n_sponsor -= 1
            soldi += l_sponsor[sponsor][0]
            print('\nSoldi guadagnati da %s : %s' % (sponsor, l_sponsor[sponsor][0]))
        else:
            print('Non hai rispettato gli obbiettivi minimi.')
            reset_sponsor()           
    if caduta:
        print(t_caduta)
        caduta = False
        cost_caduta = True
    elif cost_caduta:
        print(t_cost_caduta)
    elif c_guasto:
        print(t_guasto)
        c_guasto = False
    if n_sponsor == 0 and sponsor != 'No-Sponsor':
        reset_sponsor()
        print('\nContratto con %s scaduto!\n' % ex_sponsor)



def fine_campionato(cl_md):
    co_classifica = 0
    cla_mond = []

    for i in cl_md:
        for c in cl_md[i]:
            cla_mond.append(c)

    cla_mond = decrescente(cla_mond)
    for j in range(20):
        for i, c in enumerate(cl_md):
            for co, s in enumerate(cl_md[c]):
                if co_classifica < 16:
                    if s == cla_mond[co_classifica]:
                        pl_mnd = piloti[c][co]
                        co_classifica += 1
                        if pl_mnd == nome:
                            return s

def reset_mondiale():
    global classifica_mondiale, fm
    
    for i, c in enumerate(classifica_mondiale):
            for co, s in enumerate(classifica_mondiale[c]):
                classifica_mondiale[c][co] = 0

    #for i, c in enumerate(squadre):
        #for co, s in enumerate(squadre[c]):
            #squadre[c][co] -= 1.5
    #fm -= 10
    #print(classifica_mondiale)

def campionato(g):
    global n_gara
    global mondiale
    
    if g == 1:
        gara('Mugello', assetto_campionato)
        n_gara += 1
    if g == 2:
        gara('Misano', assetto_campionato)
        n_gara += 1
    if g == 3:
        gara('FranciaCorta', assetto_campionato)
        n_gara += 1
    if g == 4:
        gara('Le Mans', assetto_campionato)
        n_gara += 1
    if g == 5:
        gara('Catalunya', assetto_campionato)
        n_gara += 1
    if g == 6:
        gara('Quatar', assetto_campionato)
        n_gara += 1
    if g == 7:
        gara('Twin Ring Motegi', assetto_campionato)
        n_gara += 1
    if g == 8:
        gara('Termas de Rio Hondo', assetto_campionato)
        n_gara += 1
    if g == 9:
        gara('Sachsenring', assetto_campionato)
        n_gara += 1
    if g == 10:
        gara('Silverstone', assetto_campionato)
        n_gara += 1
    if g == 11:
        gara('Sepang', assetto_campionato)
        n_gara += 1
    if g == 12:
        gara('Phillip Island', assetto_campionato)
        invio()
        spazio()
        cm(classifica_mondiale)
        mondiale += 1
        n_gara = 1
        return True

def officina():
    global soldi, aerodinamica, motore, gomme, ciclistica, costo_1, c_1, costo_2, c_2, costo_3, c_3, num_miglioramenti,cost_caduta, caduta, mondiale
    lvl_a = 1
    lvl_c = 1
    lvl_m = 1
    lvl_g = 1
    c_rip = 5 * mondiale
    print('\n\nStai entrando in officina...')
    if num_miglioramenti != 1:
        if aerodinamica <= 10:
            t_a = costo_1
            lvl_a = 1
        elif aerodinamica <= 20:
            t_a = costo_2
            lvl_a = 2
        else:
            t_a = costo_3
            lvl_a = 3
        if motore <= 10:
            t_m = costo_1
            lvl_m = 1
        elif motore <= 20:
            t_m = costo_2
            lvl_m = 2
        else:
            t_m = costo_3
            lvl_m = 3
        if ciclistica <= 10:
            t_c = costo_1
            lvl_c = 1
        elif ciclistica <= 20:
            t_c = costo_2
            lvl_c = 2
        else:
            t_c = costo_3
            lvl_c = 3
        if gomme <= 10:
            t_g = costo_1
            lvl_g = 1
        elif gomme <= 20:
            t_g = costo_2
            lvl_g = 2
        else:
            t_g = costo_3
            lvl_g = 3
        t.sleep(0.5)
        while True:
            spazio()
            print('Soldi : %s' % (soldi))
            t.sleep(0.25)
            print('\nN1-Aerodinamica - Livello : %s(Costo per migliorare : %s)' % (aerodinamica, t_a))
            print('N2-Motore - Livello : %s(Costo per migliorare : %s)' % (motore, t_m))
            print('N3-Ciclistica - Livello : %s (Costo per migliorare : %s)' % (ciclistica, t_c))
            print('N4-Gomme - Livello : %s (Costo per migliorare : %s)' % (gomme, t_g))
            print('N5-Ripara Moto - Costo : %s' % (c_rip))
            print('N6 - Esci dall\'Officina.')
            t.sleep(0.25)
            s = input('\nPer migliorare una parte della moto scrivi il numero corrispondente.\n\n>>>')
            if s == '1' and soldi >= t_a:
                if lvl_a == 1:
                    costo_1 += c_1
                    soldi -= t_a
                    aerodinamica += 1
                    num_miglioramenti += 1
                    break
                elif lvl_a == 2:
                    costo_2 += c_2
                    soldi -= t_a
                    aerodinamica += 1
                    num_miglioramenti += 1
                    break
                elif lvl_a == 3:
                    costo_3 += c_3
                    soldi -= t_a
                    aerodinamica += 1
                    num_miglioramenti += 1
                    break
            elif s == '2' and soldi >= t_m:
                if lvl_m == 1:
                    costo_1 += c_1
                    soldi -= t_m
                    motore += 1
                    num_miglioramenti += 1
                    break
                elif lvl_m == 2:
                    costo_2 += c_2
                    soldi -= t_m
                    motore += 1
                    num_miglioramenti += 1
                    break
                elif lvl_m == 3:
                    costo_3 += c_3
                    soldi -= t_m
                    motore += 1
                    num_miglioramenti += 1
                    break
            elif s == '3' and soldi >= t_c:
                if lvl_c == 1:
                    costo_1 += c_1
                    soldi -= t_c
                    ciclistica += 1
                    num_miglioramenti += 1
                    break
                elif lvl_c == 2:
                    costo_2 += c_2
                    soldi -= t_c
                    ciclistica += 1
                    num_miglioramenti += 1
                    break
                elif lvl_c == 3:
                    costo_3 += c_3
                    soldi -= t_c
                    ciclistica += 1
                    num_miglioramenti += 1
                    break
                num_miglioramenti += 1
            elif s == '4' and soldi >= t_g:
                if lvl_g == 1:
                    costo_1 += c_1
                    soldi -= t_g
                    gomme += 1
                    num_miglioramenti += 1
                    break
                elif lvl_g == 2:
                    costo_2 += c_2
                    soldi -= t_g
                    gomme += 1
                    num_miglioramenti += 1
                    break
                elif lvl_g == 3:
                    costo_3 += c_3
                    soldi -= t_g
                    gomme += 1
                    num_miglioramenti += 1
                    break
            elif s == '5':
                if cost_caduta and soldi >= c_rip:
                    cost_caduta = False
                    caduta = False
                    soldi -= c_rip
                    break
                else:
                    print('\nLa tua Moto non ha bisogno di riparazione oppure non hai abbastanza soldi.')
                    invio()
                    continue
            elif s == '6':
                break
            else:
                print('\n\n\nNon hai abbastanza soldi per acquistare il miglioramento oppure hai sbagliato carattere. Riprova.\n\n\n')
                invio()
                t.sleep(1.5)
                continue
    else:
        print('\n\nHai raggiunto il numero massimo di miglioramenti.')
        print('Aspetta la prossima gara per migliorare ancora la moto!')
        invio()
        
def ct(team): #c, m, g, a
    global fm, motore, aerodinamica, gomme, ciclistica, ts, piloti
    if team != ts:
        temp = piloti[ts][1]
        tempo = piloti[team][1]
        fm, motore, aerodinamica, gomme, ciclistica, piloti[ts][1], piloti[team][1], ts = fm*0.85, squadre[team][1], squadre[team][3], squadre[team][2], squadre[team][0], tempo, temp, team 

def show_moto():
    global assetto, inge
    #manubrio, sella, sospensioni-assetto
    #manubrio, sella, sospensioni-inge
    sel = ''
    sos = ''
    man = ''
    if inge[0]:
        if assetto[0]==2:
            man = 'Aperto'
        elif assetto[0]==1:
            man = 'Normale'
        elif assetto[0]==0:
            man = 'Chiuso'
    else:
        man = 'Ancora Sconosciuto'
    if inge[1]:
        if assetto[1]==2:
            sel = 'Alta'
        elif assetto[1]==1:
            sel = 'Media'
        elif assetto[1]==0:
            sel = 'Bassa'
    else:
        sel = 'Ancora Sconosciuto'
    if inge[2]:
        if assetto[2]==2:
            sos = 'Dure'
        elif assetto[2]==1:
            sos = 'Normali'
        elif assetto[2]==0:
            sos = 'Morbide'
    else:
        sos = 'Ancora Sconosciuto'
    spazio()
    if cost_caduta:
        c = 'Da riparare'
    else:
        c = 'Nessun Problema'
    print('Team : %s' % ts)
    print('Assetto : ')
    print('-Sella > %s' % sel)
    print('-Sospensioni > %s' % sos)
    print('-Manubrio > %s' % man)
    print('Condizioni : %s' % c)
    print('\nStatistiche :\n-Aerodinamica : %s\n-Motore : %s\n-Ciclistica : %s\n-Gomme : %s' % (aerodinamica, motore, ciclistica, gomme))
    print('\nMondiali vinti : %s' % mondiali_vinti)
    invio()

def scelta_sponsor():
    global sponsor, l_sponsor, lf_sponsor, n_sponsor
    while True:
        spazio()
        print('Sponsor attuale : %s' % sponsor)
        print('Gare rimaste : %s' % n_sponsor)
        print('\n\nSponsor disponibili:')
        for i, d in enumerate(l_sponsor):
            print('N%s - %s, Paga : %s (Soldi per gara), Obbiettivo : Almeno %s' % (i+1, d, l_sponsor[d][0], l_sponsor[d][1]))
        print('N9 - Esci')
        sc = input('\n\n>>>')
        if sc == '1':
            if sponsor == 'PxF-Esport':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'PxF-Esport'
                print('\nHai firmato un contratto con PxF-Esport.')
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                invio()
        elif sc == '2':
            if sponsor == 'PxF-Music':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'PxF-Music'
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                print('\nHai firmato un contratto con PxF-Music.')
                invio()
        elif sc == '3':
            if sponsor == 'Zamsung':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'Zamsung'
                print('\nHai firmato un contratto con Zamsung.')
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                invio()
        elif sc == '4':
            if sponsor == 'Adisas':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'Adisas'
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                print('\nHai firmato un contratto con Adisas.')
                invio()
        elif sc == '5':
            if sponsor == 'pinApple':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'pinApple'
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                print('\nHai firmato un contratto con pinApple.')
                invio()
        elif sc == '6':
            if sponsor == 'Minisoft':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'Minisoft'
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                print('\nHai firmato un contratto con Minisoft.')
                invio()
        elif sc == '7':
            if sponsor == 'Niche':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'Niche'
                n_sponsor = 4
                lf_sponsor[int(sc)-1] = 'True'
                print('\nHai firmato un contratto con Niche.')
                invio()
        elif sc == '8':
            if sponsor == 'WannemaWay':
                print('\nHai già firmato un contratto con questo Sponsor.')
                invio()
            elif n_sponsor != 0:
                print('\nHai già firmato un contratto con uno Sponsor, attendi il termine del Contratto per scegliere il nuovo sponsor.')
                invio()
            else:
                if lf_sponsor[int(sc)-1] == 'True':
                    print('\nHai già firmato un contratto con questo Sponsor in passato.')
                    invio()
                    continue
                sponsor = 'WannemaWay'
                lf_sponsor[int(sc)-1] = 'True'
                n_sponsor = 4
                print('\nHai firmato un contratto con WannemaWay.')
                invio()
        elif sc =='9':
            break
        else:
            print('\nHai inserito un carattere o numero sbagliato.')
            invio()
            continue
        
def reset_sponsor():
    global sponsor, n_sponsor, ex_sponsor
    ex_sponsor = sponsor
    sponsor = 'No-Sponsor'
    n_sponsor = 0

def laboratorio():
    global assetto, inge, soldi
    #manubrio, sella, sospensioni-inge
    spazio()
    while True:
        print('Costo - 50')
        print('N1 - Sella ')
        print('N2 - Manubrio')
        print('N3 - Sospensioni')
        print('N4 - Torna al menu')
        x = input('\n>>>')
        if x == '1' or x.lower() == 'n1':
            if soldi >= 50 and inge[1] == 0:
                soldi -= 50
                inge[1] = 1
                print('\nPer vedere lo studio sulla Sella accedi dalla sezione Moto del menu.')
                invio()
                break
            else:
                print('\nNon hai sufficenti soldi per studiare la Sella della tua Moto oppure lo hai già fatto.')
                invio()
                continue
        elif x == '2' or x.lower() == 'n2':
            if soldi >= 50 and inge[0] == 0:
                soldi -= 50
                inge[0] = 1
                print('\nPer vedere lo studio sul Manubrio accedi dalla sezione Moto del menu.')
                invio()
                break
            else:
                print('\nNon hai sufficenti soldi per studiare la Sella della tua Moto oppure lo hai già fatto.')
                invio()
                continue
        elif x == '3' or x.lower() == 'n3':
            if soldi >= 50 and inge[2] == 0:
                soldi -= 50
                inge[2] = 1
                print('\nPer vedere lo studio sulle Sospensioni accedi dalla sezione Moto del menu.')
                invio()
                break
            else:
                print('\nNon hai sufficenti soldi per studiare la Sella della tua Moto oppure lo hai già fatto.')
                invio()
                continue
        elif x == '4' or x.lower() == 'n4':
            invio()
            break
    

        

def cambio_nome():
    global nome, piloti
    ex_p = ''
    while True:
        counter = 1
        spazio()
        print('Adesso avrai la possibilità di cambiare il nome a tutti i piloti se lo vorrai, altrimenti potrai continuare il Tutorial\n\n')
        for i, d in enumerate(piloti):
            for c, v in enumerate(piloti[d]):
                print('N%s - Pilota %s, nome attuale : %s ->'%(counter, d, v))
                counter += 1
        print('N17 - Continua il tutorial')
        s = input('\n\n>>>')
        if s == '1' or s.lower() == 'n1':
            ex_p = piloti['Yamaha'][0]
            piloti['Yamaha'][0] = maiuscola(input('\n ->'))
            if piloti['Yamaha'][0] == '':
                piloti['Yamaha'][0] = ex_p
            continue
        elif s == '2' or s.lower() == 'n2':
            ex_p = piloti['Yamaha'][1]
            piloti['Yamaha'][1] = maiuscola(input('\n ->'))
            if piloti['Yamaha'][1] == '':
                piloti['Yamaha'][1] = ex_p
            continue
        elif s == '3' or s.lower() == 'n3':
            ex_p = piloti['Honda'][0]
            piloti['Honda'][0] = maiuscola(input('\n ->'))
            if piloti['Honda'][0] == '':
                piloti['Honda'][0] = ex_p
            continue
        elif s == '4' or s.lower() == 'n4':
            ex_p = piloti['Honda'][1]
            piloti['Honda'][1] = maiuscola(input('\n ->'))
            if piloti['Honda'][1]  == '':
                piloti['Honda'][1]  = ex_p
            continue
        elif s == '5' or s.lower() == 'n5':
            ex_p = piloti['Ducati'][0]
            piloti['Ducati'][0] = maiuscola(input('\n ->'))
            if piloti['Ducati'][0] == '':
                piloti['Ducati'][0] = ex_p
            continue
        elif s == '6' or s.lower() == 'n6':
            ex_p = piloti['Ducati'][1]
            piloti['Ducati'][1] = maiuscola(input('\n ->'))
            if piloti['Ducati'][1] == '':
                piloti['Ducati'][1] = ex_p
            continue
        elif s == '7' or s.lower() == 'n7':
            ex_p = piloti['Suzuki'][0]
            piloti['Suzuki'][0] = maiuscola(input('\n ->'))
            if piloti['Suzuki'][0] == '':
                piloti['Suzuki'][0] = ex_p
            continue
        elif s == '8' or s.lower() == 'n8':
            if piloti['Suzuki'][1] != nome:
                ex_p = piloti['Suzuki'][1]
                piloti['Suzuki'][1] = maiuscola(input('\n ->'))
                if piloti['Suzuki'][1] == '':
                    piloti['Suzuki'][1] = ex_p
                continue
            else:
                print('\nQuesto slot è riservato al tuo personaggio, non puoi modificarne il nome.')
                invio()
                continue
        elif s == '9' or s.lower() == 'n9':
            ex_p = piloti['KTM'][0]
            piloti['KTM'][0] = maiuscola(input('\n ->'))
            if piloti['KTM'][0] == '':
                piloti['KTM'][0] = ex_p
            continue
        elif s == '10' or s.lower() == 'n10':
            ex_p = piloti['KTM'][1]
            piloti['KTM'][1] = maiuscola(input('\n ->'))
            if piloti['KTM'][1] == '':
                piloti['KTM'][1] = ex_p
            continue
        elif s == '11' or s.lower() == 'n11':
            ex_p = piloti['Aprilia'][0]
            piloti['Aprilia'][0] = maiuscola(input('\n ->'))
            if piloti['Aprilia'][0] == '':
                piloti['Aprilia'][0] = ex_p
            continue
        elif s == '12' or s.lower() == 'n12':
            if piloti['Aprilia'][1] != nome:
                ex_p = piloti['Aprilia'][1]
                piloti['Aprilia'][1] = maiuscola(input('\n ->'))
                if piloti['Aprilia'][1] == '':
                    piloti['Aprilia'][1] = ex_p
                continue
            else:
                print('\nQuesto slot è riservato al tuo personaggio, non puoi modificarne il nome.')
                invio()
                continue
        elif s == '13' or s.lower() == 'n13':
            ex_p = piloti['Piaggio'][0]
            piloti['Piaggio'][0] = maiuscola(input('\n ->'))
            if piloti['Piaggio'][0] == '':
                piloti['Piaggio'][0] = ex_p
            continue
        elif s == '14' or s.lower() == 'n14':
            if piloti['Piaggio'][1] != nome:
                ex_p = piloti['Piaggio'][1]
                piloti['Piaggio'][1] = maiuscola(input('\n ->'))
                if piloti['Piaggio'][1] == '':
                    piloti['Piaggio'][1] = ex_p
                continue
            else:
                print('\nQuesto slot è riservato al tuo personaggio, non puoi modificarne il nome.')
                invio()
                continue
        elif s == '15' or s.lower() == 'n15':
            ex_p = piloti['BMW'][0]
            piloti['BMW'][0] = maiuscola(input('\n ->'))
            if piloti['BMW'][0] == '':
                piloti['BMW'][0] = ex_p
            continue
        elif s == '16' or s.lower() == 'n16':
            ex_p = piloti['BMW'][1]
            piloti['BMW'][1] = maiuscola(input('\n ->'))
            if piloti['BMW'][1] == '':
                piloti['BMW'][1] = ex_p
            continue
        elif s == '17' or s.lower() == 'n17':
            invio()
            break
        else:
            print('\nHai inserito un carattere non corretto.')
            continue 
    
def guasto():
    global aerodinamica, motore, ciclistica, gomme, t_guasto, c_guasto
    s = r.randint(0, 3)
    if s == 0:
        aerodinamica -= 1
        t_guasto = '\n%s si è dovuto ritirare a causa di una rottura delle carene.\nAerodinamica -1' % nome
    elif s == 1:
        motore -= 1
        t_guasto = '\n%s si è dovuto ritirare a causa di un guasto al motore.\nMotore -1' % nome
    elif s == 2:
        ciclistica -= 1
        t_guasto = '\n%s si è dovuto ritirare a causa di una rottura delle molle delle sospensioni.\nCiclistica -1' % nome
    else:
        t_guasto = '\n%s si è dovuto ritirare a causa dello scoppio delle gomme per la troppa usura.\nGomme -1' % nome
        gomme -= 1
    c_guasto = True
    
##############################
while True:
    print('\n\n---------------MENU---------------\n\n')
    print('N1 - Nuova Campagna')
    print('N2 - Carica Partita')
    print('--------')
    print('Versione - %s' % versione)
    z = input('\n\n>>>')
    if z.lower() == 'n1' or z == '1':
        tutorial = True
        break
    elif z.lower() == 'n2' or z == '2':
        if carica():
            break
        else:
            t.sleep(0.75)
            continue
    else:
        print('\n\n\n' * 5)
        continue

if tutorial:
    while True:
        print('\n\nScegli la difficoltà:')
        print('N1 - Difficile')
        print('N2 - Media')
        print('N3 - Facile')
        o = input('\n\n>>>')
        if o == '1' or o.lower() == 'n1':
            diff = 2
            break
        elif o == '2' or o.lower() == 'n2':
            diff = 3
            break
        elif o == '3' or o.lower() == 'n3':
            diff = 4
            break
        else:
            continue

    
    t.sleep(3)
    print('\n\n\n§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
    t.sleep(1)
    print('\nIn questo gioco dovrai gestire un Pilota di Moto.')
    t.sleep(2.5)
    print('Comincerai con un team di fascia più bassa per poi avere la possibilità di entrare in team più forti come Yamaha e Ducati.')
    t.sleep(2.5)
    print('Alla fine di ogni stagione, che dura 12 gare, se hai ottenuto buone perfomance durante la stagione potrai farti notare dai Big.')
    t.sleep(2.5)
    print('La tua avventura comincia qui!!')
    t.sleep(3.5)

    while True:
        n = input('\n\nCome ti chiami campione?\n\n>>>')
        if n == '':
            continue
        elif len(n) > 10:
            print('\n\nPerfavore inserisci un nome più corto.')
            continue
        else:
            nome = full_maiuscola(n)
            print('\n\nHai detto %s?\nHai un nome da campione, niente ti fermerà!!' % (nome))
            break
    assetto = [r.randint(0, 2), r.randint(0, 2), r.randint(0, 2)]
    t.sleep(1.5)
    print('\n\nTi verranno concessi 150 milioni di Euro per cominciare la tua avventura nel mondo delle Moto!')
    print('Scegli una squadra tra quelle che hanno fatto un\'offerta per Te.')
    t.sleep(6.5)
    print('\n\nN1 - Suzuki, 78 Milioni, Voto dei Critici: 7')
    print('N2 - Aprilia, 64 Milioni, Voto dei Critici: 5')
    print('N3 - Piaggio, 48 Milioni, Voto dei Critici: 3')
    t.sleep(6.5)

    while True:
        sq = input('\n\nPer scegliere la tua prima squadra scrivi il numero corrispondente.\n\n>>>')
        if sq == '':
            continue
        elif sq == '1':
            ts, ciclistica, motore, gomme, aerodinamica = 'Suzuki', squadre['Suzuki'][0], squadre['Suzuki'][1], squadre['Suzuki'][2], squadre['Suzuki'][3]
            piloti['Suzuki'][1] = nome
            soldi -= 78
            break
        elif sq == '2':
            ts, ciclistica, motore, gomme, aerodinamica = 'Aprilia', squadre['Aprilia'][0], squadre['Aprilia'][1], squadre['Aprilia'][2], squadre['Aprilia'][3]
            piloti['Aprilia'][1] = nome
            soldi-= 64
            break
        elif sq == '3':
            ts, ciclistica, motore, gomme, aerodinamica = 'Piaggio', squadre['Piaggio'][0], squadre['Piaggio'][1], squadre['Piaggio'][2], squadre['Piaggio'][3]
            piloti['Piaggio'][1] = nome
            soldi -= 48
            break
        else:
            continue

    t.sleep(1.5)
    print('\n\nHai scelto %s!' % (ts))
    t.sleep(1)
    if ts == 'Suzuki':
        print('Questo è un ottimo team per cominciare e buono per puntare alla vittoria del Campionato.')
        t.sleep(2.5)
        print('La moto del team Suzuki ha un ottimo assetto aerodinamico con delle gomme molto buone che ti assicureranno prestazioni eccezionali durante tutto l\'arco della gara.')
    elif ts == 'Aprilia':
        print('Il team che hai scelto è molto buono per cominciare.\nIl costo per entrarci non è alto e ti permette di migliorare la moto sotto l\'aspetto che preferisci.')
        t.sleep(2.5)
        print('La moto del team Aprilia ha un ottima ciclistica che ti permetterà, nei tracciati più impegnativi, di entrare meglio in curva e stressare meno le gomme.')
    elif ts == 'Piaggio':
        print('Il team che hai scelto è l\'ultimo team arrivato. Infatti ha poca esperienza con prestazioni basse sotto tutti gli aspetto.')
        t.sleep(2.5)
        print('Il lato positivo è che il prezzo è molto basso e ti permette di risparmiare per le stagioni successive.')
    input('\nPremi INVIO per continuare.')
    cambio_nome()
    t.sleep(1.5)
    print('\n\n\n§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\n\n\n')
    t.sleep(1.5)
    print('Dato che questo è il tuo primo anno che corri in un team, Ti ho iscritto ad una gara amichevole dove potrai capire come fare da ora in poi nel vero e proprio campionato!')
    t.sleep(4.5)
    print('Adesso scopri chi parteciperà:\n')
    t.sleep(1.5)
    for p in piloti['Suzuki']:
        print('%s - Suzuki' % (p))
    t.sleep(1)
    for p in piloti['KTM']:
        print('%s - KTM' % (p))
    t.sleep(1)
    for p in piloti['Aprilia']:
        print('%s - Aprilia' % (p))
    t.sleep(1)
    for p in piloti['Piaggio']:
        print('%s - Piaggio' % (p))
    t.sleep(1)
    print('\nIn questa gara non parteciperanno tutti i team iscritti al campionato.')
    t.sleep(3)
    print('Solitamente i team più forti si astengono per non svelare le strategie!')
    t.sleep(3)
    print('Prima di iniziare voglio spiegarti come modificare l\'assetto in vista della tua prima gara.')
    t.sleep(1.5)
    print('Prima di ogni gara potrai modificare la tua moto sotto il punto di vista del: Manubrio,\nSella\ne Sospensioni.')
    t.sleep(3)
    print('Inoltre potrai modificare il tuo stile di guida per essere più o meno aggressivo.\nTieni conto però del fatto che uno stile di guida aggressivo causerà una maggior probabilità di caduta e viceversa.')
    t.sleep(3)
    input('\nPremi INVIO per continuare.')
    gara('Misano', assetto_tutorial)
    t.sleep(4.5)
    print('Caspita sei veramente forte!!!')
    t.sleep(2)
    print('C\'è molto da migliorare ma il tuo futuro è promettente!')
    t.sleep(2)
    print('\nPer prima cosa devi sapere che hai la possibilità di migliorare la tua Moto sotto le caratteristiche di:\n-Aerodinamica\n-Motore\n-Ciclistica\n-Gomme.')
    t.sleep(4.5)
    print('\nPuoi farlo dall\'officina dopo ogni gara!')
    t.sleep(2)
    print('\nVediamo come fare!!!')
    t.sleep(2.5)
    print('\n\nPer prima cosa dobbiamo andare in officina.')
    t.sleep(2.5)
    print('\nUna volta entrato potrai migliorare facilmente ogni caratteristica della tua moto scrivendo il numero corrispondente.')
    t.sleep(3.5)
    input('\nPremi INVIO per continuare.')
    officina()
    t.sleep(2)
    print('\nBravo, hai capito come migliorare la moto.')
    t.sleep(2)
    print('Ricorda! Dopo ogni gara potrai accedere all\'officina per un massimo di Tre volte')
    t.sleep(3)
    print('La tua avventura ha finalmente inizio...\nBuona fortuna %s' % (nome))
    salva()
    input('\nPremi INVIO per continuare.')

##############################

while True:
    spazio()
    print('Soldi : %s' % (soldi))
    print('Sponsor attuale : %s (%s Gare rimaste)' % (sponsor, n_sponsor))
    print('Posizione nel Mondiale : %s' % (clm(classifica_mondiale)))
    print('Gara numero : %s' % (n_gara))
    print('Stagione numero : %s' % mondiale)
    t.sleep(0.5)
    print('\nN1 - Officina')
    print('N2 - Laboratorio')
    print('N3 - Moto')
    print('N4 - Allenamento Fisico')
    print('N5 - Allenamento in Pista')
    print('--------')
    print('N6 - Prossima Gara')
    print('N7 - Classifica Mondiale')
    print('N8 - Scegli Sponsor')
    print('--------')
    if sviluppatore == False:
        print('N9 - Salva Partita')
    print('N10 - Carica Partita')
    print('--------')
    print('Versione - %s' % (versione))
    g = input('\n\n>>>')
    if g == '1' or g.lower() == 'n1':
        officina()
        t.sleep(0.5)
        continue
    if g == '2' or g.lower() == 'n2':
        laboratorio()
        t.sleep(0.5)
        continue
    elif g == '3' or g.lower() == 'n3':
        show_moto()
        continue
    elif g == '6' or g.lower() == 'n6':
        if campionato(n_gara):
            if clm(classifica_mondiale) == 1:
                soldi += 45
                mondiali_vinti += 1
            elif clm(classifica_mondiale) == 2:
                soldi += 40
            elif clm(classifica_mondiale) == 3:
                soldi +=35
            else:
                soldi += 30
            soldi += 3 * mondiale
            reset_sponsor()
            lf_sponsor = ['False','False','False','False','False','False','False','False']
            if fine_campionato(classifica_mondiale) > 180:
                print('\n\nSei stato scelto dal team Yamaha.\nSei libero di continuare a girare con %s oppure cambiare team.' % (ts))
                while True:
                    k = input('\n\n Vuoi trasferirti a Yamaha? [S, n]\n>>>')
                    if k.lower() == 's':
                        ct('Yamaha')
                        #motore -= 3
                        #aerodinamica -= 2
                        #gomme -= 3
                        #ciclistica -= 2
                        break
                    elif k.lower() == 'n':
                        print('Hai rifiutato il contratto!')
                        if mondiale > 5:
                            fm *= 0.9
                        break
                    else:
                        continue
            elif fine_campionato(classifica_mondiale) > 160:
                print('\n\nSei stato scelto dal team BMW.\nSei libero di continuare a girare con %s oppure cambiare team.' % (ts))
                while True:
                    k = input('\n\n Vuoi trasferirti a BMW? [S, n]\n>>>')
                    if k.lower() == 's':
                        ct('BMW')
                        #motore -= 2
                        #aerodinamica -= 3
                        #gomme -= 2
                        #ciclistica -= 2
                        break
                    elif k.lower() == 'n':
                        print('Hai rifiutato il contratto!')
                        if mondiale > 5:
                            fm *= 0.9
                        break
                    else:
                        continue
            elif fine_campionato(classifica_mondiale) > 140:
                print('\n\nSei stato scelto dal team Honda.\nSei libero di continuare a girare con %s oppure cambiare team.' % (ts))
                while True:
                    k = input('\n\n Vuoi trasferirti a Honda? [S, n]\n>>>')
                    if k.lower() == 's':
                        ct('Honda')
                        #motore -= 2
                        #aerodinamica -= 1
                        #gomme -= 2
                        #ciclistica -= 1
                        break
                    elif k.lower() == 'n':
                        print('Hai rifiutato il contratto!')
                        if mondiale > 5:
                            fm *= 0.9
                        break
                    else:
                        continue
            elif fine_campionato(classifica_mondiale) > 120:
                print('\n\nSei stato scelto dal team Ducati.\nSei libero di continuare a girare con %s oppure cambiare team.' % (ts))
                while True:
                    k = input('\n\n Vuoi trasferirti a Ducati? [S, n]\n>>>')
                    if k.lower() == 's':
                        ct('Ducati')
                        #motore -= 1
                        #aerodinamica -= 1
                        #gomme -= 2
                        #ciclistica -= 1
                        break
                    elif k.lower() == 'n':
                        print('Hai rifiutato il contratto!')
                        if mondiale > 5:
                            fm *= 0.9
                        break
                    else:
                        continue
            elif fine_campionato(classifica_mondiale) > 100:
                print('\n\nSei stato scelto dal team KTM.\nSei libero di continuare a girare con %s oppure cambiare team.' % (ts))
                while True:
                    k = input('\n\n Vuoi trasferirti a KTM? [S, n]\n>>>')
                    if k.lower() == 's':
                        ct('KTM')
                        #motore -= 1
                        #aerodinamica -= 1
                        #gomme -= 1
                        #ciclistica -= 1
                        break
                    elif k.lower() == 'n':
                        print('Hai rifiutato il contratto!')
                        if mondiale > 5:
                            fm *= 0.9
                        break
                    else:
                        continue
            else:
                print('\n\nNessun team ha fatto richiesta per averti come Pilota!!')
                invio()
                if mondiale > 5:
                            fm *= 0.9
            reset_mondiale()
            continue
        t.sleep(2)
        invio()
        continue
    elif g == '4' or g.lower() == 'n4':
        if all_pa == False and energia == False:
            print('\nStai entrando in Palestra...')
            t.sleep(1)
            spazio()
            print('Allenamento...')
            t.sleep(3)
            spazio()
            print('Il tuo allenamento è andato bene, La prossima gara sarai più a tuo agio con la Moto!')
            invio()
            fm *= 1.05
            energia = True
            all_pa = True
        else:
            print('\n\nTi sei già allenato. Devi riposare! (Allenamenti disponibili ogni 3 gare)')
            invio()
        continue
    elif g == '5' or g.lower() == 'n5':
        if all_pi == False and energia == False:
            print('\nStai entrando in Pista per allenarti...')
            t.sleep(1)
            spazio()
            print('Allenamento...')
            t.sleep(3)
            spazio()
            print('Il tuo allenamento è andato bene, La prossima gara sarai più a tuo agio con la Moto!')
            b = r.randint(0, 2)
            if b == 0:
                b = 'Aerodinamica'
                aerodinamica += 1
            elif b == 1:
                b = 'Motore'
                motore += 1
            elif b == 2:
                b = 'Ciclistica'
                ciclistica += 1
            print('\n%s è salito di 1 Punto.' % b)
            invio()
            energia = True
            all_pi = True
        else:
            print('\n\nTi sei già allenato. Devi riposare! (Allenamenti disponibili ogni 3 gare)')
            invio()
        continue
    elif g == '7' or g.lower() == 'n7':
        print('\n')
        cm(classifica_mondiale)
        invio()
        continue
    elif g == '8' or g.lower() == 'n8':
        scelta_sponsor()
        continue
    elif g == '9' or g.lower() == 'n9':
        if sviluppatore == False:
            salva()
            spazio()
            print('Salvataggio avvenuto con successo!')
            invio()
        continue
    elif g == '10' or g.lower() == 'n10':
        carica()
        continue
    else:
        continue
    
##############################