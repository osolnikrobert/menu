menu = {}

while True:
    ime_jedi = raw_input("Vnesi ime jedi: ")
    cena_jedi = raw_input("Vnesi ceno za jed %s: " % ime_jedi)
    menu[ime_jedi] = cena_jedi

    new = raw_input("Bi radi dodali novo jed (da/ne)?")

    if new == "ne":
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:
    for jedi in menu:
        menu_file.write("%s, %s EUR\n" % (jedi, menu[jedi]))# menu
