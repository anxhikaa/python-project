# Advanced CLI QR Code & Barcode Reader

A Python-based Command-Line Interface (CLI) tool designed to detect, decode, and extract data from barcodes and QR codes within images. It features spatial data extraction and the ability to export scan logs directly to text files.

## Features

- **Multi-Code Support:** Automatically detects and decodes multiple barcodes or QR codes present within a single image.
- **Quick Scan:** Rapidly extracts and displays only the decoded data and the code format (e.g., `QRCODE`, `EAN13`, `CODE128`).
- **Detailed Scan:** Extracts precise spatial data, including the exact bounding box rectangle and polygon corner coordinates (useful for overlaid graphics).
- **Data Export:** Prompt-driven option to automatically save detailed scan results to a formatted `.txt` file.
- **Robust Error Handling:** Prevents script crashes due to missing files or images lacking scannable codes.

## System Prerequisites

The `pyzbar` library relies on the `zbar` shared library. You must install this system dependency based on your OS before running the script:

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install libzbar0
  ```
- **macOS:**
  ```bash
  brew install zbar
  ```
- **Windows:**
  The Windows `.whl` package for `pyzbar` typically includes the required `zbar` DLLs, so no extra system installation is usually required.

## Installation

1. Clone or download this repository.
2. Install the required Python packages:
   ```bash
   pip install Pillow pyzbar
   ```

## Usage

Ensure the image you want to scan is located in the same directory as the script (or provide a full absolute path).

Run the script from your terminal:

```bash
python qr_reader.py
```

### Example Workflow:
1. Select option `2` for a Detailed Scan.
2. Enter the target image filename (e.g., `sample_qr.png`).
3. View the decoded string, barcode type, and spatial coordinates in the terminal.
4. Type `y` when prompted to save the output to `sample_qr_results.txt`.
