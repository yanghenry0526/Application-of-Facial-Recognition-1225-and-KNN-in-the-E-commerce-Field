from selenium import webdriver
from xlwt import Workbook
import openpyxl
from openpyxl.styles import PatternFill
import os.path
import time
import os
import test

if (os.path.exists('./ComDataSave.xlsx') == False):
    wb = openpyxl.Workbook()
    s1 = wb.worksheets[0]
    s1.title = 'Goods'
    s3 = wb.create_sheet('Category')
    s2 = wb.create_sheet('Search')
    rowNum = [s1.max_row, s2.max_row, s3.max_row]
    color = ['ffffff', '000000']

    for i in range(rowNum[0]):
        fille = PatternFill('solid', fgColor=color[0])
        s1.cell(row=i + 1, column=1, value='').fill = fille
    for i in range(rowNum[1]):
        fille = PatternFill('solid', fgColor=color[0])
        s2.cell(row=i + 1, column=1, value='').fill = fille
    for i in range(rowNum[2]):
        fille = PatternFill('solid', fgColor=color[0])
        s3.cell(row=i + 1, column=1, value='').fill = fille

    s1['B1'] = '年齡'
    s1['C1'] = '性別'
    s1['D1'] = '表情'
    s1['F1'] = '商品名稱'
    s1['G1'] = '商品網址'

    s3['B1'] = '年齡'
    s3['C1'] = '性別'
    s3['D1'] = '表情'
    s3['F1'] = '類別名稱'
    s3['G1'] = '類別網址'

    s2['B1'] = '年齡'
    s2['C1'] = '性別'
    s2['D1'] = '表情'
    s2['F1'] = '查詢關鍵字'
    s2['G1'] = '關鍵字網址'

    wb.save("ComDataSave.xlsx")
else:
    wb = openpyxl.load_workbook('ComDataSave.xlsx')
    s1 = wb['Goods']
    s2 = wb['Search']
    s3 = wb['Category']

# 變數區
detect = False
current_url = ''
current_title = ''
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
result = []


def watch_url_and_title():
    driver = webdriver.Chrome()#
    driver.get('https://www.momoshop.com.tw/main/Main.jsp')
    global current_url, current_title, number
    global original_window
    global detect
    number = 1
    while True:
        original_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.close()
                driver.switch_to.window(window_handle)
                break
        new_url = driver.current_url
        new_title = driver.title
        if new_url != current_url:
            gender, age, emotion = test.rere()
            current_url = new_url
            current_title = new_title
            judgeWhereToWrite(gender, age, emotion, new_url, new_title)
            print(f"New URL: {new_url}, Title: {new_title}")


def judgeWhereToWrite(gender, age, emotion, url, title):
    global record
    record = 0
    if ("momoshop" in url):  # momo's url
        record = judgeString("goods", "search", "category", url)  # record momo's type
    elif ("ruten" in url):  # 露天's url
        record = judgeString("item", "find", "category", url)
    elif ("pchome" in url):  # pchome's url
        record = judgeString("prod", "search", "region", url)
        record = judgeString("prod", "search", "sign", url)
        record = judgeString("prod", "search", "store", url)
        record = judgeString("prod", "search", "site", url)
    elif ("yahoo" in url):
        record = judgeString("gdsale", "search", "category", url)
    elif ("rakuten" in url):
        record = judgeString("product", "search", "category", url)
        record = judgeString("product", "search", "CT", url)
        record = judgeString("product", "search", "shop", url)
    elif ("books.com.tw" in url):
        record = judgeString("products", "search", "web", url)

    if record == 1:
        writeToExcel(1, gender, age, emotion, title, url)
    elif record == 2:
        writeToExcel(2, gender, age, emotion, title, url)
    elif record == 3:
        writeToExcel(3, gender, age, emotion, title, url)


def judgeString(item1, item2, item3, url):
    if item1 in url:
        return 1
    elif item2 in url:
        return 2
    elif item3 in url:
        return 3
    else:
        return 0


def writeToExcel(record, gender, age, emotion, title, url):
    global max_row
    if record == 1:
        max_row = s1.max_row
        s1.cell(max_row + 1, 2).value = gender
        s1.cell(max_row + 1, 3).value = age
        s1.cell(max_row + 1, 4).value = emotion
        s1.cell(max_row + 1, 6).value = title
        s1.cell(max_row + 1, 7).value = url
    elif record == 2:
        max_row = s2.max_row
        print(max_row)
        s2.cell(max_row + 1, 2).value = gender
        s2.cell(max_row + 1, 3).value = age
        s2.cell(max_row + 1, 4).value = emotion
        s2.cell(max_row + 1, 6).value = title
        s2.cell(max_row + 1, 7).value = url
    elif record == 3:
        max_row = s3.max_row
        s3.cell(max_row + 1, 2).value = gender
        s3.cell(max_row + 1, 3).value = age
        s3.cell(max_row + 1, 4).value = emotion
        s3.cell(max_row + 1, 6).value = title
        s3.cell(max_row + 1, 7).value = url

    wb.save("ComDataSave.xlsx")


watch_url_and_title()
