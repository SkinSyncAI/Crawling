# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import math

# from concurrent.futures import ProcessPoolExecutor, as_completed
# import pandas as pd
# #from tqdm import tqdm_notebook
# import warnings

# warnings.filterwarnings('ignore')
# options = webdriver.ChromeOptions()
# options.add_argument('--headless') # ensure GUI is off : cloab은 새창을 지원하지않기 때문에 창 없는 모드
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage') 
# driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options = options)

# # 데이터프레임 초기화

# def review_crawling(url):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     temp_df = pd.DataFrame(columns=['category', 'ranking', 'name', 'brand', 'price', 'sale_price', 'date', 'rate', 'id', 'skin_type', 'select_1_title', 'select_1_content', 'select_2_title', 'select_2_content', 'select_3_title', 'select_3_content', 'txt'])

#     try:
#         driver.get(url)
#         time.sleep(1)
#         driver.find_element(By.CSS_SELECTOR, '#reviewInfo > a > span').click()
#         time.sleep(1)
#         driver.find_element(By.CSS_SELECTOR, '#gdasSort > li.is-layer.on > a').click()
#         time.sleep(1)

#         for current_page in range(1, 500):
#             for i in range(1, 11):
#                 try:
#                     category = driver.find_element(By.CSS_SELECTOR, '#dtlCatNm').text
#                     ranking = 0
#                     brand = driver.find_element(By.CSS_SELECTOR, '#moveBrandShop').text
#                     price = driver.find_element(By.CSS_SELECTOR, '#Contents > div.prd_detail_box.renew > div.right_area > div > div.price > span.price-1 > strike').text
#                     sale_price = driver.find_element(By.CSS_SELECTOR, '#Contents > div.prd_detail_box.renew > div.right_area > div > div.price > span.price-2 > strong').text
#                     date = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.score_area > span.date').text
#                     rate = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.score_area > span.review_point > span').text
#                     id = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.info > div > p.info_user > a.id').text
#                     skin_type = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(1) > dd > span').text
#                     select_1_title = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(1) > dt > span').text
#                     select_1_content = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(1) > dd > span').text
#                     select_2_title = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(2) > dt > span').text
#                     select_2_content = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(2) > dd > span').text
#                     select_3_title = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(3) > dt > span').text
#                     select_3_content = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.poll_sample > dl:nth-child(3) > dd > span').text
#                     txt = driver.find_element(By.CSS_SELECTOR, f'#gdasList > li:nth-child({i}) > div.review_cont > div.txt_inner').text

#                     temp_df.loc[len(temp_df)] = [category, ranking, name, brand, price, sale_price, date, rate, id, skin_type, select_1_title, select_1_content, select_2_title, select_2_content, select_3_title, select_3_content, txt]
#                 except:
#                     pass

#             try:
#                 if current_page % 10 != 0:
#                     if current_page // 10 < 1:
#                         page_button = driver.find_element(By.CSS_SELECTOR, f'#gdasContentsArea > div > div.pageing > a:nth-child({current_page%10+1})')
#                         page_button.click()
#                         time.sleep(2)
#                     else:
#                         page_button = driver.find_element(By.CSS_SELECTOR, f'#gdasContentsArea > div > div.pageing > a:nth-child({current_page%10+2})')
#                         page_button.click()
#                         time.sleep(2)
#                 else:
#                     next_button = driver.find_element(By.CSS_SELECTOR, '#gdasContentsArea > div > div.pageing > a.next')
#                     next_button.click()
#                     time.sleep(2)
#             except:
#                 pass

#     except Exception as e:
#         print(f"Error occurred during crawling {url}: {str(e)}")

#     finally:
#         driver.quit()

#     return temp_df

# # 병렬 크롤링 함수
# def parallel_crawling(urls):
#     results = []
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         futures = [executor.submit(review_crawling, url) for url in urls]
#         for future in as_completed(futures):
#             try:
#                 result = future.result()
#                 results.append(result)
#                 print(f"Crawling completed for {urls[futures.index(future)]}")
#             except Exception as e:
#                 print(f"Error occurred during crawling {urls[futures.index(future)]}: {str(e)}")
#     return results

# # 크롤링할 URL 리스트
# url_list = [
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000188598&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000188830&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=2",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000187585&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=3",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000188874&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=4",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000187420&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=5",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000186732&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=6",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184771&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=7",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184790&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=8",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184965&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=9",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000185109&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=10",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000185156&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=11",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000187241&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=12",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000199153&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=13",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000189256&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=14",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000190441&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=15",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000197560&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=16",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000197660&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=17",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000198440&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=18",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000198625&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=19",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000198834&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=20",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000197102&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=21",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000189586&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=22",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000195660&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=23",
#     "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000193204&dispCatNo=100000100010013&trackingCd=Cat100000100010013_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%8A%A4%ED%82%A8/%ED%86%A0%EB%84%88_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=24"
# ]

# def main():
#     start = time.time()
#     # math.factorial(100000)
    
#     # 데이터베이스 초기화
#     df_review_cos1 = pd.DataFrame(columns=['category', 'ranking', 'name', 'brand', 'price', 'sale_price', 'date', 'rate', 'id', 'skin_type', 'select_1_title', 'select_1_content', 'select_2_title', 'select_2_content', 'select_3_title', 'select_3_content', 'txt'])
#     # 병렬 크롤링 실행
#     results = parallel_crawling(url_list)
#     # 결과 데이터프레임 합치기
#     for result_df in results:
#         df_review_cos1 = pd.concat([df_review_cos1, result_df], ignore_index=True)
#     end = time.time()
#     # print(df_review_cos1)
#     # df_review_cos1.to_csv('r/Applications/jisung/Crawling/crawling_data/crawling_data21_24.csv', index=False)
#     df_review_cos1.to_csv('skintoner_24_4.csv', index=False)
#     # df.to_csv("/Applications/jisung/Crawling/crawling_data")
#     print(f"{end - start:.5f} sec")

# if __name__ == '__main__':
#     main()


# # 결과 출력
