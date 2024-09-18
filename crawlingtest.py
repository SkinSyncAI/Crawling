from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # 브라우저를 백그라운드에서 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

try:
    service = Service(ChromeDriverManager().install())
    service.command_line_args()
    driver = webdriver.Chrome(service=service, options=options)
    print("ChromeDriver가 성공적으로 실행되었습니다.")
except Exception as e:
    print(f"ChromeDriver 실행 중 오류가 발생했습니다: {e}")
