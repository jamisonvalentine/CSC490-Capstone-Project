const router = require('express').Router();
let ComColCourse = require('../models/ccClass.model');

// handle HTTP get requests on /course/ URL 
router.route('/').get((req, res) => {
  ComColCourse.find()
    .then(course => res.json(course))
    .catch(err => res.status(400).json('Error: ' + err));
});

// handle HTTP get requests on /course/college URL
router.route('/college').get((req, res) => {
  ComColCourse.find().distinct('College')
    .then(course => res.json(course))
    .catch(err => res.status(400).json('Error: ' + err));
});


// handles get request for /courses/find/ URL path
router.route('/find').get((req, res) => {
  let date = req.query.date;
  ComColCourse.find({ClassID: req.query.ClassID, CourseSubject: req.query.CourseSubject, CourseRoom : req.query.classType})
      .then(course => res.json(course))
      .catch(err => res.status(400).json('Error: ' + err));
  }
);

module.exports = router;