class Task:
    '''
    Attributes:
    description (string) – string description of the task 
    date (string) – due date of the task. A string in the format: MM/DD/YYYY
    time(string) – time the task is due. A string in the format: HH:MM
    '''
    
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date  # MM/DD/YYYY
        self._time = time  # HH:MM

    @property
    def date(self):
        return self._date

    def __str__(self):
        return self._description + " - Due: " + self._date + " at " + self._time

    def __repr__(self):
        return self._description + ", " + self._date + ", " + self._time

    def __lt__(self, other):
        month, day, year = self._date.split('/')
        other_month, other_day, other_year = other._date.split('/')
        hour, minute = self._time.split(':')
        other_hour, other_minute = other._time.split(':')
        if (year, month, day, hour, minute, self._description.lower()) < (other_year, other_month, other_day, other_hour, other_minute, other._description.lower()):
            return True
        return False
    
        # if year < other_year:
        #     return True
        # elif year > other_year:
        #     return False
        # else:
        #     if month < other_month:
        #         return True
        #     elif month > other_month:
        #         return False
        #     else:
        #         if day < other_day:
        #             return True
        #         elif day > other_day:
        #             return False
        #         else:
        #             if hour < other_hour:
        #                 return True
        #             elif hour > other_hour:
        #                 return False
        #             else:
        #                 if minute < other_minute:
        #                     return True
        #                 elif minute > other_minute:
        #                     return False
        #                 else:
        #                     if self.description.lower() < other.description.lower():
        #                         return True
        #                     else:
        #                         return False
    