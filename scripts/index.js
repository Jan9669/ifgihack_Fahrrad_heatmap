var map = L.map('mapdiv').setView([51.96, 7.62], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
getCSVData();

var jsonSave="";
polyGroup = L.layerGroup();

async function createMarker(){
    $.ajax({
        url:"/csv/json",
        method: "GET",
      }).done(function(res){
        let json = JSON.parse(res);  
        jsonSave=json
        var count = json.features.length;
        console.log(json.features[0].properties)
        for(let i=0; i<count; ++i ){
            L.marker([json.features[i].geometry.coordinates[1], json.features[i].geometry.coordinates[0]]).addTo(map)
            .on('click', markerOnClick)
            .feature={
                properties:{id:json.features[i].properties.id}
            }
        }
        createBuffer(json);
    })

    
}
createMarker();

function markerOnClick(e){
    let mode=document.getElementById("mode_select");
    console.log(jsonSave)
    console.log(e)
    if(mode.value==1){
        e.sourceTarget.unbindPopup();
        for(let i=0;i<jsonSave.features.length;++i){
            if(e.latlng.lat==jsonSave.features[i].geometry.coordinates[1] && e.latlng.lng==jsonSave.features[i].geometry.coordinates[0]){
                e.sourceTarget.bindPopup("<b>Messtation: </b>"+jsonSave.features[i].properties.name+"<br> <b>Fahrräder pro Tag:</b> "+jsonSave.features[i].properties.Durchschnitt_Tag).openPopup();
            }
        }
    }else if(mode.value==2){
        e.sourceTarget.unbindPopup();
        var criteria = [];
        document.getElementById("chart").style="visibility:visible"
        console.log(e.sourceTarget)
        criteria.push({station_id: e.sourceTarget.feature.properties.id})
        console.log(criteria)
        dbTest(criteria)
    }   
}

function createBuffer(json){
    $.ajax({
        url:"/turf/",
        method: "POST",
        data: JSON.stringify(json),
        contentType: "application/json"
    }).done(function(res){
        console.log(res)
        for(var i=0;i<res.length;++i){
        polyGroup.addLayer(L.polygon(res[i].geometry.coordinates, {color: "blue", fillColor:"blue", fill:true, fillOpacity: 0.3}));
        polyGroup.addTo(map)
        }
    })
}

function dbTest(criteria){
    $.ajax({
        url:"/database/",
        method: "POST",
        data: JSON.stringify(criteria),
        contentType: "application/json"
    }).done(function(res){
        createChart(res);
        console.log("DB done")
        console.log(res)
    })
}

function changeInput(mode){
    if(mode==1){
        document.getElementById("datepicker").style="display:none;";
        document.getElementById("yearSelect").style="display:inline-block;";
        document.getElementById("chart").style.visibility="hidden"
        polyGroup.clearLayers();
        createBuffer(jsonSave)
    }else if(mode==2){
        document.getElementById("datepicker").style="display:inline-block;"
        document.getElementById("yearSelect").style="display:none;";
        map.removeLayer(polyGroup)
    }
}