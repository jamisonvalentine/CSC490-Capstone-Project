const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const uncgCourseSchema = new Schema({
    uncgCourseSubject: {type:String, request:true},
    uncgClassID: {type:String, requried:true},
    ccCourseSubject: {type:String, request:true},
    ccClassID: {type: String, required:true}
});

module.exports = mongoose.model('UncgCourse', uncgCourseSchema);
