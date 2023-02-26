import requests

def download_file_from_url(url):
    # url = "https://www.ninsheetmusic.org/download/mus/4211"
    payload={}
    headers = {
      'Cookie': 'PHPSESSID=1aeb3d5bad36da03cb36e01f5ee20c4a'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    filename = response.headers["Content-Disposition"]
    filename = filename.split("\"")[1]
    # print(response.content)

    f = open("download/" + filename, 'wb')
    f.write(response.content)
    f.close()

