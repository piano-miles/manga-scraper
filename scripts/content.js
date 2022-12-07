console.log("content.js");
// Reads and modifies the content of the page
// Live in an isolated world, meaning they can make changes to their JavaScript environment without conflicting with their host page or other extension's content scripts

/**
    const article = document.querySelector("article");

    // `document.querySelector` may return null if the selector doesn't match anything.
    if (article) {
        const text = article.textContent;
        const wordMatchRegExp = /[^\s]+/g; // Regular expression
        const words = text.matchAll(wordMatchRegExp);
        // matchAll returns an iterator, convert to array to get word count
        const wordCount = [...words].length;
        const readingTime = Math.round(wordCount / 200);
        const badge = document.createElement("p");
        // Use the same styling as the publish information in an article's header
        badge.classList.add("color-secondary-text", "type--caption");
        badge.textContent = `⏱️ ${readingTime} min read`;

        // Support for API reference docs
        const heading = article.querySelector("h1");
        // Support for article docs with date
        const date = article.querySelector("time")?.parentNode;

        (date ?? heading).insertAdjacentElement("afterend", badge);
    }
}
*/

let overlay = `
<!-- Injected by Manga Scraper Chrome extension -->

<div id="overlay-back"></div>
<div id="popup" class="front-popup">
    <div class="block">
        <h1 class="overtext">Manga Detected</h1>
    </div>
    <div class="overtext block">
        <button type="button">Cancel</button>
        <button type="button">Scrape</button>
    </div>
</div>

<style>
    .fit-picture {
        width: 100%
    }

    #overlay-back,
    #popup {
        top: 0;
        left: 0;
        width: 100%;
        height: 100%
    }

    #popup {
        position: absolute;
        display: hidden;
        margin-top: 0;
        margin-left: 0;
        background-color: rgba(25, 15, 19, .91);
        z-index: 99;
        padding: 32px;
        backdrop-filter: blur(4px)
    }

    #overlay-back {
        position: fixed;
        background: #000;
        opacity: .7;
        filter: alpha(opacity=60);
        z-index: 98;
        display: none
    }

    #popup h1.overtext {
        font-size: 60px;
        margin-bottom: 60px;
        margin-top: 175px
    }

    .overtext {
        text-align: center;
        color: #fff
    }

    #popup .overtext button {
        color: #fff;
        background-color: #2b2a2a;
        padding: 16px 64px;
        font-size: 28px;
        margin-left: 12px;
        margin-right: 12px;
        border-width: 3px;
        border-style: solid;
        border-color: #727272;
        border-radius: 8px;
        cursor: pointer;
        transition-duration: .08s
    }

    #popup .overtext button:hover {
        background-color: #202020
    }

    #popup .overtext button:active {
        box-shadow: 0 5px #666;
        transform: translateY(4px);
        padding: 14px 66px
    }

    .btn_login,
    .btn_register {
        z-index: 95
    }
</style>
`

document.body.innerHTML += overlay;