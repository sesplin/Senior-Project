from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
from cards_db import CreditcardsDB
# from http import cookies
# from sessionstore import SessionStore
# from urllib.parse import parse_qs
import json

class MyRequestHandler(BaseHTTPRequestHandler):

    def end_headers(self):

        self.send_header("Access-Control-Allow-Origin", self.headers["Origin"])
        self.send_header("Access-Control-Allow-Credentials", "true")
        BaseHTTPRequestHandler.end_headers(self)

    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not Found", "utf-8"))

    def handleCreateUser(self):
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

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        db = CreditcardsDB()
        allCards = db.getAllCreditCards()
        self.wfile.write(bytes(json.dumps(allCards), "utf-8"))

    def handleGetSortedTravel(self):

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
        username = parsed_stuff['username'][0]
        password = parsed_stuff['password'][0]

        db = creditcards()
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

    def do_OPTIONS(self):

        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):

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
        else:
            self.handleNotFound()
            print("invalid path")

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    listen = ("127.0.0.1", 53454)
    server = ThreadedHTTPServer( listen , MyRequestHandler )
    print("The server is running")
    server.serve_forever()

main()