import http.client, urllib.request, urllib.parse, urllib.error, base64, json, time, requests, cv2, numpy, pyodbc, sys,os,subprocess
import importlib as il
import mysql.connector
flag=1
flag1=True
sub=1
def connectSQLDatabase():
    server = 'daksh.database.windows.net'
    database = 'mydata_1'
    username = 'daksh'
    password = 'Daks123@'
    driver= "{SQL Server}"
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor

cursor = connectSQLDatabase()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')




class FaceID(object):
    """The FaceID Class"""

    conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    cam = cv2.VideoCapture('rtsp://admin:admin@123@192.168.43.200/1')
    # cam = cv2.VideoCapture(0)
    #cam.set(cv2.CAP_PROP_FPS, 0.1)
    personScanned = ''

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '396d59cc1b254b6785de82dd4355c5a6',
    }

    def fetchSQLData(self):
        #mydb = mysql.connector.connect(server='daksh.database.windows.net',username='daksh',password='Daks123@',database='mydata_1')

        #mycursor = mydb.cursor()

        cursor.execute("SELECT * from attendance")

        result = cursor.fetchall()

        for i in result:
            if i[0]=='1111111':
                i[0]='2016IPG-031'
            elif i[0]=='0000000':
                i[0]='2016IPG-005'
            elif i[0]=='2222222':
                i[0]='2019IMT-110'
            elif i[0]=='3333333':
                i[0]='2019IMT-046'
            elif i[0]=='4444444':
                i[0]='2019MT-085'
            elif i[0]=='5555555':
                i[0]='2019IMG-001'
            elif i[0]=='6666666':
                i[0]='2019IMT-017'
            elif i[0]=='7777777':
                i[0]='2019IMG-006'
            elif i[0]=='8888888':
                i[0]='2019IMG-030'
            print(i)
        return result
    def createGroup(self, groupId, groupName):

        params = urllib.parse.urlencode({})

        body = {
            "name" : '{}'.format(groupName),
        }

        try:
            self.conn.request("PUT", "/face/v1.0/persongroups/" + groupId + "?%s" % params, json.dumps(body), self.headers)
            response = self.conn.getresponse()
            data = response.read()
            print("GROUP CREATED")
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def addPerson(self, name, targetGroup):

        params = urllib.parse.urlencode({})

        body = {
            "name": '{}'.format(name),
        }

        try:
            self.conn.request("POST", "/face/v1.0" + targetGroup + "/persons?%s" % params, json.dumps(body), self.headers)
            response = self.conn.getresponse()
            data = response.read()
            print("PERSON ADDED: ", name)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def addFace(self, targetName, targetGroup, URL):

        # WARNING: going off the assumption that there are no duplicate names
        listOfPersons = json.loads(self.listPersonsInGroup(targetGroup))
        personId = ""
        for person in listOfPersons:
            if person["name"] == targetName:
                personId = person["personId"]
                break

        params = urllib.parse.urlencode({})

        body = {
            "url" : '{}'.format(URL)
        }

        try:
            self.conn.request("POST", "/face/v1.0/persongroups/" + targetGroup + "/persons/" + personId + "/persistedFaces?%s" % params, json.dumps(body), self.headers)
            response = self.conn.getresponse()
            data = response.read()
            print("FACE ADDED TO", targetName)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # returns a json list of people in a group
    def listPersonsInGroup(self, targetGroup):

        params = urllib.parse.urlencode({})

        try:
            self.conn.request("GET", "/face/v1.0/persongroups/" + targetGroup + "/persons?%s" % params, "{body}", self.headers)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def trainGroup(self, targetGroup):

        params = urllib.parse.urlencode({})

        try:
            self.conn.request("POST", "/face/v1.0/persongroups/" + targetGroup + "/train?%s" % params, "{body}", self.headers)
            response = self.conn.getresponse()
            data = response.read()
            print("GROUP TRAINED")
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def takeFrame(self):
        # cap = cv2.VideoCapture(0)
        #while(True):
        #     ret,img = cap.read()
        #
        #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #
        #     cv2.imshow('frame',gray)
        #
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        # cap.release()
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # if ret == True:
        # cv2.imshow('Frame',img)
        # while True:
        s, img = self.cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #
        cv2.imshow('frame',gray)
            # if cv2.waitKey(1) & 0xFF == ord('q'):

        #     faces = faceCascade.detectMultiScale(
        #         gray,
        #         scaleFactor=1.1,
        #         minNeighbors=5,
        #         minSize=(30, 30),
        #         #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        #     )
        #
        #     # for (x, y, w, h) in faces:
        #     #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #
        #     cv2.imshow('Attendance Recording System', img)
        #
        # #     if cv2.waitKey(10) & 0xFF == ord('q'):
        # #         break
        # # key = cv2.waitKey(0) & 0xFF
        #     cv2.waitKey(1) & 0xFF
        return img, cv2.imencode(".jpg",img)[1].tostring()

    # Returns faceId to be fed into identifyFace, returns -1 (integer) if no face found
    def detectFace(self, imgData):

        detectHeaders = {'Content-Type': 'application/octet-stream',
                   'Ocp-Apim-Subscription-Key': '7fc23cb44dc04fa79ad7061854f578b8'}

        url = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/detect'
        # print("aa")
        params = urllib.parse.urlencode({
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            # 'returnFaceAttributes': '{string}',
        })

        try:
            # response = requests.post(url, data=imgData, headers=headers, params=params)
            response = requests.post(url, headers=detectHeaders, data=imgData)
            return response.json()[0]["faceId"]
        except IndexError:
            print("NO FACE DETECTED")
            return -1
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def identifyFace(self, faceId, targetGroup):

        params = urllib.parse.urlencode({})

        body = {
            'faceIds' : [faceId],
            'personGroupId' : targetGroup
        }

        try:
            self.conn.request("POST", "/face/v1.0/identify?%s" % params, json.dumps(body), self.headers)
            response = self.conn.getresponse()
            data = json.loads(response.read())

            if not data or not data[0]["candidates"]:
                raise IndexError()

            candidatePersonId = data[0]["candidates"][0]["personId"]
            listOfPersons = json.loads(self.listPersonsInGroup(targetGroup))
            for person in listOfPersons:
                if person["personId"] == candidatePersonId:
                    print("PERSON IDENTIFIED: " + person["name"])
                    return person["name"]

        except IndexError:
            print("***** Idk something went wrong *****")
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def addStudentToDatabase(self, id, name, programme):
        query = "INSERT INTO students (studentID, studentName, studentProgramme) VALUES ('" + id + "', '" + name + "', '" + programme + "');"
        cursor.execute(query)
        cursor.commit()

    def takeAttendance(self, timetableKey,flag):
    # def takeAttendance(self, timetableKey):

        i =0
        try:
            while True :
                #print('Flag1 val '+str(flag1))
                # cam = cv2.VideoCapture(0)
                s, img = self.cam.read()

                # if flag:
                img = cv2.resize(img, (1000, 500))
                # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame',img)
                imgData = cv2.imencode(".jpg",img)[1].tostring()
                #
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                i=i+1;
                if i % 10000 == 0:
                    detectedFaceId = self.detectFace(imgData)
                    if detectedFaceId != -1:
                        studentId = self.identifyFace(detectedFaceId, "testgroup")
                        if studentId:
                            checkPresentQuery = "SELECT * FROM attendance WHERE (studentID = '" + studentId + "' AND timetableKey = '" + timetableKey + "');"
                            cursor.execute(checkPresentQuery)
                            data = cursor.fetchone()
                            if not data:
                                if data==1111111:
                                    data="2016IPG-031"
                                elif data==0000000:
                                    data="2016IPG-005"

                                print('Not in database, add:')
                                addQuery = "INSERT INTO attendance (studentID, timetableKey) VALUES ('" + studentId + "', '" + timetableKey + "');"
                                cursor.execute(addQuery)
                                cursor.commit()
                                self.personScanned = studentId
                            else:
                                # self.personScanned = studentId
                                print('Attendance already taken')
                # print(i)

                # img, imgData = self.takeFrame()
                # ret, frame = self.read()


            cam.release()
            cv2.destroyAllWindows()
        except KeyboardInterrupt:
            self.conn.close()

    def getLastPersonScanned(self):
        return self.personScanned

    def getStudentDetails(self, studentId):
        try:
            retrieveDetailsQuery = "SELECT * FROM students WHERE (studentID = '" + studentId + "');"
            cursor.execute(retrieveDetailsQuery)
            return cursor.fetchone()
        except Exception as e:
            print(e)

    def getCourseDetails(self, courseId):
        try:
            retrieveCourseQuery = "SELECT * FROM courses WHERE (courseID = '" + courseId + "');"
            cursor.execute(retrieveCourseQuery)
            return cursor.fetchone()
        except Exception as e:
            print(e)

    def getCourseAttendanceScore(self, studentId, courseId):
        try:
            retrieveTotalNoLecturesQuery = "SELECT timetableKey FROM timetable WHERE (courseID = '" + courseId + "');"
            cursor.execute(retrieveTotalNoLecturesQuery)
            totalNoLectures = len(cursor.fetchall())

            retrieveAllAttendancesQuery = "SELECT * FROM attendance WHERE (studentID = '" + studentId + "');"
            cursor.execute(retrieveAllAttendancesQuery)
            allAttendances = cursor.fetchall()

            totalNoAttendances = 0
            for attendance in allAttendances:
                attendanceQuery = "SELECT courseID FROM timetable WHERE timetableKey = '" + str(attendance[1]) + "';"
                cursor.execute(attendanceQuery)
                lectureCourseId = cursor.fetchone()
                if lectureCourseId:
                  if lectureCourseId[0] == courseId:
                      totalNoAttendances += 1

            score = round((totalNoAttendances/totalNoLectures)*100,1)
            return score, totalNoAttendances, totalNoLectures
        except Exception as e:
            print(e)


    def getOverallAttendanceScore(self, studentId):
        try:
            retrieveStudentCourseChoicesQuery = "SELECT courseID FROM studentsCourseChoices WHERE studentID = '" + studentId + "';"
            cursor.execute(retrieveStudentCourseChoicesQuery)
            studentChoices = cursor.fetchall()

            attendanceSum = 0
            lectureSum = 0

            for course in studentChoices:
                _, attendanceNo, lectureNo = self.getCourseAttendanceScore(studentId, course[0])
                attendanceSum += attendanceNo
                lectureSum += lectureNo

            totalScore = round((attendanceSum / lectureSum) * 100, 1)
            return totalScore

        except Exception as e:
            print(e)

    def wipeAttendanceLog(self, timetableKey):
        try:
            wipeAttendanceQuery = "DELETE FROM attendance WHERE timetableKey = '" + timetableKey + "';"
            cursor.execute(wipeAttendanceQuery)
            cursor.commit()
        except Exception as e:
            print(e)

    def getLectureAttendance(self, timetableKey):
        try:
            getAttendedStudents = "SELECT * FROM attendance WHERE timetableKey = '" + timetableKey + "';"
            cursor.execute(getAttendedStudents)
            attendedStudents = cursor.fetchall()

            getCourseId = "SELECT courseID FROM timetable WHERE timetableKey = '" + timetableKey + "';"
            cursor.execute(getCourseId)
            courseId = cursor.fetchone()

            getRegisteredStudents = "SELECT * FROM studentsCourseChoices WHERE courseID = '" + courseId[0] + "';"
            cursor.execute(getRegisteredStudents)
            registeredStudents = cursor.fetchall()

            score = round(len(attendedStudents)/len(registeredStudents)*100,2)
            return score

        except Exception as e:
            print(e)

    def getCourseAttendance(self, courseId):
        try:
            timetableKeys = self.getTimetableKeysFromCourseId(courseId)

            totalAttendees = 0
            for event in timetableKeys:
                getNoAttendees = "SELECT * FROM attendance WHERE timetableKey = '" + str(event) + "';"
                cursor.execute(getNoAttendees)
                attendeesNo = len(cursor.fetchall())
                totalAttendees += attendeesNo

            getRegisteredStudents = "SELECT * FROM studentsCourseChoices where courseID = '" + courseId + "';"
            cursor.execute(getRegisteredStudents)
            registeredStudents = len(cursor.fetchall())

            score = round(totalAttendees/(registeredStudents*len(timetableKeys)) * 100, 1)

            return score

        except Exception as e:
            print(e)

    def getTimetableKeysFromCourseId(self, courseId):
        try:
            getTimetableQuery = "SELECT timetableKey FROM timetable WHERE courseID = '" + courseId + "';"
            cursor.execute(getTimetableQuery)
            timetable = cursor.fetchall()

            timetableKeys = []
            for event in timetable:
                timetableKeys.append(event[0])

            return timetableKeys

        except Exception as e:
            print(e)

    def TrainInit(self):
        self.createGroup("testgroup", "hello group")
        self.addPerson("2016IPG-005", "testgroup")
        self.addPerson("2016IPG-031", "testgroup")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/1.JPG")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/2.JPG")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/3.JPG")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/4.JPG")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/5.JPG")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/6.jpg")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/7.jpg")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/8.jpg")
        self.addFace("2016IPG-005", "testgroup", "https://raw.githubusercontent.com/abhishek4s/pics/master/9.jpg")
        self.addFace("2016IPG-031", "testgroup", "https://github.com/dakshberry121/temp-pics/blob/master/1.jpg?raw=true")
        self.addFace("2016IPG-031", "testgroup", "https://github.com/dakshberry121/temp-pics/blob/master/2.jpg?raw=true")
        self.addFace("2016IPG-031", "testgroup", "https://github.com/dakshberry121/temp-pics/blob/master/3.jpg?raw=true")
        self.addFace("2016IPG-031", "testgroup", "https://github.com/dakshberry121/temp-pics/blob/master/4.jpg?raw=true")
        
        self.trainGroup("testgroup")
        time.sleep(2) # Give a second to train database

    def DatabaseInit(self):
       self.addStudentToDatabase("2016IPG-005", "Abhishek Arya", "IPG2016")
       self.addStudentToDatabase("2016IPG-031", "Daksh Berry", "IPG2016")
        

    def getStudentJson(self, studentId):
        studentDetails = self.getStudentDetails(studentId)

        studentDetailsDict = {
            "name" : studentDetails[1],
            "id" :  studentDetails[0],
            "degree" : studentDetails[2]
        }

        return json.dumps(studentDetailsDict)

    def getCoursesJson(self):
        try:
            getCoursesQuery = "SELECT * FROM courses"
            cursor.execute(getCoursesQuery)
            courses = cursor.fetchall()

            jsonObjects = []
            for course in courses:

                attendance = self.getCourseAttendance(course[1])

                courseDict = {
                "courseID" : course[1],
                "courseName" : course[2],
                "school" : course[3],
                "courseAbbreviation" : course[4],
                "attendance" : attendance
                }

                jsonObjects.append(json.dumps(courseDict))

            return jsonObjects

        except Exception as e:
            print(e)

    def getEventsJson(self,courseId):
        try:
            courseDetails = self.getCourseDetails(courseId)

            getTimetable = "SELECT * FROM timetable WHERE courseID = '" + courseId + "';"
            cursor.execute(getTimetable)
            timetable = cursor.fetchall()

            jsonObjects = []
            for event in timetable:
                attendance = self.getLectureAttendance(str(event[0]))

                eventDict = {
                "eventName" : event[4] + " - " + courseDetails[2],
                "start" : event[2],
                "end" : event[3],
                "attendance" : attendance
                }

                jsonObjects.append(json.dumps(eventDict))

            return jsonObjects

        except Exception as e:
            print(e)

    def main(self,flag,sub):
    # def main(self):
        # if flag:

        # self.TrainInit() # Init only once
        # self.DatabaseInit() # Also init only once
        # self.listPersonsInGroup("testgroup")
        # # print(self.getStudentDetails("0000000"))
        # print(self.getCourseDetails("IT01"))
        # print(self.getCourseAttendanceScore("0000000" ,"IT01"))
        # print(self.getOverallAttendanceScore("0000000"))
        # self.getStudentJson("0000000")
        # print(self.getLectureAttendance("1"))
        # print(self.getCourseAttendance("IT01"))
        # print(self.getTimetableKeysFromCourseId("IT01"))
        # self.getCoursesJson()
        # self.getEventsJson("IT01")
        # self.wipeAttendanceLog("1")
        print('--------------------------')
        # self.takeAttendance("1")
        if flag==1:
            #("start pid", r)
            #self.fetchSQLData()
            if sub==1:
                self.takeAttendance("1",flag)
            elif sub==2:
                self.takeAttendance("2",flag)
            elif sub==3:
                self.takeAttendance("3",flag)
            elif sub==4:
                self.takeAttendance("4",flag)
            elif sub==5:
                self.takeAttendance("5",flag)
            elif sub==6:
                self.takeAttendance("6",flag)
        else:
            # r=os.system("tasklist | findstr /spin \"python.exe\"")
            # r=os.system("taskkill /f /im python.exe ")
            # r=subprocess.check_output("tasklist | findstr /spin \"python.exe\"", shell=True)
            #flag1=False
            # s=os.getpid()
            #self.cv2.destroyAllWindows()

            self.cam.release()
            # cam = cv2.VideoCapture(0)
            #r=os.system("taskkill /pid ne "+str(s))
            #print('stop pid ',s)
        # else:
        #     # flag=0
        #     # if cv2.waitKey(1) & 0xFF == flag:
        #     cam.release()
        #     self.conn.close()

if __name__ == "__main__":
    app = FaceID()
    #flag=1

    app.main(flag,sub)
    # app.main()
