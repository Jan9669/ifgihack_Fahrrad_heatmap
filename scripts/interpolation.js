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
            .bindPopup("<b>Zählstelle: </b>"+ json.features[i].properties.name + "<br> <b>Tägliche Durchfahrten: </b>" +json.features[i].properties.Durchschnitt_Tag)
        }
        $.ajax({
            url:"/turf/",
            method: "POST",
            data: JSON.stringify(json),
            contentType: "application/json"
        }).done(function(res){
            console.log(res)
            for(var i=0;i<res.length;++i){
            //     var calc_color = (  res.features[i].properties.amount > 9000 ? "#800026" :
            //                         res.features[i].properties.amount > 8000 ? "#bd0026" :            
            //                         res.features[i].properties.amount > 7000 ? "#e31a1c" :
            //                         res.features[i].properties.amount > 6000 ? "#fc4e2a" :
            //                         res.features[i].properties.amount > 5000 ? "#fd8d3c" :
            //                         res.features[i].properties.amount > 4000 ? "#feb24c" :
            //                         res.features[i].properties.amount > 3000 ? "#fed976" :
            //                         res.features[i].properties.amount > 2000 ? "#ffeda0" :
            //                         res.features[i].properties.amount > 1000 ? "#ffffcc" :
            //                         "#FFFFFF")
            var polygon = L.polygon(res[i].geometry.coordinates, {color: "blue", fillColor:"blue", fill:true, fillOpacity: 0.3});
            polygon.addTo(map)
            }
            
        })
    })

    
}
createMarker();
