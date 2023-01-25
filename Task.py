class Task:

    def __init__(self, date, priority, description):
        self._taskdesc = description
        self._duedate = date
        self._level = priority

    def __str__(self):
        return str(self._duedate) + ', ' + str(self._level) + ': ' + str(self._taskdesc)

    #get functions
    def get_duedate(self):
        return self._duedate
    def get_priority(self):
        return self._level
    def get_description(self):
        return self._taskdesc

    #set functions
    def set_duedate(self, title):
        self._duedate = title
    def set_priority(self, level):
        self._level = level
    def set_description(self, desc):
        self._taskdesc = desc

    #comparison functions
    def __lt__(self, other):
        if self._duedate < other.get_duedate():
            return True
        elif self._duedate == other.get_duedate():
            if self._level < other.get_priority():
                return True
        else:
            return False

    def __gt__(self, other):
        if self._duedate > other.get_duedate():
            return True
        elif self._duedate == other.get_duedate():
            if self._level > other.get_priority():
                return True
        else:
            return False

    def __eq__(self, other):
        if self._duedate == other.get_duedate():
            if self._level == other.get_priority():
                return True
        else:
            return False

    def __le__(self, other):
        if self._duedate < other.get_duedate():
            return True
        elif self._duedate == other.get_duedate():
            if self._level <= other.get_priority():
                return True
        else:
            return False

    def __ge__(self, other):
        if self._duedate > other.get_duedate():
            return True
        elif self._duedate == other.get_duedate():
            if self._level >= other.get_priority():
                return True
        else:
            return False

    def __ne__(self, other):
        if self._duedate != other.get_duedate():
            x = True
            if self._level != other.get_priority():
                x = True
            return x
        elif self._duedate == other.get_duedate():
            if self._level != other.get_priority():
                return True
        else:
            return False
