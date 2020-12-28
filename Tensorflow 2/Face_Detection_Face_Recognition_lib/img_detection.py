import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from PIL import Image


def get_encoded_faces():
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            # find the .jpg and .png files in faces folder.
            if f.endswith(".jpg") or f.endswith(".png"):
                # add them into a numpy array as RGB, if say mode='L' than add images in white or black
                face = fr.load_image_file("faces/" + f)
                # made the added image, a 128-dimension face encoding
                encoding = fr.face_encodings(face)[0]
                # made label : face encoding. fe: donald trump: [1.832938, 2.32183, blabla] and add them into encoded
                encoded[f.split(".")[0]] = encoding
    return encoded


def unknown_image_encoded(img):
    # if image is not .jpg or .png
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    # took a dict that has labels in keys, array in values. known_face_names is labels now
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    # read the image that was given as parameter
    img = cv2.imread(im, 1)

    # made a list of tuples of given img's face locations (top, right, bottom, left)
    face_locations = face_recognition.face_locations(img)
    # gave all the face encodings from given image.
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # check if face encodings from given image matches with the images that have been given first
        # if not, this face is unknown.
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "unknown"

        # if they match, found all of the distances. compare the faces from given image and having first
        # and found the distances. lower distance is the face that has been looking for.
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        # if they match, gave the name of the face's owner.
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        # now draw a rectangle around face.
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)

            # we wrote the label name into rectangle
            cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)

    # and show the picture. press q to quit
    while True:
        cv2.imshow('Photo_Detector', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names


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


if __name__ == '__main__':
    # run the code. chance test10.jpg to image's name
    classify_face("test.jpg")
