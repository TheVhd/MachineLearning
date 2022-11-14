accName = input("Please Enter Your Name:")
transferAmount = int(input("Amount of transfer:"))


def moneyTransfer(accName, transferAmount):
    accs = {'Vahit': 45000, 'Murat': 17000, "Cemil": 256000, "Hasan": 78000}
    if accName in accs:
        if transferAmount > int(accs[accName]):
            print("Insufficient Funds")
        else:
            for i in accs:
                if i == accName:
                    accs[accName] -= transferAmount
                    print("Transfer Successful!" + "\n" + "Transferred amount is:" + str(transferAmount))
                    if int(accs[i]) == 0:print("Caution You ran out of funds!" + "\n" + "New Balance is: " + str(accs[i]))
                    else:
                        print("New Balance is:" + str(accs[i]))
    else:
        print("No Such Account")
    return


moneyTransfer(accName, transferAmount)

newPassword = range(1999)