const router = require('express').Router();
let ComColCourse = require('../models/ccClass.model');

// handle HTTP get requests on /course/ URL 
router.route('/').get((req, res) => {
  ComColCourse.find()
    .then(course => res.json(course))
    .catch(err => res.status(400).json('Error: ' + err));
});


// handles get request for /courses/find/ URL path
router.route('/find').get((req, res) => {
  ComColCourse.find({ClassID: req.body.ClassID, CourseSubject: req.body.CourseSubject})
      .then(course => res.json(course))
      .catch(err => res.status(400).json('Error: ' + err));
  });

  module.exports = router;