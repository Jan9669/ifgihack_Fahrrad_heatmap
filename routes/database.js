var express = require('express');
var router = express.Router();
const sqlite3 = require('sqlite3').verbose();


/* GET home page. */
router.post('/', function(req, res, next) {
    // open database in memory
    let db = new sqlite3.Database('./source/cycle_traffic.db',sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
        return console.error(err.message);
        }
        console.log('Connected to the in-memory SQlite database.');
    });
  
    db.serialize(() => {
        console.log(req.body[0].station_id)
      db.all("select sum, datetime from count_values where station_id = "+req.body[0].station_id+" and datetime like '2022_03_30 __:__'", function (err, tables) {
          console.log(tables)
          var data=[]
          for(var i=0;i<tables.length;++i){
            data.push({x:tables[i].datetime, y:tables[i].sum});
          }
          res.json(data)
      });
    });
  
    // close the database connection
    db.close((err) => {
        if (err) {
        return console.error(err.message);
        }
        console.log('Close the database connection.');
    });
});

module.exports = router;
