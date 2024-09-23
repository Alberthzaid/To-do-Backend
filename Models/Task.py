
class Task:
    def __init__(self , name , description ,status , date):
        self.name = name
        self.description = description
        self.status = status
        self.date = date

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getDate(self):
        return self.date

    def getDescription(self):
        return self.description

    def toString(self):

        return f"""
            Name : {self.name},
            Description : {self.description},
            Status : {self.status},
            Date : {self.date}
        """

