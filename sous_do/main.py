
#### Imports ####
import pyfiglet 
import json
from users import users
from data import dict_utils
import utils 
    
ascii_banner = pyfiglet.figlet_format('** Sous - Do **')

while True:
    print(ascii_banner)
    print('Please login to continue.')
    log_in = input('Username: ').lower()
    if users.log_in_check(log_in):
        passwd = input('Password: ')
        if users.passwd_check(passwd):
            utils.clear()
            while True:
                if log_in not in ad_usrs:
                    if len(dict_utils.order_guide) == 0:
                        input('You have no saved guides, Please create one. Enter to continue')
                        utils.clear()
                        continue 
                    else:
                        dict_utils.fill_guide.update(dict_utils.fill_order())
                        print(dict_utils.fill_guide)
                        break   
                else:
                    utils.clear()    
                    if ad_screen() == False:
                        utils.clear()   
                        break   
                    else:
                        continue 
        else:
            print('Incorrect password, please try again.')
            continue
    else:
        input('Can not find username in system')
        utils.clear()   
        continue

        

        
        
        
        
        
        
        
      
                 
           
           
            

        


            

    

     