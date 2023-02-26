import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_ninsheetmusic_to_sqlitedb(URL):
    options = Options()
    options.headless = True

    # URL = "https://www.ninsheetmusic.org/browse/series/FireEmblem"
    con = sqlite3.connect("ninsheetmusic.db")


    driver = webdriver.Chrome(options=options)
    driver.get(URL)



    def insert_row(data):
        sql = f''' INSERT INTO ninsheetmusic(id,pdf_url,mid_url,mus_url,popularity,sheet_title,game_title)
                      VALUES('{data["id"]}','{data["pdf_url"]}','{data["mid_url"]}','{data["mus_url"]}',
                        {data["popularity"]},'{data["sheet_title"]}','{data["game_title"]}')'''
        cur = con.cursor()
        # print(sql)
        cur.execute(sql)
        pass


    elements = driver.find_element(By.ID, 'mainContentContainer')
    contentBoxes = elements.find_elements(By.CLASS_NAME, "contentBox")
    print(str(len(contentBoxes)) + " games found")
    for contentBox in contentBoxes:
        contentboxframe = contentBox.find_element(By.CLASS_NAME, "heading-text")
        game_title = contentboxframe.find_element(By.XPATH, "h3")
        game_title = game_title.text.replace('\"', "").replace("\'", "")

        table_items = contentBox.find_elements(By.CLASS_NAME, 'tableList-row--sheet')

        for j in table_items:
            data_row = {
                "id": None,
                "pdf_url": None,
                "mid_url": None,
                "mus_url": None,
                "popularity": None,
                "sheet_title": None,
                "game_title": game_title
            }


            row_id = j.get_attribute("id")
            data_row["id"] = row_id

            sheet_title = j.find_elements(By.CLASS_NAME, 'tableList-cell--sheetTitle')
            for sheet in sheet_title:
                data_row["sheet_title"] = sheet.text.replace('\"', "").replace("\'", "")

            pdf_url_frame = j.find_element(By.CLASS_NAME, 'tableList-buttonCell--sheetPdf')
            pdf_url = pdf_url_frame.get_attribute("href")
            data_row["pdf_url"] = pdf_url

            mid_url_frame = j.find_element(By.CLASS_NAME, 'tableList-buttonCell--sheetMid')
            mid_url = mid_url_frame.get_attribute("href")
            data_row["mid_url"] = mid_url

            mus_url_frame = j.find_element(By.CLASS_NAME, 'tableList-buttonCell--sheetMus')
            mus_url = mus_url_frame.get_attribute("href")
            data_row["mus_url"] = mus_url

            p = j.find_element(By.CLASS_NAME, 'popularityBar')
            popularity = p.get_attribute("title").split(" ")[1].split("/")[0]
            data_row["popularity"] = popularity
            print(data_row)
            insert_row(data_row)
    time.sleep(2)



    driver.close()

    con.commit()
    con.close()

