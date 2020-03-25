const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const events = require('./events');
const connection = mysql.createConnection({
  host     : '127.0.0.1',
  user     : 'root',
  password : 'root',
  database : 'subscriber'
});
connection.connect();
connection.query('SELECT 1 + 1 AS solution', function (err, rows, fields) {
  if (err) throw err

  console.log('The solution is: ', rows[0].solution)
})

const port = process.env.PORT || 8080;
const app = express()
  .use(cors())
  .use(bodyParser.json())
  .use(events(connection));
app.get('/', function(req, res){
  console.log("This is home!!");
});
app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
}).on('error', function (err) {
  if(err.errno === 'EADDRINUSE') {
      console.log(`----- Port ${port} is busy, trying with port ${port + 1} -----`);
  } else {
      console.log(err);
  }
});;
app.get('/express_backend', (req, res) => {
    res.send({ express: 'Subscriber is live' });
  });

  app.get('/user', (req, res, next) => {
    connection.query(
        "SELECT * FROM user",
        (error, results) => {
            if (error){
            console.error(error);
            res.status(500).json({status: 'error'});
            }
            else{
              res.status(200).json(results);
            }
          }
      );
  });
  
  