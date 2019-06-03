# python_crawl_t1
python_crawl_t1

You can pip install scrapy on python 3.5+, you just have to pip install all the deppendencies first - from here https://docs.scrapy.org/en/latest/intro/install.html

```python
pip install lxml
pip install parsel
pip install w3lib
pip install twisted
pip install cryptography
pip install cryptography
pip install pyOpenSSL


pip install scrapy
```


https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

pip install Twisted-19.2.0-cp37-cp37m-win32.whl

## Make project

scrapy startproject xskt


scrapy genspider xskt1 xskt.com.vn


---

# project 2

https://viblo.asia/p/crawl-du-lieu-trang-web-voi-scrapy-E375zWr1KGW

scrapy startproject crawler

file json:
scrapy crawl crawler -o comments.json
hoặc file csv:
scrapy crawl crawler -o comments.csv

## Fix Error

No module named 'win32api'
>pip install pypiwin32
