//var from = document.querySelector('[name="block-stylesheet"]').getAttribute("from");
var urlbis = ".";
var urlindex = ".";
var path = window.location.pathname;
var page = path.split("/").pop();

var name_page = page.split(".");

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
                        <li class="right"><a> Page en cours:  ` + name_page[0] +` </a></li>
                        
                    </ul>
                </div>`
;

document.querySelector("footer").innerHTML = `
            <div class=cadres>
                <ul class=listcadre>
                    <li class=cl1>
                        <h4>Etat-Major</h4> 
                        <p> 24, rue René Camphin </p>
                    </li>

                    <li class=cl2>
                        <h4>Horaires d'ouverture</h4>
                        <p> Lundi au Vendredi : 9h - 17h </p>
                    </li>
            
                    <li class=cl3>
                        <h4>Contactez-nous : </h4>
                        <button id="bouton_twitter" onclick="window.location.href = 'https://twitter.com/PompiersFR?ref_src=twsrc%5Etfw%7Ctwcamp%5Eembeddedtimeline%7Ctwterm%5Eprofile%3APompiersfr%7Ctwgr%5EeyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3NrZWxldG9uX2xvYWRpbmdfMTMzOTgiOnsiYnVja2V0IjoiY3RhIiwidmVyc2lvbiI6bnVsbH0sInRmd19zcGFjZV9jYXJkIjp7ImJ1Y2tldCI6Im9mZiIsInZlcnNpb24iOm51bGx9fQ%3D%3D&ref_url=https%3A%2F%2Fwww.pompiers.fr%2Fgrand-public';">Notre Twitter</button
                    </li>

                    <li class=cl4>
                        <h4> Appelez au 18 ou 112 <br>______________________</h4>
                        <button onclick="topFunction()" id="upBtn" title="Retour au haut de la page">Retour Haut de page</button>
                    </li>
                </ul>
            </div>
            `
;

//Bouton remonte en haut de page
function topFunction(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
