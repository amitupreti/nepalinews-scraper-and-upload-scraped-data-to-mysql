# nepalinews-scraper-and-upload-scraped-data-to-mysql


## Welcome to the Nepali-news-Web-Scraper!

### with this scraper you can scrape every news article from onlinekhabar.com and  upload it to MySQL database

## Notes:
     Operating System: Linux
     Language:         python3
     libraries:        Scrapy,pymysql

     This scraper was purely  built for research purpose. 
### install pymysql
`pip3 install pymysql`

[https://www.onlinekhabar.com](https://www.onlinekhabar.com)


Please note that you might need to make some changes to the scraper 
if in future the interface of the onlinekhabar.com is 
changed.( the scraping is totally based on CSS)

### Guides to use the scrapper
 1. clone this repository to your computer
 2. Launch terminal
 3. Navigate to the folder with file scrapy.cfg
 4. `scrapy crawl onlinekhabr -a address="https://onlinekhabar.com/content/news/" 

 This is the sample code

 `scrapy crawl onlinekhabr  -a address="https://onlinekhabar.com/content/news/" 

 ### Explanation of code :  
   * it will extract  news title and  news article  and upload the data in json format to MySQL


<a href="https://ibb.co/kMd7HG"><img src="https://preview.ibb.co/eJzsjw/git.png" alt="git" border="0" /></a>



