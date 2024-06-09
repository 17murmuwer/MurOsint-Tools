import requests
from time import sleep
import os

def traceip():
    print('''

 ___ ___  __ __  ____   ___ ___  __ __  __    __    ___  ____       ____  ____         ______  ____    ____    __  __  _    ___  ____  
|   T   T|  T  T|    \ |   T   T|  T  T|  T__T  T  /  _]|    \     l    j|    \       |      T|    \  /    T  /  ]|  l/ ]  /  _]|    \ 
| _   _ ||  |  ||  D  )| _   _ ||  |  ||  |  |  | /  [_ |  D  )     |  T |  o  )_____ |      ||  D  )Y  o  | /  / |  ' /  /  [_ |  D  )
|  \_/  ||  |  ||    / |  \_/  ||  |  ||  |  |  |Y    _]|    /      |  | |   _/|     |l_j  l_j|    / |     |/  /  |    \ Y    _]|    / 
|   |   ||  :  ||    \ |   |   ||  :  |l  `  '  !|   [_ |    \      |  | |  |  l_____j  |  |  |    \ |  _  /   \_ |     Y|   [_ |    \ 
|   |   |l     ||  .  Y|   |   |l     | \      / |     T|  .  Y     j  l |  |           |  |  |  .  Y|  |  \     ||  .  ||     T|  .  Y
l___j___j \__,_jl__j\_jl___j___j \__,_j  \_/\_/  l_____jl__j\_j    |____jl__j           l__j  l__j\_jl__j__j\____jl__j\_jl_____jl__j\_j
 ''')                                                                                                                                         
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                    
    targetip = input("\033[1;91mEnter IP Address: \033[0m")
    r = requests.get("http://ip-api.com/json/" + targetip)
    print("\n\033[1;91m[*]\033[1;97m IP detail is given down below\n")
    sleep(0.1)
    print("\033[1;92m \033[1;91m➤\033[1;97m Status Code    : " + str(r.status_code))
    sleep(0.1)
    if str(r.json()['status']) == 'success':
        print(" \033[1;91m➤\033[1;97m Status         :\033[1;92m " + str(r.json()['status']))
        sleep(0.1)
    elif str(r.json()['status']) == 'fail':
        print(" \033[1;91m➤\033[1;97m Status         :\033[1;97m " + str(r.json()['status']) + '\033[1;92m')
        sleep(0.1)
        print(" \033[1;91m➤\033[1;97m Message        : " + str(r.json()['message']))
        sleep(0.1)
        if str(r.json()['message']) == 'invalid query':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is an invalid IP Address, So you can try another IP Address.\n')
            exit()
        elif str(r.json()['message']) == 'private range':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a private IP Address, So This IP can not be traced.\n')
            exit()
        elif str(r.json()['message']) == 'reserved range':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a reserved IP Address, So This IP can not be traced.\n')
            exit()
        else:
            print('\nCheck your internet connection.\n')
            exit()
    print("\033[1;92m \033[1;91m➤\033[1;97m Target IP      : " + str(r.json()['query']))
    sleep(0.1)
    print("\033[1;92m \033[1;91m➤\033[1;97m Country:    : " + str(r.json()['country']))
    sleep(0.1)
    print(" \033[1;92m\033[1;97m➤\033[1;97m Country Code    : " + str(r.json()['countryCode']))
    sleep(0.1)
    print(" \033[1;92m\033[1;97m➤\033[1;97m City    : " + str(r.json()['city']))
    sleep(0.1)
    print(" \033[1;92m\033[1;97m➤\033[1;97m Timezone    : " + str(r.json()['timezone']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Region Name    : " + str(r.json()['regionName']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Region         : " + str(r.json()['region']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m ZIP Code       : " + str(r.json()['zip']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Latitude       : " + str(r.json()['lat']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Longitude      : " + str(r.json()['lon']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m ISP            : " + str(r.json()['isp']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Organization   : " + str(r.json()['org']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m AS             : " + str(r.json()['as']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Location       : " + str(r.json()['lat']) + ',' + str(r.json()['lon']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Google Map     : \033[1;94mhttps://maps.google.com/?q=" + str(r.json()['lat']) + ',' + str(r.json()['lon']))
    sleep(0.1)
    print()
    mapaddress = input("\033[1;91m[*]\033[1;97m Press ENTER To Open Location on Google maps or press any other key to quit: ")
    if mapaddress == "":
        print()
        print("[*] Opening Location on google map")
        print()
        os.system("xdg-open https://maps.google.com/?q=" + str(r.json()['lat']) + ',' + str(r.json()['lon']) + " > /dev/null 2>&1")
        print()
    else:
        print()
        print("[*] Aborting.....")
        print()

# Call the function
traceip()
