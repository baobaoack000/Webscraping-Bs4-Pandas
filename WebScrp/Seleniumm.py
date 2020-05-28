from selenium import webdriver


driver = webdriver.Chrome(r"C:\Users\Nguyen Gia Bao\Desktop\chromedriver_win32\chromedriver")
driver.get("https://batdongsan.com.vn/nha-dat-ban")

i = 0
for title in driver.find_elements_by_class_name("p-title"):
    print("Title :"+title.text+"          " )
    i=i+1
    for content in driver.find_elements_by_class_name("p-main"):
        print("Info :"+content.text+"         ")


p = "2" 
driver.get("https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-nguyen-tri-phuong-1-phuong-thanh-son-4-prj-khu-do-thi-moi-dong-bac-khu-1/chi-tu-310-trieu-da-la-dan-a-hacom-galacity-ninh-thuan-pr25575339")
for title in driver.find_elements_by_id("product-detail"):
    print("Title :"+title.text+"          " )
    i=i+1


