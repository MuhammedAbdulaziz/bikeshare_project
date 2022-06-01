# Many of The used method are obtained from the course provided material such as panda documentation
# and solved examples and many others
# for combination method used : https://stackoverflow.com/questions/50848454/pulling-most-frequent-combination-from-csv-columns
# for day_name instead of weekday_name: https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
# for calculating time : https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day = ''
    while city not in CITY_DATA:
        city = input('Enter your City(Chicago,New York, Washington): ').lower()
        if city not in CITY_DATA:
            print("Please Enter A Valid City!!")
    while month not in MONTH:
        month = input('Enter Month(January, February, March, April, May, June) or All: ').lower()
        if month not in MONTH:
            print("Please Enter A Valid Month!!")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in DAY:
        day = input('Enter Day or All: ').lower()
        if day not in DAY:
            print("Please Enter A Valid Day!!")
    print('-' * 40)
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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH.index(month)
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The Most Frequent Month Is :", df['month'].value_counts())
    # TO DO: display the most common day of week
    print("The Most Frequent Day Of Week Is :", df['day_of_week'].value_counts())
    # TO DO: display the most common start hour
    print("The Most Frequent Start Hour Is :", df['hour'].value_counts())
    print("This Took {} Seconds ".format((time.time() - start_time)))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The Most Popular Used Start Station :", df['Start Station'].value_counts())
    # TO DO: display most commonly used end station
    print("The Most Popular Used End Station :", df['End Station'].value_counts())
    # TO DO: display most frequent combination of start station and end station trip
    print("The Most Popular Used Start Station Combined With End Station  :",
          df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print("This Took {} Seconds ".format((time.time() - start_time)))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Duration :", df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print("Average Travel Duration :", df['Trip Duration'].mean())
    print("This Took {} Seconds ".format((time.time() - start_time)))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of User Types:", df['User Type'].value_counts())
    # TO DO: Display counts of gender
    try:
        print("Counts of Gender:", df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The Earliest Birth Year:", df['Birth Year'].min())
        print("The Most Recent Year Of Birth:", df['Birth Year'].max())
        print("The Most Common Year Of Birth:", df['Birth Year'].value_counts())
        print("This Took In {} Seconds ".format((time.time() - start_time)))
    except Exception as e:
        print("Error:{} Not Available In The Provided File".format(e))

    print('-' * 40)


def load_user_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        try:
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            load_user_data(df)
            user_stats(df)

        except Exception as e:
            print("Error {} Not Provided In The List".format(e))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
