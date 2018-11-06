import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - one name of the city to analyze
        (str) month - one name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). 
    while True:
       city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
       if city in CITY_DATA:
           break
            
    # TO DO: get user input for month (all, january, february, march, ... , june)
    print('Do you like to filter the data by a specific month or by all months? Please type in a specific month from January to June or type in all.')
    while True:
        month = input().lower()
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may'or month == 'june' or month == 'all':
            print('You chose {}.'.format(month))
            break
        else:
            print('That is not a valid input. Please type one of the following options: January, February, March, April, May, June, all.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Do you like to filter the data by a specific day of the week or by all days? Please type in a day from Monday to Sunday or type in all.')
    while True:
        day = input().lower()
        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            print('You chose {}.'.format(day))
            break
        else:
            print('That is not a valid input. Please type one of the following options: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, all.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    months=['all','jan','feb','mar','apr','may','june']
    if month!='all':
        month=months.index(month)
        df=df[df['month']==month]
        
    if day !=7:
        df=df[df['day_of_week']==day]
        

    return df

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        common_month = df['month'].mode()[0]
        count_month = df['month'].value_counts().max()
        print('The most common month is {}. This occurred {} times.'.format(common_month, count_month))
	else:
		month_message = " in {}".format(month.title())

    # TO DO: display the most common day of week
    if day == 'all':
        common_day = df['day_of_week'].mode()[0]
        count_day = df['day_of_week'].value_counts().max()
        print('The most common day of the week is {}. This occurred {} times.'.format(common_day, count_day))
	else:
		day_message = " on {}".format(day.title())
	
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    count_start_hour = df['hour'].value_counts().max()
    print('The most common start hour is {}:00. This occurred {} times.'.format(common_start_hour, count_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['start_station']= df['Start Station'].value_counts()
    common_start_station= df['start_station'].mode()[0]
    print('Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    df['end_station']= df['End Station'].value_counts()
    common_end_station= df['end_station'].mode()[0]
    print('Common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + ", " + df['End Station']
    common_start_end_station= (df['Start Station'] + df['End Station'].mode()[0])
    print('Popular Combination Station:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time= df['Trip Duration'].mean()
    print('Average Travel Time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type= df['User Type'].value_counts()
    print('\nDifferenet types of users are:', user_type)
    start_time= time.time()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("Gender Counts")
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth= df['Birth Year'].max()
    print('\nThe oldest user were born in:', earliest_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    '''Displays five lines of data if the user wants to see the raw data.
    After displaying five lines of raw data, ask the user again if they would like to see five more of lines,
    continuing asking until the user enters "no".
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
        
    valid_input = False
    while valid_input == False:
        display = input('\nDo you want to see the raw data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, please type 'yes' or 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nDo you want to see more?'
                                     ' Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, please type 'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
	
	def display_data(df):
    view_data = input('Would you like to see the next five rows of data? Yes or No: ')
    view_data = view_data.lower()

    if view_data == 'yes':
        print('\033[1;31m=\033[1;m'*40)
        print(df.head(5))
        display_data(df)
    else:
        exit(print("Thank you for Exploring US Bikeshare Data"))
	
	def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
