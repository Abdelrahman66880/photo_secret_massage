from PIL import Image
import os
import shutil
import time


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. "
letter_num_dict = {letter: index + 1 for index, letter in enumerate(letters)}
mypath = os.getcwd()
current_directory = os.path.join(mypath, os.path.dirname(__file__))
Result_directory = os.path.join(current_directory, "Result")



# print(mypath)

images = []


def clean_user_input(user_word):
    """Clean the user input from invalid charchter"""
    for letter in user_word:
        if letter in letter_num_dict:
            continue
        else:
            user_word = user_word.replace(letter, "")
    return user_word


def create_paths_list(user_word):
    """Create a list of image paths based on the user input"""
    for letter in user_word:
        if letter in letter_num_dict:
            image_name = f"{letter_num_dict[letter]}.jpg"
            image_path = os.path.join(current_directory, image_name)
            if os.path.exists(image_path):
                images.append(image_path)
            else:
                print(f"File not found: {image_name}")
    return images


def clear_Result_photos():
    """Clear the directory content if not empty"""
    result_directory_path = os.path.join(current_directory, "Result")
    photos = os.listdir(result_directory_path)
    for photo in photos:
        if photo.endswith(".jpg"):
            os.remove(os.path.join(result_directory_path, photo))


def copy_images_to_result_directory(path_list):
    """Copy images to the Result folder and rename them sequentially"""
    result_directory_path = os.path.join(current_directory, "Result")
    clear_Result_photos()
    if not os.path.exists(result_directory_path):
        os.makedirs(result_directory_path)

    for i, image_path in enumerate(path_list):
        target = os.path.join(result_directory_path, "{:02d}.jpg".format(i))
        shutil.copyfile(image_path, target)


if __name__ == "__main__":
    user_input = input("Enter your name: ").upper()
    cleaned_input = clean_user_input(user_input)
    paths_list = create_paths_list(cleaned_input)
    copy_images_to_result_directory(paths_list)
    # display_images(paths_list)
    print("\nCheck the Result folder!")
