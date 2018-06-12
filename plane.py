#!/usr/bin/python3
#Won't work b/c I don't have the data file, but should show some good stuff anyways
import os;

class Point:
	def __init__(self,time="",lat=0,lon=0,alt=0):
		self.time=time;
		self.lat=lat;
		self.lon=lon;
		self.alt=alt;
	def getKMLPoint(self):
		return "<when>"+self.time+"</when><gx:coord>"+self.lon+" "+" "+self.lat+" "+self.alt+"</gx:coord>";
	def __repr__(self):
		return getKMLPoint(self);

def convertTime(inTime):
	#inTime: "2018-04-29 00:03"
	#outTime: "2018-04-29T00:03Z"
	time = inTime.replace(" ","T")+"Z";
	return time;

class Flight:
	def __init__(self,fid="",hexid="",callsign=""):
		self.__points=[];
		self.fid=fid;
		self.hexid=hexid;
		self.callsign=callsign
	def addPoint(self,time,lat,lon,alt):
		time = convertTime(time);
		alt = str(float(alt)/3.33333333);
		p1 = Point(time,lat,lon,alt);
		self.__points.append(p1);
	def getKMLData(self);
		output="<Placemark>";
		if (self.callsign==""):
			output+="<name>Icao: "+self.hexid+"</name>\n";
		else:
			output+="<name>"+self.callsign+"</name>\n";
		ouput+="	<styleUrl>#redPoly";
		#more stuff goes here, but it's boring copy paste stuff
		output+="</Placemark>";
