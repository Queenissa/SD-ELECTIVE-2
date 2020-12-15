// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

// var broker = 'wss://mqtt.eclipse.org:443/mqtt';
var broker  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')
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

// client.on('message', function (topic, message) {
//   // message is Buffer
//   console.log(message.toString())
// //   client.end()
// })

// var pub_button = document.getElementById('pub-button');
// var pub_input = document.getElementById('pub-input');
// pub_button.addEventListener('click', () => {
//   // console.log('clicked');
//   // console.log(pub_input.value);
//   client.publish('junrey/messages', pub_input.value)
//   pub_input.value = "";
// })
var pub_switch0 = document.getElementById('pub-switch0');
var pub_switch1 = document.getElementById('pub-switch1');
var pub_switch2 = document.getElementById('pub-switch2');

pub_switch0.onclick = () => {
    console.log(pub_switch0.checked)
    client.publish('switch-control', (pub_switch0.checked)? "slider1Enabled":"slider1Disabled")
}

pub_switch1.onclick = () => {
    console.log(pub_switch1.checked)
    client.publish('switch-control', (pub_switch1.checked)? "slider2Enabled":"slider2Disabled")
}
pub_switch2.onclick = () => {
    console.log(pub_switch2.checked)
    client.publish('switch-control', (pub_switch2.checked)? "slider3Enabled":"slider3Disabled")
}