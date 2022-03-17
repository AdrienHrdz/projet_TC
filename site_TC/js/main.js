//var from = document.querySelector('[name="block-stylesheet"]').getAttribute("from");
var urlbis = ".";
var urlindex = ".";
var path = window.location.pathname;
var page = path.split("/").pop();

if(page != "index.html")
{
    urlindex = "../";
    urlbis = "./";
}

else
{
    urlindex = "./";
    urlbis = "html/";
}

document.querySelector("header").innerHTML = `

                <section class="header" id="modelHeader">
                <h1>Sapeurs Pompiers de France</h1>
                <div class="grid_2">
                    <ul class="navbar">
                        <li><a href="`+ urlindex +`index.html">Accueil</a></li>
                        <li><a href="`+ urlbis +`map.html">Map</a></li>
                        <li><a href="`+ urlbis +`video.html">Vidéo</a></li>
                    </ul>
                </div>`;

document.querySelector("footer").innerHTML = `

                <div>
                    <h3>ETAT-MAJOR</h3>
                    <p>24 rue René Camphin - CS 60068</p>
                    <h3>Horaires d'ouverture</h3>
                </div>
                <button onclick="topFunction()" id="upBtn" title="Retour au haut de la page">Retour Haut de page</button>
                
                `;

//Bouton remonte en haut de page
function topFunction(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}