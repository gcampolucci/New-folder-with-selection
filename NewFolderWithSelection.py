#! /usr/bin/python3 -OOt
import sys
import os
import shutil


# Lista vuota per la memorizzazione dei files selezionati
sel_files = []

# Inserimento dei files selezionati nella lista
# I files selezionati sono memorizzati nel primo parametro
# (il primo parametro è il nome dello script) come una
# unica stringa. I files sono tra doppi apici e separati da un singolo carattere vuoto
# esempio: "/home/user/file1" "/home/user/file2"
for i in sys.argv[1:]:
    sel_files.append(i)


# Directory comune tra i files selezionati
commonPath = os.path.commonpath(sel_files)
# Nome di default della nuova directory
newFolder = "New Folder with items"
# Nuova directory dove verranno spostati i files selezionati
commonPath = os.path.join(commonPath,newFolder)

# Contatore cartella
x = 1
# Stringa per contatore cartella
s = ""

# se la cartella esiste verranno provati nomi incrementati di 1...esempio:
#  New Folder with items
#  New Folder with items (2)
#  New Folder with items (3)
while os.path.isdir(commonPath + s):
    # viene incrementato il contatore
    x = x + 1
    s = " (" + str(x) + ")"
else:
    # la nuova cartella viene creata
    os.makedirs(commonPath + s)
    # i files vengono spostati nella nuova cartella
    for i in sel_files:
        shutil.move(i, commonPath + s)
