// Start
sessionStorage.clear()

//
// For each page
//

// mangaclash.com
images = [];
next_page = document.getElementsByClassName("btn next_page")[0];

for (var i = 0; i < 100; i++) {
    img = document.getElementById("image-" + i);
    if (img != null) {
        images.push(img.getAttribute("src"));
    }
}

page = 1;
if (sessionStorage.getItem("page_number") != null) {
    page = parseInt(sessionStorage.getItem("page_number")) + 1;
}

sessionStorage.setItem("page_number", page);
sessionStorage.setItem("page" + page + "_data", images);

next_page.click();

// kissmanga
images = [];
next_page = document.getElementById("btnNext");

b = document.getElementById("centerDivVideo");
c = b.querySelectorAll("img");
for (var i=0; i<b.childElementCount-1; i++) {
    images.push(c[i].getAttribute('src'));
}

page = 1;
if (sessionStorage.getItem("page_number") != null) {
    page = parseInt(sessionStorage.getItem("page_number")) + 1;
}

sessionStorage.setItem("page_number", page);
sessionStorage.setItem("page" + page + "_data", images);

next_page.click();
