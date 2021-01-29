import os
import time
from pytube import YouTube

os.system('cls')
os.system('color b')


url = input("Please paste the youtube uniform resource allocator : ")
vedio = YouTube(url)
choice = input("Audio or vedio (a or v) ? : ")



if choice == "v" :

    options = vedio.streams.filter(adaptive = True)
    print("-"*80)
    print("\n"*2)

    for i in options :
        print (i)

    print("\n"*2)
    print("-"*80)
    print ("\n" * 3)

    quality = input("Please type the itag value : ")
    name = input("\n" +"Type the file name : ")
    print("\n" +"downloading..." + "\n")

    result = vedio.streams.get_by_itag(quality)
    result.download("youtubedownloads",filename = name)




else :

    options = vedio.streams.filter(only_audio=True)
    print("-"*80)
    print("\n"*2)

    for i in options :
        print (i)

    print("\n"*2)
    print("-"*80)
    print ("\n" * 3)

    quality = input("Please type the itag value : ")
    name = input("\n" +"Type the file name : ")
    print("\n" +"downloading..." + "\n")

    result = vedio.streams.get_by_itag(quality)
    result.download("youtubedownloads",filename = name)


print("Done good bye ")
time.sleep(2)
