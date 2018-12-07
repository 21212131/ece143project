
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import scipy

def string_dollar_to_integer(data, column):
    '''
    Change string dollar to integer dollar
    example : $75,000.00 to 75000
    Input:
    data: type = pandas.core.frame.DataFrame, the dataframe for cleaning
    column: type = str, valid column name in data
    '''
    
    assert isinstance(column, str)
    assert data.columns.contains(column)
    
    data[column] = data[column].apply(lambda x: int(x.replace(",","").strip('$').split('.')[0]) if isinstance(x, str) else x)

def visulize_region_difference(College_df, stage_str):
    '''
    Visualize the relation between regions and salaries at different stages of the career
    Input:
    College_df : type = pandas.core.frame.DataFrame,  the dataframe of the salaries sampled by schools
    stage_str: type = str, the stage of the career to be compared
    Output:
    f: type = matplotlib.figure.Figure
    '''
    
    assert isinstance(stage_str, str)
    assert isinstance(College_df, pd.core.frame.DataFrame)
    
    plotly.offline.init_notebook_mode(connected=True)
    
    State_group = College_df.groupby(['State'])
    state = State_group[stage_str].mean().index
    value = State_group[stage_str].mean().values
    
    data = dict(type = 'choropleth',
               locations = state,
               locationmode = 'USA-states',
               colorscale = 'Portland',
               text = state,
               marker = dict(line=dict(color='rgb(255,255,255)', width=2)),
               z = value,
               colorbar = {'title': stage_str})

    layout = dict(title = 'Region wise divide to show '+ stage_str,
             geo=dict(scope = 'usa')) 

    choromap2 = plotly.graph_objs.Figure(data = [data],layout=layout)
    f = plotly.offline.iplot(choromap2)

def visulize_schooltype_distribution(College_df, stage_str):
    '''
    Visualize the salaries distribution for both school type (public or private) at different stages of the career
    Input:
    College_df : type = pandas.core.frame.DataFrame,  the dataframe of the salaries sampled by schools
    stage_str: type = str, the stage of the career to be compared
    Output:
    f: type = matplotlib.figure.Figure, figure object
    '''
    
    assert isinstance(stage_str, str)
    assert isinstance(College_df, pd.core.frame.DataFrame)
    
    Public_df = College_df[College_df['School Type']=='Public']
    Private_df = College_df[College_df['School Type']=='Private']
    
    sns.set(style="ticks")
    sns.set(style="darkgrid")
    sns.set(font_scale=1.2)
    
    f, ax = plt.subplots(figsize=(12, 8))
    sns.distplot(Public_df[stage_str].values, bins=15, kde=False, fit=scipy.stats.gamma, label='Public');
    sns.distplot(Private_df[stage_str].values, bins=15, kde=False, fit=scipy.stats.gamma, label='Private');
    ax.set_xlabel(stage_str)
    plt.legend()
    return f

def visulize_schooltype_difference(College_df):
    '''
    Visualize the relation between school type (public or private) and median salaries at different stages of the career
    Input:
    College_df : type = pandas.core.frame.DataFrame,  the dataframe of the salaries sampled by schools
    Output:
    f: type = matplotlib.figure.Figure, figure object
    '''
    
    assert isinstance(College_df, pd.core.frame.DataFrame)
    
    sns.set(style="ticks")
    sns.set(style="darkgrid")
    sns.set(font_scale=1.2)
    
    f = sns.relplot(x="Starting Median Salary", y="Mid-Career Median Salary", alpha=0.5, 
                hue='School Type', hue_order=['Public', 'Private'], height=8, aspect=1.2, data=College_df)
    return f
def visulize_major_difference(Degree_df):
    '''
    Visualize the relation between majors and median salaries at different stages in career
    Input:
    Degree_df : type = pandas.core.frame.DataFrame,  the dataframe of the salaries sampled by degrees
    Output:
    f: type = matplotlib.figure.Figure, the figure object
    '''

    assert isinstance(Degree_df, pd.core.frame.DataFrame)
    
    Degree_df = Degree_df.sort_values(by=['Mid-Career Median Salary', 'Starting Median Salary'], ascending=False)
    sns.set(style="ticks")
    sns.set(style="darkgrid")
    
    f, ax = plt.subplots(figsize=(10, 15))
    
    sns.set_color_codes("pastel")
    sns.barplot(x="Mid-Career Median Salary", y="Undergraduate Major", data=Degree_df,
                label="Mid-Career", color="b")
    
    sns.set_color_codes("muted")
    sns.barplot(x="Starting Median Salary", y="Undergraduate Major", data=Degree_df,
                label="Starting", color="b")
    
    ax.legend(ncol=1, loc="lower right", frameon=True)
    ax.set(xlabel="Starting to Mid-Career Median Salary")
    sns.despine(left=True, bottom=True)
    
    return f
def visualize_salaries_increase_detail(Degree_df):
    '''
    Visualize the salaries increasing trending of different majors
    Input:
    Degree_df : type = pandas.core.frame.DataFrame, the dataframe of the salaries sampled by degrees
    Output:
    f: type = matplotlib.figure.Figure, the figure object
    '''
    
    assert isinstance(Degree_df, pd.core.frame.DataFrame)
    
    Degree_df = Degree_df.sort_values(by=['Mid-Career Median Salary', 
                                          'Mid-Career 90th Percentile Salary', 
                                          'Mid-Career 10th Percentile Salary'], ascending=False)
    sns.set(style="ticks")
    sns.set(style="darkgrid")
    
    f, ax = plt.subplots(figsize=(10, 15))
    
    sns.set_color_codes("pastel")
    sns.barplot(x="Mid-Career 90th Percentile Salary", y="Undergraduate Major", data=Degree_df,
                label="90th Percentile", color="b")
    
    sns.set_color_codes("muted")
    sns.barplot(x="Mid-Career Median Salary", y="Undergraduate Major", data=Degree_df,
                label="Median", color="b")
    
    sns.set_color_codes("dark")
    sns.barplot(x="Mid-Career 10th Percentile Salary", y="Undergraduate Major", data=Degree_df,
                label="10th Percentile", color="b")
    
    ax.legend(ncol=1, loc="lower right", frameon=True)
    ax.set(xlabel="Mid-Career salaries at different percentiles")
    sns.despine(left=True, bottom=True)
    
    return f  
def get_top_k_school(College_df, basedOn="Starting Median Salary", k=20, ascending=False, palette="Blues_d"):
    '''
    Visualize the relation between school type (public or private) and salaries
    Input:
    College_df: type = pandas.core.frame.DataFrame, the dataframe of the salaries sampled by schools
    basedOn: type = str, ordering metric
    k: type = int, the number of the school to be visualized
    ascending: type = bool, indicator of the order to be ascending or decending 
    palette: type = str, the color parameter of the figure
    Output:
    f: type = matplotlib.figure.Figure, the figure object
    '''
    
    assert isinstance(College_df, pd.core.frame.DataFrame)
    assert isinstance(k, int) and k>0
    assert isinstance(ascending, bool)
    assert basedOn in list(College_df.columns.values)
    assert isinstance(palette, str)
    
    sns.set(style="ticks")
    sns.set(style="darkgrid")
    sns.set(font_scale=1.2)
    f, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x=basedOn, y="School Name", palette=palette, 
                data=College_df.sort_values(by=[basedOn], ascending=ascending).head(k), ax=ax)
    return f