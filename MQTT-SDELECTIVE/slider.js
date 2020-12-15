
var broker = 'wss://mqtt.eclipse.org:443/mqtt';
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
})

let clueValue = {
    temperature: 0,
    pressure: 1013,
    gyro_x: 0,
    gyro_y: 0,
    gyro_z: 0,
    accelerometer_x:0,
    accelerometer_y:0,
    accelerometer_z:0,
    magnetic_x:0,
    magnetic_y:0,
    magnetic_z:0,
    humidity:0,
    proximity: 0,
    color_r: 0,
    color_g: 0,
    color_b: 0,
    color_c: 0,
};


const functions = {
    input: (e) => {
        let name = e.target.name;
        let value = $(`input[name=${name}]`).val();
        $(`#${name}`).text(value);                
    },
    mouseup: (e) => {
        let name = e.target.name;
        let value = $(`input[name=${name}]`).val();
        clueValue[name] = value;
        client.publish('slider-clue', JSON.stringify(clueValue));
    }
};

const sliders = $(".slider");
console.log(sliders);
for(let slider of sliders) {
    for(let key in functions) {
        slider.addEventListener(key, functions[key]);
    }
}