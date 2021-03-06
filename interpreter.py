import sys
import os.path
import time
import re

print("STALINIUM V1 PAR ALEXDIEU")

if len(sys.argv) > 1:
    file = sys.argv[1]
    if os.path.isfile(file):
        pass
    else:
        print("Error , File doesn't exist !")
else:
    file = input(">>>")

variables = {}

lignes = []

try:
    with open(file, "r") as f:
        for index, value in enumerate(f.readlines()):
            lignes.append(value.strip("\n"))
            lignes = [i for i in lignes if i] 
except:
    lignes.append(file)
    
def lts(a):
    lt = ""
    return ' '.join(a)
    
def CHEZCFIRST(mot, ligne):
    exitp = False
    sec = ''
    prem = ''
    try:
       prem = ligne.partition(mot)[0]
       exitp = True
    except:
       return True
    if exitp == True:
        if prem.isspace() == True:
            return True
        elif prem == '' or prem == None:
            return True
        else:
            return False

def calc(ligne: list) -> float:
    tried2 = True
    try:
        if ligne[2] == "+":
            return float(ligne[1]) + float(ligne[3])
        if ligne[2] == "-":
            return float(ligne[1]) - float(ligne[3])
        if ligne[2] == "*":
            return float(ligne[1]) * float(ligne[3])
        if ligne[2] == "/":
            return float(ligne[1]) / float(ligne[3])
        if ligne[2] == "**":
            return float(ligne[1]) ** float(ligne[3])
        if ligne[2] == "//":
            return float(ligne[1]) % float(ligne[3])
        else:
            check_if(ligne.split())
    except:
        try:
            if "+" in ligne[1]:
                prems = ligne[1].partition("+")[0]
                sec = ligne[1].partition("+")[2]
                ope = "+"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            elif "-" in ligne[1]:
                prems = ligne[1].partition("-")[0]
                sec = ligne[1].partition("-")[2]
                ope = "+"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            elif "*" in ligne[1]:
                prems = ligne[1].partition("*")[0]
                sec = ligne[1].partition("*")[2]
                ope = "*"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            elif "/" in ligne[1]:
                prems = ligne[1].partition("/")[0]
                sec = ligne[1].partition("/")[2]
                ope = "/"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            elif "**" in ligne[1]:
                prems = ligne[1].partition("**")[0]
                sec = ligne[1].partition("**")[2]
                ope = "**"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            elif "//" in ligne[1]:
                prems = ligne[1].partition("//")[0]
                sec = ligne[1].partition("//")[2]
                ope = "**"
                return("ERREUR 1 , les nombres doivent êtrent espacés de l\'opérateur comme ça : " + prems + " " + ope + " " + sec)
            else:
                if tried2 == True:
                    return("ERREUR 2 , Opérateur inconnu ! : " + lignes[0])
                else:
                    check_if(ligne.split())
        except:
            return "ERREUR 7 : AUCUN CALCUL DONNE"

def check_if(ligne: list) -> float:
    args = []
    tried2 = True
    try:
        for arg in ligne[1:]:
            args.append(arg)
        if args[1] == "?=":
            if args[0] == args[2]:
                return "Vrai"
            else:
                return "Faux"
        elif args[1] == "<":
            if args[0] < args[2]:
                return "Vrai"
            else:
                return "Faux"
        elif args[1] == ">":
            if args[0] > args[2]:
                return "Vrai"
            else:
                return "Faux"
        elif args[1] == "<=":
            if args[0] <= args[2]:
                return "Vrai"
            else:
                return "Faux"
        elif args[1] == "!=":
            if args[0] != args[2]:
                return "Vrai"
            else:
                return "Faux"
        elif args[1] == ">=":
            if args[0] >= args[2]:
                return "Vrai"
            else:
                return "Faux"
        else:
            if tried2 == True:
                return("ERREUR 2 , Opérateur inconnu ! : " + arg[0])
            else:
                calc(ligne.split())
    except:
        return "ERREUR 7 AUCUNE CONDITION DONNE"
        

def scan(lignes: list):
    for ligne in lignes:
        sortie = []
        check = ''
        bon = False
        ans = False
        split_ligne = ligne.split()
        if "montre" in ligne:
            ans = False
            ans = CHEZCFIRST("montre", ligne)
            if ans == True:
                lit = " ".join(split_ligne[1:])
                if ":" in lit:
                    check = lit.partition(":")[0]
                    check = check[-1:]
                    if check == "\\":
                        pass
                    else:
                        erreurs = 0
                        erreur = []
                        erN = []
                        ni = False
                        name = lit.partition(":")[2]
                        name = name.split()
                        NAME = ''
                        NAMEV = ''
                        ende = len(name)
                        for i in range(0, ende):
                                NAME = NAME + '-' + name[i]
                                if i == 0:
                                    NAMEV = NAMEV + ':' + name[i]
                                else:
                                    NAMEV = NAMEV + ' ' + name[i]
                                if NAME in variables:
                                    erreurs = erreurs + 1
                                    erreur.append(NAME)
                                    erN.append(NAMEV)
                                else:
                                    pass
                        if len(erreur) == 0:
                            ni = True
                            print("ERREUR 6 : VARIABLE N'EXISTE PAS")
                        if len(erreur) == 1:
                            ni = True
                            val = variables[erreur[0]]
                            lit = lit.replace(NAMEV, val, 1)
                        if len(erreur) == 2:
                            ni = True
                            print("ATTENTION : DEUX VARIABLES ONT UN NOM SIMILIAIRE AU DEBUT : "+ erN[0] +" et "+ erN[1] +" ! STALINIUM prends la première par défault ! ")
                            val = variables[erreur[0]]
                            lit = lit.replace(NAMEV, val, 1)
                        else:
                            if ni == False:
                                print("ATTENTION : PLUSIEURS VARIABLES ONT UN NOM SIMILIAIRE AU DEBUT ! STALINIUM prends la première par défault ! ")
                                val = variables[erreur[0]]
                                lit = lit.replace(NAMEV, val, 1)
                            else:
                                pass
                if "\\:" in lit:
                    lit = lit.replace("\\:", ":")
                else:
                    pass
                print(lit)
                bon = True
            else:
                pass
        if "calcul" in ligne:
            ans = False
            ans = CHEZCFIRST("calcul", ligne)
            if ans == True:
                print(calc(split_ligne))
                bon = True
            else:
                pass
        if "si" in ligne:
            ans = False
            ans = CHEZCFIRST("si", ligne)
            if ans == True:
                print(check_if(split_ligne))
                bon = True
            else:
                pass
        if "sortir" in ligne:
            ans = False
            exitp = False
            sec = ''
            prem = ''
            try:
                prem = ligne.partition("sortir")[0]
                sec = ligne.partition("sortir")[2]
                exitp = True
            except:
                exit()
            if exitp == True:
                if sec.isspace() == True and  prem.isspace() == True:
                    exit()
                elif sec == '' or sec == None and prem == '' or prem == None:
                    exit()
                else:
                    pass
        if 'dors' in ligne:
            listDORS = []
            ans = False
            ans = CHEZCFIRST("dors", ligne)
            if ans == True:
                try:               
                    bon = int(" ".join(split_ligne[1]))
                except:
                    print("ERREUR 3 : Mauvaise SYNTAXE pour DORS : DORS + TEMPS // exemple : dors 2")
                try:
                    listDORS = split_ligne
                    listDORS.remove(str(bon))
                    listDORS.remove("dors")
                    arg = lts(listDORS)
                except:
                    print("DORS ARG : IMPOSSIBLE DE CONVERTIR EN LITTERAIRE ")
                    arg = ''
                if arg != '':
                    print(arg)
                else:
                    pass
                time.sleep(bon)
                bon = True
            else:
                pass
        if "pause" in ligne:
            ans = False
            ans = CHEZCFIRST("pause", ligne)
            if ans == True:
                pause = False
                sec = ''
                prem = ''
                try:
                    prem = ligne.partition("pause")[0]
                    sec = ligne.partition("pause")[2]
                    pause = True
                except:
                    input("Pause ...")
                if pause == True:
                    sec = sec[1:]
                    if prem.isspace() == True:
                        input(sec + "...")
                    elif prem == '' or prem == None:
                        input(sec + "...")
                    else:
                        pass
            bon = True
        if ":" in ligne:
            NAME = ''
            verif = ligne.partition(":")[0]
            if verif == '' or verif.isspace() == True:
                try:
                    verif2 = ligne.partition("=")[2]
                    if verif2 == '' or verif2.isspace() == True:
                        try:
                            namevar = ligne.partition(":")[2]
                            namevar = namevar.split()
                            ende = len(namevar)
                            for i in range(0, ende):
                                NAME = NAME + '-' + namevar[i]
                            try:
                                print(variables[NAME])
                            except:
                                print("ERREUR 6 VARIABLE N'EXISTE PAS")
                        except:
                            print("ERREUR 6 VARIABLE NON DEFINIE !")
                    else:
                        namevar = ligne.partition(":")[2]
                        namevar = namevar.split()
                        ende = len(namevar)
                        stop = 100000
                        NAME = ''
                        STOCK = ''
                        if namevar[0] == '=':
                            print("ERREUR 6 NOM DE VARIABLE NON DEFINIE")
                        else:
                            for i in range(0, ende):
                                if namevar[i] == '=':
                                    stop = i
                                elif stop < i:
                                    pass
                                else:
                                    NAME = NAME + '-' + namevar[i]
                            for i in range(0, ende):
                                if i <= stop:
                                    pass
                                elif stop + 1 == i:
                                    STOCK = STOCK + namevar[i]
                                else:
                                    STOCK = STOCK + ' ' + namevar[i]
                            try:
                                variables[NAME] = STOCK
                            except:
                                print("ERREUR ?? : erreur inconnue")
                                
                except:
                    print("ERREUR 6 VARIABLE N'A PAS DE DEFINITION")
            else:
                pass
        else:
            if "if" in ligne:
                if bon == True:
                    pass
                else:
                    v = ligne.partition("if")[2]
                    print("ERREUR 3 : On est pas en Angleterre ici ! Pour si :"," si " + v)
                    bon = True
            if "print" in ligne:
                if bon == True:
                    pass
                else:
                    v = ligne.partition("print")[2]
                    print("ERREUR 3 : On est pas en Angleterre ici ! Pour montrer :"," montre " + v)
                    bon = True
            if "output" in ligne:
                if bon == True:
                    pass
                else:
                    v = ligne.partition("output")[2]
                    print("ERREUR 3 : On est pas en Angleterre ici ! Pour montrer :"," montre " + v)
                    bon = True
            if "operat" in ligne:
                if bon == True:
                    pass
                else:
                    v = ligne.partition(" ")[2]
                    print("ERREUR 3 : On est pas en Angleterre ici ! Pour calcul :"," calcul " + v)
                    bon = True
            if "exit" in ligne:
                if bon == True:
                    pass
                else:
                    print("ERREUR 3 : On est pas en Angleterre ici ! Pour sortir :"," sortir")
                    bon = True
            if "calcul" in ligne:
                bon = True
                pass
            else:
                if bon == True:
                    pass
                else:
                    print("Uh , je n'arrive pas a déterminer ce que fait cette commande : " + ligne)
                
if ".cccp" in file:
    lignes = []
    if os.path.isfile(file):
        with open(file, "r") as f:
            for index, value in enumerate(f.readlines()):
                lignes.append(value.strip("\n"))
                lignes = [i for i in lignes if i] 
            scan(lignes)
    else:
        lignes.append(file)
        scan(lignes)
    
else:
    lignes = []
    lignes.append(file)
    scan(lignes)

lignes = []
   
while True:
    file = input(">>>")
    lignes = []
    if ".cccp" in file:
        lignes = []
        if os.path.isfile(file):
            with open(file, "r") as f:
                for index, value in enumerate(f.readlines()):
                    lignes.append(value.strip("\n"))
                    lignes = [i for i in lignes if i] 
                scan(lignes)
        else:
            lignes.append(file)
            scan(lignes)
    else:
        lignes.append(file)
        scan(lignes)
