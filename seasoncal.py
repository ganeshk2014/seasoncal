#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask
# get the current day of the year
from  datetime import datetime
app=Flask(__name__)
@app.route('/default')
def default():
    doy = datetime.today().timetuple().tm_yday

    # "day of year" ranges for the northern hemisphere
    #winter = range(, 59)
    summer = range(60, 152)
    fall = range(153, 305)
    # winter = everything else
    if doy in summer:
        season = '1'
    elif doy in fall:
        season = '0'
    else:
        season = '2'
    return season
if __name__=='__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:




