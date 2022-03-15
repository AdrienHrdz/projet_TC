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

                <h3>C'est la navbarre</h3>`;

document.querySelector("footer").innerHTML = `

                <h3>C'est le footer</h3>
                    <ul>
                    <li>Tikiwinki</li>
                    <li>Lala</li>
                    <li>Poooo</li>
                    <li>Oh le bad je suis en pleine redescente</li>
                </ul>`;