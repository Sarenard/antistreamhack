# c'est le bot utilisé par tous

import requests
import time
import threading
from discord_webhook import DiscordWebhook
from datetime import datetime

liste_tdc = set([])
urls = []  # les webhooks ici
liste_allemands = set([
    "arfore", "tellybridger", "austriangamingg", "blizzor",
    "caravasyt", "castcrafter", "nxtfake" "realbenex", "stegi", "Fabo",
    "tjantv", "verweisunq", "wichtiger", "x_sus", "xlymex", "zombiezocktyt",
    "priimme", "Trustcn", "xpieps_"])
liste_esp = set([
    "aurigas", "axozer", "barcagamer", "bobicraftmc", "cibergun",
    "conterstine", "crisgreen", "esvandal", "geramc", "giaantv", "hasvik",
    "icraktv", "lakshartnia", "luh", "mayichi", "serpias", "shadoune666",
    "suwie", "soypandih"])
liste_ita = set([
    "dere_x", "francycoso", "giankoextreme", "giacomoinsano",
    "guerrareturns", "iskandert", "micha3l_tv", "sonomrdomi", "MICHA3L_tv",
    "napo7700", "nolifegabbo", "nonsonolink", "nonsonolink", "novaxciv",
    "tech4play", "triton_707", "ultimateita", "alphatvlive"])
liste_US = set([
    "a6doff", "antfrost", "bekyamon", "brumin", "golriver__", "graecie",
    "ragetrain", "reddoons", "velvetiscake", "sammygreen", "realsdslayer",
    "seapeekay", "spideyarmy", "spifeyy", "theorionsound", "tryhord_",
    "turbopiggyyt", "vgumiho", "vrax", "zachplaysanlive"])
liste_france = set([
    "aypierre", "bichard", "frigiel", "fukano", "fuzeiii", "guep",
    "jimmyboyyy", "mathieulapin", "luccio", "magicknup", "mathox", "nems",
    "niimbustv", "ninjaxxu", "nino_mssclick", "redtoxx_", "soulravenn",
    "thatdamngirll", "theguill84", "tityyy"])
time.sleep(2)


def check(streamer, nb):
    _temp = set(requests.get(
        "https://tmi.twitch.tv/group/user/" + streamer + "/chatters?v=" +
        str(nb)).text.split('"viewers":[')[1].split('","'))
    _al = ("ALLEMAND", list(liste_allemands.intersection(_temp)))
    _es = ("ESPAGNOL", list(liste_esp.intersection(_temp)))
    _it = ("ITALIEN", list(liste_ita.intersection(_temp)))
    _us = ("RICAIN", list(liste_US.intersection(_temp)))
    for _nation in list(filter(lambda x: x, [_al, _es, _it, _us])):
        for _hack in _nation[1]:
            _msg = str(datetime.now()) + " : " + _hack + " streamhack " + \
            streamer + " (ça veut pas forcément dire streamhack, ils peuvent \
                 être amis...) c'est un " + _nation[0]
            # print(_msg)
            if nb % 60 == 0:
                liste_tdc.clear()
            liste_tdc.add(_hack)
            for url in urls:
                DiscordWebhook(url=url, content=_msg).execute()
            token = "Mot de passe API"
            data = {
                    "token": token,
                    "team": _nation[0],
                    "pseudo": _hack,
                    "streamer": streamer,
                    }
            print(requests.post(
                "https://dadodasyra.fr/city/api/streamhack.php",
                data=data).text)

nb = 0
while True:
    nb += 1
    print(
        str(datetime.now()) + " boucle numéro :", nb, "ça fait", nb/60,
        "heures que le bot tourne")
    for streamer in liste_france:
        x = threading.Thread(target=check, args=(streamer, nb), daemon=True)
        x.start()
    time.sleep(60)
