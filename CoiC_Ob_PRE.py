import numpy as np
import pandas as pd

VV_10=pd.read_csv('Forecasting_data.csv')
ww=pd.read_csv('Observation_data.csv')



WW=open('Obser_forecast.csv','w')
WW.write('time,lat,lon,Temp_1,Temp_2\n')


DATA_SELET=[]

for i in range (len(VV_10)):
    timi=VV_10['time_1'][i]
    lati=VV_10['lat_1'][i]
    loni=VV_10[' lon_1'][i]
    ui=VV_10['Temp_1'][i]
    
    Data=ww[(ww['time_2']==timi) & (ww['lat_2']==lati) & (ww[' lon_2']==loni)].copy()
    if len(Data)>0:
        
        
        print(timi,lati,loni,ui,Data['Temp_2'].values[0])
        DATA_SELET=[timi,lati,loni,ui,Data['Temp_2'].values[0]]
        for ki,k in enumerate(DATA_SELET):
            if ki==len(DATA_SELET)-1:
                WW.write(str(k)+'\n')
            else:
                WW.write(str(k)+',')
                
