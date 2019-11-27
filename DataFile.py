import datetime
import time
import json
from alpha_vantage.timeseries import TimeSeries

class DataFile:
	def __init__(self,name,tag):
		self.__name = name
		self.__tag = tag
		self.__timestamp = None
		self.__data = None
		self.__ts = TimeSeries('IIB8DA6B2CRR6UL7')
		garb = self.updateData()

	def getName(self):
		return self.__name

	def getTag(self):
		return self.__tag

	def getTimestamp(self):
		return self.__timestamp

	def getData(self):
		return self.__data

	def updateData(self):
		timeFileName = self.__name + "_time.txt"
		try:
			t = open(timeFileName,'x')
		except:
			pass
		t = open(timeFileName,'r')
		temp = t.read()
		t.close()
		if temp == '':
			now = datetime.datetime.now()
			sucess = self.requestData()

			t = open(timeFileName,'w')
			t.write(str(now))
			t.close()
		else:
			self.__timeStamp = datetime.strptime(temp,'%Y-%m-%d %H:%M:%S.%f')

	def requestData(self):
		fileName = self.__name + ".json"
		try:
			self.__data,garb = self.__ts.get_daily(self.__tag)
			print("REQUESTED DATA FROM ALPHAVANTAGE")
			t.open(fileName,'w+')
			print("OPENED FILE")
			t.write(self.__data)
			print("WRITTEN ON FILE")
			t.close()
			print("CLOSED FILE")
			return True
		except:
			return False


def timeCheck(timestamp,deltaMax):
	now = datetime.datetime.now()
	deltaTime = now-timestamp
	if deltaTime<deltaMax:
		return True
	else:
		return False

def deltaMin(minute):
	return datetime.timedelta(minutes = minute)

def deltaDay(day):
	return datetime.timedelta(days = day)

a = DataFile('BTC','BTC')