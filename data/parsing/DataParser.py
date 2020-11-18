import pandas as pd
import re
from datetime import datetime



globalSubject = []
globalClassID = []
globalSectionNumber = []
globalCourseName = []
globalTimeOfCourse = []
globalCourseBuilding = []
globalRoom = []
globalClassDays = []
globalDateRange = []
globalLocations = []
globalSemesterWeeks = []
globalSemester = []
globalYear = []
globalWebsite = []
globalCost = []
globalUncgID = []
globalUncgTitle = []

globalCounter = []


def determineEquivalencies(iterator):

    equivalencyDF = pd.read_csv("uncg_equivalencies.csv")

    comColID = equivalencyDF["caa_id"].to_list()
    uncgID = equivalencyDF["uncg_id"].to_list()
    uncgTitle = equivalencyDF["uncg_title"].to_list()

    fullComColCourse = globalSubject[iterator] + "-" + globalClassID[iterator]

    # check if course exists in equivalencies
    if comColID.count(fullComColCourse) > 0:

        globalCounter.append(fullComColCourse)

        # get the index of the equivalency
        equivalentIndex = comColID.index(fullComColCourse)

        # add UNCG title and ID at that index
        globalUncgID.append(uncgID[equivalentIndex])
        globalUncgTitle.append(uncgTitle[equivalentIndex])

    else:
        globalUncgID.append("No equivalency found")
        globalUncgTitle.append("No equivalency found")


def printResults(iterator):
    print("Subject is: " + globalSubject[iterator])
    print("Class ID is: " + globalClassID[iterator])
    print("Section Number is: " + globalSectionNumber[iterator])
    print("Course Name is: " + globalCourseName[iterator])
    print("Time of Course is: " + globalTimeOfCourse[iterator])
    print("Building is: " + globalCourseBuilding[iterator])
    print("Course Room is: " + globalRoom[iterator])
    print("Class days are:  " + globalClassDays[iterator])
    print("Class date range is:  " + globalDateRange[iterator])
    print("Number of weeks in semester: " + str(globalSemesterWeeks[iterator]))
    print("Class semester is: " + globalSemester[iterator])
    print("Class year is: " + globalYear[iterator])
    print("Class location is:  " + globalLocations[iterator])
    print("Class website is:  " + globalWebsite[iterator])
    print("Class cost is:  " + globalCost[iterator])
    print("UNCG course equivalent ID is: " + globalUncgID[iterator])
    print("UNCG course equivalent name is: " + globalUncgTitle[iterator])

    print("\n")


def standardizeOnline(iterator):
    location = str(df.iloc[iterator, 6])

    standardOnline = "Online"

    if "Internet-Based Course" in location:
        location = standardOnline
    elif "On line" in location:
        location = standardOnline
    elif "Online Course" in location:
        location = standardOnline
    elif "On-Line Courses" in location:
        location = standardOnline
    elif "Distance Ed" in location:
        location = standardOnline
    elif "Off Campus" in location:
        location = standardOnline
    elif "Off-Campus" in location:
        location = standardOnline
    elif "World Wide Web" in location:
        location = standardOnline
    elif "Internet/Distance Learning" in location:
        location = standardOnline
    elif "Asynchronous Online" in location:
        location = standardOnline
    elif "Synchronous Online" in location:
        location = standardOnline
    elif "Internet Courses" in location:
        location = standardOnline
    elif "Virtual Learning" in location:
        location = standardOnline
    elif "On Line" in location:
        location = standardOnline

    globalLocations.append(location)


def addWebsite(iterator):

    website = ""

    if "Alamance Community College" in collegeName[iterator] :
        website = "https://www.alamancecc.edu/"
    elif "Blue Ridge Community College" in collegeName[iterator] :
        website = "https://www.blueridge.edu/"
    elif "Caldwell Community College and Technical Institute" in collegeName[iterator] :
        website = "https://www.cccti.edu/"
    elif "Cape Fear Community College" in collegeName[iterator] :
        website = "https://cfcc.edu/"
    elif "Central Carolina Community College" in collegeName[iterator] :
        website = "https://www.cccc.edu/"
    elif "Cleveland Community College" in collegeName[iterator]:
        website = "https://clevelandcc.edu/"
    elif "College of the Albemarle" in collegeName[iterator]:
        website = "https://www.albemarle.edu/"
    elif "Craven Community College" in collegeName[iterator]:
        website = "https://cravencc.edu/"
    elif "Davidson County Community College" in collegeName[iterator]:
        website = "https://www.davidsonccc.edu/"
    elif "Durham Technical Community College" in collegeName[iterator]:
        website = "https://www.durhamtech.edu/"
    elif "Edgecombe Community College" in collegeName[iterator]:
        website = "https://www.edgecombe.edu/"
    elif "Gaston College" in collegeName[iterator]:
        website = "https://www.gaston.edu/"
    elif "Guilford Technical Community College" in collegeName[iterator]:
        website = "https://www.gtcc.edu/"
    elif "Johnston Community College" in collegeName[iterator]:
        website = "https://www.johnstoncc.edu/"
    elif "Lenoir Community College" in collegeName[iterator]:
        website = "https://www.lenoircc.edu/"
    elif "Nash Community College" in collegeName[iterator]:
        website = "https://www.nashcc.edu/"
    elif "Sandhills Community College" in collegeName[iterator]:
        website = "https://www.sandhills.edu/"
    elif "Wayne Community College" in collegeName[iterator]:
        website = "https://www.waynecc.edu/"
    elif "Wake Technical Community College" in collegeName[iterator]:
        website = "https://www.waketech.edu/"


    globalWebsite.append(website)



def extractSubIDandNum(iterator):
    section = df.iloc[iterator, 2]

    # split section on -
    splitSection = str(section).split("-")

    # take first value of split section
    classSubject = splitSection[0]

    # filter out junk values in edge cases
    classSubject = re.sub('[^0-9a-zA-Z]+', '', classSubject)

    # take second value of split section
    classID = splitSection[1]

    # take third value of split section
    classSectionNum = splitSection[2]

    # add ) back after splitting on )
    classSectionNum = [e + ")" for e in classSectionNum.split(")") if e]

    globalSubject.append(classSubject)
    globalClassID.append(classID)
    globalSectionNumber.append(classSectionNum[0])


def extractCourseName(iterator):
    section = df.iloc[iterator, 2]

    nameOfCourse = ""

    try:
        # get value after second space in section column
        nameOfCourse = "".join(section.split(" ", 2)[2])
    except:
        print("")

    globalCourseName.append(nameOfCourse)


def extractTime(iterator):
    dates = df.iloc[iterator, 5]

    # find time by locating : value and getting left and right sides
    time = dates[dates.find(':') - 2: dates.find(':') + 15]

    firstTime = time.split("-")[0][:-3]

    # ensure time matches proper format
    time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
    properTime = bool(time_re.match(firstTime))

    if time.find(':') == -1:
        time = "No time given"
    elif not properTime:
        time = "No time given"

    globalTimeOfCourse.append(time)



def extractBuilding(iterator):
    dates = df.iloc[iterator, 5]

    try:
        daysToFilter = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        # remove days from full date string so comma split below will work properly
        for day in daysToFilter:
            dates = dates.replace(day + ",", "")

        if "ONLNE" in dates or "Distance" in dates:
            building = "Online"
        elif "Times to be Announced" in dates:
            building = "TBA"
        else:
            # select right side of split on comma after filtering out days
            building = dates.split(",")[1]

            # remove excess trailing information for a few cases
            building = ",".join(building.split(",", 2)[:2])

        if (not building):
            building = "No building found"

        globalCourseBuilding.append(building)

    except:
      globalCourseBuilding.append("No building found")



def extractDays(iterator):
    dates = df.iloc[iterator, 5]
    days = ""

    acceptableDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # scan total dates string for days and add to days string if there are matches
    for day in acceptableDays:
        count = dates.count(day)
        if count > 0:
            days += day + ", "

    # remove final comma
    days = days.rsplit(',', 1)[0]

    if "to be Announced" in dates:
        days = "Days to be Announced"

    globalClassDays.append(days)


def extractDateRange(iterator):
    dates = df.iloc[iterator, 5]

    # extract left side after split on space to get date range
    dateRange = dates.split()[0].strip()

    globalDateRange.append(dateRange)


def extractRoom(iterator):
    try:
        dates = df.iloc[iterator, 5]

        # split right on Room to get everything after
        room = dates.rsplit("Room")[1]

        # split on parenthesis to remove trailing info after room
        room = room.split("(")[0]

        if "ONLNE" in dates or "ONLINE" in dates:
            room = "Online"

        if "Room to be Announced" in dates:
            room = "TBA"

        globalRoom.append(room)

    except:
         globalRoom.append("No room found")


def extractSemesterLength(iterator):
    dates = df.iloc[iterator, 5]

    # extract left side after split on space to get date range
    dateRange = dates.split()[0].strip()

    dateSplit = dateRange.split("-")

    # get date on left side
    firstDate = dateSplit[0].replace("/", "-")

    # get date on right side
    secondDate = dateSplit[1].replace("/", "-")

    # format with datetime module
    firstDate = datetime.strptime(firstDate, "%m-%d-%Y")
    secondDate = datetime.strptime(secondDate, "%m-%d-%Y")

    # get time difference between days and divide by 7 to get weeks
    difference = abs((secondDate - firstDate).days) / 7

    # add rounded result to global list
    globalSemesterWeeks.append(round(difference))


def calculateCost(iterator):

    credits = collegeCredits[iterator]
    cost = int(credits * 76)

    globalCost.append("$" + str(cost))


def extractSemester():
    globalSemester.append("Fall")


def extractYear():
    globalYear.append("2020")


def splitSection(iterator):
    extractSubIDandNum(iterator)
    extractCourseName(iterator)


def splitDates(iterator):
    extractDateRange(iterator)

    extractSemester()

    extractYear()

    extractSemesterLength(iterator)

    extractDays(iterator)

    extractTime(iterator)

    extractBuilding(iterator)

    extractRoom(iterator)


if __name__ == '__main__':

    df = pd.read_csv("wa_courses.csv")

    collegeName = df["college"].to_list()
    collegeCredits = df["credits"].to_list()
    collegeInstructor = df["instructor"].to_list()

    # iterate through all functions
    for i in range(0, len(collegeName)):
        print("Counter Variable is: " + str(i))
        splitSection(i)
        splitDates(i)
        standardizeOnline(i)
        addWebsite(i)
        calculateCost(i)
        determineEquivalencies(i)
        printResults(i)


    # construct new dataframe from old CSV and extracted values
    newDF = pd.DataFrame(
        {'College': collegeName,
         'Credits': collegeCredits,
         'Instructor': collegeInstructor,
         'CourseSubject': globalSubject,
         'ClassID': globalClassID,
         'SectionNumber': globalSectionNumber,
         'CourseName': globalCourseName,
         'Cost': globalCost,
         'TimeOfCourse': globalTimeOfCourse,
         'CourseBuilding': globalCourseBuilding,
         'CourseRoom': globalRoom,
         'ClassDays': globalClassDays,
         'Dates': globalDateRange,
         'WeeksInSemester': globalSemesterWeeks,
         'Semester': globalSemester,
         'Year': globalYear,
         'Location': globalLocations,
         'Website': globalWebsite,
         'UncgID': globalUncgID,
         'UncgTitle': globalUncgTitle
         })

    # save to CSV
    newDF.to_csv("Parsed Wa Courses Two.csv")