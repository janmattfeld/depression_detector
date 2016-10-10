<?php
if (PHP_SAPI === 'cli') {
    $argument1 = $argv[1];
}
else {
    $argument1 = $_GET['argument1'];
}
 
// Get the PHP helper library from twilio.com/docs/php/install
require_once('/root/twilio-twilio-php-d7d9be9-2/Services/Twilio.php'); // Loads the library
 
// Your Account Sid and Auth Token from twilio.com/user/account
$sid = „some_sid“; 
$token = „some_token“; 
$client = new Services_Twilio($sid, $token);
 
$call = $client->account->calls->create("+4915735982123", $argument1, "http://188.166.167.189/depressed-call.xml", array());
echo $call->sid;
 
 
 
 
 
 
 
