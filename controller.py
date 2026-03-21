import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def verfica_lingua_scelta(self, e):
        language = e.control.value
        if language is not None:
            self._view._lvOut.controls.append(
                ft.Text(f"Language correctly set to: {language}", color="green"))
        self._view.update()

    def verfica_modalita_scelta(self, e):
        mod = e.control.value
        if mod is not None:
            self._view._lvOut.controls.append(
                ft.Text(f"Modality correctly set to: {mod}", color="green"))
        self._view.update()

    def handleSpellCheck(self, e):
        lingua = self._view._ddLingua.value
        modalita= self._view._ddModalita.value
        testo = self._view._txtInFrase.value

        if not lingua:
            self._view._lvOut.controls.append(
                ft.Text(f"Devi scegliere una lingua", color="red"))
            self._view.update()
            return

        if not modalita:
            self._view._lvOut.controls.append(
                ft.Text(f"Devi scegliere una modalità", color="red"))
            self._view.update()
            return

        paroleErrate, tempo = self.handleSentence(testo, lingua, modalita)
        self._view._lvOut.controls.append(
            ft.Text(f"Frase inserita: {testo}"))
        self._view._lvOut.controls.append(
            ft.Text(f"Parole errate: {paroleErrate}"))
        self._view._lvOut.controls.append(
            ft.Text(f"Tempo richiesto dalla ricerca: {tempo}"))
        self._view.update()

        self._view._ddLingua.value = None
        self._view._ddModalita.value = None
        self._view._txtInFrase.value = ""  # ← stringa vuota per il TextField
        self._view.update()














def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

