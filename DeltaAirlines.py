from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import datetime
import calendar
import time

def weekday_from_date(day, month, year):
    return calendar.day_name[
        datetime.date(day=day, month=month, year=year).weekday()
    ]

def check(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def clickWhenPossible(xpath):
    while True:
        result = check(xpath)
        if result:
            driver.find_element(By.XPATH, xpath).click()
            break

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver")

class Trip:
    def __init__(self, origin, destination, type, month, day, year, passangers, code, email):
        self.origin = origin
        self.destination = destination
        self.type = type
        self.month = month
        self.day = day
        self.year = year
        self.date = [self.month, self.day, self.year]
        self.email = email
        self.passangers = passangers - 1
        self.code = code

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


driver.get("https://www.delta.com/")

popup = "/html/body/modal-container/div/div/ng-lang-select-confirmation/div/div/div/div[2]/button"
clickWhenPossible(popup)

Vacation = Trip("MKE", "NYC", "One Way", 7, 7, 2022, 1, "DL4931", "rosewoodfic@gmail.com")

originElement = driver.find_element(By.XPATH, "//*[@class='airport-code d-block']").click()


originInputData = "//input[@id='search_input']"
clickWhenPossible(originInputData)
originInput = driver.find_element(By.XPATH, originInputData).send_keys(Vacation.origin)
clickWhenPossible("//*[@class='airport-city col-sm-10 col-md-11 col-lg-10 col-xl-10 col-xxl-10 pl-0']")

destinationElement = driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-home[1]/ngc-global-nav[1]/header[1]/div[1]/div[1]/ngc-book[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[1]").click()
destinationInputData = "//input[@id='search_input']"
clickWhenPossible(destinationInputData)
originInput = driver.find_element(By.XPATH, destinationInputData).send_keys(Vacation.destination)
clickWhenPossible("//*[@class='airport-city col-sm-10 col-md-11 col-lg-10 col-xl-10 col-xxl-10 pl-0']")

clickWhenPossible("//span[@id='selectTripType-val']")
clickWhenPossible("//li[@id='ui-list-selectTripType1']")
clickWhenPossible("//*[@id='input_departureDate_1']")

weekday = weekday_from_date(Vacation.day, Vacation.month, Vacation.year)

while True:
    dateXpath = f"//a[@aria-label[contains(.,'{Vacation.day} {months[Vacation.month]} {Vacation.year}')]]"
    print(dateXpath)
    if check(dateXpath):
        dateElement = driver.find_element(By.XPATH, dateXpath)
        dateElement.click()
        break
    clickWhenPossible("//span[normalize-space()='Next']")

time.sleep(5)

doneElement = driver.find_element(By.XPATH, "//button[@value='done']")
doneElement.click()

# clickWhenPossible("//span[@id='passengers-val']")
# clickWhenPossible(f"//*[@id='ui-list-passengers{Vacation.passangers}']")
clickWhenPossible("//*[@id='btn-book-submit']")

code = f"//*[a[contains(., '{Vacation.code} ')]]//a"
while True:
    result = check(code)
    if result:
        break

code = driver.find_element(By.XPATH, code).find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..")

price = code.find_element(By.XPATH, '//*[@class="priceBfrDec ng-star-inserted"]')
priceName = price.find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "//*[@class='ng-star-inserted']")
breakpoint()
