import re

class Date:
    max_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_days_in_month_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date_string):
        match_result = re.match(r'^\d\d-\d\d-\d\d\d\d$', date_string)
        if match_result is None:
            raise Exception(f"{date_string} - incorrect date format, use dd-mm-yyyy format")
        self.date_string = date_string
        self.day, self.month, self.year = map(int, date_string.split('-'))

    @classmethod
    def extract(cls, date_string):
        date = cls(date_string)
        return [date.day, date.month, date.year]

    @staticmethod
    def validate(date_string):
        date = Date(date_string)
        is_not_zero = date.day > 0 and date.month > 0 and date.year > 0
        if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month_ly[date.month - 1]
        else:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month[date.month - 1]
        return is_not_zero and is_fit_boundaries


if __name__ == '__main__':
    real_date_str = '22-12-1983'
    not_valid_date_str = '29-02-2019'
    incorrect_date_str = '9-02/*019'

    real_date = Date(real_date_str)
    print(f"{real_date.extract(real_date_str)} - extracted numbers")

    not_valid_date = Date(not_valid_date_str)
    print(f"{real_date.extract(not_valid_date_str)} - extracted numbers")

    try:
        incorrect_date = Date(incorrect_date_str)
    except Exception as e:
        print(e)

    if Date.validate(real_date_str):
        print(f"{real_date_str} - valid date")
    else:
        print(f"{real_date_str} - invalid date")

    if Date.validate(not_valid_date_str):
        print(f"{not_valid_date_str} - valid date")
    else:
        print(f"{not_valid_date_str} - invalid date")