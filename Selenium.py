import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def init_driver():
    driver = webdriver.Firefox()
    return driver


def lookup(driver, query):  # В поиске вводит фразу из переменной 'query' и нажимает "enter"
    driver.get("https://www.work.ua/ua/jobs/?ss=1")
    box = driver.find_element_by_id("search")
    box.send_keys(query)
    box.send_keys(Keys.RETURN)
    time.sleep(5)


def vacancy(driver, numb):  # Заходит на вакансию после чего возвращается назад
    job = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[1]/div[' + str(numb) + ']/h2/a')
    job.send_keys(Keys.RETURN)
    time.sleep(2)

    vacancy_operator(driver)
    time.sleep(2)
    driver.back()
    time.sleep(2)


def vacancy_operator(driver): # Возращает список с Именем, Городом и Описанием Вакансии
    name = driver.find_element_by_id("h1-name").text # Название вакансии
    city = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[1]/div[3]/div/dl/dd[2]').text # Город вакансии
    description = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[1]/div[3]/div/div[2]').text.encode("utf-8") # Описание вакансии
    raw_info = [name, city, description] # Переменная со Списком

    csv_writer(raw_info)


def csv_writer(raw_info): # Функция для записи списка в "vacancy.csv" файл
    with open(csv_vacancy, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(raw_info)



if __name__ == "__main__":
    csv_vacancy = "vacancy.csv"
    driver = init_driver()
    lookup(driver, "Python")
    numb = 3 # numb - переменная для xpath в def vacancy , первая вакансия = 3, вторая = 4 и т.д.
    while numb != 18: # Число 17 в xpath последнее, Последняя вакансия numb = 17
        if numb != 10: # Число 10 - отсутствует в xpath, после числа 9 идет 11, число 10 визывает ошибку
            vacancy(driver, numb)
        numb += 1
