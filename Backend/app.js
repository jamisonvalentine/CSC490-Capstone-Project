var express = require('express');
var logger = require('morgan');
var cors = require('cors')
// Mongoose
const mongoose = require('mongoose');

const uncgCourseRouter = require('./routes/uncgRoute');
const ccCourseRouter = require('./routes/ccRoute');

require('dotenv').config();

var app = express();

const URI = process.env.MONGODB_URI;

mongoose.connect(URI, { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

const connection = mongoose.connection;
connection.once('open', () => {
  console.log("Connected to MongoDB");
})

app.use(cors());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use('/uncgcourse', uncgCourseRouter);
app.use('/cccourse', ccCourseRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
