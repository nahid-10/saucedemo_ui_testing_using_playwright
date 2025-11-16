from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

page.goto("https://www.saucedemo.com/")

page.fill("input#user-name", "standard_user")
page.fill("input#password", "secret_sauce")
page.click("input#login-button")

page.click("button#add-to-cart-sauce-labs-backpack")

page.click("a.shopping_cart_link")

title = page.text_content("div.inventory_item_name")
print("Product name is:", title)

page.click("button#react-burger-menu-btn")

page.click("a#logout_sidebar_link")

browser.close()
playwright.stop()
