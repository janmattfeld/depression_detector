'use strict';

/*
 * An express server to start the twilio help call on GET http://localhost:1337/call
 */

var express = require('express');
var app = express();

const callRouter = require('./call_router');
app.use('/', callRouter);

app.listen(process.env['PORT'] || 1337);