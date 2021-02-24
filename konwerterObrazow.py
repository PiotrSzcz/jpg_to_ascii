from PIL import Image
import glob
import random

ascii_pool_s = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "." ] #http://paulbourke.net/dataformats/asciiart/
ascii_pool_xl = [i for i in r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "]

def mono_converter(image):
    gray_image = image.convert("L")
    return gray_image

def resize(image, new_width=100):
    width, height = image.size
    hw_ratio = height / width
    new_height = int((new_width/2) * hw_ratio)
    resized_image = image.resize((new_width, new_height)) 
    return resized_image

def image_to_ascii(image, high_detels):
    pixel_image = image.getdata()
    if high_detels == False:
        ascii_characters = "".join([ascii_pool_s[pixel//25] for pixel in pixel_image])
    else:
        ascii_characters = "".join([ascii_pool_xl[pixel//100] for pixel in pixel_image])

    return ascii_characters

def main():
    file_path_list = []

    for filename in glob.glob(r'miejsce_na_obrazy\*.jpg'):
        file_path_list.append(filename)

    x=0    
    for counter in file_path_list:
        print(f'{x:<5}{counter.replace("miejsce_na_obrazy", "").replace(".jpg", "")}')
        x+=1

    jpg_path = input("Wybierz obraz do konwersji: ")
    desired_width = input("Podaj pożądaną szerokość obrazku: ")
    if int(desired_width) > 400:
        desired_detals = True
    else:
        desired_detals = False
    
    if int(jpg_path) <= len(file_path_list):
        try:
            image = Image.open(file_path_list[int(jpg_path)])
        except:
            print('Wybrano błędny indeks pliku')
        
        new_image = image_to_ascii(mono_converter(resize(image, int(desired_width))), desired_detals)
        pixel_counter = len(new_image)
        ascii_image = "\n".join(new_image[i:(i+int(desired_width))] for i in range(0, pixel_counter, int(desired_width)))
        
        new_path=file_path_list[int(jpg_path)].replace('\\', '').replace("miejsce_na_obrazy", "").replace(".jpg", "") + str(random.randint(1,99))
        #print(ascii_image)
        with open(f'{new_path}.txt', 'w+') as file:
            file.write(ascii_image)
        
if __name__ == '__main__': 
    main() 