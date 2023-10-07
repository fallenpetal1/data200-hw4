import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
####
### Deployed at :
### https://data200hw4-dpnzjv95fs.streamlit.app/
####
st.write()
df = pd.read_csv("toy_dataset.csv")
st.header("Toy Dataset")
st.write("A small sample of the dataset :")
st.write(df.head())
st.write(df.shape)
st.subheader("Distribution of population across cities")
# Interactive - Diff representations of population in city - pie, line, stem?, 
chart = st.radio(
    "Choose how you wish to view the population spread across the cities.",
    ["Scatter plot", "Line chart", "Area plot"],
    index=None,
)
df_city = df.groupby(['City']).count().reset_index()[['City', 'Number']]

if (chart == 'Scatter plot'):
    st.scatter_chart(data=df_city, x="City", y="Number")
elif (chart == 'Line chart'):
    st.line_chart(df_city, x="City", y="Number")
elif (chart == 'Area plot'):
    st.area_chart(df_city, x="City", y="Number")

st.write("The plots show that New York City has the most population (50,307) with San Diego being (4881) the least populated as per the sample")
###############
st.subheader("Distribution of incomes across cities")
import altair as alt
c = (
   alt.Chart(df)
   .mark_circle()
   .encode(x="City", y="Income")
)

st.altair_chart(c, use_container_width=True)
st.write("The plot shows the datapoints of income in each city. From the representation the ranges of income in each city is evident, with Mountain View having the highest incomes, ranging from around \$95,523 to \$1,77,157. Dallas has the lowest incomes ranging between \$584 to \$91,479")

# Representation of Incomes based on Gender in the various cities
st.subheader("Representation of gender-wise incomes in various cities")
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
st.write("The plots show that the men's average income are a little higher than that of women in all cities with Mountainview having the highest avg income and that the number of men living in the cities are also more than women with New York being the most populated.")




