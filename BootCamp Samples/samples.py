name = input("Hello, Can i get your name please? :")
tekrar = ""
if len(name) > 0:print("Hello, " + name)
else:print("Hello, World")

soru = input("Would you like to play a game? :")
if len(soru) > 0:
    if soru == "yes":print("So do you really have enough time?")
    else:print("Okay Good Bye!")
else:
    tekrar = input("Please say something: ")
    if len(tekrar) > 0: print(f"Do you think {tekrar} is meaningful?")
    else:print("Okay no more questions " + name + " Goodbye!")
