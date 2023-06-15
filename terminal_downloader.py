import downloader_funcs as mydownloader
import os
os.system('color')
ans = ""
def menu():
    print('Select (by typing de marked words) one of the next options to operate')
    print('\x1b[3;33;40m'+ '- url' +'\x1b[0m' + ' downloads directly from url')
    print('\x1b[3;33;40m'+ '- fil' +'\x1b[0m' + ' downloads urls from a file that contains urls')
    print('\x1b[7;30;41m'+ '- ext' +'\x1b[0m' + '')
menu()
ans = input('-> ')

while ans != "ext":
    image_amount = 0
    if(ans == "url"):
        url = input('Input url: ')
        try:
            url = url.strip()
            mydownloader.download_from_url(url)
            image_amount += 1
        except mydownloader.instaloader.InstaloaderException as ie:
            print(ie)
        else:
            print('\x1b[6;30;42m'+ "Success!" +'\x1b[0m')
    elif(ans == "fil"):
        folder_path = os.path.join(os.getcwd(), 'link_folder')
        filename = input('Input file name with extension: ')
        path =  os.path.join(folder_path, filename)
        if not os.path.exists(path):
            print('\x1b[1;37;41m'+ 'NO FILE FOUND AS ['+ filename +'] IN ['+ folder_path +']' +'\x1b[0m' + '')
        else:
            archivo = open(path,"rt")
            for url in archivo:
                image_amount += 1
                try:
                    mydownloader.download_from_url(url)
                except mydownloader.instaloader.InstaloaderException as ie:
                    print(ie)
            print('\x1b[6;30;42m'+ str(image_amount) + " images downloaded" + '\x1b[0m')
            
    if image_amount > 0:
        downloads_folder_path = os.path.join(os.getcwd(), 'downloads')
        downloads_folder = os.listdir(downloads_folder_path)
        
        for folder_name in downloads_folder:
            
            folder_path = os.path.join(downloads_folder_path, folder_name)
            folder = os.listdir(folder_path)
            
            for file in folder:
                if not ((file.endswith('.jpg')) or (file.endswith('.png')) or (file.endswith('.mp4'))):
                    os.remove(os.path.join(folder_path, file))
    
    menu()
    ans = input('-> ')



