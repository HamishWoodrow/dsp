[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
import matplotlib.pyplot as plt
resp = nsfg.ReadFemResp()

d={}
dbi={}
d_pmf = {}
dbi_pmf = {}

#Unbiased distribution
for num in resp.numkdhh:
    d[num]=d.get(num,0)+1
#Calculate PMF of unbiased distribution
n=resp.numkdhh.sum()
for x,y in d.items():
    d_pmf[x]= y/n

#Calculate biased PMF
for i,j in d_pmf.items():
    dbi[i]=(i*j)

#Normalise dbi
size = sum(dbi.values())
for ind,val in dbi.items():
    dbi_pmf[ind] = val/size
    
mean_un = resp.numkdhh.mean()
mean_bi = sum([(i*j) for i,j in dbi_pmf.items()])/sum(dbi_pmf.values())


#Create DataFrame from results
df=pd.DataFrame([d_pmf,dbi_pmf])
df.rename(index={0:"Unbiased",1:"Biased"},inplace=True)
df=df.T

#Display PMF table & Means
print(df)
print ('Unbiased Mean:', round(mean_un,2))
print ('Biased Mean:', round(mean_bi,2))

ax=df[['Unbiased','Biased']].plot(kind='bar',title='Number of Children',legend=True, figsize=(15,10),fontsize=12)
ax.set_xlabel("Number of Children",fontsize=12)
ax.set_ylabel("PMF", fontsize=12)
plt.show()
```
>>Unbiased Mean: 1.02
>>Biased Mean: 2.4