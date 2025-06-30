# Webcrawlbot-diemthi.vnexpress


## **Overview:**
### Web Crawler - [diemthi.vnexpress.net](http://diemthi.vnexpress.net/)


A Python crawler using Scrapy/Selenium to collect university admission data from [https://diemthi.vnexpress.net](https://diemthi.vnexpress.net/).

### Repo Structure 

```bash
project/
│
├── vnexpress_uni/              # Scrapy spider and Selenium logic
│   ├── spiders/
│   ├── [items.py]
│   ├── [pipelines.py]
│   └── [settings.py]
│
├── requirement.txt             # Python dependencies
├── .gitignore                  # Ignore compiled and venv files
└── [README.md](http://readme.md/)                   # Project documentation

```

```bash
pip install -r requirement.txt
scrapy crawl allinfo

```

 ### Business Objective

This project aims to develop an automated web crawler that annually collects university admission data from **diemthi.vnexpress.net**. The extracted data will be structured into a centralized dataset to support internal teams in:

- Conducting competitive analysis across universities and majors
- Understanding trends and shifts in the higher education landscape in Vietnam
- Informing recruitment and market research strategies with evidence-based insights

By automating this process, the project minimizes manual effort, ensures greater accuracy, and enables consistent annual reporting

### Technical Overview:

This project is built using **Python**, combining the strengths of **Scrapy** and **Selenium** to crawl and extract structured university admission data from diemthi.vnexpress.net.
**Packages Used:**

- **Scrapy**: for crawling grouped major URLs based on sitemap rules
- **Selenium**: for extracting content from JavaScript-rendered tables
- **Python venv**: for dependency isolation and environment management

**Crawler Architecture Overview**

*The following diagram illustrates how the crawler is structured and how each component interacts:*

![process.drawio.png](/image/process.drawio.png)

 **How It Works:**

1. The Scrapy spider starts by parsing the sitemap and follows URLs matching specific patterns contained “nhom-nganh”
2. For each matched page, Selenium is used to wait for the table containing admission scores to fully render.
3. It then extracts:
    
    `“program_group”`
    
    `“program_name”`
    
    `“program_code”`
    
    `“entry_score”`
    
    `“tuition_fee”`
    
    `“university_name”`
    
4. The extracted data is structured and exported to CSV or JSON format for further use.
