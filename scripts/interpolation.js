var map = L.map('mapdiv').setView([51.96, 7.62], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
getCSVData();

async function createMarker(){
    $.ajax({
        url:"/csv/json",
        method: "GET",
      }).done(function(res){
        let json = JSON.parse(res);  
        var count = json.features.length;
        for(let i=0; i<count; ++i ){
            L.marker([json.features[i].geometry.coordinates[1], json.features[i].geometry.coordinates[0]]).addTo(map)
            .on('click', markerOnClick);
        }
        $.ajax({
            url:"/turf/",
            method: "POST",
            data: JSON.stringify(json),
            contentType: "application/json"
        }).done(function(res){
            console.log(res)
            for(var i=0;i<res.length;++i){
            var polygon = L.polygon(res[i].geometry.coordinates, {color: "blue", fillColor:"blue", fill:true, fillOpacity: 0.3});
            polygon.addTo(map)
            }
            
        })
    })

    
}
createMarker();

function markerOnClick(e){
    var criteria = [];
    document.getElementById("chart").style="visibility:visible"
    var marker = this;
    criteria.push({coordinates:e.latlng})
    dbTest(criteria)
}

function dbTest(criteria){
    $.ajax({
        url:"/database/",
        method: "POST",
        data: JSON.stringify(criteria),
        contentType: "application/json"
    }).done(function(res){
        console.log("DB done")
        console.log(res)
    })
}