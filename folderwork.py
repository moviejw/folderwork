from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import clipboard

# Create WebDriver (Chrome)
driver = webdriver.Chrome()

# Access to the web page
driver.get("https://folderwork.com/")

time.sleep(3)

# Direct input the login informations
email = "YOUR_ID_HERE"
password = "YOUR_PASSWORD_HERE"

# Find the login form
email_input = driver.find_element(By.XPATH, "//input[@type='email']")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")

# Input the login informations
email_input.send_keys(email)
password_input.send_keys(password)

# Click the login button
login_button = driver.execute_script(
    """return document.getElementsByClassName("hover\\:cursor-pointer align-middle")[0];"""
)
login_button.click()

# Wait for the page to load
time.sleep(3)

# Read the urls from the file
with open("url.txt", "r") as url_file:
    urls = url_file.read().splitlines()

# Loop through the urls
for url in urls:
    # Access to the web page
    driver.get(url)

    time.sleep(2)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.w-screen.min-safe-h-screen.flex.flex-col.note-bg > div > div.flex.flex-col.flex-auto.w-full.overflow-y-hidden > div.flex.items-center.justify-between.p-2.border-t.border-slate-500 > div > div > div.flex.space-x-2 > svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.h-6.w-6.hover\\:cursor-pointer.css-vubbuv")))

    first_button = driver.find_element(By.CSS_SELECTOR,"#__next > div.w-screen.min-safe-h-screen.flex.flex-col.note-bg > div > div.flex.flex-col.flex-auto.w-full.overflow-y-hidden > div.flex.items-center.justify-between.p-2.border-t.border-slate-500 > div > div > div.flex.space-x-2 > svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.h-6.w-6.hover\\:cursor-pointer.css-vubbuv")
    first_button.click()
    
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.w-screen.min-safe-h-screen.flex.flex-col.note-bg > div > div.flex.flex-col.flex-auto.w-full.overflow-y-hidden > div.flex.items-center.justify-between.p-2.border-t.border-slate-500 > div > div > div.flex.space-x-2 > div > div.py-5.px-2.space-y-4 > p:nth-child(1)")))

    second_button = driver.find_element(By.CSS_SELECTOR,"#__next > div.w-screen.min-safe-h-screen.flex.flex-col.note-bg > div > div.flex.flex-col.flex-auto.w-full.overflow-y-hidden > div.flex.items-center.justify-between.p-2.border-t.border-slate-500 > div > div > div.flex.space-x-2 > div > div.py-5.px-2.space-y-4 > p:nth-child(1)")
    second_button.click()

    # Take the text from clipboard
    copied_text = clipboard.paste()

    # Write the text to the file
    with open("memo1.txt", "a", encoding="utf-8") as file:
        file.write(copied_text)

# Close the browser
driver.quit()
