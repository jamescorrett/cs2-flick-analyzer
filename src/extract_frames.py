import cv2
import os

def extract_frames(video_path, output_folder, every_n_frames=1):
    """
    Extract frames from a video and save them as image files.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where frames will be saved.
        every_n_frames (int): Save every nth frame.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    if not vidcap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    success, frame = vidcap.read()
    count = 0
    saved = 0

    while success:
        if count % every_n_frames == 0:
            filename = f"frame_{saved:05d}.jpg"
            filepath = os.path.join(output_folder, filename)
            cv2.imwrite(filepath, frame)
            print(f"Saved: {filename}")
            saved += 1

        success, frame = vidcap.read()
        count += 1

    vidcap.release()
    print(f"Done! {saved} frames saved.")

if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")
    parser.add_argument("--every_n_frames", type=int, default=1, help="Save every nth frame (default: 1).")
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_folder, args.every_n_frames)