
var joy = new JoyStick("joyDiv");

var direction = document.getElementById('direction');

setInterval(function(){
    direction.value = joy.GetDir();
    console.log(direction.value);
    client.publish('joystick-microbit', direction.value);
}, 1500)



var broker = 'wss://mqtt.eclipse.org:443/mqtt';
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header');

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
    
}) 