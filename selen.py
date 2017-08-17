# -*- coding: utf-8 -*-

import time

from application import Application
from lekarstvo import Lekarstvo

app = Application()

try:
    app.init_apteki()
    app.search_lekarstvo(Lekarstvo(name = "парацетамол"))
    time.sleep(5)
    app.search_apteki()
    app.search_lekarstvo(Lekarstvo(name = "нурофен"))
    time.sleep(5)
    app.search_apteki()
    app.city_apteka("Тольятти")
    #choice_togliatty()
    app.search_lekarstvo(Lekarstvo(name = "амиксин"))
    time.sleep(5)
    app.search_apteki()
    app.city_apteka("Самара")
    #choice_samara()
    app.search_lekarstvo(Lekarstvo(name = "аугментин"))
    time.sleep(5)
finally:
    app.quit()
