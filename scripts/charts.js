function createChart(){
    $.ajax({
        url:"/database/",
        method: "GET"
    }).done(function(res){
        console.log("HElloooooooooooooooooooooooooo")
        console.log(res)
        var options = {
            chart: {
              type: 'line'
            },
            series: [
              {
                name: 'Bikes per 15 Minutes',
                data: res
              }
            ],
            xaxis: {
              type:'datetime'
            },
            stroke:{
                curve:'smooth',
                colors: ['#CC5500'],
                width: 1
            },
          }
          
          var chart = new ApexCharts(document.querySelector('#chart'), options)
          chart.render()
    })
    
}
//createChart();
