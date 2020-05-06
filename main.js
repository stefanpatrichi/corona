const http = require('http');

http.createServer(function(req, res) {
  res.write('Hello NodeJS');
  res.end();
}).listen(8080);
