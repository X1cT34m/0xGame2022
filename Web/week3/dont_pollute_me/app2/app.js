var express = require('express');
const { exec } = require('child_process');


var app = express();
app.use(express.json()); 
app.use(express.urlencoded({ extended:true })); 
var user = {};
function merge(target, source) {
    for (let key in source) {
        if (key in source && key in target) {
            merge(target[key], source[key]);
        } else {
            target[key] = source[key];
        }
    }
    return true;
}

app.get('/time', (req, res) => { 

        let time = {
            "cmd1": "uptime",
        };
        for (let cmd in time) {
            exec(time[cmd], {shell:'/bin/bash'}, (err, stdout, stderr) => {
                if (err) {
                    return;
                }
	        });
        }
        res.send('time is a bi*ch')
})

app.post('/gotit', (req, res) => {
	var client = req.body;
    if(JSON.stringify(client)!=='{}'){
        console.log(client);
        for(key in Object.keys(user.__proto__)){
            delete user.__proto__[key];
        }
        try{
            merge(user,client)
        } catch(error) {
            res.send('error');
            return;
        }

        res.send('got it bro');
    }
    else{
        res.send('WTH is that?');
    }
})

app.get('/', (req, res) => {
    res.send('whats up bro');
})

app.get('/source', (req, res) => {
    res.download('app.js');
})

app.use(function(req, res, next) {
  res.status(404).send('404 not found');
});


app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.status(500).send('Error');
});


const port = 3000;
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
