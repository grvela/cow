const filesystem = require('fs');
const qrcode = require('qrcode-terminal');
const axios = require('axios').default;

const { Client } = require('whatsapp-web.js');


const SESSION_FILE_PATH = './session.json';

let sessionData;
if(filesystem.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}

const client = new Client({
    session:sessionData
});


client.initialize();


client.on('qr', (qr) => {
	qrcode.generate(qr, {small: true});
});


client.on('ready', () => {
    console.log('Client is ready!');
});



client.on('authenticated', (session) => {
    sessionData = session;
    filesystem.writeFile(SESSION_FILE_PATH, JSON.stringify(session), function (err) {
        if (err) {
            console.error(err);
        }
    });
});


client.on('message', msg => {

            axios.post('http://localhost:5005/webhooks/rest/webhook', {
                'sender': 'User',
                'message': msg.body
            })
            .then(function(response){
                console.log(response.data)

            })
                   
});
