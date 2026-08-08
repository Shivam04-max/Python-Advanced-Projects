import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


class Browser:
    def __init__(self):
        print("Starting browser...")

        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-extensions")

        # Selenium Manager downloads the correct ChromeDriver automatically
        self.browser = webdriver.Chrome(options=self.chrome_options)

    def scrape_emails(self, url: str):
        print(f'Scraping "{url}" for emails...')

        self.browser.get(url)

        page_source = self.browser.page_source

        emails = set(re.findall(EMAIL_REGEX, page_source))

        return emails

    def close_browser(self):
        print("Closing browser...")
        self.browser.quit()


def main():
    browser = Browser()

    url = "https://www.randomlists.com/email-address?qty=50"

    emails = browser.scrape_emails(url)

    if emails:
        print(f"\nFound {len(emails)} email(s):\n")

        for i, email in enumerate(sorted(emails), start=1):
            print(f"{i}: {email}")
    else:
        print("No emails found.")

    browser.close_browser()


if __name__ == "__main__":
    main()
