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
		fileName = self.__name + "_data.json"
		try:
			t = open(timeFileName,'x')
		except:
			pass
		t = open(timeFileName,'r')
		temp = t.read()
		t.close()
		if temp == '':
			self.__requestData()
		else:
			self.__timestamp = datetime.datetime.strptime(temp,'%Y-%m-%d %H:%M:%S.%f')
			if timeCheck(self.__timestamp,deltaDay(1)):
				self.__requestData()
			else:
				with open(fileName) as json_file:
					self.__data = json.load(json_file)

	def __updateTime(self,time):
		timeFileName = self.__name + "_time.txt"
		t = open(timeFileName,'w')
		t.write(str(time))
		t.close()

	def __requestData(self):
		fileName = self.__name + "_data.json"
		try:
			f = open(fileName,'x')
		except:
			pass
		try:
			self.__data,garbage = self.__ts.get_daily(self.__tag)
			with open(fileName, 'w') as outfile:
				json.dump(self.__data, outfile)
			now = datetime.datetime.now()
			self.__timestamp = now
			self.__updateTime(now)
		except:
			print("ERROR: COULD NOT REQUEST DATA FROM ALPHAVANTAGE")


def timeCheck(timestamp,deltaMin):
	now = datetime.datetime.now()
	deltaTime = now-timestamp
	if deltaTime>deltaMin:
		return True
	else:
		return False

def deltaMin(minute):
	return datetime.timedelta(minutes = minute)

def deltaDay(day):
	return datetime.timedelta(days = day)

n,t = input("Insira <nome do stonks> <tag do stonks na API do ALPHAVANTAGE>\n").split()
a = DataFile(name = n,tag = t)