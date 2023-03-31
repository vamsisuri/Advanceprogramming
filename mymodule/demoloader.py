import threading

import line as line
import requests
import time
import concurrent.futures
from threading import current_thread
with open('urls.txt','r') as url_list:
    print(current_thread(getname()))
    img_urls = [str(line) for line in url.readlines()]
print(img_urls)
print(len(img_urls))
i=1
def download_image(img_url):
    img_bytes = requests.get(img_url).content

    global i
    img_name='img'+str(i)
    i+=1


    img_name = f'{img_name}.jpg'
    folder_path="./images/"
    with open(folder_path+img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_names} was downloaded...')

t1 = time.perf_counter()
with cocurrent.futures.ThreadPoolExecutor() as executor:
    for url in img_urls:
        executor.submit(download_image, url)