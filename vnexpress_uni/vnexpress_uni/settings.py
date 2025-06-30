# Scrapy settings for vnexpress_uni project

BOT_NAME = "vnexpress_uni"

SPIDER_MODULES = ["vnexpress_uni.spiders"]
NEWSPIDER_MODULE = "vnexpress_uni.spiders"

# Selenium Configuration
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

# Selenium Settings
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = None  # Will use webdriver-manager to auto-download
SELENIUM_DRIVER_ARGUMENTS = [
    '--headless=new',  # Remove this to see the browser in action
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--window-size=1920,1080',
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]

# Browser window size
SELENIUM_BROWSER_WINDOW_SIZE = (1920, 1080)

# How long to wait for page to load (seconds)
SELENIUM_PAGE_LOAD_TIMEOUT = 30

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests (keep low for Selenium)
CONCURRENT_REQUESTS = 1  # Important: Keep this at 1 for Selenium to avoid issues

# Configure delay between requests
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = 0.5

# Disable cookies for simpler operation
COOKIES_ENABLED = False

# AutoThrottle settings
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Set settings whose default value is deprecated
FEED_EXPORT_ENCODING = "utf-8"

# Logging
LOG_LEVEL = 'INFO'

# Request fingerprinting
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"