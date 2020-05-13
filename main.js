const http = require('http');
const fs = require('fs');
function get_last(filename, cb) {
  fs.readFile(filename, function(err, data) {
    if(err) throw err;

    var lines = data.toString('utf-8').split('\n');
    cb(null, lines[lines.length - 2]);
  });
}

function write_last(err, line) {
  http.createServer((req, res) => {
    res.end(line);
  }).listen(8080);
}

get_last('public/data/cases.in', write_last);
