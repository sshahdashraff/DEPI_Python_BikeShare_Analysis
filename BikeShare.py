import time 
import datetime
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np  
CityData={'new_york_city':'new_york_city.csv',
        'chicago':'chicago.csv',
        'washington':'washington.csv'}
def filter_data():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filtered
    (str) day - name of the day of week to filter by, or "all" to apply no day filtered
    """
    print('Hello let\'s explore some of US BikeShare data!')

    # get the city entered by the user (new_york_city, chicago or washington )
    print('please enter the city you want(new_york_city, chicago or washington )')
    while True:
        try:
            city=input().lower()
            if(city == 'new_york_city' or city == 'chicago' or city == 'washington'):
                print('the city you want is {}'.format(city))
                break
        
            else:
                print("you entered a city is not from the list, please choose from [new york,chicago or washington]".format(city))
            
        except ValueError:
            print("you entered a city is not from the list, please choose from [new york,chicago or washington]")
            continue
        
#get the  month entered by the user (all or from january to june )
    print("please enter the month you want january, february, march till june or enter all to choose all months ")           
    MonthList=['january','february','march','april','may','june']
    NoDataMonthList=['september','october','november','december','july','august']    

    while True:
        try:
            month = input().lower()
        
            if month in MonthList:
                print('the month you want is {}'.format(month))
                break
        
            if month in NoDataMonthList:
                print('there is no available data for {}, please enter another month'.format(month))
                continue
        
            elif month == 'all':
                print('you chose all months of the year')
        
            else:
                print("this is not a month from the list, please enter a valid month")
        except:
            print("this is not a month from the list, please enter a valid month")
            continue
    

#get the day entered by the user (all or from saturday to friday )
    print("enter the day you want from all days in week or enter all to choose all days")
    DayList=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    while True:
        try:
            day = input().lower()
        
            if day in DayList:
                print('the day you want is {}'.format(day))
                break
        
            elif day == 'all':
                print('you chose all days of the week')
        
            else:
                print("this is not a day from the list, please enter a valid day")
        except ValueError:
            print("this is not a day from the list, please enter a valid day")
            continue
    
    print('#'*50)
    return city,month,day

def load_data(city, month, day):
    """
    Loads data from the specified city and filters by month and day if applicable 

    Args:    
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filtered
        (str) day - name of the day of week to filter by, or "all" to apply no day filtered

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CityData[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])   
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    
    if month != 'all':
        MonthList=['january','february','march','april','may','june','july','august']
        month=MonthList.index(month)+1
        df = df[df['month']==month]
        
    if day != 'all':
        df=df[df['day']==day.title()]
    return df
print('#'*50)

def time_statistics(df):
    """Displays Statistics on the most frequent times of travel"""
    print('\n Calculating the most frequent times of travel: \n')
    
    if not df.empty:  # Check if DataFrame is empty
        df['month']=df['Start Time'].dt.month
        common_month=df['month'].mode()[0]
        print('the most frequent month:',common_month)
    
    if not df.empty:
        df['day']=df['Start Time'].dt.day
        common_day=df['day'].mode()[0]
        print('the most frequent day:',common_day)
    
    if not df.empty:
        df['hour']=df['Start Time'].dt.hour
        common_hour=df['hour'].mode()[0]
        print('the most frequent hour:',common_hour)
    
    
# Create a bar chart for month counts
    month_counts = df['month'].value_counts()
    plt.figure(figsize=(10, 6))
    month_counts.plot(kind='bar')
    plt.title('Most Frequent Months')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.show()
    
    print('#'*50)
    
    
def station_statistics(df):
    """Displays Statistics on the most popular stations and trip"""
    print('\n Calculating the most popular stations and trip:  \n')
    
    common_start_station=df['Start Station'].mode()[0]
    print('the most commonly used start station is {}'.format(common_start_station))
    
    common_end_station=df['End Station'].mode()[0]
    print('the most commonly used end station is {}'.format(common_end_station))
    
    # Create a pie chart for start station distribution
    start_station_counts = df['Start Station'].value_counts().head(10)
    plt.figure(figsize=(8, 8))
    plt.pie(start_station_counts, labels=start_station_counts.index, autopct='%1.1f%%')
    plt.title('Top 10 Start Stations')
    plt.show()
    
    print('#'*50)
    
    
def trip_duration_statistics(df):
    """Displays Statistics on the total and average trip duration"""
    print('\n Calculating Trip Duration:  \n')
    
    total_trip_time=df['Trip Duration'].sum()
    print('Total Travel Time is {} in seconds '.format(round(total_trip_time,2)))
    
    
    avg_trip_time=df['Trip Duration'].mean()
    print('Average Travel Time is {} in seconds '.format(round(avg_trip_time,2)))
    
    print('#'*50)
    
    
def users_statistics(df):
    """Displays Statistics On BikeShare Users""" 
    print('\n Calculating Users Statistics:  \n')
    
    user_type_count=df['User Type'].value_counts()
    print("Count of user types is: \n{}".format(user_type_count))
    
    try:
        gender_count=df['Gender'].value_counts()
        print("Count of gender types is: \n{}".format(gender_count))
        
    except KeyError:
        print("\n Washington doesn't have data for Gender types")
        
        
def main():
    while True:
        city, month, day = filter_data()
        df = load_data(city, month, day)
        time_statistics(df)
        station_statistics(df)
        trip_duration_statistics(df)
        users_statistics(df)
        
        print('\n Would you like to continue? Please enter yes or no. \n')
        cont=input()
        if cont.lower() != 'yes':
            break 
if __name__ == "__main__":
    main()
