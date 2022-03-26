import os, base64

class SessionStore:
	# DATA
	#  a dictionary of dictionaries

	# METHODS

	def __init__(self):
		self.sessions = {}

	def createSession(self):
		sessionId = self.createSessionId()
		self.sessions[sessionId] = {}
		return sessionId

##I should sign my cookies with a hash but I don't need to do that
#encoding random number to a random string and returning it
	def createSessionId(self):
		rnum = os.urandom(32)
		rstr = base64.b64encode(rnum).decode("utf-8")
		return rstr

	def getSessionData(self, sessionId):
		if sessionId in self.sessions:
			return self.sessions[sessionId]
		else:
			return None