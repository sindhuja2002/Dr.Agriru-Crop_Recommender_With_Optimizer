import pandas as pd
import weather
import plotly.graph_objects as go


def convert(a,b):
    for i in range(len(b)):
        if(b[i]=='1'):
            a[i]=a[i]*0.001
        elif(b[i]=='2'):
            a[i]= a[i]*0.0025
    return a



def loc_att(state,city):
    temp , hum = weather.weather(city)
    rf=pd.read_csv('./resources/rainfall.csv')
    rnf = rf[rf['state']==state]['rainfall'].iloc[0]
    return [temp,hum,rnf]

def state_id(state_no):
    rf=pd.read_csv('./resources/rainfall.csv')
    st=rf.iloc[state_no].state
    return st

def graph_val(out):
    df=pd.read_csv('./resources/FertilizerData.csv')
    N = df[df['Crop']==out]['N'].iloc[0]
    P = df[df['Crop']==out]['P'].iloc[0]
    K = df[df['Crop']==out]['K'].iloc[0]
    ph =df[df['Crop']==out]['pH'].iloc[0]
    ca = df[df['Crop']==out]['calcium'].iloc[0]
    mg= df[df['Crop']==out]['magnesium'].iloc[0]
    s = df[df['Crop']==out]['sulphur'].iloc[0]
    b =df[df['Crop']==out]['boron'].iloc[0]
    zn = df[df['Crop']==out]['zinc'].iloc[0]
    fe = df[df['Crop']==out]['iron'].iloc[0]
    mn = df[df['Crop']==out]['magnese'].iloc[0]
    opt =[N,P,K,ca,mg,s,b,fe,zn,mn,ph]
    
    return(opt)


    

def graph_scaling(avil,std):
    req=[]
    for i in range(len(avil)):
        ext=std[i] - avil[i]
        if(ext<=0):
            ext = 0
        req.append(ext)
    return req

def graph(avail,req):
    fig = go.Figure()
    x=['Nitrogen','potassium','Phosporous','calcium','magnesium','sulphur','boron','iron','zinc','manganese','ph']
    fig.add_bar(y=x,x=avail,orientation='h',width=0.5,name='available',marker = dict(color=' rgb(10, 24, 219)' ))

    fig.add_bar(y=x,x=req,orientation='h', width=0.5,name='required',marker = dict(color=' rgb(219, 21, 11)'))
    fig.update_layout(barmode="relative")
    #fig.show()
    return fig


