function getCSVData(){
    $.ajax({
        url:"/csv",
        method: "GET",
      }).done(function(res){
        console.log(res[0]);
    })
}
