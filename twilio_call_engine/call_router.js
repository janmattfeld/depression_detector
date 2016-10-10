'use strict';

const router = module.exports = require('express').Router();

var accountSid = ''; // Your Account SID from www.twilio.com/console
var authToken = '';   // Your Auth Token from www.twilio.com/console

var client = require('twilio')(accountSid, authToken);

router.get('/call', (req, res) => {
	client.makeCall({

		to:'+49', // Any number Twilio can call
		from: '+49', // A number you bought from Twilio and can use for outbound communication
		url: 'http://188.166.167.189/depressed-call.xml' // A URL that produces an XML document (TwiML) which contains instructions for the call

	}, function(err, responseData) {

		//executed when the call has been initiated.
		console.log(responseData.from); // Outputs calling number

	})
});