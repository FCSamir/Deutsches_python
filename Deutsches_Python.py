
import logging
from colorama import Fore, Style
from tkinter import *
import matplotlib.pyplot as plt
import pygame
import random
# Konfiguriere das Logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

"""Ein Modul, mit Deutschen Python Befehlen!"""

class Errors:
    def __init__(self, error):
        """
        Initialisiert die Errors-Klasse mit einem Fehler.

        :param error: Der Fehler, der behandelt werden soll.
        """
        self.error = error

   
    def run(self):
        """
        Funktion, die die Fehlermeldungen in Deutsch anzeigt.
        """
        run = "running"
        while run == "running":
            if ModuleNotFoundError:
                error_message = "❌❌ Modul nicht gefunden! ❌❌ ‼️ vielleicht musst du im Terminal das Modul installieren!‼️"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif IndexError:
                error_message = "❌❌ Index Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif MemoryError:
                error_message = "❌❌ Speicher Fehler aufgetreten ❌❌ ‼️ Entferne ein paar Objekte!‼️"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif OverflowError:
                error_message = "❌❌ Überlauf Fehler aufgetreten ❌❌ !! Versuche es mit kleineren Zahlen !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif RecursionError:
                error_message = "❌❌ Rekursions Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
               
            elif SyntaxError:
                error_message = "❌❌ Syntax Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif TabError:
                error_message = "❌❌ Tab Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif TypeError:
                error_message = "❌❌ Typ Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif ValueError:
                error_message = "❌❌ Wert Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif ZeroDivisionError:
                error_message = "❌❌ Division durch null geht nicht ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif NameError:
                error_message = "❌❌ Name Fehler aufgetreten ❌❌ !! Definiere die Funktion oder die Variable vor dem Aufruf !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            elif FileNotFoundError:
                error_message = "❌❌ Datei nicht gefunden ❌❌ !! Benenne die gemeinte Datei richtig um oder erstelle sie !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
            else:
                print(Fore.GREEN + "✅✅ Keine Fehler gefunden! ✅✅" + Style.RESET_ALL)
                break

    def stoprun(self):
        """
        Funktion, die das Programm beendet sobald ein Fehler auftritt.
        """
        stop = "stop"
        while stop == "stop":
            if ModuleNotFoundError:
                error_message = "❌❌ Modul nicht gefunden! ❌❌ ‼️ vielleicht musst du im Terminal das Modul installieren!‼️"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif IndexError:
                error_message = "❌❌ Index Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif MemoryError:
                error_message = "❌❌ Speicher Fehler aufgetreten ❌❌ ‼️ Entferne ein paar Objekte!‼️"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif OverflowError:
                error_message = "❌❌ Überlauf Fehler aufgetreten ❌❌ !! Versuche es mit kleineren Zahlen !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif RecursionError:
                error_message = "❌❌ Rekursions Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif SyntaxError:
                error_message = "❌❌ Syntax Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif TabError:
                error_message = "❌❌ Tab Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif TypeError:
                error_message = "❌❌ Typ Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif ValueError:
                error_message = "❌❌ Wert Fehler aufgetreten ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif ZeroDivisionError:
                error_message = "❌❌ Division durch null geht nicht ❌❌"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif NameError:
                error_message = "❌❌ Name Fehler aufgetreten ❌❌ !! Definiere die Funktion oder die Variable vor dem Aufruf !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break
            elif FileNotFoundError:
                error_message = "❌❌ Datei nicht gefunden ❌❌ !! Benenne die gemeinte Datei richtig um oder erstelle sie !!"
                print(Fore.RED + error_message + Style.RESET_ALL)
                logging.error(error_message)
                
                break

    def stopastoprun(self):
        """
        Funktion, die stoprun() Funktion stoppt.
        """
        stop = "stopped"

    def stoparun(self):
        """
        Funktion, die run() Funktion stoppt.
        """
        run = "stopped"
class Funktionen:
    def __init__(self):
        pass
    def zeige(self, Text):
        """
        Funktion, die den Text anzeigt.
        """
        print(Text)
    def Frage(self, Text):
        """
        Funktion, die etwas abfragt. (input())
        """
        input(Text)
    def in_grossbuchstaben_umwandeln(self, Text):
        """
        Funktion, die den Text in Großbuchstaben umwandelt.
        """
        return Text.upper()
    def in_kleinbuchstaben_umwandeln(self, Text):
        """
        Funktion, die den Text in Kleinbuchstaben umwandelt.
        """
        return Text.lower()
    def text_länge(self, Text):
        """
        Funktion, die die Textlänge anzeigt.
        """
        return len(Text)
    def caesar_verschluesseln(text, shift):
        """
        Funktion, die den Text mit einer Caesar-Verschlüsselung verschlüsselt.
    
        :param text: Der zu verschlüsselnde Text.
        :param shift: Die Anzahl der Stellen, um die jeder Buchstabe verschoben wird.
        :return: Der verschlüsselte Text.
        """
        verschluesselt = ""
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                verschluesselt += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                verschluesselt += char
        return verschluesselt
    def caesar_entschluesseln(text, shift):
        """
        Funktion, die den Text mit einer Caesar-Verschlüsselung entschlüsselt.
        
        :param text: Der zu entschlüsselnde Text.
        :param shift: Die Anzahl der Stellen, um die jeder Buchstabe verschoben wurde.
        :return: Der entschlüsselte Text.
        """
        return caesar_verschluesseln(text, -shift)
    def text_zu_zahlen_verschluesseln(self, text):
        """
        Funktion, die den Text in Zahlen verschlüsselt.
        
        :param text: Der zu verschlüsselnde Text.
        :return: Der verschlüsselte Text.
        """
        return " ".join(str(ord(char)) for char in text)
    def zahlen_zu_text_entschluesseln(self, text):
        """
        Funktion, die den Text aus Zahlen entschlüsselt.
        """
        return "".join(chr(int(char) for char in text.split()))
    def TextInKasten(self, Text, einezeileauslassen=True, Linkezeichen="|", Rechtezeichen="|", oberezeichen="-", unterezeichen="-"):
        """
        Funktion, die den Text in einen Kasten setzt.
        """
        if einezeileauslassen:
            print(oberezeichen * len(Text))
            print("")
            print(Linkezeichen + Text + Rechtezeichen)
            print("")
            print(unterezeichen * len(Text))
        else:
            print(oberezeichen * len(Text))
            print(Linkezeichen + Text + Rechtezeichen)
            print(unterezeichen * len(Text))
class tkinterfunktionen:
    def __init__(self):
        self.root = Tk()
    def fenstertitel(self, titel):
        """
        Funktion, die den Fenstertitel setzt.
        """
        self.root.title(titel)
    def fenstergroesse(self, breite, hoehe):
        """
        Funktion, die die Fenstergröße setzt.
        """
        self.root.geometry(f"{breite}x{hoehe}")
    def fenster(self):
        """
        Funktion, die das Fenster anzeigt.
        """
        self.root.mainloop()
    def schliessen(self):
        """
        Funktion, die das Fenster schließt.
        """
        self.root.quit()
    def label(self, text):
        """
        Funktion, die ein Label anzeigt.
        """
        label = Label(self.root, text=text)
    def allesPacken(self):
        """
        Funktion, die alles packt.
        """
        self.root.pack()
    def button(self, text):
        """
        Funktion, die einen Button anzeigt.
        """
        button = Button(self.root, text=text)
    def kannGeklicktWerden(self):
        """
        Funktion, die den Button klickbar macht.
        """
        button.pack()
    def kasten_erstellen(self):
        """
        Funktion, die einen Kasten erstellt.
        """
        frame = Frame(self.root)
class pltfunktionen:
    def __init__(self):
        """Achtung: Diese Funktionen benötigen das Modul matplotlib!
        in terminal: pip install matplotlib
        sonst wird ein Fehler auftreten!"""
        pass
    def plot(self, x, y):
        """
        Funktion, die ein Diagramm erstellt.
        """
        plt.plot(x, y)
    def anzeigen(self):
        """
        Funktion, die das Diagramm anzeigt.
        """
        plt.show()
    def speichern(self, name):
        """
        Funktion, die das Diagramm speichert.
        """
        plt.savefig(name)
class Pygamefunktionen:
    def __init__(self):
        """Achtung: Diese Funktionen benötigen das Modul pygame!
        in terminal: pip install pygame
        sonst wird ein Fehler auftreten!"""
        pass
    def init(self):
        """
        Funktion, die Pygame initialisiert.
        """
        pygame.init()
    def fenster(self, breite, hoehe):
        """
        Funktion, die das Fenster erstellt.
        """
        screen = pygame.display.set_mode((breite, hoehe))
    def farbe(self, farbe):
        """
        Funktion, die die Farbe setzt.
        """
        return pygame.Color(farbe)
    def hintergrundfarbe(self, farbe):
        """
        Funktion, die die Hintergrundfarbe setzt.
        """
        screen.fill(farbe)
    def anzeigen(self):
        """
        Funktion, die das Fenster anzeigt.
        """
        pygame.display.flip()
    def schliessen(self):
        """
        Funktion, die das Fenster schließt.
        """
        pygame.quit()
    def text(self, text, x, y, farbe):
        """
        Funktion, die den Text anzeigt.
        """
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, farbe)
        screen.blit(text, (x, y))
    def rechteck(self, farbe, x, y, breite, hoehe):
        """
        Funktion, die ein Rechteck anzeigt.
        """
        pygame.draw.rect(screen, farbe, (x, y, breite, hoehe))
    def kreis(self, farbe, x, y, radius):
        """
        Funktion, die einen Kreis anzeigt.
        """
        pygame.draw.circle(screen, farbe, (x, y), radius)
    def linie(self, farbe, x1, y1, x2, y2):
        """
        Funktion, die eine Linie anzeigt.
        """
        pygame.draw.line(screen, farbe, (x1, y1), (x2, y2))
    def bild(self, bild, x, y):
        """
        Funktion, die ein Bild anzeigt.
        """
        screen.blit(bild, (x, y))
    def bild_laden(self, bild):
        """
        Funktion, die ein Bild lädt.
        """
        return pygame.image.load(bild)
class randomFunktionen:
    def init(self):
        """
        Funktion, die random initialisiert.
        """
        pass
    def zufallszahl(self, min, max):
        """
        Funktion, die eine Zufallszahl generiert.
        """
        return random.randint(min, max)
    def zufallsliste(self, liste):
        """
        Funktion, die eine Zufallsliste generiert.
        """
        return random.choice(liste)
    def zufallsfarbe(self):
        """
        Funktion, die eine Zufallsfarbe generiert.
        """
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def zufallswort(self, wort):
        """
        Funktion, die ein Zufallswort generiert.
        """
        return random.choice(wort)

    