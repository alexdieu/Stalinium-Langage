# Stalinium-Langage
Simple langage de programmation en FR , basé sur python3 

Ce langage est un langage très simple , avec pour l'instant 6 instructions :

- **MONTRE** , agit comme print() ca imprimera ce qu'il y a après SYNTAXE : ```montre Salut, Staline !```
- **CALCUL** , effectue n'importe quel calcul , ```+``` ```-```  ```/``` ```*``` ```**``` ```//``` exemple : ```calcul 4 // 4``` en python donnerait ```4%4```
- **SI** , retourne vrai ou faux en foction de la condition : ```?=``` ```!=``` ```<``` ```>``` ```<=``` ```>=``` exemple : ```si 4 ?= 5``` en python ca donnerait ```if 4 == 5```
- **SORTIR** , sors du code et de l'interpréteur ```SORTIR```
- **DORS** , attendre .  syntaxe : DORS secondes {optionnel : afficher quelquechose a la fin du temps} exemple:``` dors 4 ```Autre exemple: (l'argument de fin agi comme ```MONTRE```) ```dors 5 dormir 5 sec```
- **PAUSE** , attends que l'utilisateur tape la touche entrée pour continuer , syntaxe : pause {raison} exemple : ```pause``` ou ```pause ceci est une pause```
- ```:``` , definir une variable ou la montrer exemples : ```:D = SALUT/BONJOUR MON POTE : chuis de , bonne, humeur ! (:``` et pour la montrer : ```:D``` , sachez juste que quand votre variable est stockée , les espaces sont réinitialisés et donc cette instruction : ```:Fouoaoau oauaao  =  salut      mon    pote```, ca donnera : 
```
>>>:Fouoaoau oauaao
salut mon pote
```
POUR PLUS D'AIDE , REGARDEZ MAIN.CCCP ET VOUS COMPRENDREZ MIEUX LA SYNATXE

CE LANGAGE EST CREE DANS LE BUT D'AIDER A COMMENCER A DEVELOPPER , IL EST EXTREMENT SIMPLE , PASSEZ Y 20 MIN SI VOUS N'AVEZ JAMAIS TOUCHE UNE LIGNE DE CODE CELA POURRAIT VOUS AIDER A VOUS LANCER DANS VOTRE LANGAGE DE PROGRAMMATION

TESTEZ ONLINE : https://repl.it/@alexdieuveult/Stalinium-Langage#main.py

## DEBUG

Debug est un prog fait pour comprendre les erreurs dans le programme , comme dans l'interpréteur . Il faut s'y connaitre en python , et savoir les exceptions que l'on peut y rencontrer , pour les patcher . 
Par exemple , pour main.cccp :
```
C:\Urss\Stalin\projects\stalinium>python DEBUG.py main.cccp
STALINIUM DEBUGGER V1 PAR ALEXDIEU
montre Salut, STALINE!
Salut, STALINE!
calcul 3 ** 3
9
si 6 <= 8
Vrai
ron pisch
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
-D== name
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
= == 0
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
['D', '=', 'SALUT/BONJOUR', 'MON', 'POTE', ':', 'chuis', 'de', ',', 'bonne,', 'humeur', '!', '(:']
SALUT/BONJOUR
SALUT/BONJOUR MON == stock
SALUT/BONJOUR MON POTE == stock
SALUT/BONJOUR MON POTE : == stock
SALUT/BONJOUR MON POTE : chuis == stock
SALUT/BONJOUR MON POTE : chuis de == stock
SALUT/BONJOUR MON POTE : chuis de , == stock
SALUT/BONJOUR MON POTE : chuis de , bonne, == stock
SALUT/BONJOUR MON POTE : chuis de , bonne, humeur == stock
SALUT/BONJOUR MON POTE : chuis de , bonne, humeur ! == stock
SALUT/BONJOUR MON POTE : chuis de , bonne, humeur ! (: == stock
-D
{'-D': 'SALUT/BONJOUR MON POTE : chuis de , bonne, humeur ! (:'}
SALUT/BONJOUR MON POTE : chuis de , bonne, humeur ! (:
 aprÃ¨s ca je quitte le prog...
sortir
```
