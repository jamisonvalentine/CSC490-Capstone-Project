const router = require('express').Router();
let UncgCourse = require('../models/uncgClass.model');

router.route('/').get((req, res) => {
    UncgCourse.find()
      .then(course => res.json(course))
      .catch(err => res.status(400).json('Error: ' + err));
  });

router.route('/add').post((req, res) => {
    const uncgCourseID = req.body.uncgCourseID;
    const ccCourseID = req.body.ccCourseID;
  
    const course = new UncgCourse({
      uncgCourseID, 
      ccCourseID
    });
  
    course.save()
    .then(() => res.json('Course added'))
    .catch(err => res.status(400).json('Error: ' + err));
  });

router.route('/find').get((req, res) => {
    UncgCourse.find({uncgCourseID: req.body.uncgCourseID})
      .then(course => res.json(course))
      .catch(err => res.status(400).json('Error: ' + err));
  });

  module.exports = router;