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

                <h3>C'est la navbarre</h3>
                
                `;

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