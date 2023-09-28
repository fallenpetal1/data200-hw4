import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
####
### Deployed at :
### https://data200hw4-dpnzjv95fs.streamlit.app/
####

df = pd.read_csv("toy_dataset.csv")

#1. Representation of Incomes based on Gender in the various cities
fig, x = plt.subplots()
df_income = df.groupby(["City", "Gender"]).Income.mean().unstack(0)
df_t = df_income.transpose() 

fig = plt.figure() 

ax1 = fig.add_subplot(1,2,1) 

df_t.Female.plot(kind='bar', color='pink', ax=ax1, width=0.3, position=1)
df_t.Male.plot(kind='bar', color='lavender', ax=ax1, width=0.3, position=0)

ax1.set_xlabel('City')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

ax1.set_ylabel('Income')
ax1.legend(title='Gender')

plt.xlabel("City")
plt.xticks(rotation=45, horizontalalignment='right')


#2. Distribution of men and women across cities
ax2 = fig.add_subplot(1,2,2) 
df_ill_gr = df.groupby(['City', 'Gender']).Age.count().unstack(0)
df_ill = df_ill_gr.transpose()#.reset_index()
df_ill.Female.plot(kind='bar', color='pink', ax=ax2, width=0.3, position=1)
df_ill.Male.plot(kind='bar', color='lavender', ax=ax2, width=0.3, position=0)

ax2.set_xlabel('City')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

ax2.set_ylabel('Count')
#ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()
ax2.legend(title='Gender')

plt.xlabel('City')
plt.xticks(rotation=45, horizontalalignment='right')

st.pyplot(fig)
st.write("The plots show that the men's average income are a little higher than that of women in all cities and that the number of men living in the cities are also more than women.")
st.write(df_t)
st.write(df_ill)
