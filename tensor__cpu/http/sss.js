var http = require("http");

var options = {
  "method": "POST",
  "hostname": "10.33.2.231",
  "port": "8008",
  "path": "/rec/idcard/",
  "headers": {
    "content-type": "application/json",
    "cache-control": "no-cache",
    "postman-token": "15a11d94-c964-f65f-e088-93cb8894d151"
  }
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({ appid: '123456',
  card_type: 0,
  url_list: [ 'http://10.33.2.69:8008/id_img/20171130/43062619930120585X_0.JPG' ] }));
req.end();