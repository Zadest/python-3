import random
from time import sleep

# Hallo Welt

"""
   Hallo mehrzeiliger Kommentar
   ciao 
"""

print("Willkommen beim Nummernspiel. Errate welche Nummer gesucht wird")
print("Suche eine Nummer zwischen 0 und 100...")
answer = random.randint(0,100)
versuche = 0
guesses = []
sleep(random.random())
print("Habe eine Nummer gefunden!")
 
while True:
    # try:
    user_input = input("An welche Zahl denke ich?\n> ")
    # except KeyboardInterrupt:
    #     user_input = ""
    #     pass

    if user_input.lower() == "end":
        print(f"{guesses=}")
        break
    
    try:
        user_input_integer = int(user_input)
    except:
        print("Die Eingabe war keine Zahl. Versuch es nochmal oder gib 'end' ein, um dass Spiel zu verlassen")
    else:
        guesses.append(user_input_integer)
        versuche += 1
        if user_input_integer == answer:
            print(f"Gewonnen! Ich habe an die Zahl {answer} gedacht. Du hast {versuche} Versuche gebraucht")
            print(f"{guesses=}")
            break
        if user_input_integer < answer:
            print(f"Deine Zahl ist kleiner als die gesuchte Zahl")
        if user_input_integer > answer:
            print(f"Deine Zahl ist größer als die gesuchte Zahl")


# Beispiel : Inhalte aus Datei lesen
with open('gamelog.txt','r',encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)


# Beispiel : Inhalte in Datei schreiben
string_guesses = []
for guess in guesses:
    string_guesses.append(str(guess))

line = ";".join(string_guesses)+"\n"

with open('gamelog.txt','a',encoding="utf-8") as f:
    f.write(line)