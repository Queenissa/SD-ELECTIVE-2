
var btn = document.getElementById('btn')
var message = document.getElementById('message')


btn.onclick = () => {
    console.log(message.value)
    client.publish('clue-message', message.value )
    message.value = "";
    
}


var broker = 'wss://mqtt.eclipse.org:443/mqtt';
var client  = mqtt.connect(broker);

client.on('connect', function () {
    console.log('Connected to '+broker)
})