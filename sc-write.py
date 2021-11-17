import playwright
from playwright.sync_api import sync_playwright
from time import sleep

case_num = "123"
last_name = "test"
court = "G"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto("http://www2.greenvillecounty.org/scjd/publicindex/")
    page.click("id=ContentPlaceHolder1_ButtonAccept")
    sleep(5)
    page.fill("id=ContentPlaceHolder1_TextBoxCaseNumber", case_num)
    page.fill("id=ContentPlaceHolder1_TextBoxlastName", last_name)
    page.select_option("id=ContentPlaceHolder1_DropDownListCourtType", court)
    browser.close()
