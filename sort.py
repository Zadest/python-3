import os
from pathlib import Path

# Beispiel: Sortiere Dateinamen nach Dateiendung

def my_sorting_criteria(element):
    return element.split('.')[-1]

liste_aller_dateien = os.listdir(".")
sortierte_liste_dateinamen = liste_aller_dateien.sort(key=my_sorting_criteria)

print(sortierte_liste_dateinamen,sep="\n")