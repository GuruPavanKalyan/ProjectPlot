#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install cufflinks')
get_ipython().system('pip install plotly')


# In[18]:


import numpy as np
import pandas as pd
import chart_studio.plotly as pl
#import plotly.plotly as pl
import plotly.offline as po
import cufflinks as cf


# In[19]:


#setting offline mode
po.init_notebook_mode(connected=True)
cf.go_offline()


# #### Creating the data

# In[20]:


def createdata(data):
    #if user selects 1, I have to to genrate dataframe created randomly
    if(data==1):
        x= np.random.rand(100,5)
        df1=pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif(data==2):
        # if user selects 2, I have to genrate dataframe which the user want
        
        # for columns
        x = [0,0,0,0,0]
        r1 = [0,0,0,0,0]
        r2= [0,0,0,0,0]
        r3= [0,0,0,0,0]
        r4= [0,0,0,0,0]
        print("Enter the values for columns")
        i=0
        for i in [0,1,2,3,4]:
            x[i]=input()
            i = i +1
        print("Enter the values for row 1")
        i=0
        for i in [0,1,2,3,4]:
            r1[i]=input()
            i = i +1
        print("Enter the values for row 2")
        i=0
        for i in [0,1,2,3,4]:
            r2[i]=input()
            i = i + 1
        print("Enter the values for row 3")
        i=0
        for i in [0,1,2,3,4]:
            r3[i]=input()
            i = i +1 
        print("Enter the values for row 4")
        i=0
        for i in [0,1,2,3,4]:
            r4[i]=input()
            i = i +1   
            
        df1= pd.DataFrame([r1,r2,r3,r4],columns=x)
        
    elif(data==3):
        file= input("Enter the file name: ")
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
        
    else:
        print("DataFrame Creation failed please enter in between 1 to 3 and try again")
    return df1   
        


# In[ ]:





# In[21]:


def plotter1(plot):
    if plot==1:
        fplot = df1.iplot(kind = 'scatter')
        
    elif plot==2:
        fplot = df1.iplot(kind = 'scatter',mode='markers',symbol='x',colorscale='paired')
    elif plot==3:
        fplot = df1.iplot(kind="bar")
    elif plot==4:
        fplot = df1.iplot(kind="hist")
    elif plot==5:
        fplot = df1.iplot(kind="box")
    elif plot==6:
        fplot = df1.iplot(kind="surface")
    else:   
        fplot =print("Select only between 1 to 6")
    return fplot    
    


# In[7]:


def plotter2(plot):
    col = input("Enter the number of columns you want to plot by selecting 1,2 or 3")
    col = int(col)
    if col==1:
        colm = input("Enter the column")
        if plot==1:
            fplot = df1[colm].iplot(kind = 'scatter')
        elif plot==2:
             fplot = df1[colm].iplot(kind = 'scatter',mode='markers',symbol='x',colorscale='paired')
        elif plot==3:
             fplot = df1[colm].iplot(kind="bar")
        elif plot==4:
             fplot = df1[colm].iplot(kind="hist")
        elif plot==5:
             fplot = df1[colm].iplot(kind="box")
        elif plot==6 or plot==7:
            print("For Bubble plot and Surface plot requires atleast 2 columns")
        else:   
            fplot =print("Select only between 1 to 7")
        return fplot   
    elif col==2:
        colm = input("Enter the column 1: ")
        colm1=input("Enter the column 2: ")
        if plot==1:
            fplot = df1[[colm,colm1]].iplot(kind = 'scatter')
        
        elif plot==2:
             fplot = df1[[colm,colm1]].iplot(kind = 'scatter',mode='markers',symbol='x',colorscale='paired')
        elif plot==3:
             fplot = df1[[colm,colm1]].iplot(kind="bar")
        elif plot==4:
             fplot = df1[[colm,colm1]].iplot(kind="hist")
        elif plot==5:
             fplot = df1[[colm,colm1]].iplot(kind="box")
        elif plot==6:
            fplot = df1[[colm,colm1]].iplot(kind="surface")
        elif plot==7:
            s =input("Enter the size: ")
            fplot = df1.iplot(kind="bubble",x=colm,y=colm1,size =s)
        else:   
            fplot =print("Select only between 1 to 7") 
    elif col ==3:
        colm = input("Enter the column 1: ")
        colm1 = input("Enter the column 2: ")
        colm2 = input("Enter the column 3: ")
        if plot==1:
            fplot = df1[[colm,colm1,colm2]].iplot(kind = 'scatter')
        
        elif plot==2:
             fplot = df1[[colm,colm1,colm2]].iplot(kind = 'scatter',mode='markers',symbol='x',colorscale='paired')
        elif plot==3:
             fplot = df1[[colm,colm1,colm2]].iplot(kind="bar")
        elif plot==4:
             fplot = df1[[colm,colm1,colm2]].iplot(kind="hist")
        elif plot==5:
             fplot = df1[[colm,colm1,colm2]].iplot(kind="box")
        elif plot==6:
            fplot = df1[[colm,colm1,colm2]].iplot(kind="surface")
        elif plot==7:
            #ple
            s = input("Enter the size: ")
            fplot = df1.iplot(kind="bubble",x=colm,y=colm1,z=colm2,size =s)
        else:   
            fplot =print("Select only between 1 to 7")
    else:
        fplot = print("Select only between 1 to 3")
    


# In[22]:


def main(cate):
    if cate ==1:
        print("select the type of plot u need to plot by writing 1 to 6")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        plot = int(input())
        out = plotter1(plot)
    elif cate ==2:
        print("select the type of plot u need to plot by writing 1 to 6")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        print("7.Bubble Sort")
        plot = int(input())
        out = plotter2(plot)
    else:   
        print("Please enter 1 or 2, Try Again")
        


# In[ ]:





# In[24]:


#starting 
print("select the type of data you need to plot(By writing 1,2 or 3)")
#if I select 3 it will goes to the createdata class
print("1.Random dat with 100 rows and 5 columns")
print("2.customise data farme with 4 rows and 5 columns ")
print("3.upload csv/json/txt file:")
data = int(input())
df1 =createdata(data)


# In[32]:


df1.describe()


# In[30]:


print("what kind of plot u need, the  complete data plot or column plot")

cate= input("Enter 1 for  plotting all columns or Enter 2 for specifying columns to plot")
cate = int(cate)


# In[31]:


main(cate)


# In[ ]:




