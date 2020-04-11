# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:49:17 2020

@author: HDTT
"""

import requests
from bs4 import BeautifulSoup
import os

archive_url = "http://ds.iris.edu/pub/userdata/wilber/sun/2019-07-06-mw71-central-california/timeseries_data/"

def get_pdf_links():
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    #find all the file and save in a list
    pdf_links = [archive_url + link['href'] for link in links if link['href'].endswith('txt')]
    return pdf_links

#download pdf in list
def download_pdf_series(pdf_links,oklist):
#oklist is the pdf which are download successfully before.
    #The oklist is to prevent from downloading file repeatly.  
  
    failed_list=[];#file list is file that are failed to download.
    for link in pdf_links:
        file_name = link.split('/')[-1]
        if file_name in oklist:
            print("%s already existed!\n" % file_name);
            continue;
        else:
                
            print("Downloading file:%s" % file_name)

            try:#try to download, wait for 10 s and try 1 times.
                r = requests.get(link, stream=True,timeout=(10,1))
            except: #time out
                print("time out");
                failed_list.append(file_name);
                continue;   
        # download started
            with open(file_name, 'wb') as f:
                f.write(r.content);
                #just for big files,i do not need.
              #  for chunk in r.content():
               #     if chunk:
                #       f.write(chunk)
                print("%s downloaded!\n" % file_name)
    return failed_list



    print("All videos downloaded!")

    return
links_list=get_pdf_links();
filepath=r'C:\Users\16000\Desktop';
#get ok_list from the filepath.
ok_list=os.listdir(filepath);
failed_list=download_pdf_series(links_list,ok_list);

    