var express = require('express');
var router = express.Router();
const fs = require('fs');
const fsPromises = fs.promises
var csv = require('jquery-csv');


/* GET home page. */
router.get('/', async function(req, res, next) {
    console.log("Express")
    var urlArray=['./source/2022-02_promenade.csv','./source/2022-02.csv']
    var firstMeasureArray = await readCSV(urlArray)
    res.json(firstMeasureArray)      
});

async function readCSV(url){
    var array = [];
    for(var i=0;i<url.length;++i){
        fsPromises.readFile(url[i], 'utf8' , (err, data) => {
            if (err) {
                console.error(err)
                return
            }
            var csvArray = csv.toObjects(data);
            array.push(csvArray[0]);
        }) 
    }
}
router.get('/json', async function(req, res, next) {
    console.log("Express")
    fs.readFile('./source/2020_Jahresdurchschnitt.json', 'utf8' , (err, data) => {
        if (err) {
            console.error(err)
            return
        }
        res.json(data);
    }) 
});

module.exports = router;
