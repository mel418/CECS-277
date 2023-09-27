class Task:
    '''
    Attributes:
    description (string) – string description of the task 
    date (string) – due date of the task. A string in the format: MM/DD/YYYY
    time(string) – time the task is due. A string in the format: HH:MM
    '''
    
    def __init__(self, desc, date, time):
        self.description = desc
        self.date = date
        self.time = time
        
    def __str__(self):
        '''String representation of a task - user facing.'''
        return self.description + " - Due: " + self.date + " at " + self.time

    def __repr__(self):
        '''String representation of a task - file facing'''
        return self.description + "," + self.date + "," + self.time
    
    def __lt__(self, other):
        month, day, year = self.date.split('/')
        other_month, other_day, other_year = other.date.split('/')
        hour, minute = self.time.split(':')
        other_hour, other_minute = other.time.split(':')
        if (year, month, day, hour, minute, self.description.lower()) < (other_year, other_month, other_day, other_hour, other_minute, other.description.lower()):
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
        #                     if self.description < other.description:
        #                         return True
        #                     else:
        #                         return False
    