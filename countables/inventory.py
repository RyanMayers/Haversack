class Item:
    def __init__(self, name="", amount=0, description=""):
        self.name = name
        self.amount = amount
        self.description = description
    
    def toDict(self):
        itemDict = {
            "name": self.name,
            "amount": self.amount,
            "description": self.description
        }
        return itemDict
    
    def add(self, num):
        self.amount += num
        response = f"Added {num} to {self.name}. New total: {self.amount}"
        return response

    def remove(self, num):
        self.amount += num
        response = f"Removed {num} to {self.name}. New total: {self.amount}"
        return response
    
    def getInfo(self):
        print(f'''
{self.name} (x{self.amount})

{self.description}

        ''')
