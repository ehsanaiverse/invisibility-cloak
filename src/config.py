"""
Configuration file for Invisibility Cloak project
Contains all HSV ranges and settings
"""

import numpy as np

class Config:
    # Camera settings
    CAMERA_INDEX = 0
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    
    # HSV color ranges for RED detection
    # Red color wraps around in HSV space, so we need two ranges
    LOWER_RED1 = np.array([0, 120, 70])
    UPPER_RED1 = np.array([10, 255, 255])
    LOWER_RED2 = np.array([170, 120, 70])
    UPPER_RED2 = np.array([180, 255, 255])
    
    # Morphological operations kernel size
    KERNEL_SIZE = (5, 5)
    MORPH_OPEN_ITERATIONS = 3
    MORPH_DILATE_ITERATIONS = 2
    MORPH_CLOSE_ITERATIONS = 2
    
    # Background capture settings
    BACKGROUND_FRAMES = 50  # Number of frames to average for background
    COUNTDOWN_SECONDS = 3
    
    # Mask smoothing
    GAUSSIAN_BLUR_KERNEL = (7, 7)
    MASK_BLUR_KERNEL = (21, 21)
    
    # Video recording settings
    VIDEO_CODEC = 'XVID'
    VIDEO_FPS = 20.0
    OUTPUT_FOLDER = 'output'
    
    # UI settings
    FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
    FONT_SCALE = 0.5
    FONT_COLOR = (255, 255, 255)
    FONT_THICKNESS = 1
    
    # Window names
    MAIN_WINDOW = 'Invisibility Cloak'