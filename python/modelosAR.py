##################################################################################
# Modelos AR(p).
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Analise de autocorrelacao e autocorrelacao parcial e estimacao de 
# modelos AR(p).
##################################################################################

# Importando libraries
import statsmodels.api   as sm
import pandas            as pd
import matplotlib.pyplot as plt
import numpy             as np

from statsmodels.graphics.tsaplots      import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')

# Definindo funcoes

def autocorr(lag,df):
    data         = np.array(df.iloc[lag:204,:])
    dataCentered = data - data.mean()   
    lagged         = np.array(df.diff(periods = lag).dropna())
    laggedCentered = lagged - lagged.mean()
    crossSum  = np.multiply(laggedCentered, dataCentered).sum()
    squareSum = (dataCentered**2).sum()  
    return crossSum / squareSum

def analiseExploratoria(data,x,y,lags):
    fig,axes = plt.subplots(nrows=2, ncols =2, figsize=(12, 12))
    fig.tight_layout()
    axes[0,0].plot(data)
    axes[1,0].boxplot(data)
    plot_acf( x=y, lags=lags, ax= axes[0,1])
    plot_pacf(x=y, lags=lags, ax= axes[1,1])    
    

#  EDA dos dados

acfArray = np.empty(shape=(20,1))
for i in range(20):
    acfArray[i,0] = autocorr(lag=i,df=df)

plt.plot(acfArray)

analiseExploratoria(data=df,x= df.index,y=df.value,lags=12)    

df_diff = df.diff(periods = 1).dropna()

analiseExploratoria(data=df_diff,x= df_diff.index, y=df_diff.value.squeeze(),lags=12)  

# Estimando AR(p) e extraindo métricas baseadas na verossimilhanca

start = 1
stop  = 10
metricas = pd.DataFrame(np.zeros((stop,2), dtype=float))
t=0
for p in range(start,stop+1):
    if p == 0:
        pass
    else:
        modelo = SARIMAX(endog = df_diff, order=(p,0,0), seasonal_order = (0,0,0,0)).fit()
        metricas.iloc[t,0] = modelo.aic
        metricas.iloc[t,1] = modelo.bic
        t += 1

metricas.rename(columns={0:'BIC',1:'AIC'})

