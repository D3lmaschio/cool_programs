from modules import py_lottery as lottery


inp_start = input("Do you want to play lottery game? (y/N)\n")
inp_autofill = input("Do you want to let te program fill the ticket for "
                     " you? (y/N)\n")

lottery = lottery.Lottery()
result = False
count = 0
print("Initializing the program...\n")
while not result:
    # Var count to count how many times the player played:
    count += 1

    # If user want to manually enter the values:
    if inp_autofill.strip().lower() == 'n':
        inp_values = []
        for entry in range(0, lottery.ticket_len()):
            inp_value = input(f"Entry {entry}> ")
            inp_values.insert(entry, inp_value)
        u_ticket = lottery.create_ticket(inp_values)
    else:
        u_ticket = lottery.create_ticket()

    # Checking the results:
    checked_ticket = lottery.check_ticket(u_ticket)
    result = lottery.get_result(checked_ticket)
    if result:
        print(f"Seu ticket: {u_ticket}")
        print(f"Ticket sortudo: {lottery.lucky_entry}")
        print(f"Resultado: {checked_ticket}")
        print(f"Jogadas: {count}")

        # Asking if user wants to play again:
        inp_repeat = input("\nDo you want to play again? (y/N)\n")
        if inp_repeat.strip().lower() == 'y':
            result = False
        else:
            print("\nBye")
