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

    def getUserCreditCards(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ?", "1")
        cards = self.cursor.fetchall()
        return cards

    def getSortedTravel(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ? ORDER BY travel DESC", "1")
        cards = self.cursor.fetchall()
        return cards

    def getSortedDining(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ? ORDER BY dining DESC", "1")
        cards = self.cursor.fetchall()
        return cards

    def getSortedGrocery(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ? ORDER BY groceries DESC", "1")
        cards = self.cursor.fetchall()
        return cards

    def getSortedGas(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ? ORDER BY fuel DESC", "1")
        cards = self.cursor.fetchall()
        return cards

    def getSortedShopping(self):
        self.cursor.execute("SELECT * FROM cards, usercards WHERE cards.card_id = usercards.card_id AND usercards.user_id = ? ORDER BY shopping DESC", "1")
        cards = self.cursor.fetchall()
        return cards

    def getOneCard(self, card_id):
        cardid = [card_id]
        self.cursor.execute("SELECT * FROM cards WHERE id=?", cardid)
        card = self.cursor.fetchone()
        return card

    def addUser(self, fName, lName, email, password):
        hashPass = bcrypt.hash(password)
        data = [fName, lName, email, password]
        
        self.cursor.execute("INSERT INTO users (first_name, last_name, email, salted_pass) VALUES(?,?,?,?)", data)
        self.connection.commit()

    def addCard(self, cardName, company, travelp, diningp, groceriesp, fuelp, shoppingp):
        data = [cardName, company, travelp, diningp, groceriesp, fuelp, shoppingp]

        self.cursor.execute("INSERT INTO cards (card_name, company, Travel, dining, groceries, fuel, shopping) VALUES(?,?,?,?,?,?,?)", data)
        self.connection.commit()

    def addCardtoUser(self, cardId):
        # data = [cardName]

        self.cursor.execute("SELECT card_id FROM cards WHERE card_id=?", cardId)
        card = self.cursor.fetchone()

        cardid = card.get("card_id")
        self.cursor.execute("INSERT INTO usercards (user_id, card_id) VALUES(1,?)", str(cardid))
        self.connection.commit()

    def validateUser(self, email, password):
        data = [email]
        self.cursor.execute("SELECT * FROM users WHERE email=?", data)
        user = self.cursor.fetchone()
        print(email)
        if user == None:
            return False
        else:
            check = bcrypt.verify(password, user["password"])
            if check == False:
                print("wrong password")
                return check
            return user

    def deleteCard(self, id):
        data = [id]
        self.cursor.execute("DELETE FROM usercards WHERE card_id = ? AND user_id = 1", data)
        self.connection.commit()
