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
    console.log(points)
    var collection = turf.featureCollection(points);
    var options = {gridType: 'square', property: 'amount', units: 'kilometers'};
    var grid = turf.interpolate(collection, 0.1, options); 
    res.json(grid)
});

module.exports=router;