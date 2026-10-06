
#Listen dict

    
tasks = {
    "Offen": ["kochen", "einkaufen", "schalfen", "saufen", "schwimmen"],
    "in Arbeit": ["putzen", "auto waschen", "aufräumen", "streichen"],
    "Erledigt": ["tanken", "ausmisten"], 
    }


# Listen anzeigen
def show_lists():
    for status, task_list in tasks.items():
        print(f"{status}:")
        for task in task_list:
            print(f"- {task}")
        print()  # Leerzeile für bessere Lesbarkeit



#programm beenden
def close_app():
    while True:
        abbr = input("Wollen Sie die eingabe Beenden? (y, n): ").lower()
        if abbr == "y":
            return True
        elif abbr == "n":
            return False



#aufgabe finden
def find_task(tasks, task_name):
    for status, task_list in tasks.items():
        if task_name in task_list:
            return status


# Wert einer Liste hinzufügen
def wert_hinzufuegen():
    show_lists()
    while True:
        print("-------------------------------------------")
        print("Zum beenden des Programms, leere Eingabe mit >Enter< bestätigen")
        liste_erweitern = input("Welche Aufgabe willst du Hinzufügen?: ")
        print("-------------------------------------------")
        if liste_erweitern == "":
            if close_app():
                break
            else:
                continue
        else:
            tasks["Offen"].append(liste_erweitern)
            key = "Offen"
            if key in tasks:
                print(f"Aufgaben - {key}:")
                for task in tasks[key]:
                    print(task)  # Jede Aufgabe in einer neuen Zeile





# Wert einer Liste entfernen
def wert_entfernen():
    show_lists()
    while True:
        print("-------------------------------------------")
        print("Zum beenden des Programms, leere Eingabe mit >Enter< bestätigen")
        liste_entfernen = input("Welche Aufgabe willst du Entfernen?: ")
        print("-------------------------------------------")

        if liste_entfernen == "":
            if close_app():
                break
            else:
                continue
        status = find_task(tasks, liste_entfernen)
        if status is None:
            print("Aufgabe nicht gefunden.")
            continue

        tasks[status].remove(liste_entfernen)
        show_lists()
        print(f"Aufgabe '{liste_entfernen}' aus '{status}' entfernt.")
    




# Wert einer Liste schieben
def wert_schieben():
    show_lists()
    while True:
        print("-------------------------------------------")
        print("Zum beenden des Programms, leere Eingabe mit >Enter< bestätigen")
        liste_schieben = input("Welche Aufgabe willst du verschieben?: ").lower()
        liste_schieben_neu = input("In welche liste willst du die Aufgabe verschieben?: ").capitalize()
        print("-------------------------------------------")

        if liste_schieben == "":
            if close_app():
                break
            else:
                continue
        status = find_task(tasks, liste_schieben)
        if status is None:
            print("Aufgabe nicht gefunden.")
            continue
        if liste_schieben_neu == "":
            abbr = input("Wollen Sie die eingabe Beenden? (y, n): ").lower()
            if close_app():
                break
            else:
                continue
        status = find_task(tasks, liste_schieben_neu)
        if status is None:
            print("Aufgabe nicht gefunden.")
            continue
        tasks[status].append(liste_schieben_neu)
        tasks[status].remove(liste_schieben)
        print(f"Aufgabe '{liste_schieben}' aus '{status}' entfernt und in '{liste_schieben_neu}' verschoben.")
    




# Aktion Abfragen
def change_tasks():
    while True:
        print("> Zum beenden des Programms, leere Eingabe mit >Enter< bestätigen <")
        choice = ["1. Anzeigen", "2. Hinzufügen", "3. Status ändern", "4. Löschen"]
        print(*choice, sep="\n")
        print("_____________________")
        action = input("Was möchtest du tun? Wähle aus den oberen Optionen (z.B. 1): ")
        print("")
        try:
            action = int(action)
            # Alle Liste anziegen
            if action == 1: 
                print_choice = ["1. Alle", "2. in Arbeit", "3. Erledigt", "4. Offen"]
                print(*print_choice, sep="\n")
                print_choice = input("Welche Liste willst du sehen?: ")
                #Programm beenden prüfen
                if print_choice == "":
                    if close_app():
                        break
                    else:
                        continue
                #Alle Listen anzeigen
                elif print_choice == 1:
                    show_lists()
                #Liste "in Arbeit" anzeigen
                elif print_choice == 2:
                    print(tasks["in Arbeit"])
                    close_app()
                #Liste "Erledigt" anzeigen
                elif print_choice == 3:
                    print(tasks["Erledigt"])
                #Liste "Offen" anzeigen            
                elif print_choice == 4:
                    print(tasks["Offen"])
            #Aufgbae Hinzufügen
            if action == 2:
                wert_hinzufuegen()
                print("_____________________")
            #Aufgbae Verschieben
            if action == 3:
                wert_schieben()
                print("_____________________")            
            #Aufgbae Löschen
            if action == 4:
                wert_entfernen()
                print("_____________________")                
        #Eingabe fehler prüfen
        except ValueError:
            print("Ungültige Eingabe es muss eine Zahl eingegeben werden!")


##Funktionen Testen
#change_tasks()
#wert_hinzufuegen()
#wert_entfernen()
