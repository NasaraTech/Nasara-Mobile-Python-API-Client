from nasaramobileapiclient import NasaraMobileApiClient

phone = "233244209193"
senderId = "Testing"
message = "hey there, this is a test message!"

smsApi = NasaraMobileApiClient("9EEPC38Eyf9N6Mc8beMEH")
result = smsApi.sendSms(phone, senderId, message)


if(result == '1801'):
	print "message sent successfully"
elif(result == '1802'):
        print "message sending failed"
elif(result == '1803'):
        print "invalid login phone or password given"
elif(result == '1804'):
        print "not enough sms credit"
elif(result == '1805'):
        print "sender id must be more than 1 character and less than 12 characters"
elif(result == '1806'):
        print "phone number must be more than 8 characters"
