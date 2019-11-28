import datetime
import time
import json
from alpha_vantage.techindicators import TechIndicators

class DataFile:
	def __init__(self,name,tag):
		self.__name = name
		self.__tag = tag
		self.__timestamp = None
		self.__sma7 = ''
		self.__sma21 = ''
		self.__ti = TechIndicators('IIB8DA6B2CRR6UL7')
		garb = self.updateData()

	def getName(self):
		return self.__name

	def getTag(self):
		return self.__tag

	def getTimestamp(self):
		return self.__timestamp

	def getData(self,period):
		if period == 7:
			return self.__sma7
		else:
			return self.__sma21

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
			self.__sma7 = self.__requestData(7)
			self.__sma21 = self.__requestData(21)
		else:
			self.__timestamp = datetime.datetime.strptime(temp,'%Y-%m-%d %H:%M:%S.%f')
			if timeCheck(self.__timestamp,deltaMin(60)):
				self.__sma7 = self.__requestData(7)
				self.__sma21 = self.__requestData(21)
			else:
				with open(self.__fileName(7)) as json_file:
					self.__sma7 = json.load(json_file)
				with open(self.__fileName(21)) as json_file:
					self.__sma21 = json.load(json_file)

		now = datetime.datetime.now()
		self.__timestamp = now
		self.__updateTime(now)

	def __updateTime(self,time):
		timeFileName = self.__name + "_time.txt"
		t = open(timeFileName,'w')
		t.write(str(time))
		t.close()

	def __fileName(self,period):
		fileName = self.__name + "_sma"+ str(period) +"_data.json"
		return fileName

	def __requestData(self,period):
		fileName = self.__fileName(period)
		try:
			f = open(fileName,'x')
		except FileExistsError:
			pass
		try:
			data = self.__requestAlphaVantage(period)
			with open(fileName, 'w') as outfile:
				json.dump(data, outfile)
		except:
			print("ERROR: COULD NOT REQUEST DATA FROM ALPHAVANTAGE")
		return data


	def __requestAlphaVantage(self,period):
		data,garbage = self.__ti.get_sma(symbol=self.__tag, interval='60min', time_period=period, series_type='close')
		return data

def timeCheck(timestamp,deltaMin):
	now = datetime.datetime.now()
	deltaTime = now-timestamp
	if deltaTime>deltaMin:
		return True
	else:
		return False

def deltaMin(minute):
	return datetime.timedelta(minutes = minute)

n,t = input("Insira <nome do stonks> <tag do stonks na API do ALPHAVANTAGE>\n").split()
a = DataFile(name = n,tag = t)