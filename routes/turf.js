var express = require('express');
var router = express.Router();
var turf = require("@turf/turf");


/* GET home page. */
router.post('/', function(req, res, next) {
    var points=[];
    for(let i=0; i<req.body.features.length;++i){
        var coordPair = [req.body.features[i].geometry.coordinates[1],req.body.features[i].geometry.coordinates[0]]
        var point = turf.point(coordPair,{name:req.body.features[i].properties.name, amount: req.body.features[i].properties.Durchschnitt_Tag})
        points.push(point)
    }
    var buffered = [];
    var collection = turf.featureCollection(points);
    console.log(collection)
    for(var i=0; i<collection.features.length;++i){
        buffered.push(turf.buffer(collection.features[i], (collection.features[i].properties.amount/50000), {units: 'kilometers'})); 
    }
    res.json(buffered)
});

module.exports=router;