import cv2
import sys


def open_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        sys.exit("Camera can't be opened!")
    return camera


def read_next_frame(camera):
    return camera.read()[1]


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
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


def draw_rectangles(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def show_image(image):
    cv2.imshow('Camera', image)


def release_destroy(camera):
    camera.release()
    cv2.destroyAllWindows()


def detect_faces_on_camera(camera, detector):
    while True:
        frame = read_next_frame(camera)
        gray_scale_frame = gray_image(frame)
        faces = detect_faces(detector, gray_scale_frame)
        draw_rectangles(frame, faces)
        show_image(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


def main():
    cascade_path = '../resources/haarcascade_frontalface_default.xml'

    camera = open_camera()
    detector = get_detector(cascade_path)
    detect_faces_on_camera(camera, detector)
    release_destroy(camera)


if __name__ == '__main__':
    main()
