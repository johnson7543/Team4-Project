# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:06:03 2020

@author: User
"""

import pandas as pd
res = pd.read_html("https://itouch.cycu.edu.tw/active_system/query_data/student/ssgogo.jsp")
data = res[1].iloc[:,0:10]
data.to_excel("scholarship.xlsx")