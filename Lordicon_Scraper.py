# Website: https://lordicon.com/icons

import requests

# websites to be scraped
baseUrl = 'https://lordicon.com/api/library/icons?loadData=1&categoryId='
# Local download directory
download_dir = '/home/vossi/Downloads/'
# Limit the maximum number of downloads. None = download everything
numDownloads = 100


def scrape():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    files_created = 0
    for i in range(numDownloads):

        print(f'Download {i + 1} / {numDownloads} from: {baseUrl} {i}')

        request = requests.get(baseUrl + str(i), headers=headers)

        print(f"Status code: {request.status_code}; Headers: {request.headers['content-type']}; "
              f"Encoding: {request.encoding}")

        # Don't write empty files
        if len(request.content) < 3:
            continue

        with open(f'{download_dir}lottie_json_{i}.json', 'wb') as file:
            file.write(request.content)
            files_created += 1

    print(" ")
    print(f'Done. Scraped `{numDownloads}` URLs and created `{files_created}` lottie json files at `{download_dir}')


if __name__ == '__main__':
    scrape()
