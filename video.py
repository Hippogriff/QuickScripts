"""
Uses imageio to read images and create a video
"""
import imageio
import os
import sys
import cv2


def create_video(image_folder, video_name):
    """
    Create a video from a folder of images
    """
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") and img.startswith("0")]
    images.sort(key=lambda x: int(x.split(".")[0]))
    # images = images[:300]
    frame = imageio.imread(os.path.join(image_folder, images[0]))

    height, width, _ = frame.shape
    video = imageio.get_writer(video_name, fps=10)

    for image in images:
        iteration_id = int(image.split(".")[0])

        image = imageio.imread(os.path.join(image_folder, image))
        image = cv2.putText(image, str(iteration_id), (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 2)
        video.append_data(image)

    video.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python video.py <image_folder> <video_name>")
        sys.exit(1)

    create_video(sys.argv[1], sys.argv[1] + sys.argv[2])