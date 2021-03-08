class Employee:

    def __init__(self, name="", gross_pay=0):
        self.name = name
        self.gross_pay = gross_pay

    def get_name(self):
        return self.name

    def get_gross_pay(self):
        return self.gross_pay
