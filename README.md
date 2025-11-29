# 🪄 Invisibility Cloak - Real-Time Computer Vision Magic

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

*Experience the magic of Harry Potter's invisibility cloak in real-time!*

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Contributing](#-contributing)

</div>

---

## 📖 About

A Python-based computer vision project that creates a real-time invisibility cloak effect using OpenCV. Simply wear or hold a red cloth, and watch it disappear like magic! This project demonstrates advanced image processing techniques including HSV color detection, morphological operations, and seamless frame blending.

## ✨ Features

- 🎯 **Real-time Processing** - Smooth 20+ FPS performance
- 🎨 **Advanced Color Detection** - HSV-based red cloth detection
- 🖼️ **Smart Background Capture** - 50-frame median averaging for stability
- 🎬 **Video Recording** - Save your magical moments
- 📊 **Enhanced Visibility** - Professional UI with semi-transparent overlays
- 🔧 **Optimized Processing** - Advanced morphological operations for smooth edges
- 💡 **User-Friendly** - Clear on-screen instructions and visual feedback

## 🎥 Demo

![Invisibility Cloak Demo](assets/demo.gif)

*Red cloth becomes completely invisible, revealing the background behind it!*

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam
- Good lighting conditions

### Step 1: Clone the Repository
```bash
git clone https://github.com/ehsanaiverse/invisibility-cloak.git
cd invisibility-cloak
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage
```bash
python src/main.py
```

### Controls

| Key | Action |
|-----|--------|
| `B` | Capture/Recapture Background |
| `R` | Start/Stop Recording |
| `Q` or `ESC` | Quit Application |

### Step-by-Step Guide

1. **Run the program**
```bash
   python src/main.py
```

2. **Position yourself** - Stand in front of the camera

3. **Capture background** - Press `B` and move out of frame when countdown starts

4. **Grab red cloth** - Use a bright, solid red cloth for best results

5. **Experience magic!** - Watch the cloth become invisible

6. **Record video** - Press `R` to save your magical moment

7. **Exit** - Press `Q` or `ESC` when done

## 🛠️ How It Works

### 1. Background Capture
- Captures 50 frames and uses median averaging
- Applies Gaussian blur for smooth blending
- Stores the clean background for replacement

### 2. Color Detection
- Converts frames to HSV color space
- Detects red color using two HSV ranges (red wraps around in HSV)
- Creates binary mask of detected regions

### 3. Mask Processing
- **Morphological Opening** - Removes noise
- **Morphological Closing** - Fills gaps
- **Dilation** - Expands mask slightly
- **Gaussian Blur** - Smooths mask edges

### 4. Frame Blending
- Uses normalized mask for smooth alpha blending
- Replaces red regions with background
- Creates seamless invisibility effect

### Technical Details
```python
# HSV Color Ranges for Red Detection
LOWER_RED1 = [0, 120, 70]
UPPER_RED1 = [10, 255, 255]
LOWER_RED2 = [170, 120, 70]
UPPER_RED2 = [180, 255, 255]
```

## 📁 Project Structure
```
invisibility-cloak/
├── src/
│   ├── main.py          # Entry point
│   ├── cloak.py        # Core logic
│   ├── config.py       # Configuration
│   └── utils.py        # Helper functions
├── output/             # Saved videos
├── assets/            # Demo files
├── docs/              # Documentation
└── requirements.txt   # Dependencies
```

## 🎓 Learning Outcomes

This project teaches:

- ✅ Computer Vision fundamentals
- ✅ HSV color space and color detection
- ✅ Image masking and bitwise operations
- ✅ Morphological transformations
- ✅ Real-time video processing
- ✅ Frame blending techniques
- ✅ OpenCV advanced features

## 💡 Tips for Best Results

1. **Lighting** - Use bright, even lighting
2. **Cloth** - Bright solid red cloth works best
3. **Background** - Keep background static during capture
4. **Distance** - Stand 3-5 feet from camera
5. **Movement** - Stay still when capturing background

## 🐛 Troubleshooting

### Cloth not detected?
- Ensure good lighting
- Use a brighter red cloth
- Check if cloth is wrinkled (use smooth cloth)

### Flickering effect?
- Improve lighting conditions
- Ensure stable camera position
- Recapture background in better lighting

### Poor quality output?
- Check camera resolution
- Ensure clean camera lens
- Improve lighting setup

## 📊 Performance

- **FPS**: 20-30 (depending on hardware)
- **Resolution**: 640x480 (configurable)
- **Latency**: < 50ms
- **RAM Usage**: ~200MB

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## 📝 To-Do

- [ ] Support for multiple colors
- [ ] GUI for color selection
- [ ] Mobile app version
- [ ] Real-time color calibration
- [ ] Performance optimization for low-end devices
- [ ] Multi-person support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ehsan Ullah**
- GitHub: [@ehsanaiverse](https://github.com/ehsanaiverse)
- LinkedIn: [Ehsan Ullah](https://linkedin.com/in/ehsanaiverse)
- Email: ehsanullah.contact@gmail.com

## 🙏 Acknowledgments

- Inspired by Harry Potter's invisibility cloak
- Built with [OpenCV](https://opencv.org/)
- Thanks to the computer vision community

## 📚 References

- [OpenCV Documentation](https://docs.opencv.org/)
- [HSV Color Space](https://en.wikipedia.org/wiki/HSL_and_HSV)
- [Morphological Transformations](https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn something new!

---

<div align="center">

**Made with ❤️ and Python**

[Report Bug](https://github.com/ehsanaiverse/invisibility-cloak/issues) • [Request Feature](https://github.com/ehsanaiverse/invisibility-cloak/issues)

</div>
```