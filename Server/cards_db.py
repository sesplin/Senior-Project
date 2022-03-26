import sqlite3
# from passlib.hash import bcrypt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class CreditcardsDB:
    def __init__(self):
        self.connection = sqlite3.connect("creditcards.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    def getAllCreditCards(self):
        self.cursor.execute("SELECT * FROM cards")
        cards = self.cursor.fetchall()
        return cards

    def getSortedTravel(self):
        self.cursor.execute("SELECT * FROM cards ORDER BY travel DESC")
        cards = self.cursor.fetchall()
        return cards

    def getSortedDining(self):
        self.cursor.execute("SELECT * FROM cards ORDER BY dining DESC")
        cards = self.cursor.fetchall()
        return cards

    def getSortedGrocery(self):
        self.cursor.execute("SELECT * FROM cards ORDER BY groceries DESC")
        cards = self.cursor.fetchall()
        return cards

    def getSortedGas(self):
        self.cursor.execute("SELECT * FROM cards ORDER BY fuel DESC")
        cards = self.cursor.fetchall()
        return cards

    def getSortedShopping(self):
        self.cursor.execute("SELECT * FROM cards ORDER BY shopping DESC")
        cards = self.cursor.fetchall()
        return cards

    def getOneCard(self, card_id):
        cardid = [card_id]
        self.cursor.execute("SELECT * FROM cards WHERE id=?", cardid)
        card = self.cursor.fetchone()
        return card

    def addUser(self, fName, lName, email, password):
        # hashPass = bcrypt.hash(password)
        data = [fName, lName, email, password]
        
        self.cursor.execute("INSERT INTO users (first_name, last_name, email, salted_pass) VALUES(?,?,?,?)", data)
        self.connection.commit()

    def addCard(self, cardName, company, travelp, diningp, groceriesp, fuelp, shoppingp):
        data = [cardName, company, travelp, diningp, groceriesp, fuelp, shoppingp]

        self.cursor.execute("INSERT INTO cards (card_name, company, Travel, dining, groceries, fuel, shopping) VALUES(?,?,?,?,?,?,?)", data)
        self.connection.commit()

    # def validateUser(self, username, password):
    #     data = [username]
    #     self.cursor.execute("SELECT * FROM users WHERE email=?", data)
    #     user = self.cursor.fetchone()
    #     print(username)
    #     if user == None:
    #         return False
    #     else:
    #         check = bcrypt.verify(password, user["password"])
    #         if check == False:
    #             print("wrong password")
    #             return check
    #         return user