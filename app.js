var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var csvRouter = require('./routes/csv');
var turfRouter = require('./routes/turf');
var databaseRouter = require('./routes/database');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/scripts', express.static(__dirname + '/scripts/'));
app.use('/csv',csvRouter);
app.use('/turf',turfRouter);
app.use('/database',databaseRouter)


module.exports = app;
