#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# NOTE YOU WILL HAVE TO MODIFY IT ACCORDINT TO UR REQUIREMENT
# change 1 : 
#    os.system('sudo docker -divt /root/YOUR_PROJECT_NAME_ON_GITHUB:/root/ --name docker DOCKER_IMAGE NAME')


import os
def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

if check_if_string_in_file('Main.py', 'Conv2D'):
    os.system('sudo docker -divt /root/Devops:/root/ --name Docker_OS pythoni:v1')

else:
    os.system('sudo docker -divt /root/Devops:/root/ --name Docker_OS phpi:v1')

    
    


# In[ ]:




