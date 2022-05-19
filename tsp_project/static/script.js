var map=new MapmyIndia.Map("map",{ center:[28.61, 77.23],zoomControl: true,hybrid:true });
let loc="";
map.on("click", function (e)
{
var pt = e.latlng; //event returns lat lng of clicked point
    console.log(pt);
    L.marker([pt.lat,pt.lng]).addTo(map);
    loc+=pt.lng+","+pt.lat+";";
//Do your related operation here
});
// -122.42,37.78;-122.45,37.91;-122.48,37.73
document.getElementById('submit-btn').addEventListener('click',findDistanceMatrix);

async function findDistanceMatrix(){
    var link="https://api.mapbox.com/directions-matrix/v1/mapbox/driving/"+loc.slice(0,loc.length-1)+"?approaches=curb;curb;curb;curb&access_token=pk.eyJ1Ijoia3VzaDc4IiwiYSI6ImNsMzVqZHF3djBmMWMza3A1c2MzY3Y1NjkifQ.-PI6HfCVSnQVi5MguiQISQ";
    let response = await fetch(link);
    let data = await response.json();
    console.log(data);
}
