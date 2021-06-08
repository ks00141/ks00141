const puppeteer = require('puppeteer');

(async ()=>{
    const browers = await puppeteer.launch();
    const page = await browers.newPage();
    await page.goto("https://youtube.com");
    // await page.screenshot({path : "../test.png"});

    const test = await page.evaluate(()=>{
        return document.querySelector("#video-title").innerText;
    });
    console.log(test);
    await browers.close();
})();