import requests
from urllib import urlencode

class NasaraMobileApiClient:
	def __init__(self, apiKey):
		self.apiKey = apiKey
		self.baseUrl = "http://sms.nasaramobile.com/api/"
		self.baseUrlArguments = "?api_key=%s"%self.apiKey
	
	def sendSms(self, phone, senderID, message):
		query = { 'api_key' : self.apiKey,
			  'phone' : phone,
			  'sender_id' : senderID,
			  'message' : message
			}

		response = requests.get(self.baseUrl, params=query) 
		
		return response.text

	def checkCredit(self, queryData=None):
		return self._genericGetRequest('accounts/credit', queryData)


	def sendSmsVersionTwo(self, phoneNumbers, senderId, message, groups=None, contactIds=None):
		query = { 'api_key' : self.apiKey,
                          'phone_numbers' : urlencode(phoneNumbers), 
                          'sender_id' : senderId, 
                          'message' : message 
                        }
		
		response = requests.post(self.baseUrl+'v2/sendsms', data=query)
		
		return response.text


	def fetchContacts(self, queryData=None):
		return self._genericGetRequest('v2/contacts/', queryData)

	def fetchContactDetails(self, contactId, queryData=None):
		return self._genericGetRequest('v2/contacts/'+str(contactId), queryData)

	def fetchGroups(self, queryData=None):
		return self._genericGetRequest('v2/groups', queryData)

	def fetchGroupDetails(self, groupId, queryData=None):
		return self._genericGetRequest('v2/groups/'+str(groupId), queryData)

	def fetchAccountCredit(self, queryData=None):
		return self._genericGetRequest('v2/accounts/credit', queryData)

	
	def _genericGetRequest(self, url, queryData=None):
		if not(queryData):
			queryData = {'api_key' : self.apiKey }
		
		query = queryData
		response = requests.get(self.baseUrl+url, params=query)

		return response.text


