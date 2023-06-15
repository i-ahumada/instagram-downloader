import downloader_funcs as mydownloader
import os
os.system('color')
ans = ""
def menu():
    print('Select (by typing the colored numbers) one of the next options to operate')
    print('\x1b[3;33;40m'+ '- 1' +'\x1b[0m' + ' downloads directly from url')
    print('\x1b[3;33;40m'+ '- 2' +'\x1b[0m' + ' downloads urls from a file that contains urls')
    print('\x1b[3;33;40m'+ '- 3' +'\x1b[0m' + ' downloads first n images by username (up to 6 months from today)')
    print('\x1b[3;33;40m'+ '- 4' +'\x1b[0m' + ' downloads first n images by username from a file (up to 6 months from today)')
    print('\x1b[7;30;41m'+ '- 5' +'\x1b[0m' + ' exit')
menu()
incorrect_input = True
while incorrect_input:
    ans = input('-> ').strip()
    try:
        ans = int(ans)
        if not ((ans >= 1) and (ans <= 5)):
            raise ValueError
        incorrect_input = False
    except ValueError:
        print('\x1b[1;37;41m'+ 'ERROR:' +'\x1b[0m' + ' Input must be an integer between 1 and 5')
    

while ans != 5:
    downloads_happened = False
    if(ans == 1):
        url = input('Input url: ')
        try:
            url = url.strip()
            mydownloader.download_from_url(url)
            downloads_happened = True
        except mydownloader.instaloader.InstaloaderException as ie:
            print(ie)
        else:
            print('\x1b[6;30;42m'+ "||||||  POST DOWNLOADED  ||||||" +'\x1b[0m')
            
    elif(ans == 2):
        folder_path = os.path.join(os.getcwd(), 'link_folder')
        filename = input('Input file name with extension: ')
        path =  os.path.join(folder_path, filename)
        if os.path.exists(path):
            archivo = open(path,"rt")
            downloads_counter = 0
            for url in archivo:
                downloads_happened = True
                downloads_counter += 1
                try:
                    mydownloader.download_from_url(url)
                except mydownloader.instaloader.InstaloaderException as ie:
                    print(ie)
            print('\x1b[6;30;42m'+ '||||||  ' + str(downloads_counter) + " IMAGES DOWNLOADED  ||||||" + '\x1b[0m')
        else:
            print('\x1b[1;37;41m'+ '||||||  NO FILE FOUND AS ['+ filename +'] IN ['+ folder_path +']   ||||||' +'\x1b[0m')
            
    elif(ans == 3):
        username = input("Input username: ")
        n = input("Input number of images from last uploaded: ")
        downloads_happened = True
        mydownloader.download_last_n(username, int(n))
        
    elif(ans == 4):
        folder_path = os.path.join(os.getcwd(), 'user_folder')
        filename = input('Input file name with extension: ')
        path =  os.path.join(folder_path, filename)
        if os.path.exists(path):
            n = input('Input number of images from last uploaded: ')
            archivo = open(path,"rt")
            for username in archivo:
                downloads_happened = True
                username = username.strip()
                try:
                    mydownloader.download_last_n(username, int(n))
                except mydownloader.instaloader.InstaloaderException as ie:
                    print(ie)
        else:
            print('\x1b[1;37;41m'+ '||||||  NO FILE FOUND AS ['+ filename +'] IN ['+ folder_path +']   ||||||' +'\x1b[0m' + '')
            
    if downloads_happened:
        downloads_folder_path = os.path.join(os.getcwd(), 'downloads')
        downloads_folder = os.listdir(downloads_folder_path)
        
        for folder_name in downloads_folder:
            
            folder_path = os.path.join(downloads_folder_path, folder_name)
            folder = os.listdir(folder_path)
            
            for file in folder:
                if not ((file.endswith('.jpg')) or (file.endswith('.png')) or (file.endswith('.mp4'))):
                    os.remove(os.path.join(folder_path, file))
    
    menu()
    incorrect_input = True
    while incorrect_input:
        ans = input('-> ').strip()
        try:
            ans = int(ans)
            if not ((ans >= 1) and (ans <= 5)):
                raise ValueError
            incorrect_input = False
        except ValueError:
            print('\x1b[1;37;41m'+ 'ERROR: ' +'\x1b[0m' + 'input must be an integer between 1 and 5')



