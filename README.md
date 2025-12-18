# PingLinker 🚀

**PingLinker** is a professional command-line tool for testing internet connection speed. It provides a clean, visual interface to measure download/upload speeds and ping latency, powered by `speedtest-cli` and `rich`.

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Overview

PingLinker offers a modern terminal experience for network diagnostics. Whether you need a full connection audit or a quick latency check, PingLinker delivers accurate results with color-coded performance indicators.

## ✨ Features

-   **Full Speed Test**: Measure Download, Upload, and Ping in one go.
-   **Modular Testing**: Flags to run specific tests individually (e.g., just download).
-   **Connection Details**: Display ISP, Server location, and Country.
-   **Rich UI**: Beautiful terminal output with progress spinners and colored results.
-   **Performance Grading**: Visual color cues (Green/Yellow/Orange) indicating connection quality.

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/K1taSun/PingLinker
    cd PingLinker
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Run the tool directly from the command line:

```bash
python main.py
```

### Command Options

You can use flags to perform specific actions:

| Flag | Short | Description |
|------|-------|-------------|
| `--download` | `-d` | Test **Download** speed only |
| `--upload` | `-u` | Test **Upload** speed only |
| `--ping` | `-p` | Measure **Ping** latency only |
| `--info` | `-i` | Show **ISP** and **Server** information |
| `--help` | | Show all available options |

**Examples:**

```bash
# Run only a download test
python main.py -d

# Check connection info and ping
python main.py -i
```

## 📦 Dependencies

-   `click`: For the command-line interface.
-   `rich`: For beautiful terminal formatting.
-   `speedtest-cli`: For the underlying network testing.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Copyright (c) 2025 Nikita Parkovskyi

