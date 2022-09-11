from random import choice

LUCKY_TICKET = ['16', '24', '32', '46', '53', '36', '63',
                '2', '7', '71', 'd', 'h', 'k', 'o', 'y'
                ]


class Lottery:
    """A class to represent a lottery game."""

    def __init__(self, ticket_len=4):
        """Generates the default lucky ticket."""
        self.lucky_entry = {}
        self.ticket_len = ticket_len
        for entry in list(range(0, self.ticket_len)):
            self.lucky_entry[entry] = choice(LUCKY_TICKET)

    def generate(self, ticket_len=4):
        """Generates the lucky ticket with given length."""
        self.ticket_len = ticket_len
        for entry in list(range(0, self.ticket_len)):
            self.lucky_entry[entry] = choice(LUCKY_TICKET)

    def check_ticket(self, ticket={}):
        """
        Returns the checked_ticket of given ticket.
        - Will return None if no entries are passed.
        """
        checked_ticket = {}
        for entry, value in ticket.items():
            entry = int(entry)
            checked_ticket[entry] = self.lucky_entry.get(entry) == value
        return checked_ticket

    def get_result(self, checked_ticket={}):
        """
        Returns True if and only if the values from checked_ticket
        are all true.
        """
        for result in checked_ticket.values():
            if result is False:
                return False
        return True

    def create_ticket(self, entries=[]):
        """
        Returns a ticket with given entries.
        - If entry len doesn't match with instance len will return None.
        """
        ticket = {}
        if len(entries) == self.ticket_len:
            for entry in range(0, self.ticket_len):
                value = entries[entry]
                ticket[entry] = value
            return ticket
        else:
            # cmd pollution
            # print("Wrong entry for ticket are passed, autofilling your "
            #      "ticket...")
            for entry in range(0, self.ticket_len):
                ticket[entry] = choice(LUCKY_TICKET)
            return ticket
