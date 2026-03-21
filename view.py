import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT # tema chiaro di default

        # Controller
        self.__controller = None

        # UI= user interface elements:gli elementi visivi che l'utente vede e usa
        #In Flet ogni elemento visivo è un "control".
        self.__title = None
        self.__theme_switch = None
        self._ddLingua = None # dropdown lingua
        self._ddModalita= None # dropdown modalità
        self._txtInFrase= None #frase da inserire
        self._btnCheck =None #bottone per partire
        self._lvOut = None #spazio bianco x stringhe

    def setController(self, controller):
        self.__controller = controller

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self._ddLingua =ft.Dropdown(label= "Select languages", expand=True,
                                    options=[ft.dropdown.Option("italian"),
                                             ft.dropdown.Option("english"),
                                             ft.dropdown.Option("spanish")],
                                    on_change= self.__controller.verfica_lingua_scelta)
        row1 = ft.Row(controls=[self._ddLingua])

        self._ddModalita= ft.Dropdown(label= "Search Modality", width=200,
                                    options=[ft.dropdown.Option("Default"),
                                             ft.dropdown.Option("Linear"),
                                             ft.dropdown.Option("Dichotomic")],
                                    on_change= self.__controller.verfica_modalita_scelta)

        self._txtInFrase = ft.TextField(label="Add your sentence here", expand=True)

        self._btnCheck= ft.ElevatedButton(text= "Spell Check",
                                        on_click= self.__controller.handleSpellCheck,
                                        width=200)

        row2= ft.Row(spacing=5, controls=[self._ddModalita, self._txtInFrase, self._btnCheck],
                     alignment=ft.MainAxisAlignment.START)

        self._lvOut = ft.ListView(expand=1, #occupa tutto lo spazio verticale disponibile nella pagina (equivale a expand=True)
                                  spacing=10, #spazio in pixel tra un elemento e l'altro dentro la lista
                                  padding=5, #spazio interno di 20px tra il bordo della lista e il contenuto
                                  auto_scroll=True #scorre automaticamente verso il basso quando viene aggiunto nuovo contenuto
                                  )
        self.page.add(row1, row2, self._lvOut)
        self.page.update()

    def update(self):
        self.page.update()

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        # valore_se_vero if condizione else valore_se_falso
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        """In versione lunga:
            if self.page.theme_mode == ft.ThemeMode.LIGHT:
                self.page.theme_mode = ft.ThemeMode.DARK
            else:
                self.page.theme_mode = ft.ThemeMode.LIGHT"""

        self.__theme_switch.label = (
            "Light theme"
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else "Dark theme"
        )
        self._ddLingua.bgcolor = (
            ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        )
        self._ddModalita.bgcolor = (
            ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        )
        self._txtInFrase.bgcolor = (
            ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
