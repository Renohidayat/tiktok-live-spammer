from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROMEDRIVER_PATH = r"C:\Users\hi\Documents\Projeck\tiktok-live-spammer\chromedriver.exe"

KOMENTAR_LIST = [
    "LB SATSET ABANGKU 🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶",
    "LB SAT SET ABANGKUU 💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜",
]

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "tiktok.com" in driver.current_url and "live" in driver.current_url:
        print(f"✅ Tab: {driver.title}")
        break

time.sleep(2)

def kirim_komentar(teks):
    try:
        input_box = driver.find_element(By.CSS_SELECTOR, '[data-e2e="room-chat-input-field"]')
        driver.execute_script(
            """
            var el = arguments[0];
            var text = arguments[1];
            el.focus();
            el.textContent = '';
            document.execCommand('selectAll', false, null);
            document.execCommand('insertText', false, text);
            """,
            input_box, teks
        )
        time.sleep(0.1)
        input_box.send_keys(Keys.RETURN)
        print(f"✅ {teks[:45]}...")
        return True
    except Exception as e:
        print(f"❌ Gagal: {e}")
        return False


print("\n🚀 Kirim komentar NONSTOP... (Ctrl+C untuk stop)\n")

index = 0
while True:
    komentar = KOMENTAR_LIST[index % len(KOMENTAR_LIST)]
    kirim_komentar(komentar)
    index += 1
time.sleep(0.5)  # ← jeda hanya 0.5 detik
