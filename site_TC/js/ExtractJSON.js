//JSON
var header = document.querySelector("header");
var section = document.querySelector("section");
//var section = document.querySelector("map");

//lien du json
var requestURL = "../../RecupLigne.json"; //peut mettre un lien github : 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';
//ATTENTION a l'endroit ou on enregistre le json

var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
    var repRequete = request.response;
    foncAffichage(repRequete);
}


function foncAffichage(jsonObj) {

  let ListeRangement = [];
  let ListeX = [];
  let ListeY = [];

  for (var j = 0 ; j<Object.keys(jsonObj).length ;j++){
    var mur = jsonObj[String(j)];
    console.log("mur numero : " + j);

    for (var i =0; i<2; i++){
      console.log("first " + mur[0].First[0][i]);
      console.log( "finish " + mur[0].Finish[0][i]);
      ListeRangement.push(mur[0].First[0][i]);
      ListeRangement.push(mur[0].Finish[0][i]);
    }

    ListeX.push(mur[0].First[0][0]);
    ListeX.push(mur[0].Finish[0][0]);
    ListeY.push(mur[0].First[0][1]);
    ListeY.push(mur[0].Finish[0][1]);
  
  }

  console.log(ListeX);

  Xmax=Math.max(...ListeX);
  Xmin=Math.min(...ListeX);
  Ymax=Math.max(...ListeY);
  Ymin=Math.min(...ListeY);

  AffichagePropre(ListeRangement,Xmax,Xmin,Ymax,Ymin);
  
}

function AffichagePropre(ListeRangement,Xmax,Xmin,Ymax,Ymin) {
  var canvas = document.querySelector('.map');
  var ctx = canvas.getContext('2d')
  //ctx.strokeStyle='white';

  console.log($(".map").height());
  var multiX = $(".map").width(); //Width canvas
  var multiY = $(".map").height(); //Height canvas
  var MaxMinX = Xmax-Xmin;
  var MaxMinY = Ymax-Ymin;

  for (var i=0; i<ListeRangement.length;i++){
    ctx.beginPath();
    ctx.moveTo(multiX*(ListeRangement[i]-Xmin)/MaxMinX, multiY*(Ymax-ListeRangement[i+2])/MaxMinY);
    ctx.lineTo(multiX*(ListeRangement[i+1]-Xmin)/MaxMinX, multiY*(Ymax-ListeRangement[i+3])/MaxMinY);
    ctx.stroke();
    i=i+3;
  }
  
}