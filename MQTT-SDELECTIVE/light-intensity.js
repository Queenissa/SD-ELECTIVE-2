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

var slider = document.getElementById("myRange");

var lightIntensity = document.getElementById('light-intensity')

lightIntensity.innerHTML = slider.value; 

slider.oninput = function() {
    lightIntensity.innerHTML = this.value;
}



slider.onmouseup = function() {
    console.log(this.value)
    client.publish('lightIntensity', this.value)
}



