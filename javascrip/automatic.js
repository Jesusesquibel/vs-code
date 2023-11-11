import * as puppeteer from "puppeteer";

const bot = async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

/*PASO 1 - LOGIN*/
    await page.goto('https://app.todoist.com/auth/login')

    const user = await page.$('#documento');
    await user?.type('USERNAME');
    
    const password = await page.$('#inputpassword');
    await password?.type('USERPASSWORD');

    let url = await page.url();
    await console.log(url); // --> FUNCIONA OK, IMPRIME BIEN URL

    await page.screenshot({path: '1-credentialsForm.png'}); //  --> FUNCIONA OK, APARECE IMAGEN CON FORM RELLENO

    let btn = await page.$('#loginForm > div > div:nth-child(2) > div > button');

    await Promise.all([
        page.waitForNavigation(),
        btn?.click()
    ]);

/*PASO 2 - CONTINUAR */
    btn = await page.$('body > div > div > div > main > div > div > div._bottom30._display-flex._top30 > button');

    url = await page.url();
    await console.log(url); // --> FUNCIONA OK, IMPRIME BIEN URL

    await page.screenshot({path: '2-continue.png'}); // --> FUNCIONA OK, APARECE IMAGEN CON BTN CONTINUAR

    await Promise.all([
        page.waitForNavigation(),
        btn?.click()
    ]);

/* PASO 3 - OBTENCIÓN PARÁMETRO */
    url = await page.url();
    await console.log(url); // ERROR -> IMPRIME: chrome-error://chromewebdata/

    await page.screenshot({path: '3-end.png'}); // ERROR -> APARECE IMAGEN EN BLANCO


    console.log(await browser.pages()); 
    await browser.close();


};