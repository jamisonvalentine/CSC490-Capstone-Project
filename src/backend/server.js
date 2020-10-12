const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const uri = process.env.ATLAS_URI;
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true }
);
const connection = mongoose.connection;
connection.once('open', () => {
  console.log("Connected to MongoDB");
})

const uncgCourseRouter = require('./routes/uncgRoute');
const ccCourseRouter = require('./routes/ccRoute');


app.use('/uncgcourse', uncgCourseRouter);
app.use('/cccourse', ccCourseRouter);


app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});