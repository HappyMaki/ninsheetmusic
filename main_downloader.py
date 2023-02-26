from download_file import download_file_from_url
import sqlite3
import time
import random

con = sqlite3.connect("ninsheetmusic.db")

con.row_factory = lambda cursor, row: row[0]
c = con.cursor()
urls = c.execute("""
    SELECT mus_url FROM ninsheetmusic
""").fetchall()
con.close()

total_urls = len(urls)
i = 0
for url in urls:
    # print(url)
    time.sleep(random.randint(1, 3))
    download_file_from_url(url)
    i += 1
    if i % 100 == 0:
        print(f"Downloaded: {i}/{total_urls}")





