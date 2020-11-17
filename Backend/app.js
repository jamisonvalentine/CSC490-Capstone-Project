var express = require('express');
var logger = require('morgan');
var cors = require('cors')
// Mongoose
const mongoose = require('mongoose');
const createError = require('http-errors');
const path = require('path');
const uncgCourseRouter = require('./routes/uncgRoute');
const ccCourseRouter = require('./routes/ccRoute');
const contactUsRouter = require('./routes/contactUsRoute');

var app = express();
const PORT = process.env.PORT || 8080;


require('dotenv').config();

const uri = process.env.MONGODB_URI;
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true }
);
const connection = mongoose.connection;
connection.once('open', () => {
  console.log("Connected to MongoDB");
})

app.use(cors());
app.use(logger('dev'));
app.use(express.json());

app.use('/uncgcourse', uncgCourseRouter);
app.use('/cccourse', ccCourseRouter);
app.use('/contactUs', contactUsRouter);

app.use(express.static('Frontend/build'));
app.get('*', (request, response) => {

  response.sendFile("Frontend/build/index.html");

});



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
  res.json({
    message: err.message,
    error: err
  });
});

if(process.env.NODE_ENV === 'production') {
  app.use(express.static('Frontend/build'));
  
  app.get('*', (request, response) => {

  response.sendFile("Frontend/build/index.html");

  });
 
}
app.listen(PORT, () => {
  console.log(`Our app is running on port ${ PORT }`);
});
module.exports = app;
