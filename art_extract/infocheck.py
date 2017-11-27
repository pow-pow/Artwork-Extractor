import csv


class InfoCheck:
    def __init__(self, args):
        self.list_paintings = []

        # format dates
        one, two = self.format_dates(args.date)
        self.date_one = one
        self.date_two = two

        # check CSV file for relevant artwork
        with open(args.in_csv, 'r', encoding='utf8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip header

            for row in csvreader:
                if args.style:
                    if not self.arg_match(args.style, row[3]):
                        continue

                if args.genre:
                    if not self.arg_match(args.genre, row[4]):
                        continue

                if args.date:
                    if not self.match_date(row[5]):
                        continue

                self.list_paintings.append(row[0])

    def arg_match(self, arg, val):
        return arg.lower() == val.lower()

    def match_date(self, val):
        if val == "":
            return False

        # format date
        val = val.strip()
        if val.startswith('c.'):
            val = val[2:]
        if val.endswith('.0'):
            val = val[:-2]
        val = int(val)

        if self.date_two == -1:
            return self.date_one == val
        else:
            return self.date_one <= val <= self.date_two

    def format_dates(self, date):
        if not date:
            return -1, -1

        dates = date.split(',')

        if len(dates) > 0:
            date_one = int(dates[0])
            if len(dates) > 1:
                date_two = int(dates[1])
            else:
                date_two = -1
        else:
            print("Dates are in an invalid format.")
            return

        return date_one, date_two
