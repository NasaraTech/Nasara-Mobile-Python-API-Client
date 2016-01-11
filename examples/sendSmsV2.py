from nasaramobileapiclient import NasaraMobileApiClient
import json

phoneNumbers = "233xxxxxxxxx, 24342xxxxxx"
groups = ""
contactIds = ""
senderId = "NTesting"
message = "hey there, this is a test message!"


smsApi = NasaraMobileApiClient("9EEPC38Eyf9N6Mc8beMEH")
response = smsApi.sendSmsVersionTwo(phoneNumbers, senderId, message)
response = json.loads(response)
