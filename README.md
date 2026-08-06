# SwiftFetch

SwiftFetch is a lightweight command-line tool for downloading PDF files from an HTTP directory listing, such as one served by Python's `uploadserver`.

## Features

- Download all PDF files from a local HTTP file server.
- Simple command-line interface.
- Lightweight and easy to use.

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/swiftfetch.git
```

Move into the project directory:

```bash
cd swiftfetch
```

Install the package:

```bash
pip install -e .
```

## Usage

Start an HTTP file server (for example, with `uploadserver`):

```bash
python -m uploadserver 3000
```

Then run:

```bash
swiftfetch 192.168.0.118 3000
```

All PDF files will be downloaded to the current working directory.

## Requirements

- Python 3.10+
- requests
- beautifulsoup4

## Roadmap

- [x] Download PDF files
- [ ] Custom download directory
- [ ] Support any file extension
- [ ] Download all file types
- [ ] Multithreaded downloads
- [ ] Progress bar
- [ ] Recursive directory downloads
- [ ] Resume interrupted downloads

## Contributing

Contributions, suggestions, and bug reports are welcome.

## License

This project is licensed under the MIT License.