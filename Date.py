class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class USADate(Date):
    def format(self):
        return f"{self.month:02d}-{self.day:02d}-{self.year}"


class ItalianDate(Date):
    def format(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"



dates = [
    USADate(2023, 10, 5),
    ItalianDate(2023, 10, 5)
]

for date in dates:
    print("Formatted:", date.format())      #выводит форматированную дату
    print("ISO Format:", date.iso_format())  #выводит ISO-формат даты
