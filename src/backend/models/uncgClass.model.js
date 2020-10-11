const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const uncgCourseSchema = new Schema({
    uncgCourseID: {type:String, requried:true},
    ccCourseID: {type: String, required:true}
});

module.exports = mongoose.model('Course', uncgCourseSchema);
