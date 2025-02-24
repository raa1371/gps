from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🟢 دریافت مختصات از فایل ذخیره‌شده توسط بات تلگرام
with open("gps_points.txt", "r") as f:
    gps_data = f.read().strip()

# تبدیل مختصات به فرمت مناسب
gps_points = [tuple(gps_data.split())]

# 🟢 راه‌اندازی WebDriver
driver = webdriver.Chrome()
driver.get("https://cadastre.mimt.gov.ir/Map/Map.aspx?PNid=0")

# 🟢 کلیک روی دکمه جستجو
try:
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#Div_InsertPoint')]"))
    )
    search_button.click()
    print("✅ دکمه جستجو کلیک شد.")
except:
    print("❌ دکمه جستجو پیدا نشد!")

# 🟢 وارد کردن نقاط GPS
time.sleep(2)

for i, (lngD, lngM, lngS, latD, latM, latS) in enumerate(gps_points):
    try:
        driver.find_element(By.ID, "LngD").send_keys(lngD)
        driver.find_element(By.ID, "LngM").send_keys(lngM)
        driver.find_element(By.ID, "LngS").send_keys(lngS)
        driver.find_element(By.ID, "LatD").send_keys(latD)
        driver.find_element(By.ID, "LatM").send_keys(latM)
        driver.find_element(By.ID, "LatS").send_keys(latS)

        driver.find_element(By.ID, "BtnAddPoint").click()
        print(f"✅ نقطه {i+1} اضافه شد.")
        time.sleep(1)
    except:
        print(f"❌ خطا در افزودن نقطه {i+1}!")

# 🟢 گرفتن اسکرین‌شات
time.sleep(5)
screenshot_path = "map_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"📸 اسکرین‌شات ذخیره شد در: {screenshot_path}")

# بستن مرورگر
driver.quit()
