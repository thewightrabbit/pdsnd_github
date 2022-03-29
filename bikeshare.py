import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

days = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
    ]

months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')

    # gets user input for city (chicago, new york city, washington) using a while loop to handle invalid inputs
    while True:
        city = input('please enter one of the following cities: chicago, new york city or washington: ').lower()
        if city not in CITY_DATA:
            print('that is not a valid city. please try again')
        else:
            break

    # gets user input for month (all, january, february, ... , june)
    while True:
        month = input('please enter one of the following months or type "all" to display data for all months: ').lower()
        months = [
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            ]
        if month != 'all' and month not in months:
            print('that is not a valid month. please try again')
        else:
            break

    # gets user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter one of the following days or type "all" to display data for all days: ').lower()
        days = [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            ]
        if day != 'all' and day not in days:
            print('that is not a valid day. please try again')
        else:
            break

        # loads the data into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # gets user input to view first five rows of data
    view_data = input('would you like to see the first five rows of data? please type "yes" or "no" ').lower()
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input('would you like to see the next five rows of data? please type "yes" or "no" ').lower()
        if view_display == "no": 
            keep_asking = False

    print('-' * 40)
    return (city, month, day)


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

    # converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extracts month,day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour
    # filters by month if applicable
    if month != 'all':
        # uses the index of the months list to get the int
        month = months.index(month) + 1
        # filters by month to create the new dataframe
        df = df[df['month'] == month]
    # filters by day if applicable
    if day != 'all':
        # filters by day to create the new dataframe
        df = df[df['day'] == day.title()]


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displays the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month: ', common_month)

    # displays the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day: ', common_day)

    # displays the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', common_start_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displays the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', common_start_station)

    # displays the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', common_end_station)

    # displays the most frequent combination of start station and end station trip
    common_start_end_combo = (df['Start Station'] + ' - '
                              + df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Stations: ', common_start_end_combo)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time; ', total_travel_time, ' seconds, or ', total_travel_time / 3600, ' hours')

    # displays the mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time; ', avg_travel_time, ' seconds, or ', total_travel_time / 3600, ' hours')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # displays the counts of user types
    print('Counts of User Types:\n', df['User Type'].value_counts())

    # displays the counts of gender
    if 'Gender' in df:
        print('Counts of Gender:\n', df['Gender'].value_counts())

    # displays the earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = int(df['Birth Year'].min())
        print('\nEarliest Year of Birth:', earliest_yob)
        most_recent__yob = int(df['Birth Year'].max())
        print ('\nMost Recent Year of Birth:', most_recent_yob)
        most_common_yob = int(df['Birth Year'].mode())
        print ('\nMost Common Year of Birth:', most_common_yob)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        (city, month, day) = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
