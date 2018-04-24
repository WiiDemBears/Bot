import random
import time
import numpy
import json
import redis
IMAGEDATA=json.loads(open("C:/Users/Darri/Desktop/node/Poseidon/classes/imagedata.json",'r').read())
DEVICESIGNATURE="20,20,40,20,40,40,60,20,20,20,0,0,20,180,"
class BotDetector:
    def __init__(self):
        self.trand=False
        self.start_ts=self.get_cf_date()
        self.cookie="2"
        self.useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        self.forminfo="0,0,0,0,630,630,0;"
        self.url="https://www.footlocker.com/account/?action=accountCreate"
        self.screensize=(768,1366)
        self.d3=None
        self.mact=""
        self.mval=0
        self.doact=""
        self.doval=0
        self.dmact=""
        self.dmval=0
        self.totalaction=0
        self.tst=8
        self.r = redis.Redis(host='35.190.140.1', port=6380, db=0)
    def get_cf_date(self):
        if self.trand:
            time.sleep(float(random.randint(1,5))/1000)
        return int(time.time()*1000)
    def update_t(self):
        return self.get_cf_date()-self.start_ts
    def ab(self,t):
        if t==None:
            return -1
        a=0
        for p in t:
            if ord(p)<128:
                a+=ord(p)
        return a
    def gd(self):
        t=self.useragent
        e=str(self.ab(t))
        c=str(self.start_ts/2)
        if (self.start_ts%2)!=0:
            c+=".5"
        self.z1=int(self.start_ts/(2016*2016))
        ll=random.randint(500,999)
        l="0."+str(ll)+str(random.randint(100000,999999))+str(ll/2)
        if self.d3==None:
            self.d3=self.get_cf_date()%10000000
        #12147,4 depends on browser
        return t + ",uaend,12147,20030107,en-US,Gecko,4,0,0,0," + str(self.z1) + "," + str(self.d3) + ",1366,728,1366,768,1366,"+str(random.randint(550,720))+",1366,,cpen:0,i1:0,dm:0,cwen:1,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1," + e + "," + l + "," + c + ",loc:"
    def x1(self):
        return numpy.base_repr(random.randint(16777216,16777216*2-1),36).lower()
    def o9(self):
        t=e=self.d3
        for c in range(0,5):
            n = int(t / (10**c)) % 10
            a = n + 1
            mn=n%4
            if mn==0:
                e=e*a
            elif mn==1:
                e=e+a
            else:
                e=e-a
        return e
    def od(self,t,e):
        t=str(t)
        e=str(e)
        n=len(e)
        c=[]
        for a in range(0,len(t)):
            o=ord(t[a])
            f=t[a]
            i=ord(e[a%n])
            if (o>47)&(o<=57):
                o=o+(i%10)
                if o>57:
                    o=o-10
            if o!=ord(t[a]):
                f=chr(o)
            c.append(f)
        return "".join(c)
    def generatesensordata(self):
        start=self.get_cf_date()
        t=self.get_cf_date()
        e=self.update_t()
        c=self.cookie
        n=self.gd()
        i="do_en,dm_en,t_en"
        r=self.forminfo
        d=self.url
        s = "0,0"
        u = 25279115
        l = self.get_cf_date()-self.start_ts
        _ = int(int(self.z1/23) / 6)
        v=30261689
        m="0,0,0,0,0,0,0,"+str(e)+",0,"+str(self.start_ts)+",-999999,"+str(int(self.z1/23))+",0,0,"+str(_)+",0,0,"+str(l)+",0,0,"+c+","+str(self.ab(c))+",-1,-1,"+str(v)
        h="94"
        g="0,0,0,0,1,0,0"
        sensor_data="1.26-1,2,-94,-100," + n + "-1,2,-94,-101," + i + "-1,2,-94,-105," + "-1,2,-94,-102," + "-1,2,-94,-108,"+ "-1,2,-94,-110," + "-1,2,-94,-117," + "-1,2,-94,-111," + "-1,2,-94,-109," + "-1,2,-94,-114," + "-1,2,-94,-103," + "-1,2,-94,-112," + d + "-1,2,-94,-115," + m + "-1,2,-94,-106," + s
        sensor_data = sensor_data + "-1,2,-94,-119,-1-1,2,-94,-122," + g
        w = self.ab(sensor_data)
        sensor_data = sensor_data + "-1,2,-94,-70,-1-1,2,-94,-80," + h + "-1,2,-94,-116," + str(self.o9()) + "-1,2,-94,-118," + str(w) + "-1,2,-94,-121,"
        b=self.od("0a46G5m17Vrp4o4c","afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq")[:16]
        y=int(self.get_cf_date()/3600000)
        k=self.get_cf_date()
        C=b+self.od(y,b)+self.od(sensor_data,b)
        sensor_data=C+";"+str(self.get_cf_date()-t)+";-1;0"
        self.trand=True
        self.tst=self.get_cf_date()-start
        self.r.set(random.randint(100000,999999),sensor_data)
    def domouseaction(self):
        macttime=self.update_t()
        mousex=random.randint(400,600)
        mousey=random.randint(100,300)
        self.mact+="0,3,"+str(macttime)+","+str(mousex)+","+str(mousey)+",-1;"
        self.mval+=3+macttime+mousex+mousey
        self.totalaction+=macttime
    def dodeviceaction(self):
        doactime=random.randint(200,400)
        self.doact+="0,"+str(doactime)+",-1,-1,-1;"
        self.doval+=doactime
        self.totalaction+=doactime
        dmactime=doactime+2
        self.dmact+="0,"+str(dmactime)+",-1,-1,-1,-1,-1,-1,-1,-1,-1;"
        self.dmval+=dmactime
        self.totalaction+=dmactime
    def generatesensordata1(self):
        n=self.gd()
        time.sleep(float(random.randint(1,500))/1000)
        self.dodeviceaction()
        time.sleep(float(random.randint(1000,1500))/1000)
        self.domouseaction()
        start=self.get_cf_date()
        t=self.get_cf_date()
        e=self.update_t()
        c=self.cookie
        i="do_en,dm_en,t_en"
        r=self.forminfo
        d=self.url
        s = "1,1"
        u = 25279115
        l = self.get_cf_date()-self.start_ts
        _ = int(int(self.z1/23) / 6)
        v=30261689
        imageval=random.randint(100,999)
        m="0,"+str(self.mval)+",0,"+str(self.doval)+","+str(self.dmval)+",0,"+str(self.mval+self.doval+self.dmval)+","+str(e)+",0,"+str(self.start_ts)+","+str(random.randint(1,10))+","+str(int(self.z1/23))+",0,1,"+str(_)+",1,0,"+str(l)+","+str(self.totalaction)+",0,"+c+","+str(self.ab(c))+","+str(imageval)+","+IMAGEDATA[imageval-100]+","+str(v)
        h="5164"
        g="0,0,0,0,1,0,0"
        sensor_data="1.26,1.26-1,2,-94,-100,"
        sensor_data="1.26-1,2,-94,-100," + n + "-1,2,-94,-101," + i + "-1,2,-94,-105," + "-1,2,-94,-102," + r + "-1,2,-94,-108,"+ "-1,2,-94,-110," + self.mact + "-1,2,-94,-117," + "-1,2,-94,-111," + self.doact + "-1,2,-94,-109," + self.dmact + "-1,2,-94,-114," + "-1,2,-94,-103," + "-1,2,-94,-112," + d + "-1,2,-94,-115," + m + "-1,2,-94,-106," + s
        sensor_data = sensor_data + "-1,2,-94,-119,"+DEVICESIGNATURE+"-1,2,-94,-122," + g
        w = self.ab(sensor_data)
        sensor_data = sensor_data + "-1,2,-94,-70,-999120978;dis;,7,8,19;true;true;true;-330;true;24;24;true;false;-1-1,2,-94,-80," + h + "-1,2,-94,-116," + str(self.o9()) + "-1,2,-94,-118," + str(w) + "-1,2,-94,-121,"
        b=self.od("0a46G5m17Vrp4o4c","afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq")[:16]
        y=int(self.get_cf_date()/3600000)
        k=self.get_cf_date()
        C=b+self.od(y,b)+self.od(sensor_data,b)
        sensor_data=C+";"+str(self.tst)+";"+str(self.get_cf_date()-start+1)+";1"
        self.r.set(random.randint(100000,999999),sensor_data)

    def run(self):
        self.generatesensordata()
while True:
    BotDetector().run()
    time.sleep(30)
