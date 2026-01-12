# WAP to rename filenames, testing loop and functions
filenames= [
    "invoice1.pdf",
    "invoice2.pdf",
    "invoice3.pdf"
]

def rename_file(filename):
    new_name = "processed_" + filename
    return new_name

for file in filenames:
    new_filename = rename_file(file)
    print(new_filename)


# WAP to rename and uppercase a list of images after uploaded

imgnames = [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg",
    "img4.jpg"
]

# def uploaded_imgs(imgname):
#     uploaded_imgname = "uploaded_"+imgname              
#     cap_uploaded_imgname = uploaded_imgname.upper()
#     return cap_uploaded_imgname

def uploaded_imgs(imgname):
    return ("uploaded_"+imgname).upper()

for img in imgnames:
    new_uploaded_imgname = uploaded_imgs(img)
    print(new_uploaded_imgname)
