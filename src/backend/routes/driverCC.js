const router = require('express').Router();
let ComColCourse = require('../models/ccClass.model.js');

// handle HTTP get requests on /course/ URL 
router.route('/').get((req, res) => {
  ComColCourse.find()
    .then(course => res.json(course))
    .catch(err => res.status(400).json('Error: ' + err));
});


// handles get request for /courses/find/ URL path
router.route('/find').get((req, res) => {

  ComColCourse.find({ComColCourseID: req.body.ComColCourse})
      .then(course => res.json(course))
      .catch(err => res.status(400).json('Error: ' + err));
  });

  module.exports = router;
