import urllib.request as ur
import json
def trainRoute():
    print("Enter Train Number : ",end='')
    trainNumber=input()
    extension=trainNumber+'.txt'
    try:
        f=open(extension,'r')
        print(f.read())
        f.close()


    except Exception:
        print("url request")
        url='https://api.railwayapi.com/v2/route/train/'+trainNumber+'/your-APi-Key/'
        reqObject=ur.Request(url)
        with ur.urlopen(reqObject) as response:
            page=response.read()
            result=str()
            jsonFormat=json.loads(page)
            fileObject=open(extension,'a+')
            print('S.no'+'     '+'Arrival_Time     '+'Departure_Time     '+'Station_Name')
            fileObject.write("TrainNumber=")
            fileObject.write(trainNumber)
            fileObject.write('\n')
            fileObject.write('S.no'+'     '+'Arrival_Time     '+'Departure_Time     '+'Station_Name')
            fileObject.write('\n')
            print("\n")
            for data in jsonFormat['route']:
                result+=str(data['no'])+'          '+data['scharr']+'             '+data['schdep']+'          '+data['station']['name']+'\n'



            fileObject.write(result)
            fileObject.write("\n")
            fileObject.close()
            print(result)

def liveStatus():
    print("Enter Train Number : ", end='')
    trainNumber=input()
    date=input("Date in format(dd-mm-yyyy) :")
    url='https://api.railwayapi.com/v2/live/train/'+trainNumber+'/date/'+date+'/apikey/your-APi-Key/'
    reqObject = ur.Request(url)
    with ur.urlopen(reqObject) as response:
        page=response.read()
        result=str()
        jsonFormat=json.loads(page)
        result+='Current_position : '+jsonFormat['position']+'\n'+'Current_Station : '+jsonFormat['current_station']['name']
    print(result)

def fareEnquiry():
    print("Enter Train Number : ", end='')
    trainNumber=input()
    sourceStation=input("Enter Source Station Code(in capital letters) : ")
    destinationStation=input("Enter Destination Code(in capital letters) : ")
    date=input("Date in format(dd-mm-yyyy) :")
    age=input("Enter Your Age : ")
    pref=input("Enter class Code(1A,2A,3A,SL,CC,2S,3E,FC) : ")
    # quota=input("Enter Quota(GN) : ")
    url='https://api.railwayapi.com/v2/fare/train/'+trainNumber+'/source/'+sourceStation+'/dest/'+destinationStation+'/age/'+age+'/pref/'+pref+'/quota/'+'GN'+'/date/'+date+'/apikey/your-APi-Key/'
    reqObject = ur.Request(url)
    with ur.urlopen(reqObject) as response:
        page=response.read()
        result=str()
        jsonFormat=json.loads(page)
        result+='FARE : '+str(jsonFormat['fare'])
    print(result)

def stationCodeEnquiry():
    stationName=input("Enter Station Name : ")
    url='https://api.railwayapi.com/v2/name-to-code/station/'+stationName+'/apikey/your-APi-Key/'
    reqObject = ur.Request(url)
    with ur.urlopen(reqObject) as response:
        page=response.read()
        result=str()
        jsonFormat=json.loads(page)
        for data in jsonFormat['stations']:
            result+='Station Name : '+data['name']+'\n'+'Station Code : '+data['code']+'\n\n'
        print(result)

def seatAvailability():
    print("Enter Train Number : ", end='')
    trainNumber=input()
    sourceStation=input("Enter Source Station Code(in capital letters) : ")
    destinationStation=input("Enter Destination Code(in capital letters) : ")
    date=input("Date in format(dd-mm-yyyy) :")
    pref=input("Enter class Code(1A,2A,3A,SL,CC,2S,3E,FC) : ")
    # quota=input("Enter Quota(GN) : ")

    url='https://api.railwayapi.com/v2/check-seat/train/'+trainNumber+'/source/'+sourceStation+'/dest/'+destinationStation+'/date/'+date+'/pref/'+pref+'/quota/'+'GN'+'/apikey/your-APi-Key/'
    reqObject = ur.Request(url)
    with ur.urlopen(reqObject) as response:
        page=response.read()
        result=str()
        jsonFormat=json.loads(page)
        for data in jsonFormat['availability']:
            result+='Date :'+data['date']+'\n'+'Status :'+data['status']+'\n\n'
    print(result)

while True:
    print("1.Train Route")
    print("2.Live Status")
    print("3.Fare Enquiry")
    print("4.Station Code Enquiry")
    print("5.Seat Availability")
    print("6.Exit")
    print('\n\n')
    userInput=int(input())
    if userInput is 1:
        trainRoute()
    elif userInput is 2:
        liveStatus()
    elif userInput is 3:
        fareEnquiry()
    elif userInput is 4:
        stationCodeEnquiry()
    elif userInput is 5:
        seatAvailability()
    elif userInput is 6:
        quit()
