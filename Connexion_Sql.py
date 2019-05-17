# Initialisation des librairies/modules
import sys
import time
import MySQLdb
import socket
import Connexion

from PIL import Image
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

# # # # # # # # #Definition du code


class Conn:
    def __init__(self, ip_bdd, pnom, plargeur, phauteur, pextrainfo = "" ):
        localhost = "127.0.0.1"
        SRV_NAO = "192.168.0.19"
        db = MySQLdb.connect(host=ip_bdd,  # your host
                             user="olivier",  # username
                             passwd="olivier",  # password
                             db="olivier")  # name of the database

        # Create a Cursor object to execute queries.
        self.cur = db.cursor()

        # Select data from table using SQL query.
        if (pnom != "") and (plargeur != "") and (phauteur != ""):
            if pextrainfo == "":
                plargeur_max = plargeur + 0.015
                plargeur_min = plargeur - 0.015
                phauteur_max = phauteur + 0.015
                phauteur_min = phauteur - 0.015
                req = ("SELECT `InfoPersonne`, `idFaciale`, `Largeur_Visage`, `Hauteur_Visage`,"
                       " `Extra_Info`, `idApprenant`, `idProfesseur` "
                       " FROM `faciale` WHERE `InfoPersonne` = '" + pnom + "'"
                       " AND `Largeur_Visage` < %.3f AND `Largeur_Visage` > %.3f"
                       " AND `Hauteur_Visage` < %.3f AND `Hauteur_Visage` > %.3f") % (plargeur_max, plargeur_min, phauteur_max, phauteur_min)
                print req
                self.cur.execute(req)
            else:
                self.cur.execute("SELECT `InfoPersonne`, `idFaciale`, `Largeur_Visage`, `Hauteur_Visage`,"
                                 "`Extra_Info`, `idApprenant`, `idProfesseur` "
                                 "FROM `faciale` WHERE `InfoPersonne` = '" + pnom + "' AND `Largeur_Visage` = '" + plargeur + "' AND `Hauteur_Visage` = '" + phauteur + "' AND `Extra_Info` = '" + pextrainfo + "' ")

    def InsertInfo(self, pnom, plargeur, phauteur, pextrainfo = ""):
        self.cur.execute("INSERT INTO faciale(`InfoPersonne`,`Largeur_Visage`, `Hauteur_Visage`, `Extra_Info` ,`idApprenant` ,`idProfesseur`) "
                         "VALUES (pnom, plargeur, phauteur, pextrainfo, idApprenant, idProfesseur)")

    def RecupVal(self, num_col=-1):
        i = 0
        rc = self.cur.rowcount
        val = ""
        for row in self.cur.fetchall():
            while i < rc:
                if val == "":
                    val = row[i]
                else:
                    val = val + "," + row[i]
                i += 1
        return val