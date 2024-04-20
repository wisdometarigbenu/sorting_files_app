



# try:
#     divisor = float(input("please enter a number: "))
#     dividend = float(input("please enter the dividend"))

#     quotient = (dividend / divisor)

# except(ZeroDivisionError) as err: 
#     print("cannot divide by zero", err)

# except(NameError) as err: 
#     print( err)


# except(ValueError) as err: 
#     print("please enter only numbers", err)

# else:
#     print(quotient)

# finally: 
#     print("thanks for using our calculator")

# create a file but read trough a try except block



# try:
#     wi xjth open('index.txt', 'w') as file:
#         file.write(" this is some content in the file.")
#         print(file.read())

# except FileNotFoundError:
#     print("File not found.")

# except Exception as e:
#     print("An error occurred:", e)


# Write a python application that loop all the files in your system download folder,
# the doc related files(pdf, excel, csv, doc etc) it should be put them in your document folder , 
# the one that are video(mkv, mp4 etc)  it should put them in the video folder,
# then pitures(png,jpg etc )  should be  in the Picture folder,
# and all audio files (mp3 etc) should be sorted and put into the music folder,
# and the windows executables to the desktop folder and finnaly,
# any other one that we have not mentioned should be in a newly created Miscellaneous folder.
import os
import shutil

download_folder = "C:\\Users\\Wisdom\\Downloads"
document_folder = "C:\\Users\\Wisdom\\Documents"
video_folder = "C:\\Users\\Wisdom\\Videos"
picture_folder = "C:\\Users\\Wisdom\\Pictures"
music_folder = "C:\\Users\\Wisdom\\Music"
desktop_folder = "C:\\Users\\Wisdom\\Desktop"
miscellaneous_folder = "C:\\Users\\Wisdom\\Miscellaneous"

document_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.csv']
video_extensions = ['.mp4', '.mkv', '.avi', '.mov']
picture_extensions = ['.jpg', '.jpeg', '.png', '.gif']
music_extensions = ['.mp3', '.wav', '.flac']
executable_extensions = ['.exe', '.msi']

for filename in os.listdir(download_folder):
    source_file = os.path.join(download_folder, filename)
    if os.path.isfile(source_file):
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in document_extensions:
            destination_folder = document_folder
        elif file_extension in video_extensions:
            destination_folder = video_folder
        elif file_extension in picture_extensions:
            destination_folder = picture_folder
        elif file_extension in music_extensions:
            destination_folder = music_folder
        elif file_extension in executable_extensions:
            destination_folder = desktop_folder
        else:
            destination_folder = miscellaneous_folder
        destination_file = os.path.join(destination_folder, filename)
        shutil.move(source_file, destination_file)

        





            
        

