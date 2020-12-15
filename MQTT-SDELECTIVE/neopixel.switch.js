var broker = 'wss://mqtt.eclipse.org:443/mqtt'; 
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
    client.subscribe('quency/messages', function (err) {
        if (!err) {
            client.publish('quency/messages', 'Hello mqtt')
        }
    })
})


var pub_switch = document.getElementById('pub-switch');


pub_switch.onclick = () => {
    console.log(pub_switch.checked)
    client.publish('neopixelSwitch', (pub_switch.checked)? "enabled1":"disabled1" )
}






