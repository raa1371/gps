from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 🟢 تنظیمات کروم برای Headless اجرا روی Railway
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # بدون UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# 🟢 اجرای WebDriver
service = Service("/usr/bin/chromedriver")  # مسیر اجرا روی Railway
driver = webdriver.Chrome(service=service, options=chrome_options)

# باز کردن سایت
driver.get("https://cadastre.mimt.gov.ir/Map/Map.aspx?PNid=0")
print("✅ سایت باز شد.")

# 🟢 کلیک روی دکمه جستجو
try:
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#Div_InsertPoint')]"))
    )
    search_button.click()
    print("✅ دکمه جستجو کلیک شد.")
except:
    print("❌ دکمه جستجو پیدا نشد!")

# 🟢 گرفتن اسکرین‌شات
time.sleep(5)
screenshot_path = "map_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"📸 اسکرین‌شات ذخیره شد در: {screenshot_path}")

# بستن مرورگر
driver.quit()
