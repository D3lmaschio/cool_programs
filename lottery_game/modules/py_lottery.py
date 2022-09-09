from random import choice

LOTTERY_VALUES = ['16', '24', '32', '46', '53', '36', '63', '2', '7',
                  '71', 'd', 'h', 'k', 'o', 'y']


class Lottery:
    """A class to represent a lottery game."""

    def __init__(self, entry_len=4):
        """Generates the default lucky ticket."""
        self.input_ticket = {}
        self.lucky_entry = {}
        self.entry_len = entry_len
        for entry in list(range(0, self.entry_len)):
            self.lucky_entry[entry] = choice(LOTTERY_VALUES)

    def get_lucky_entry(self):
        """Returns the lucky entry."""
        return self.lucky_entry

    def get_lottery_values(self):
        """
        Returns the values that will be used to generate the lucky_entry.
        """
        return LOTTERY_VALUES

    def generate(self, entry_len=4):
        """
        Generates the lucky ticket with given length using LOTTERY_VALUES
        """
        self.entry_len = entry_len
        for entry in list(range(0, self.entry_len)):
            self.lucky_entry[entry] = choice(LOTTERY_VALUES)

    def ticket_match(self, ticket={}):
        """
            Returns the results of match between
            passed ticket and [self.lucky_value].
        - Will return None if no entries are passed.
        """
        checked_results = {}
        if ticket:
            for entry, value in ticket.items():
                entry = int(entry)
                checked_results[entry] = self.lucky_entry.get(entry) == value

            return checked_results
        else:
            return False

    def get_result(self, checked_result={}):
        """
        Returns True if and only if the
        checked_result.values() are all true.
        """
        if checked_result:
            entries_result = []
            for entry in range(0, self.entry_len):
                entries_result.insert(entry,
                                      (checked_result.get(entry)
                                       is True))

            for result in entries_result:
                if result is False:
                    return False

            return True
        else:
            return False

    def make_ticket(self, entries=[]):
        """
        Returns a ticket with given entries.
        - If entry len doesn't match with instance len will return None.
        - If no entries are passed, will return a random ticket.
        """
        ticket = {}
        if len(entries) == self.entry_len:
            for entry in range(0, self.entry_len):
                value = entries[entry]
                ticket[entry] = value

            return ticket
        else:
            for entry in list(range(0, self.entry_len)):
                ticket[entry] = choice(LOTTERY_VALUES)

            return ticket
