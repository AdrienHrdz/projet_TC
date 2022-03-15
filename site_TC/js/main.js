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
                <h1>Sapeurs pompiers de France</h1>
                <ul>
                  <li><a href="`+ urlindex +`index.html">Accueil</a></li>
                  <li><a href="`+ urlbis +`map.html">Map</a></li>
                  <li><a href="`+ urlbis +`video.html">Vidéo</a></li>
                  <li>Oh le bad je suis en pleine redescente</li>
                </ul>`;

document.querySelector("footer").innerHTML = `

                <h3>C'est le footer</h3>
                    <ul>
                    <li>Tikiwinki</li>
                    <li>Lala</li>
                    <li>Poooo</li>
                    <li>Oh le bad je suis en pleine redescente</li>
                </ul>`;