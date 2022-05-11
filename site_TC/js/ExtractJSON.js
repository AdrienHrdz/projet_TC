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

  for (var j = 0 ; j<Object.keys(jsonObj).length ;j++){
    var mur = jsonObj[String(j)];
    console.log("mur numero : " + j);

    for (var i =0; i<2; i++){
      console.log("first " + mur[0].First[0][i]);
      console.log( "finish " + mur[0].Finish[0][i]);
      ListeRangement.push(mur[0].First[0][i]);
      ListeRangement.push(mur[0].Finish[0][i]);
    }
  

    //Affichage joli à voir plus tard pour affichage des lignes
    var myArticle = document.createElement('article');
    var myPara1 = document.createElement('p');
    var myPara2 = document.createElement('p');

    myPara1.textContent = 'Premier Point X: ';
    myPara2.textContent = 'Premier Point Y: ';
    myPara1.textContent = 'Dernier Point X: ';
    myPara2.textContent = 'Dernier Point Y: ' ;


    myArticle.appendChild(myPara1);
    myArticle.appendChild(myPara2);
    section.appendChild(myArticle);

  }

  console.log(ListeRangement);
  
  if ((Math.max(...ListeRangement)-Math.abs(Math.min(...ListeRangement)))>0){
    var echelleMax = Math.max(...ListeRangement);
  }

  else {
    var echelleMax = Math.abs(Math.min(...ListeRangement));
  }


  console.log(echelleMax);
  
}