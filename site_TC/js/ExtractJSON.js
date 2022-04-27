//JSON
var header = document.querySelector("header");
//var section = document.querySelector("section");
var section = document.querySelector("map");
//lien du json
var requestURL = "testjson.json"; //peut mettre un lien github : 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';
var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
    var repRequete = request.response;
    foncAffichage(repRequete);
}


function foncAffichage(jsonObj) {
    var heroes = jsonObj['members'];
  
    for (var i = 0; i < heroes.length; i++) {
      var myArticle = document.createElement('article');
      var myPara1 = document.createElement('p');
  
      myPara1.textContent = 'Secret identity: ' + heroes[i].secretIdentity;

      myArticle.appendChild(myPara1);
      
      section.appendChild(myArticle);
    }
}