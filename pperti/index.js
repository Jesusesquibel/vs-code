import puppeteer from 'puppeteer'

 async function Opentodoist(){
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 400
    })
    const page = await browser.newPage()

    await page.goto('https://app.todoist.com/')
  //  await new Promise(r => setTimeout(r,5000));
    await browser.close()
 }

 Opentodoist()