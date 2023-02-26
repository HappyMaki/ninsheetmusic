from scrape_data_into_db import scrape_ninsheetmusic_to_sqlitedb

urls = ["https://www.ninsheetmusic.org/browse/series/AnimalCrossing"
        ]

for url in urls:
    scrape_ninsheetmusic_to_sqlitedb(url)
