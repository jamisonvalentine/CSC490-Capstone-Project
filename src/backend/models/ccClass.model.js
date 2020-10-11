const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ccCourseSchema = new Schema({
    ccCourseID: {type: String, required: true},
    collegeName: {type: String, required: true},
    courseName: {type: String, required: true},
    sectionNumber: {type: Number, required: true},
    time: {type: String, required: true},
    courseBuilding: {type: String, required: true},
    courseRoom: {type: String, required: true},
    classDays: {type: String, required: true},
    dates: {type: String, required: true}, 
    location: {type: String, required: true}
});

module.exports = mongoose.model('ccCourse', ccCourseSchema);