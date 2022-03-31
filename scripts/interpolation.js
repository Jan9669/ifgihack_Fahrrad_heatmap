var map = L.map('mapdiv').setView([51.505, -0.09], 13);

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
        console.log(json)
        for(let i=0; i<count; ++i ){
            L.marker([json.features[i].geometry.coordinates[1], json.features[i].geometry.coordinates[0]]).addTo(map)
            .bindPopup(json.features[i].properties.Durchschnitt_Tag + " " + json.features[i].properties.name)
            .openPopup();
        }
        $.ajax({
            url:"/turf/",
            method: "POST",
            data: JSON.stringify(json),
            contentType: "application/json"
        }).done(function(res){
            for(var i=0;i<res.features.length;++i){
                console.log(res.features[i].properties.amount)
                var calc_color = (  res.features[i].properties.amount > 9000 ? "#DF1B1B" :
                                    res.features[i].properties.amount > 7500 ? "#BA373C" :            
                                    res.features[i].properties.amount > 6000 ? "#95525E" :
                                    res.features[i].properties.amount > 4500 ? "#6F6E7F" :
                                    res.features[i].properties.amount > 3000 ? "#4A89A1" :
                                    res.features[i].properties.amount > 1500 ? "#25A5C2" :
                                    "#FFFFFF")
                var polygon = L.polygon(res.features[i].geometry.coordinates, {color: calc_color, fillColor:calc_color, fill:true, fillOpacity: 1.0});
                polygon.bindPopup(res.features[i].properties.amount);
                polygon.addTo(map)
                
            }
        })
    })

    
}
createMarker();
