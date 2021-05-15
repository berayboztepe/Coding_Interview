import face_recognition
import os
import cv2
import numpy as np
from PIL import Image


def main():
    # to get the images which find in faces directory
    def get_photo():
        whoami = {}
        for root, dirs, files in os.walk("./faces"):
            # to find the files that end with .jpg or .png and to get the face locations in every image.
            # added all the locations and the name of the images to the dict and returned it.
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    face = face_recognition.load_image_file("faces/" + file)
                    who = face_recognition.face_encodings(face)[0]
                    whoami[file.split(".")[0]] = who
        return whoami

    def open_photo(img):
        # to add the names and locations which returned as a dict from get_photo function.
        names = list(get_photo().keys())
        locs = list(get_photo().values())
        im = cv2.imread(img, 1)
        # to get the locations of the image which do a recognition.
        face_locat = face_recognition.face_locations(im)
        face_encod = face_recognition.face_encodings(im, face_locat)

        get_names = []
        for faces in face_encod:
            # we have all the faces that we add to faces directory. this is for comparing them with the image
            # which we use now.
            match = face_recognition.compare_faces(locs, faces)
            name = "Unknown"

            # to find the distance between the image and the known faces from faces directory.
            # the smallest distance is what we need
            face_dis = face_recognition.face_distance(locs, faces)
            min_match = np.argmin(face_dis)

            # when find the min distance, checking it with the known faces. if them match, we find the face from given
            # image belongs to a face from known faces.
            if match[min_match]:
                name = names[min_match]

            get_names.append(name)
            # to draw a rectangle to the face with the help of face locations. Then add the name below the rectangle
            for (top, right, bottom, left), name in zip(face_locat, get_names):
                cv2.rectangle(im, (left - 50, top - 20), (right + 50, bottom + 20), (255, 0, 0), 2)
                cv2.rectangle(im, (left - 50, bottom - 15), (right + 50, bottom + 20), (255, 0, 0), cv2.FILLED)
                cv2.putText(im, name.upper(), (((left + right - 100 - len(name)) // 2), (bottom + 10)),
                            cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 2)

        while True:
            cv2.imshow('Photo_Detector', im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

    # resize the image. if resolution is big, then we may not find the face! rename image as test10.jpg or chance it.
    # I did 800, 600 if the image is horizontal
    """size = 800, 600
    im = Image.open("test10.jpg")
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("test10.jpg")"""
    # if the image is vertical
    """size = 600, 1000
    im = Image.open("test10.jpg")
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("test10.jpg")"""
    # after to rotate image 90, 180, 270, 360
    """rotated = im.rotate(180)
    rotated.save("test10.jpg")"""
    # to change format to .jpg or .png
    """im = Image.open("test9.jpeg")
    im.save("test9.jpg") 
    or
    im.save("test9.png")"""

    # write the given photo
    open_photo("test.jpg")


if __name__ == "__main__":
    main()
