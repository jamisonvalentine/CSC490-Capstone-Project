import pandas as pd
import re

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


def printResults(counter):
    print("Subject is: " + globalSubject[counter])
    print("Class ID is: " + globalClassID[counter])
    print("Section Number is: " + globalSectionNumber[counter])
    print("Course Name is: " + globalCourseName[counter])
    print("Time of Course is: " + globalTimeOfCourse[counter])
    print("Building is: " + globalCourseBuilding[counter])
    print("Course Room is: " + globalRoom[counter])
    print("Class days are:  " + globalClassDays[counter])
    print("Class date range is:  " + globalDateRange[counter])
    print("Class location is:  " + globalLocations[counter])

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

    globalLocations.append(location)


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


def splitSection(iterator):
    extractSubIDandNum(iterator)
    extractCourseName(iterator)


def extractTime(iterator):
    dates = df.iloc[iterator, 5]

    # find time by locating : value and getting left and right sides
    time = dates[dates.find(':') - 2: dates.find(':') + 15]

    if time.find(':') == -1:
        time = "No time given"

    globalTimeOfCourse.append(time)


def extractBuilding(iterator):
    dates = df.iloc[iterator, 5]

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


def splitDates(iterator):
    extractDateRange(iterator)

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
        printResults(i)

    # construct new dataframe from old CSV and extracted values
    newDF = pd.DataFrame(
        {'College': collegeName,
         'Credits:': collegeCredits,
         'Instructor': collegeInstructor,
         'Course Subject': globalSubject,
         'Class ID': globalClassID,
         'Section Number': globalSectionNumber,
         'Course Name': globalCourseName,
         'Time of Course': globalTimeOfCourse,
         'Course Building': globalCourseBuilding,
         'Course Room': globalRoom,
         'Class Days': globalClassDays,
         'Dates': globalDateRange,
         'Location': globalLocations
         })

    # save to CSV
    newDF.to_csv("Output.csv")
