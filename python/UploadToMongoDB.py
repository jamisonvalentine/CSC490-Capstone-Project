import pymongo
import csv

myclient = pymongo.MongoClient("PASTE URI HERE")

data = csv.DictReader(open("Parsed Wa Courses.csv"))

mydb = myclient["ExerciseTracker"]
mycol = mydb["CCcourses"]

mycol.insert_many(list(data))
