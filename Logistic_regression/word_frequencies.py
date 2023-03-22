#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pre_processing
import numpy as np


# In[24]:


def get_freq_table(tweets, labels):
    labels = np.squeeze(labels).tolist()
    freq = {}
    for tweet, label in zip(tweets, labels):
        for token in pre_processing.process_tweets(tweet):
            pair = (token, label)
            if pair in freq:
                freq[pair]+=1
            else:
                freq[pair]=1
    return freq


# In[25]:


def get_freq_table_for_a_tweet(tweet ,freq):
    data = []
    for token in tweet:
        pos = 0
        neg = 0
        if (token,1) in freq:
            pos = freq[(token,1)]
        if (token,0) in freq:
            neg = freq[(token,0)]
        data.append([token, pos, neg])
    return data


# In[26]:


import matplotlib.pyplot as plt
def show_plot(data):
    fig, ax = plt.subplots(figsize = (8, 8))

    # convert positive raw counts to logarithmic scale. we add 1 to avoid log(0)
    x = np.log([x[1] + 1 for x in data])  

    # do the same for the negative counts
    y = np.log([x[2] + 1 for x in data]) 

    # Plot a dot for each pair of words
    ax.scatter(x, y)  

    # assign axis labels
    plt.xlabel("Log Positive count")
    plt.ylabel("Log Negative count")

    # Add the word as the label at the same position as you added the points just before
    for i in range(0, len(data)):
        ax.annotate(data[i][0], (x[i], y[i]), fontsize=12)

    ax.plot([0, 9], [0, 9], color = 'red') # Plot the red line that divides the 2 areas.
    plt.show()


# In[ ]:




