"""
Utility functions for the Invisibility Cloak project
"""

import cv2
import numpy as np
import os
import time
from config import Config

def create_output_folder():
    """Create output folder if it doesn't exist"""
    if not os.path.exists(Config.OUTPUT_FOLDER):
        os.makedirs(Config.OUTPUT_FOLDER)
        print(f"Created '{Config.OUTPUT_FOLDER}' folder for video recordings")

def get_video_filename():
    """Generate timestamped filename for video recording"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{Config.OUTPUT_FOLDER}/invisibility_cloak_{timestamp}.avi"
    return filename

def display_text(frame, text, position, font_scale=0.5, color=(255, 255, 255), thickness=1):
    """
    Display text on frame
    
    Args:
        frame: Image frame
        text: Text to display
        position: (x, y) coordinates
        font_scale: Size of the font
        color: BGR color tuple
        thickness: Text thickness
    """
    cv2.putText(frame, text, position, Config.FONT, font_scale, color, thickness)

def display_instructions(frame, background_captured, is_recording):
    """
    Display instructions and status on frame with improved visibility
    
    Args:
        frame: Image frame
        background_captured: Boolean indicating if background is captured
        is_recording: Boolean indicating if recording is active
    """
    # Create semi-transparent overlay for better text visibility
    overlay = frame.copy()
    height, width = frame.shape[:2]
    
    # Draw semi-transparent background rectangle for instructions
    cv2.rectangle(overlay, (5, 5), (width - 5, 155), (0, 0, 0), -1)
    
    # Blend the overlay with the frame
    alpha = 0.7  # Transparency factor (increased for better visibility)
    frame_with_overlay = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    
    # Add border around instruction box
    cv2.rectangle(frame_with_overlay, (5, 5), (width - 5, 155), (0, 255, 255), 2)
    
    instructions = [
        "CONTROLS:",
        "  'B' - Capture/Recapture Background",
        "  'R' - Start/Stop Recording",
        "  'Q' or 'ESC' - Quit Program"
    ]
    
    y_offset = 30
    for i, instruction in enumerate(instructions):
        color = (0, 255, 255) if i == 0 else (255, 255, 255)  # Cyan for header
        thickness = 2 if i == 0 else 2  # All bold text
        font_scale = 0.8 if i == 0 else 0.65
        
        cv2.putText(frame_with_overlay, instruction, (20, y_offset + i * 32),
                   Config.FONT, font_scale, color, thickness, cv2.LINE_AA)
    
    # Display background status with background box
    status_text = "Background: " + ("CAPTURED ✓" if background_captured else "NOT CAPTURED ✗")
    status_color = (0, 255, 0) if background_captured else (0, 0, 255)
    
    # Background box for status
    status_y = height - 55
    cv2.rectangle(frame_with_overlay, (5, status_y - 5), (width - 5, height - 5), (0, 0, 0), -1)
    overlay_status = frame_with_overlay.copy()
    cv2.rectangle(overlay_status, (5, status_y - 5), (width - 5, height - 5), (0, 0, 0), -1)
    frame_with_overlay = cv2.addWeighted(overlay_status, 0.7, frame_with_overlay, 0.3, 0)
    
    # Add border to status box
    cv2.rectangle(frame_with_overlay, (5, status_y - 5), (width - 5, height - 5), status_color, 2)
    
    cv2.putText(frame_with_overlay, status_text, (20, status_y + 22),
               Config.FONT, 0.8, status_color, 2, cv2.LINE_AA)
    
    # Display recording indicator with pulsing effect
    if is_recording:
        # Create pulsing red circle
        import time
        pulse = int(abs(np.sin(time.time() * 3) * 8))
        cv2.circle(frame_with_overlay, (width - 120, 35), 15 + pulse, (0, 0, 255), -1)
        cv2.circle(frame_with_overlay, (width - 120, 35), 15 + pulse, (255, 255, 255), 2)
        cv2.putText(frame_with_overlay, "REC", (width - 85, 43),
                   Config.FONT, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
    
    return frame_with_overlay

def apply_morphological_operations(mask):
    """
    Apply morphological operations to clean up the mask
    
    Args:
        mask: Binary mask
    
    Returns:
        Cleaned mask
    """
    import numpy as np
    kernel = np.ones(Config.KERNEL_SIZE, np.uint8)
    
    # Remove noise with opening
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, 
                           iterations=Config.MORPH_OPEN_ITERATIONS)
    
    # Fill gaps with closing
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel,
                           iterations=Config.MORPH_CLOSE_ITERATIONS)
    
    # Expand the mask slightly
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, 
                           iterations=Config.MORPH_DILATE_ITERATIONS)
    
    # Smooth the edges of the mask
    mask = cv2.GaussianBlur(mask, Config.MASK_BLUR_KERNEL, 0)
    
    return mask

def print_welcome_message():
    """Print welcome message and instructions"""
    print("\n" + "="*50)
    print(" "*10 + "INVISIBILITY CLOAK PROJECT")
    print("="*50)
    print("\n📋 Instructions:")
    print("  1. Press 'B' to capture background")
    print("  2. Wear/hold a RED cloth")
    print("  3. Watch the magic happen!")
    print("  4. Press 'R' to record video")
    print("  5. Press 'Q' or 'ESC' to quit")
    print("\n💡 Tips:")
    print("  - Use bright lighting for best results")
    print("  - Keep background static when capturing")
    print("  - Use a solid red cloth")
    print("="*50 + "\n")