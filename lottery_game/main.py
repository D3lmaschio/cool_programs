from modules.py_lottery import Lottery
from modules import listen_kb

listener = listen_kb.kboard.Listener()
listener.start()
listen_kb.on_release(listen_kb.kboard.Key.esc)

inp_start = input("Do you want to play lottery game? (y/n)\n> ")

if inp_start == 'y':
    print("Enter ESQ when you want to quit.")
    listen_kb.on_release(listen_kb.kboard.Key.esc)

    lottery = Lottery()
    print("These are the list that will be used to generate the"
          f"lucky sequence:\n\t{lottery.get_lottery_values()}")
    auto_entry = input("\nDo you want to let the program generate "
                       "your ticket? (y/n) n = You'll need to manually\n"
                       "entry each value until you enter the lucky "
                       "ticket.\n> ")

    count = 0
    flag = False
    while flag is False:

        count += 1
        my_ticket = {}

        if auto_entry == 'y':
            for entry in lottery.entry_len():
                print("Choose one value from the lucky sequence list for:")
                inp_value = input(f"Entry {entry}:\n\t> ")
                my_ticket[entry] = inp_value

        my_ticket = lottery.make_ticket()
        checked_results = lottery.ticket_match(my_ticket)
        result = lottery.get_result(checked_results)

        if result is True:
            print(f"\nYour ticket:\n {my_ticket}\n"
                  f"Lucky sequence:\n - {lottery.get_lucky_entry()}\n"
                  f"Result:\n - {checked_results}")
            print(f"\nLottery games count: {count}")

        flag = result

listener.stop()
