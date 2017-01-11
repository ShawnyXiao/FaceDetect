import cv2
import sys


def load_video(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        sys.exit("The video can't be opened!")
    return video


def read_next_frame(video):
    return video.read()


def gray_image(image):
    gray = image
    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def get_detector(cascade_path):
    return cv2.CascadeClassifier(cascade_path)


def detect_faces(detector, gray_scale_image):
    return detector.detectMultiScale(
        gray_scale_image,
        scaleFactor=1.25,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


def draw_rectangles(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


def show_image(image):
    cv2.imshow('Video', image)


def release_destroy(video):
    video.release()
    cv2.destroyAllWindows()


def detect_faces_on_video(video, detector):
    while video.isOpened():
        is_successed, frame = read_next_frame(video)
        if not is_successed:
            break
        gray_scale_frame = gray_image(frame)
        faces = detect_faces(detector, gray_scale_frame)
        draw_rectangles(frame, faces)
        show_image(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


def main():
    video_path = sys.argv[1]
    cascade_path = '../resources/haarcascade_frontalface_default.xml'

    video = load_video(video_path)
    detector = get_detector(cascade_path)
    detect_faces_on_video(video, detector)
    release_destroy(video)


if __name__ == '__main__':
    main()
