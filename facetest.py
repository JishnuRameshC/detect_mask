import face_recognition

img_ur1 = "D:\\RISS\\works\\facemask\\static\\sachin.jpg"  # captured img
img_ur2 = "D:\\RISS\\works\\facemask\\static\\sachin.jpg"  # captured img
# img_ur2 = "D:\\RISS\\works\\facemask\\" + img  # db image

# img = "C:/aswathi/mpmd/mpmd/MPMD/static/userreg/nazriya@gmail.com.jpg"

b_img = face_recognition.load_image_file(img_ur1, 'RGB')
b_imgs = face_recognition.face_encodings(b_img)
b_img2 = face_recognition.load_image_file(img_ur2, 'RGB')
b_imgs2 = face_recognition.face_encodings(b_img2)

for a in b_imgs2:
    # unknown_face_encoding = face_recognition.face_encodings(b_imgs)
    results = face_recognition.compare_faces(a, b_imgs, tolerance=0.5)
    print("----"+str(results))
    for r in results:
        if r== True:
            print("ok")

