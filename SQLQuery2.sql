CREATE TABLE dbo.timetable
(
	timetableKey int ,
	courseID Nvarchar(50),
	starttime int ,
	endtime int ,
	eventName Nvarchar(50)
)
GO

INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('1','IT01','9','10','WCT')
INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('2','IT02','10','11','MS')
INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('3','IT03','11','12','ISS')
INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('4','IT04','12','13','AI')
INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('5','IT05','14','15','ECOSD')
INSERT INTO timetable (timetableKey,courseID,starttime,endtime,eventName) VALUES('6','IT06','15','16','FL')
GO