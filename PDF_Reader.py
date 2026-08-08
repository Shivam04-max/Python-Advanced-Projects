import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    try:
        with open(pdf_file, "rb") as pdf:
            reader = PdfReader(pdf, strict=False)

            print("Pages:", len(reader.pages))

            pdf_text: list[str] = [
                page.extract_text() or ""
                for page in reader.pages
            ]

            return pdf_text

    except FileNotFoundError:
        print(f"Error: The file '{pdf_file}' was not found.")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []

    for text in text_list:
        split_text = re.split(r"\s+|[,;?!.-]\s*", text.lower())
        all_words.extend(word for word in split_text if word)

    return Counter(all_words)


def main():
    extracted_text = extract_text_from_pdf("Python is a high.pdf")

    # Stop if the PDF couldn't be read
    if not extracted_text:
        return

    counter = count_words(extracted_text)

    for page in extracted_text:
        print(page)
        print()

    for word, mentions in counter.most_common(7):
        print(f"{word:10}: {mentions} times")


if __name__ == "__main__":
    main()
