from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Get the url of the portal to test
url = "https://w4.cuevana3.ai"
#specifying a web browser
driver = webdriver.Chrome()
driver.get(url)

def test_select_genre():
    genres = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div/div/nav/ul/li[2]/a")
    genres.click()
    driver.save_screenshot('img/tesingGenres.png')
    time.sleep(1)
    selectedGenre = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div/div/nav/ul/li[2]/ul/li[1]/a")
    selectedGenre.click()
    time.sleep(1)
    

def test_search_serie():
    searchInput = driver.find_element(By.ID,"keysss")
    searchInput.send_keys("Ozark")
    driver.save_screenshot('img/searchSerie.png')
    time.sleep(2)
    #clicking the selected item
    selectSerie = driver.find_element(By.ID,"searchsubmit")
    selectSerie.click()
    #clicking the correct image
    selectImage = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/main/section/ul/li[2]/div/a/div/figure/img")
    selectImage.click()
    time.sleep(3)


def test_select_season():
    season = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/main/section[1]/div/select/option[3]")
    season.click()
    driver.save_screenshot('img/selectSeason.png')
    time.sleep(3)

def test_select_chapter():
    chapter = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/main/section[1]/ul[3]/li[2]/article/a/div/figure")
    chapter.click()
    driver.save_screenshot('img/chapterSelect.png')
    time.sleep(2)
