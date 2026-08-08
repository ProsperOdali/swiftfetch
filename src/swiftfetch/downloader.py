import requests
import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_object_urls(url: str) -> list[str]:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return [link["href"] for link in links]


def download_file(filename: str,
                  url: str,
                  destination: Path | None)-> None:

        file_url = urljoin(url, filename)
        response = requests.get(file_url)
        response.raise_for_status()

        if destination == None:
             with open(filename, "wb") as f:
                  f.write(response.content)
        else:
            with open(destination / filename, "wb") as f:
                f.write(response.content)

def download_folder(folder_name: str,
                   url: str,
                   destination: Path,
                   recurse: bool =False) -> None:
     folder_url = urljoin(url, folder_name)
     response = requests.get(folder_url)
     response.raise_for_status()
     html = response.text
     soup = BeautifulSoup(html, "html.parser")
     links = soup.find_all("a")

     files = [link["href"] for link in links if not link["href"].endswith("/")]
     sub_folders = [link["href"] for link in links if link["href"].endswith("/")]

     if files == [] and sub_folders == []:
          print(f"{folder_name} is empty!")

     else:
        for file in files:             
             download_file(file,
                           folder_url,
                           destination)

        if recurse:
            for folder in sub_folders:
                download_folder(folder,
                               folder_url,
                               destination,
                               recurse=True)      

     
def download(object_name: str,
             url: str,
             destination: Path,
             recurse: bool=False) -> None:
    if object_name.endswith("/"):
        download_folder(object_name,
                        url,
                        destination,
                        recurse)
    else:
        download_file(object_name,
                      url,
                      destination)

    print("Done!") 


def main(ip: str, port: int) -> None:
    url = f"http://{ip}:{port}"
    files = get_object_urls(url)
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