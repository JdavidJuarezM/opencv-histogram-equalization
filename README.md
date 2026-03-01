<div align="center">

# 📊 OpenCV Histogram Equalization

**A computer vision script for enhancing grayscale image contrast using OpenCV**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![Data Visualization](https://img.shields.io/badge/Data_Viz-FF6F00?style=for-the-badge&logo=python&logoColor=white)](#)

*A Python-based utility that converts images to grayscale, calculates their intensity distributions, and applies histogram equalization to drastically improve contrast while generating visual plots of the results.*

</div>

<br />

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Architecture & Structure](#️-architecture--structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Execution](#execution)
- [🛠️ Tech Stack](#️-tech-stack)

---

## ✨ Key Features

* **✔️ Grayscale Conversion:** Automatically reads and converts standard color images into single-channel grayscale for accurate intensity analysis.
* **✔️ Contrast Enhancement:** Applies mathematical histogram equalization to stretch the dynamic range of the image, revealing hidden details in overexposed or underexposed areas.
* **✔️ Visual Analytics:** Generates and saves detailed `.png` plots using Matplotlib, comparing the pixel intensity distributions before and after equalization.
* **✔️ Automated File Management:** Neatly organizes all processed images and generated histogram charts into a dedicated `output/` directory.

---

## 🏗️ Architecture & Structure

The repository is kept simple and highly focused on the core computer vision mathematical transformations:

```text
opencv-histogram-equalization/
├── histogram_equalization.py    # Main image processing and plotting script
├── input_image.jpg              # Sample input image to process
├── output/                      # Automatically generated outputs
│   ├── equalized_image.jpg      # The final contrast-enhanced image
│   ├── grayscale_image.jpg      # The intermediate grayscale conversion
│   ├── equalized_histogram.png  # Histogram plot of the equalized image
│   └── grayscale_histogram.png  # Histogram plot of the original grayscale image
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

To run this project, ensure you have Python installed on your local machine along with the required computer vision and plotting libraries:

* **Python:** Version 3.x
* **OpenCV:** For image processing (`cv2`)
* **Matplotlib:** For generating histogram plot visualizations

You can install the required dependencies using pip:
```bash
pip install opencv-python matplotlib
```

### Execution

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd opencv-histogram-equalization
   ```
3. Run the Python script:
   ```bash
   python histogram_equalization.py
   ```
4. The script will read `input_image.jpg`, process it, and save all resulting images and analytical plots inside the `output/` folder.

---

## 🛠️ Tech Stack

* **Python** - Core programming language
* **OpenCV (`cv2`)** - Computer Vision and image array manipulation
* **Matplotlib (`pyplot`)** - Mathematical plotting and histogram generation

<br />

<div align="center">
  <i>Developed with ☕ to explore Image Processing and Computer Vision.</i>
</div>
