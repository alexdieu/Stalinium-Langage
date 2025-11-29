import sys
import os
import time
import operator

class StaliniumInterpreter:
    def __init__(self):
        self.variables = {}
        self.running = True
        self.ops = {
            "+": operator.add, "-": operator.sub, "*": operator.mul,
            "/": operator.truediv, "**": operator.pow, "//": operator.mod,
            "%": operator.mod,
        }
        self.comparators = {
            "?=": operator.eq, "!=": operator.ne, "<": operator.lt,
            ">": operator.gt, "<=": operator.le, ">=": operator.ge
        }

    def normalize_var_name(self, name_parts):
        """Converts ['my', 'var'] to '-my-var' to match original behavior."""
        return "-" + "-".join(name_parts)

    def resolve_variables(self, text):
        """Replaces variables in a string with their values."""
        if ":" not in text:
            return text

        words = text.split()
        resolved_words = []
        i = 0
        while i < len(words):
            word = words[i]
            if word.startswith(":") and not word.startswith("\\:"):
                match_found = False
                for length in range(len(words) - i, 0, -1):
                    potential_name_parts = words[i:i+length]
                    potential_name_parts[0] = potential_name_parts[0][1:]
                    key = self.normalize_var_name(potential_name_parts)
                    
                    if key in self.variables:
                        resolved_words.append(str(self.variables[key]))
                        i += length
                        match_found = True
                        break
                
                if not match_found:
                    resolved_words.append(word)
                    i += 1
            else:
                resolved_words.append(word.replace("\\:", ":"))
                i += 1
        return " ".join(resolved_words)

    def cmd_montre(self, args):
        text = " ".join(args)
        print(self.resolve_variables(text))

    def cmd_calcul(self, args):
        if len(args) < 3:
            return "ERREUR 7 : AUCUN CALCUL DONNE"
        try:
            left, op, right = float(args[0]), args[1], float(args[2])
            if op in self.ops:
                return str(self.ops[op](left, right))
            return f"ERREUR 2, Opérateur inconnu ! : {op}"
        except ValueError:
            return "ERREUR 4 : Valeurs non numériques"
        except ZeroDivisionError:
            return "ERREUR: Division par zéro"

    def cmd_si(self, args):
        if len(args) != 3:
            return "ERREUR 7 AUCUNE CONDITION DONNE"
        try:
            left, op, right = args[0], args[1], args[2]
            try:
                left = float(left)
                right = float(right)
            except ValueError:
                pass 
                
            if op in self.comparators:
                return "Vrai" if self.comparators[op](left, right) else "Faux"
            return f"ERREUR 2, Opérateur inconnu ! : {op}"
        except Exception as e:
            return f"ERREUR INTERNE: {e}"

    def cmd_dors(self, args):
        if not args:
            return "ERREUR 3 : Mauvaise SYNTAXE pour DORS"
        try:
            duration = int(args[0])
            if len(args) > 1:
                print(" ".join(args[1:]))
            time.sleep(duration)
        except ValueError:
            return "ERREUR 3 : Le temps doit être un entier"

    def cmd_pause(self, args):
        msg = " ".join(args) if args else "Pause ..."
        input(msg + "...")

    def cmd_sortir(self, args):
        self.running = False

    def handle_assignment(self, line):
        """Handles variable assignment line like ':var name = value'."""
        try:
            left_side, _, right_side = line.partition('=')
            name_parts = left_side.strip().split()

            if name_parts[0].startswith(':'):
                name_parts[0] = name_parts[0][1:]
            
            key = self.normalize_var_name(name_parts)
            value = right_side.strip()
            
            if not value:
                if key in self.variables:
                    print(self.variables[key])
                else:
                    print("ERREUR 6 VARIABLE N'EXISTE PAS")
            else:
                self.variables[key] = value
        except Exception:
            print("ERREUR 6 VARIABLE N'A PAS DE DEFINITION VALIDE")

    def execute_line(self, line):
        line = line.strip()
        if not line: return

        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]
        
        commands = {
            "montre": self.cmd_montre,
            "calcul": lambda a: print(self.cmd_calcul(a)),
            "si": lambda a: print(self.cmd_si(a)),
            "dors": self.cmd_dors,
            "pause": self.cmd_pause,
            "sortir": self.cmd_sortir
        }

        if cmd in commands:
            commands[cmd](args)
        elif line.startswith(":"):
            self.handle_assignment(line)
        else:
            if cmd == "print": print("ERREUR 3 : On est pas en Angleterre ici ! Pour montrer : montre ...")
            elif cmd == "if": print("ERREUR 3 : On est pas en Angleterre ici ! Pour si : si ...")
            elif cmd == "exit": print("ERREUR 3 : On est pas en Angleterre ici ! Pour sortir : sortir")
            else: print(f"Commande inconnue : {cmd}")

    def run_file(self, filename):
        if not os.path.isfile(filename):
            print("Error, File doesn't exist!")
            return

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if not self.running: break
            self.execute_line(line)

def main():
    print("STALINIUM V2 (OPTIMIZED)")
    interpreter = StaliniumInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        while True:
            try:
                file = input(">>> ")
                interpreter.running = True
                interpreter.run_file(file)
            except KeyboardInterrupt:
                print("\nAu revoir, Camarade!")
                break
            except Exception as e:
                print(f"Erreur critique: {e}")

if __name__ == "__main__":
    main()
