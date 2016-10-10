?php echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
if ($_REQUEST['Digits']==1){ echo "<Response><Gather timeout=\"10\" finishOnKey=\"1\">
<Say voice=\"alice\">Do you think that sadness and disappointment are a regular part of life, and that happy people are only deceiving themselves?</Say>
<Pause length=\"1\"/>
</Gather>
<Gather timeout=\"10\" finishOnKey=\"1\">
<Say voice=\"alice\">Do you try to avoid dealing with other people?</Say>
</Gather>    
<Pause length=\"1\"/>
<Say voice=\"alice\">Thank you for your time and honesty Markus. May I redirect you to a human colleague of mine? He will listen and also give you some advice if you like.</Say> 
<Pause length=\"1\"/>
</Response>";
}else{ echo "<Response><Gather timeout=\"10\" finishOnKey=\"1\"><Say voice=\"alice\">Do you think that sadness and disappointment are a regular part of life, and that happy people are only deceiving t$
<Pause length=\"1\"/></Gather><Gather timeout=\"10\" finishOnKey=\"1\"><Say voice=\"alice\">Do you try to avoid dealing with other people?</Say></Gather>
<Pause length=\"1\"/><Say voice=\"alice\">Thank you for your time and honesty Markus. Seems like you are in a perfect mental condition! Have a nice day!</Say><Pause length=\"1\"/></Response>";}
?>
