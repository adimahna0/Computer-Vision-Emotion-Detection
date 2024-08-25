import cv2
import dlib
import numpy as np
import os
import random

# Initialize the face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dlib.face_utils.PREDICTOR_68_POINT)

# Create a directory to save the processed videos
output_dir = 'processed_videos'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def process_frame(frame, landmarks):
    # Apply edge detection
    edges = cv2.Canny(frame, 100, 200)

    # Apply Gaussian Blurring
    blurred = cv2.GaussianBlur(edges, (5, 5), 0)

    # Apply Histogram Equalization
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    # Apply Contrast Stretching
    min_val, max_val = np.min(equalized), np.max(equalized)
    contrast_stretched = np.uint8((equalized - min_val) / (max_val - min_val) * 255)

    # Apply Random Cropping
    height, width = contrast_stretched.shape[:2]
    x = random.randint(0, width // 2)
    y = random.randint(0, height // 2)
    cropped = contrast_stretched[y:y+height//2, x:x+width//2]

    return cropped

def main(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video details
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a video writer to save the processed video
    out_path = os.path.join(output_dir, os.path.basename(video_path))
    out = cv2.VideoWriter(out_path, fourcc, fps, (width // 2, height // 2), isColor=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray_frame)

        for face in faces:
            landmarks = predictor(gray_frame, face)
            landmarks = dlib.face_utils.shape_to_np(landmarks)

            # Crop the face from the frame
            (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
            face_img = frame[y:y+h, x:x+w]

            # Process the face image
            processed_face = process_frame(face_img, landmarks)

            # Resize processed face to match output video dimensions
            processed_face_resized = cv2.resize(processed_face, (width // 2, height // 2))

            # Write the processed frame to the video file
            out.write(processed_face_resized)

    cap.release()
    out.release()

if __name__ == "__main__":
    # Path to your video file
    video_path = 'input_video.mp4'
    main(video_path)
