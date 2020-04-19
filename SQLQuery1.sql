CREATE TABLE dbo.courses
(
	courseKey int ,
	courseID Nvarchar(50),
	courseName Varchar(50),
	Department Nvarchar(50),
	courseAbbreviation Varchar(10)
)
GO

INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('1','IT01','Wireless Communications','IPG2016','WCT')
INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('2','IT02','Modeling and Simulations','IPG2016','MS')
INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('3','IT03','Informations and System Security','IPG2016','ISS')
INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('4','IT04','Artificial Intelligence','IPG2016','AI')
INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('5','IT05','Ecosystem and Sustainable Development','IPG2016','ECOSD')
INSERT INTO courses (courseKey,courseID,courseName,Department,courseAbbreviation) VALUES('6','IT06','Foreign Language','IPG2016','FL')
GO
	

