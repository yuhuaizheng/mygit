# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
MONGODB_SETTINGS = {'db' : 'dataAnalysis', 'port':27017, 'host': '139.196.47.181'}
MYSQL_SETTINGS = {
    'host': '123.59.156.239', 'port': 3306, 
    'user': 'root','passwd': 'noahark@8225','charset': 'utf8'
    }

SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'mysql://root:51ykbYKB@139.196.47.181:3306/data_analysis')
CSRF_ENABLED = True

PER_PAGE = 15