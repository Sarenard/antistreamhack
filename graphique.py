from discord_webhook import DiscordWebhook
import tkinter as tk
import threading
import requests
import time

fenetre=tk.Tk()
fenetre.title('ANTI STREAMHACK')
fenetre.geometry("1000x700+0+0")
fenetre.resizable(False, False)

webhook_texte = tk.Label(fenetre, text = "LIEN DU WEBHOOK ICI : ")
webhook_texte.pack()
webhook_texte.place(width = 800, height = 25, y = 10, x = 100)

webhook_entry = tk.Entry(fenetre)
webhook_entry.insert(0, "Lien du webhook ici")
webhook_entry.pack()
webhook_entry.place(width = 800, height = 25, y = 50, x = 100)


liste_streamers_texte = tk.Label(fenetre, text = "Liste des streamers a protéger du streamhack, séparés par des virgules, sans espaces : ")
liste_streamers_texte.pack()
liste_streamers_texte.place(width = 800, height = 25, y = 100, x = 100)

liste_streamers_entry = tk.Entry(fenetre)
liste_streamers_entry.insert(0, "Liste des streamers ici, séparés par des virgules, sans espaces")
liste_streamers_entry.pack()
liste_streamers_entry.place(width = 800, height = 100, y = 140, x = 100)


liste_streamackers_potentiels_texte = tk.Label(fenetre, text = "Liste des potentiels streamhackers, séparés par des virgules, sans espaces : ")
liste_streamackers_potentiels_texte.pack()
liste_streamackers_potentiels_texte.place(width = 800, height = 100, y = 240, x = 100)

liste_streamackers_entry = tk.Entry(fenetre)
liste_streamackers_entry.insert(0, "Liste des potentiels streamhackers, séparés par des virgules, sans espaces : ")
liste_streamackers_entry.pack()
liste_streamackers_entry.place(width = 800, height = 100, y = 340, x = 100)

def check(streamer):
    global liste_streamers
    global liste_streamackers
    global webhook_link
    liste_viewers = requests.get("https://tmi.twitch.tv/group/user/"+streamer+"/chatters").text.split('"viewers":[')[1].split('","')
    pseudo_du_streamhacker = ""
    for item in liste_streamackers:
        for x in liste_viewers:
            if item == x:
                pseudo_du_streamhacker = item
    truc_a_envoyer = pseudo_du_streamhacker + " streamhack " + streamer
    DiscordWebhook(url=webhook_link, content=truc_a_envoyer).execute()
    
def valider2():
    global liste_streamers
    global liste_streamackers
    global webhook_link
    liste_streamers = liste_streamers_entry.get().split(",")
    liste_streamackers = liste_streamackers_entry.get().split(",")
    webhook_link = webhook_entry.get()
    while True:
        for streamer in liste_streamers:
            x = threading.Thread(target=check, args=(streamer, ), daemon=True)
            x.start()
            time.sleep(60)
    
def valider():
    bouton_valider.configure(text="Programme lancé")
    threading.Thread(target=valider2, args=()).start()

bouton_valider = tk.Button(fenetre, text="Valider et lancer le programme", command=valider, background="red", activebackground="blue")
bouton_valider.pack()
bouton_valider.place(width = 400, height = 100, y = 460, x = 300)

fenetre.mainloop()
