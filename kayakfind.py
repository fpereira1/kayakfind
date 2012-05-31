#!/usr/bin/python

# DO WHAT YOU WANT TO PUBLIC LICENSE 
#                     Version 2, December 2004 
# 
#  Copyright (C) 2004 Filype Pereira <pereira.filype@gmail.com> 
# 
#  Everyone is permitted to copy and distribute verbatim or modified 
#  copies of this license document, and changing it is allowed as long 
#  as the name is changed. 
# 
#             DO WHAT YOU WANT TO PUBLIC LICENSE 
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
# 
#   0. You just DO WHAT YOU WANT TO. 
#
#  This program is free software. It comes without any warranty, to
#  the extent permitted by applicable law. You can redistribute it
#  and/or modify it under the terms of the Do What You Want

# kayakfind - A script to find flights on kayak.com using their RSS

# Configurations for the script
version  = '0.0.2'
app_name = 'kayakfind'
file_log = 'logs/history.log'

# Settings
currency = 'NZD'
a = 'AKL'
b = 'SYD'

import urllib2

url = 'https://www.kayak.com/h/rss/fare?code=' + a + '&dest=' + b + '&mc=' + currency

req = urllib2.Request(url)
res = urllib2.urlopen(req)

print(app_name + " - " + version);
print("Searching: " + a + " to " + b + " in " + currency)

print(res.read())