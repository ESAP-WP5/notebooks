#!/usr/bin/env python
# coding: utf-8

# <h1>Workflow for discovering, querying and visualizing astronomy data in the VO</h1>

# In[ ]:


import pyvo
from pyvo.registry import search as regsearch


# # Data Discovery (VO)

# ## Find all TAP Services with 'quasars'

# In[ ]:


services = regsearch(keywords=['quasar'], servicetype='tap')
print (services)


# ## Find all TAP Services with keyword "ukidss"

# In[ ]:


services = regsearch(keywords=['ukidss'], servicetype='tap')
print (services)


# ## Get Specific TAP Resource form list

# In[ ]:


ivoid=b'ivo://wfau.roe.ac.uk/osa-tap'
matching_row_indices = [i for i, val in enumerate(services["ivoid"]==ivoid) if val]
first_row_index = matching_row_indices[0] if len(matching_row_indices) > 0 else None
if (first_row_index==None):
    print ("No Matching services")
else:
    record = services.getrecord(first_row_index)
    tap_url = record["access_url"].decode('UTF-8')
    print("TAP URL: {}".format(tap_url))




