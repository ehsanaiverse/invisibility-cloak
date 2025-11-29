```markdown
# 📦 Installation Guide

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: 4GB
- **Webcam**: Any USB or built-in webcam
- **Processor**: Intel i3 or equivalent

### Recommended Requirements
- **RAM**: 8GB or higher
- **Processor**: Intel i5 or equivalent
- **Webcam**: HD (720p) or better

## Installation Steps

### 1. Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer and **check "Add Python to PATH"**
3. Verify installation:
```bash
python --version
```

#### macOS
```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
```

### 2. Clone Repository

```bash
git clone https://github.com/ehsanaiverse/invisibility-cloak.git
cd invisibility-cloak
```

### 3. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Installation

```bash
python src/main.py
```

## Troubleshooting

### Issue: OpenCV import error

**Solution**:
```bash
pip uninstall opencv-python opencv-python-headless
pip install opencv-python
```

### Issue: Camera not detected

**Solution**:
- Check camera permissions in system settings
- Try different camera index in `config.py`
- Ensure no other application is using the camera

### Issue: Permission denied on Linux

**Solution**:
```bash
sudo usermod -a -G video $USER
# Logout and login again
```

## Updating

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

```bash
# Deactivate virtual environment
deactivate

# Remove project folder
cd ..
rm -rf invisibility-cloak
```