from flask import Flask, render_template, request, redirect,send_from_directory
import main2 as pro
import importlib as il
import json
from fpdf import FPDF
import pdfkit
from datetime import datetime

app = Flask(__name__)
attendanceApp = pro.FaceID()
sub=0
counter=0
fix=0
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stops", methods=["GET", "POST"])
def stops():
    # if sub==1:
    #     attendanceApp.wipeAttendanceLog("1")
    #     attendanceApp.main(0,sub)
    # elif sub==2:
    #     attendanceApp.wipeAttendanceLog("2")
    #     attendanceApp.main(0,sub)
    # elif sub==3:
    #     attendanceApp.wipeAttendanceLog("3")
    #     attendanceApp.main(0,sub)
    # elif sub==4:
    #     attendanceApp.wipeAttendanceLog("4")
    #     attendanceApp.main(0,sub)
    # elif sub==5:
    #     attendanceApp.wipeAttendanceLog("5")
    #     attendanceApp.main(0,sub)
    # elif sub==6:
    #     attendanceApp.wipeAttendanceLog("6")
    #     attendanceApp.main(0,sub)
    attendanceApp.main(0,sub)
    il.reload(pro)
    return render_template("index.html")

# @app.route("/createPDF", methods=["GET", "POST"])
# def createPDF():
#     # return render_template("empty.html")
#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Attendance Report", ln=1, align="C")
    # for i in range(1,10):
    #     pdf.cell(200, 10, int=i, ln=1, align="C")

    # pdf.output("Attendance_report.pdf")
    # return render_template("empty.html")
    # attendanceApp.main(0)
    # il.reload(UV)
    # return render_template("index.html")

    # self.conn.close()
@app.route("/course", methods=["GET", "POST"])
def courses():
    sub=1
    attendanceApp.wipeAttendanceLog("2")
    attendanceApp.wipeAttendanceLog("3")
    attendanceApp.wipeAttendanceLog("4")
    attendanceApp.wipeAttendanceLog("5")
    attendanceApp.wipeAttendanceLog("6")
    #sub=3
#     if request.method == "GET":
#         return render_template("courses.html")
# # def cool_form():
#     # elif request.method == "POST":
#     #     # do stuff when the form is submitted
#     #
#     #     # redirect to end the POST handling
#     #     # the redirect can be to the same route or somewhere else
#     #     return redirect(url_for('index'))
#
#     # POST request
#     elif request.method == "POST":
    attendanceApp.main(1,1)
@app.route("/course1", methods=["GET", "POST"])
def courses1():
    sub=2
    attendanceApp.wipeAttendanceLog("1")
    attendanceApp.wipeAttendanceLog("3")
    attendanceApp.wipeAttendanceLog("4")
    attendanceApp.wipeAttendanceLog("5")
    attendanceApp.wipeAttendanceLog("6")
    attendanceApp.main(1,2)

@app.route("/course2", methods=["GET", "POST"])
def courses2():
    sub=3
    attendanceApp.wipeAttendanceLog("1")
    attendanceApp.wipeAttendanceLog("2")
    attendanceApp.wipeAttendanceLog("4")
    attendanceApp.wipeAttendanceLog("5")
    attendanceApp.wipeAttendanceLog("6")
    attendanceApp.main(1,3)

@app.route("/course3", methods=["GET", "POST"])
def courses3():
    sub=4
    attendanceApp.wipeAttendanceLog("1")
    attendanceApp.wipeAttendanceLog("3")
    attendanceApp.wipeAttendanceLog("2")
    attendanceApp.wipeAttendanceLog("5")
    attendanceApp.wipeAttendanceLog("6")
    attendanceApp.main(1,4)

@app.route("/course4", methods=["GET", "POST"])
def courses4():
    sub=5
    attendanceApp.wipeAttendanceLog("1")
    attendanceApp.wipeAttendanceLog("3")
    attendanceApp.wipeAttendanceLog("4")
    attendanceApp.wipeAttendanceLog("2")
    attendanceApp.wipeAttendanceLog("6")
    attendanceApp.main(1,5)

@app.route("/course5", methods=["GET", "POST"])
def courses5():
    sub=6
    attendanceApp.wipeAttendanceLog("1")
    attendanceApp.wipeAttendanceLog("3")
    attendanceApp.wipeAttendanceLog("4")
    attendanceApp.wipeAttendanceLog("5")
    attendanceApp.wipeAttendanceLog("2")
    attendanceApp.main(1,6)

@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method == "GET":
        coursesList = attendanceApp.getCoursesJson()
        coursesListOfDicts = []
        for course in coursesList:
            coursesListOfDicts.append(json.loads(course))
        return render_template("list.html", coursesList=coursesListOfDicts)

    # POST request
    else:
        return redirect("/list")


@app.route("/createPDF")
def generatePDF():
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-bottom': '0.75in',
        'margin-right': '0.75in',
        'margin-left': '0.75in',
    }

    result = attendanceApp.fetchSQLData()
    for j in result:
        fix=j[1]
    # if sub==1:
    #      attendanceApp.wipeAttendanceLog("1")
    # #     attendanceApp.main(0,sub)
    # elif sub==2:
    #      attendanceApp.wipeAttendanceLog("2")
    # #     attendanceApp.main(0,sub)
    # elif sub==3:
    #      attendanceApp.wipeAttendanceLog("3")
    # #     attendanceApp.main(0,sub)
    # elif sub==4:
    #      attendanceApp.wipeAttendanceLog("4")
    # #     attendanceApp.main(0,sub)
    # elif sub==5:
    #      attendanceApp.wipeAttendanceLog("5")
    # #     attendanceApp.main(0,sub)
    # elif sub==6:
    #      attendanceApp.wipeAttendanceLog("6")
    #     attendanceApp.main(0,sub)
    if fix==1:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Wireless and Communication Technlogies (IT01)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Prof.Aditya Trivedi</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")

    elif fix==2:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Modelling and Simulation(IT02)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Dr. Ajay Kumar</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")

    elif fix==3:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Information and System security (IT03)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Dr. Saumya Bhadauria</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")

    elif fix==4:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Artficial Intelligence(IT04)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Dr. Ritu Tiwari</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")

    elif fix==5:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Ecosystem and Sustainable Development(IT05)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Dr. Arun Agariya</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")

    elif fix==6:
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                        }
                        th, td {
                            padding-left: 10px;
                        }
                        body {
                            width: 100%;
                        }
                        table {
                            width: 98%;
                        }
                        h2   {text-align: center;}
                    </style>
                </head>
                <body>


                    <p id="date"></p>
        <script>
        document.getElementById("date").innerHTML = Date();
        </script>
        <h2>Attendance Report(IPG 2016)</h2>
        <h2>Foreign Language(IT06)</h2>
                        <table>
                            <tr>
                                <th>Sr no.</th>
                                <th>Present students Roll No.</th>
                            </tr>
            """
        footer = """

                    </table>
                </body>
            </html>
            <footer>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <br>
              <p>Faculty Coordinator: Dr. L Bhutia</p>
            </footer>
        """
        body = ''
        counter=0
        for i in result:
            counter=counter+1
            body = body + f'<tr><td>{counter}</td><td>{i[0]}</td></tr>'

        pdfkit.from_string(header+body+footer, 'attendance.pdf', configuration=config, options=options)
        return render_template("index.html")


@app.route("/poll")
def poll():
    lastPersonScannedId = attendanceApp.getLastPersonScanned()
    #personScannedData = '{"ID" : "' + lastPersonScannedId + '"}'
    personScannedData = attendanceApp.getStudentJson(lastPersonScannedId)
    return personScannedData

if __name__ == '__main__':
    app.run(debug=True)
