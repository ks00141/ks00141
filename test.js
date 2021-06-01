const puppeteer = require('puppeteer');

(async ()=>{
    const browers = await puppeteer.launch();
    const page = await browers.newPage();
    await page.goto("http://gw.wisol.co.kr");
    // await page.screenshot({path : "../test.png"});

    const test = await page.evaluate(()=>{
        return document.querySelector("iFrame").innerHTML;
    });
    console.log(test);
    await browers.close();
})();