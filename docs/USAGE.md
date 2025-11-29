```markdown
# 📖 Usage Guide

## Quick Start

```bash
python src/main.py
```

## Detailed Usage

### Step 1: Launch Application

Open terminal in project directory:
```bash
cd invisibility-cloak
python src/main.py
```

### Step 2: Position Camera

- Place camera on stable surface
- Ensure good lighting (natural light or bright room)
- Position yourself 3-5 feet from camera

### Step 3: Capture Background

1. Press `B` key
2. Countdown timer appears (3 seconds)
3. Move completely out of frame
4. System captures 50 frames automatically
5. Wait for "Background captured successfully!" message

### Step 4: Use the Cloak

1. Hold or wear a **bright red cloth**
2. Move the cloth in front of camera
3. Watch it become invisible!

### Step 5: Record Video (Optional)

1. Press `R` to start recording
2. Recording indicator appears (red pulsing circle)
3. Press `R` again to stop
4. Video saved in `output/` folder

### Step 6: Exit

Press `Q` or `ESC` to quit

## Keyboard Controls

| Key | Function |
|-----|----------|
| `B` | Capture/Recapture Background |
| `R` | Toggle Recording On/Off |
| `Q` | Quit Application |
| `ESC` | Quit Application |

## Tips & Tricks

### For Best Results

1. **Lighting**
   - Use bright, even lighting
   - Avoid harsh shadows
   - Natural daylight works best

2. **Cloth Selection**
   - Use solid, bright red cloth
   - Smooth fabric (no wrinkles)
   - Larger cloth = better effect

3. **Background**
   - Use static background
   - Avoid moving objects
   - Plain backgrounds work better

4. **Camera Position**
   - Keep camera stable
   - Avoid moving camera after background capture
   - Mount on tripod for best results

### Advanced Techniques

#### Recapturing Background
- Change location or lighting? Press `B` to recapture
- Move furniture? Recapture background
- Time of day changed? Recapture for best results

#### Better Detection
- If cloth not detected well, try:
  - Brighter lighting
  - Different red cloth
  - Adjust position relative to light source

## Output Files

### Video Format
- **Location**: `output/` folder
- **Format**: `.avi`
- **Naming**: `invisibility_cloak_YYYYMMDD_HHMMSS.avi`
- **Codec**: XVID

### Playing Recorded Videos
- Use VLC Media Player (recommended)
- Windows Media Player
- Any modern video player

## Customization

### Changing Settings

Edit `src/config.py`:

```python
# Camera resolution
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Background capture frames
BACKGROUND_FRAMES = 50  # Increase for better quality

# HSV color ranges (adjust for your cloth)
LOWER_RED1 = np.array([0, 120, 70])
UPPER_RED1 = np.array([10, 255, 255])
```

## Common Use Cases

### 1. Photography/Videography
- Create magical photos
- Special effects for videos
- Creative content for social media

### 2. Education
- Learn computer vision
- Demonstrate HSV color spaces
- Teach image processing concepts

### 3. Entertainment
- Party tricks
- Magic shows
- Fun with kids

## Troubleshooting Common Issues

### Cloth Not Disappearing
✅ Check lighting conditions
✅ Try brighter red cloth
✅ Recapture background

### Flickering Effect
✅ Improve lighting (reduce shadows)
✅ Keep camera stable
✅ Use smoother cloth

### Lag/Slow Performance
✅ Close other applications
✅ Reduce resolution in config.py
✅ Check CPU usage

### Recording Not Working
✅ Check output folder exists
✅ Ensure write permissions
✅ Check disk space

## Performance Optimization

### For Low-End Systems
```python
# In config.py
BACKGROUND_FRAMES = 30  # Reduce from 50
FRAME_WIDTH = 480  # Reduce from 640
FRAME_HEIGHT = 360  # Reduce from 480
```

### For High-End Systems
```python
# In config.py
BACKGROUND_FRAMES = 100  # Increase for better quality
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
```
```