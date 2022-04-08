from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
from cards_db import CreditcardsDB
from http import cookies
from sessionstore import SessionStore
from urllib.parse import parse_qs
import json

gSessionStore = SessionStore()

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def loadCookie(self):
        if "Cookie" in self.headers:
            self.cookie = cookies.SimpleCookie(self.headers["Cookie"])
        else:
            self.cookie = cookies.SimpleCookie()

    def sendCookie(self):
        for morsel in self.cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())

    def loadSession(self):
        self.loadCookie()
        if "sessionId" in self.cookie:
            sessionId = self.cookie["sessionId"].value
            self.sessionData = gSessionStore.getSessionData(sessionId)
            if self.sessionData == None:
                sessionId = gSessionStore.createSession()
                self.sessionData = gSessionStore.getSessionData(sessionId)
                self.cookie["sessionId"] = sessionId

        else:
            sessionId = gSessionStore.createSession()
            self.sessionData = gSessionStore.getSessionData(sessionId)
            self.cookie["sessionId"] = sessionId

    def end_headers(self):
        self.sendCookie()
        self.send_header("Access-Control-Allow-Origin", self.headers["Origin"])
        self.send_header("Access-Control-Allow-Credentials", "true")
        BaseHTTPRequestHandler.end_headers(self)

    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not Found", "utf-8"))

    def handleCreateUser(self):

        if "userId" not in self.sessionData:
            self.handleNotFound()
            return

        Length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(Length).decode("utf-8")
        print("Request body: " , request_body)
        parsed_stuff = parse_qs(request_body)
        print("The parsed body: ", parsed_stuff)

        user_fName = parsed_stuff['fname'][0]
        user_lName = parsed_stuff['lname'][0]
        user_email = parsed_stuff['email'][0]
        user_pass = parsed_stuff['pass'][0]

        db = CreditcardsDB()
        db.addUser(user_fName, user_lName, user_email, user_pass)
        self.send_response(201)
        self.end_headers()

    def handleGetAllCards(self):

        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        db = CreditcardsDB()
        allCards = db.getAllCreditCards()
        self.wfile.write(bytes(json.dumps(allCards), "utf-8"))

    def handleGetUserCards(self):

        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        db = CreditcardsDB()
        userCards = db.getUserCreditCards()
        self.wfile.write(bytes(json.dumps(userCards), "utf-8"))


    def handleGetSortedTravel(self):
        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        db = CreditcardsDB()
        sortedType = db.getSortedTravel()
        if sortedType != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sortedType), "utf-8"))
        else:
            print("invalid request")
            self.handleNotFound()


    def handleGetSortedDining(self):
        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        db = CreditcardsDB()
        sortedType = db.getSortedDining()
        if sortedType != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sortedType), "utf-8"))
        else:
            print("invalid request")
            self.handleNotFound()

    def handleGetSortedGrocery(self):
        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        db = CreditcardsDB()
        sortedType = db.getSortedGrocery()
        if sortedType != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sortedType), "utf-8"))
        else:
            print("invalid request")
            self.handleNotFound()


    def handleGetSortedGas(self):
        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return

        db = CreditcardsDB()
        sortedType = db.getSortedGas()
        if sortedType != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sortedType), "utf-8"))
        else:
            print("invalid request")
            self.handleNotFound()

    def handleGetSortedShopping(self):
        # if "userId" not in self.sessionData:
        #     self.handleNotFound()
        #     return
        db = CreditcardsDB()
        sortedType = db.getSortedShopping()
        if sortedType != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sortedType), "utf-8"))
        else:
            print("invalid request")
            self.handleNotFound()

    def handleValidateUser(self):
        contlength = int(self.headers["Content-Length"])
        request_stuff = self.rfile.read(contlength).decode("utf-8")
        parsed_stuff = parse_qs(request_stuff)
        username = parsed_stuff['name'][0]
        password = parsed_stuff['pass'][0]

        db = CreditcardsDB()
        check = db.validateUser(username, password)
        if check == False:
            print("user doesn't exist")
            self.send_response(401)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Invalid User", "utf-8"))

        else:
            self.send_response(201)
            self.send_headers()
            self.sessionData["userId"] = check["userId"]

    def handleAddCard(self):
        contlength = int(self.headers["Content-Length"])
        request_stuff = self.rfile.read(contlength).decode("utf-8")
        # print(request_stuff)
        # parsed_stuff = parse_qs(request_stuff)
        # cardname = parsed_stuff["cardname"]
        # cardname = request_stuff.get("cardname")
        cardname = request_stuff[12]
        # print(cardname)
        db = CreditcardsDB()
        db.addCardtoUser(cardname)
        self.send_response(201)
        self.end_headers()

    def handleDeleteCard(self, card_name):
        db = CreditcardsDB()
        oneRecord = db.deleteCard(card_name)
        if oneRecord != None:
            db.deleteCard(card_name)
            self.send_response(200)
            self.end_headers()
        else:
            self.handleNotFound()

    def do_OPTIONS(self):
        self.loadSession()
        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self.loadSession()
        splitpath = self.path.split('/')
        collection = splitpath[1]

        if len(splitpath) > 2:
            Type = splitpath[2]
            print(Type)
        else:
            Type = None

        if collection == "cards":
            if Type == "travel":
                self.handleGetSortedTravel()
                print("gotTravel")
            elif Type == "dining":
                self.handleGetSortedDining()
                print("gotDining")
            elif Type == "grocery":
                self.handleGetSortedGrocery()
                print("gotGrocery")
            elif Type == "gas":
                self.handleGetSortedGas()
                print("gotGas")
            elif Type == "shopping":
                self.handleGetSortedShopping()
                print("gotShopping")
            else:
                self.handleGetAllCards()
                print("gotEverything")
        elif collection == "usercards":
            self.handleGetUserCards()
        else:
            self.handleNotFound()
            print("invalid path")

    def do_POST(self):
        self.loadSession()
        if self.path == "/add":
            print("trying to add")
            self.handleAddCard()
        elif self.path == "/sessions":
            self.handleValidateUser()
        else:
            self.handleNotFound()

    def do_DELETE(self):
        self.loadSession()
        splitpath = self.path.split('/')
        collection = splitpath[1]
        if len(splitpath) > 2:
            member_id = splitpath[2]
        else:
            member_id = None

        if collection == "card":
            if member_id:
                self.handleDeleteCard(member_id)
            else:
                self.handleNotFound()
        else:
            self.handleNotFound()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    listen = ("127.0.0.1", 53454)
    server = ThreadedHTTPServer( listen , MyRequestHandler )
    print("The server is running")
    server.serve_forever()

main()