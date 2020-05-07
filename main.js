const http = require('http');
const fs = require('fs');
const { exec } = require('child_process');
function get_last(filename, cb) {
  fs.readFile(filename, function(err, data) {
    if(err) throw err;

    var lines = data.toString('utf-8').split('\n');
    cb(null, lines[lines.length - 2]);
  });
}

function write_last(err, line) {
  exec('cd src && python3 main.py', function (error, stdout, stderr) {
    if(error) {
      console.log('error: ' + error.message);
      return;
    }
    console.log(stdout);
  });
  http.createServer(function(req, res) {
    res.write(line);
    res.end();
  }).listen(8080);
}

get_last('public/data/cases.in', write_last);
