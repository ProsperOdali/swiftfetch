import requests
import argparse
from bs4 import BeautifulSoup


def get_pdf_files(url: str) -> list[str]:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return [link["href"] for link in links if link["href"].endswith(".pdf")]

def download_file(filename: str, url: str) -> None:
    print(f"Downloading {filename}...")
    file_url = url + "/" + filename
    response = requests.get(file_url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

def main(ip: str, port: int) -> None:
    url = f"http://{ip}:{port}"
    files = get_pdf_files(url)
    for filename in files:
        download_file(filename, url)

def cli():
    parser = argparse.ArgumentParser(
        description="Download PDF files from an uploadserver."
    )

    parser.add_argument("ip", help="Ip address of the server")
    parser.add_argument("port", type=int, help="Port number")

    args = parser.parse_args()

    main(args.ip, args.port)

if __name__ == "__main__":
    cli()