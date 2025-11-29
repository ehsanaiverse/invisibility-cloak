"""
Core Invisibility Cloak class
Handles camera, background capture, masking, and video recording
"""

import cv2
import numpy as np
from config import Config
from utils import (create_output_folder, get_video_filename, 
                  display_instructions, apply_morphological_operations)

class InvisibilityCloak:
    def __init__(self):
        """Initialize the Invisibility Cloak system"""
        # Initialize webcam
        self.cap = cv2.VideoCapture(Config.CAMERA_INDEX)
        self.background = None
        self.recording = False
        self.video_writer = None
        
        # HSV ranges from config
        self.lower_red1 = Config.LOWER_RED1.copy()
        self.upper_red1 = Config.UPPER_RED1.copy()
        self.lower_red2 = Config.LOWER_RED2.copy()
        self.upper_red2 = Config.UPPER_RED2.copy()
        
        # Create output folder
        create_output_folder()
        
        # Create main window
        cv2.namedWindow(Config.MAIN_WINDOW)
    
    def capture_background(self):
        """Capture the background frame with improved quality"""
        print("\n🎬 Preparing to capture background...")
        print("⚠️  Please move out of the frame!")
        print("💡 Tip: Keep the camera and lighting steady\n")
        
        # Countdown with visual feedback
        for i in range(Config.COUNTDOWN_SECONDS, 0, -1):
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                
                # Create semi-transparent overlay
                overlay = frame.copy()
                height, width = frame.shape[:2]
                
                # Large countdown circle
                center = (width // 2, height // 2)
                radius = 120
                cv2.circle(overlay, center, radius, (0, 165, 255), -1)
                frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)
                cv2.circle(frame, center, radius, (255, 255, 255), 5)
                
                # Countdown number
                text = str(i)
                font_scale = 5
                thickness = 10
                text_size = cv2.getTextSize(text, Config.FONT, font_scale, thickness)[0]
                text_x = center[0] - text_size[0] // 2
                text_y = center[1] + text_size[1] // 2
                cv2.putText(frame, text, (text_x, text_y),
                           Config.FONT, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
                
                # Instruction text
                instruction = "Move out of frame!"
                cv2.putText(frame, instruction, (width // 2 - 200, height - 100),
                           Config.FONT, 1.2, (0, 165, 255), 3, cv2.LINE_AA)
                
                cv2.imshow(Config.MAIN_WINDOW, frame)
                cv2.waitKey(1000)
        
        # Capture multiple frames with progress indicator
        print("📸 Capturing background frames...")
        background_frames = []
        
        for i in range(Config.BACKGROUND_FRAMES):
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                background_frames.append(frame)
                
                # Show progress every 10 frames
                if (i + 1) % 10 == 0:
                    progress_frame = frame.copy()
                    progress_text = f"Capturing: {i + 1}/{Config.BACKGROUND_FRAMES}"
                    cv2.putText(progress_frame, progress_text, (20, 50),
                               Config.FONT, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.imshow(Config.MAIN_WINDOW, progress_frame)
                    cv2.waitKey(1)
        
        # Use median for better noise reduction
        self.background = np.median(background_frames, axis=0).astype(np.uint8)
        
        # Apply slight blur to background for smoother blending
        self.background = cv2.GaussianBlur(self.background, Config.GAUSSIAN_BLUR_KERNEL, 0)
        
        print("✅ Background captured successfully!")
        print("🎨 Background processed and optimized\n")
    
    def create_mask(self, hsv):
        """
        Create mask for red color detection
        
        Args:
            hsv: Frame in HSV color space
        
        Returns:
            Binary mask
        """
        # Red color wraps around in HSV, so we need two ranges
        mask1 = cv2.inRange(hsv, self.lower_red1, self.upper_red1)
        mask2 = cv2.inRange(hsv, self.lower_red2, self.upper_red2)
        mask = mask1 + mask2
        
        # Apply morphological operations to clean up
        mask = apply_morphological_operations(mask)
        
        return mask
    
    def start_recording(self, frame_width, frame_height):
        """Start video recording"""
        filename = get_video_filename()
        fourcc = cv2.VideoWriter_fourcc(*Config.VIDEO_CODEC)
        self.video_writer = cv2.VideoWriter(filename, fourcc, Config.VIDEO_FPS, 
                                           (frame_width, frame_height))
        self.recording = True
        print(f"🎥 Recording started: {filename}")
    
    def stop_recording(self):
        """Stop video recording"""
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
            self.recording = False
            print("⏹️  Recording stopped and saved!\n")
    
    def process_frame(self, frame):
        """
        Process frame to create invisibility effect with improved blending
        
        Args:
            frame: Input frame
        
        Returns:
            Processed frame with invisibility effect
        """
        # Convert frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create mask for red color
        mask = self.create_mask(hsv)
        
        # Normalize mask to 0-1 range for smooth blending
        mask_normalized = mask.astype(float) / 255.0
        mask_normalized = np.stack([mask_normalized] * 3, axis=-1)
        
        # Convert to float for blending
        frame_float = frame.astype(float)
        background_float = self.background.astype(float)
        
        # Smooth blend using the normalized mask
        final_output = (background_float * mask_normalized + 
                       frame_float * (1 - mask_normalized))
        
        # Convert back to uint8
        final_output = final_output.astype(np.uint8)
        
        return final_output
    
    def run(self):
        """Main loop for the invisibility cloak effect"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("❌ Failed to capture frame")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            if self.background is not None:
                # Apply invisibility effect
                final_output = self.process_frame(frame)
                
                # Display instructions with improved visibility
                final_output = display_instructions(final_output, True, self.recording)
                
                # Save frame if recording
                if self.recording and self.video_writer:
                    self.video_writer.write(final_output)
                
                cv2.imshow(Config.MAIN_WINDOW, final_output)
            else:
                # No background captured yet
                frame_with_instructions = display_instructions(frame, False, False)
                
                # Add prominent message to capture background
                height, width = frame.shape[:2]
                
                # Semi-transparent box for main message
                overlay = frame_with_instructions.copy()
                box_height = 120
                box_y = (height - box_height) // 2
                cv2.rectangle(overlay, (40, box_y), (width - 40, box_y + box_height), (0, 0, 255), -1)
                frame_with_instructions = cv2.addWeighted(overlay, 0.6, frame_with_instructions, 0.4, 0)
                
                # Add border
                cv2.rectangle(frame_with_instructions, (40, box_y), (width - 40, box_y + box_height), (255, 255, 255), 3)
                
                # Main instruction text
                cv2.putText(frame_with_instructions, "Press 'B' to Capture Background!", 
                           (50, box_y + 55),
                           Config.FONT, 1.0, (255, 255, 255), 3, cv2.LINE_AA)
                cv2.putText(frame_with_instructions, "(Move out of frame first)", 
                           (50, box_y + 90),
                           Config.FONT, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
                
                cv2.imshow(Config.MAIN_WINDOW, frame_with_instructions)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('b') or key == ord('B'):
                self.capture_background()
            
            elif key == ord('r') or key == ord('R'):
                if not self.recording:
                    self.start_recording(frame.shape[1], frame.shape[0])
                else:
                    self.stop_recording()
            
            elif key == ord('q') or key == ord('Q') or key == 27:  # 27 is ESC
                print("👋 Exiting...")
                break
        
        # Cleanup
        if self.recording:
            self.stop_recording()
        
        self.cap.release()
        cv2.destroyAllWindows()
        print("✅ Program ended successfully!")