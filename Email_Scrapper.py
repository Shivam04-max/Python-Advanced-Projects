import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


EMAIL_REGEX = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"


class Browser:
    def __init__(self):
        print("Starting up browser...")

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")

        # Selenium Manager automatically downloads the correct ChromeDriver
        self.browser = webdriver.Chrome(options=chrome_options)

    def scrape_emails(self, url: str) -> set:
        print(f'Scraping: "{url}" for emails')

        self.browser.get(url)

        page_source = self.browser.page_source

        emails = set()

        for match in re.finditer(EMAIL_REGEX, page_source):
            emails.add(match.group())

        return emails

    def close_browser(self):
        print("Closing browser...")
        self.browser.quit()


def main():
    browser = Browser()

    emails = browser.scrape_emails(
        "https://www.randomlists.com/email-addresses?qty=50"
    )

    print("\nEmails Found:")

    for i, email in enumerate(emails, start=1):
        print(f"{i}: {email}")

    print(f"\nTotal emails found: {len(emails)}")

    browser.close_browser()


if __name__ == "__main__":
    main()
