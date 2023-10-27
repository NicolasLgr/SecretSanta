import random
from email.message import EmailMessage
import ssl
import smtplib

personne = [
    ["Nicolas LEGER", "nico.leger99@laposte.net"], 
    ["Maelys MOLLARD", "m.mollard5102@laposte.net"],
    ["Madeleine DOUBLET", "madeleine.doublet@yahoo.fr"],
    ["Antoine LESPINE", "antoine.lespine02@gmail.com"],
    ["Antoine SZUL", "anto.szul15@gmail.com"],
    ["Camille CACHON", "camillecachon@gmail.com"],
    ["Kevin HALLOUIN", "kevin.h.02@hotmail.fr"],
    ["Yoann DESRAYAUD", "desrayaudyoann@gmail.com"],
    ["Hugo BAUDOIN", "beaudoin.hugo1306@gmail.com"],
    ["Claire DUPRE", "claire.dupre4@gmail.com"],
    ["Theodore LANDI", "theodore-landi@hotmail.fr"],
    ["Floriane LETOURNEUR", "floriane.letourneur@gmail.com"],
    ["Pierre VILLOTEAU", "pierre.villoteau@hotmail.fr"],
    ]

liste_duo = []
trio = False

for i in range(6):
    
    if trio == False:
        perso = random.choice(personne)
        personne.remove(perso)
        
        perso_deux = random.choice(personne)
        personne.remove(perso_deux)
        
        perso_trois = random.choice(personne)
        personne.remove(perso_trois)
        
        liste_duo.append([perso, perso_deux, perso_trois])
        trio = True
    else:
        perso = random.choice(personne)
        personne.remove(perso)
        
        perso_deux = random.choice(personne)
        personne.remove(perso_deux)
        
        liste_duo.append([perso, perso_deux])

def core_email(receiver, team_mate):
    email_sender = "nico.leger99@gmail.com"
    email_password = "xdbq mtgg pfiq mref"

    subject = "Ton duo pour le nouvel an !!!!"
    body = "Salut la team ! Ton groupe est composé de {} !!! N'hésitez surtout pas à vous contacter !".format(team_mate)

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl._create_unverified_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())

def send_email(people_duo):
    for i in range(len(people_duo)):
        for j in range(len(people_duo[i])):
            core_email(people_duo[i][j][1], [item[0] for item in people_duo[i]])

send_email(liste_duo)
