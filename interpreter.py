import sys
import os.path
import time
import re

print("STALINIUM V1 PAR ALEXDIEU")

if len(sys.argv) > 1:
    file = sys.argv[1]
    if not os.path.isfile(file):
        print("Error, File doesn't exist!")
        sys.exit(1)
else:
    file = input(">>>")

variables = {}

def lts(a):
    return ' '.join(a)

def CHEZCFIRST(mot, ligne):
    prem = ligne.partition(mot)[0]
    if prem.isspace() or prem == '':
        return True
    else:
        return False

def calc(ligne: list) -> str:
    try:
        op = ligne[2]
        left = float(ligne[1])
        right = float(ligne[3])
        if op == "+":
            return str(left + right)
        elif op == "-":
            return str(left - right)
        elif op == "*":
            return str(left * right)
        elif op == "/":
            return str(left / right)
        elif op == "**":
            return str(left ** right)
        elif op == "//":
            return str(left % right)  # Note: Changed to % as per original intent, but // typically floor div
        else:
            return check_if(ligne)
    except IndexError:
        try:
            expr = ligne[1]
            if "+" in expr:
                prems, _, sec = expr.partition("+")
                ope = "+"
            elif "-" in expr:
                prems, _, sec = expr.partition("-")
                ope = "-"
            elif "*" in expr:
                prems, _, sec = expr.partition("*")
                ope = "*"
            elif "/" in expr:
                prems, _, sec = expr.partition("/")
                ope = "/"
            elif "**" in expr:
                prems, _, sec = expr.partition("**")
                ope = "**"
            elif "//" in expr:
                prems, _, sec = expr.partition("//")
                ope = "//"
            else:
                return "ERREUR 2, Opérateur inconnu ! : " + ' '.join(ligne)
            return "ERREUR 1, les nombres doivent être espacés de l'opérateur comme ça : " + prems + " " + ope + " " + sec
        except:
            return "ERREUR 7 : AUCUN CALCUL DONNE"
    except ValueError:
        return "ERREUR 4 : Valeurs non numériques pour l'opération"

def check_if(ligne: list) -> str:
    args = ligne[1:]
    if len(args) != 3:
        return "ERREUR 7 AUCUNE CONDITION DONNE"
    try:
        left = float(args[0])
        right = float(args[2])
        op = args[1]
        if op == "?=":
            return "Vrai" if left == right else "Faux"
        elif op == "<":
            return "Vrai" if left < right else "Faux"
        elif op == ">":
            return "Vrai" if left > right else "Faux"
        elif op == "<=":
            return "Vrai" if left <= right else "Faux"
        elif op == ">=":
            return "Vrai" if left >= right else "Faux"
        elif op == "!=":
            return "Vrai" if left != right else "Faux"
        else:
            return "ERREUR 2, Opérateur inconnu ! : " + op
    except ValueError:
        left = args[0]
        right = args[2]
        op = args[1]
        if op == "?=":
            return "Vrai" if left == right else "Faux"
        elif op == "!=":
            return "Vrai" if left != right else "Faux"
        else:
            return "ERREUR 4 : Opérateur de comparaison nécessite des nombres ou ?= / !="

def scan(lignes: list):
    for ligne in lignes:
        bon = False
        split_ligne = ligne.split()
        if CHEZCFIRST("montre", ligne):
            lit = " ".join(split_ligne[1:])
            if ":" in lit:
                check = lit.partition(":")[0]
                if check and check[-1] == "\\":
                    pass
                else:
                    erreurs = 0
                    erreur = []
                    erN = []
                    name = lit.partition(":")[2].split()
                    NAME = ''
                    NAMEV = ''
                    ende = len(name)
                    for i in range(ende):
                        NAME += '-' + name[i]
                        if i == 0:
                            NAMEV = ':' + name[i]
                        else:
                            NAMEV += ' ' + name[i]
                        if NAME in variables:
                            erreurs += 1
                            erreur.append(NAME)
                            erN.append(NAMEV)
                    ni = False
                    if erreurs == 0:
                        ni = True
                        print("ERREUR 6 : VARIABLE N'EXISTE PAS")
                    if erreurs == 1:
                        ni = True
                        val = variables[erreur[0]]
                        lit = lit.replace(erN[0], val, 1)
                    if erreurs == 2:
                        ni = True
                        print("ATTENTION : DEUX VARIABLES ONT UN NOM SIMILIAIRE AU DEBUT : " + erN[0] + " et " + erN[1] + " ! STALINIUM prends la première par défault ! ")
                        val = variables[erreur[0]]
                        lit = lit.replace(erN[0], val, 1)
                    elif erreurs > 2:
                        ni = True
                        print("ATTENTION : PLUSIEURS VARIABLES ONT UN NOM SIMILIAIRE AU DEBUT ! STALINIUM prends la première par défault ! ")
                        val = variables[erreur[0]]
                        lit = lit.replace(erN[0], val, 1)
            if "\\:" in lit:
                lit = lit.replace("\\:", ":")
            print(lit)
            bon = True
        if CHEZCFIRST("calcul", ligne):
            print(calc(split_ligne))
            bon = True
        if CHEZCFIRST("si", ligne):
            print(check_if(split_ligne))
            bon = True
        if CHEZCFIRST("sortir", ligne):
            prem = ligne.partition("sortir")[0]
            sec = ligne.partition("sortir")[2]
            if (prem.isspace() or prem == '') and (sec.isspace() or sec == ''):
                sys.exit(0)
        if CHEZCFIRST("dors", ligne):
            try:
                bon_sleep = int(split_ligne[1])
                listDORS = split_ligne.copy()
                listDORS.remove("dors")
                listDORS.remove(split_ligne[1])
                arg = lts(listDORS)
                if arg:
                    print(arg)
                time.sleep(bon_sleep)
                bon = True
            except (IndexError, ValueError):
                print("ERREUR 3 : Mauvaise SYNTAXE pour DORS : DORS + TEMPS // exemple : dors 2")
        if CHEZCFIRST("pause", ligne):
            sec = ligne.partition("pause")[2].lstrip()
            if sec:
                input(sec + "...")
            else:
                input("Pause ...")
            bon = True
        if ":" in ligne and not bon:
            verif = ligne.partition(":")[0]
            if verif.isspace() or verif == '':
                try:
                    verif2 = ligne.partition("=")[2]
                    if verif2.isspace() or verif2 == '':
                        namevar = ligne.partition(":")[2].split()
                        NAME = ''
                        ende = len(namevar)
                        for i in range(ende):
                            NAME += '-' + namevar[i]
                        try:
                            print(variables[NAME])
                        except KeyError:
                            print("ERREUR 6 VARIABLE N'EXISTE PAS")
                    else:
                        namevar = ligne.partition(":")[2].split()
                        ende = len(namevar)
                        stop = ende
                        NAME = ''
                        STOCK = ''
                        if namevar[0] == '=':
                            print("ERREUR 6 NOM DE VARIABLE NON DEFINIE")
                        else:
                            for i in range(ende):
                                if namevar[i] == '=':
                                    stop = i
                                    break
                                NAME += '-' + namevar[i]
                            for i in range(stop + 1, ende):
                                if STOCK:
                                    STOCK += ' ' + namevar[i]
                                else:
                                    STOCK = namevar[i]
                            variables[NAME] = STOCK
                except:
                    print("ERREUR 6 VARIABLE N'A PAS DE DEFINITION")
                bon = True
        if not bon:
            if "if" in ligne:
                v = ligne.partition("if")[2]
                print("ERREUR 3 : On est pas en Angleterre ici ! Pour si :", " si " + v)
            elif "print" in ligne or "output" in ligne:
                key = "print" if "print" in ligne else "output"
                v = ligne.partition(key)[2]
                print("ERREUR 3 : On est pas en Angleterre ici ! Pour montrer :", " montre " + v)
            elif "operat" in ligne:
                v = ' '.join(ligne.split()[1:])
                print("ERREUR 3 : On est pas en Angleterre ici ! Pour calcul :", " calcul " + v)
            elif "exit" in ligne:
                print("ERREUR 3 : On est pas en Angleterre ici ! Pour sortir :", " sortir")
            else:
                print("Uh , je n'arrive pas a déterminer ce que fait cette commande : " + ligne)

lignes = []
try:
    with open(file, "r") as f:
        lignes = [line.strip("\n") for line in f.readlines() if line.strip("\n")]
except:
    lignes = [file]

scan(lignes)

while True:
    file = input(">>>")
    lignes = []
    try:
        with open(file, "r") as f:
            lignes = [line.strip("\n") for line in f.readlines() if line.strip("\n")]
    except:
        lignes = [file]
    scan(lignes)
