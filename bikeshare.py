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
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which City you would you like to analyze (chicago, new york city, washington): ').lower()
        if city not in CITY_DATA:
             print('Sorry, invalid city name . Please try again.') #telling the user that the input is wrong
             continue
        else:
            break
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:# asking the user which month to filter the data by
        month = input('Please enter the month you would like to filter by (january, february, march, april, may, june), or type "all": ').lower()# using lower() in case sensitive
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please enter another month name.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:# asking the user which day to filter the data by
        day = input('Please enter the day of week you would like to filter by (monday, tuesday, wednesday, thursday, friday, saturday, sunday), or type "all": ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Please enter another day name.')


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
    # Loading data file into a DataFrame
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    
    # Converting the "Start Time" column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extracting month and day of week from the "Start Time" column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
     # Filtering by month
    if month !='all':
        # Converting month name to corresponding month number
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # Filtering by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Finding the most common month (month with the highest count) and display the result
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)


    # TO DO: display the most common day of week
    # Finding the most common day of the week (day with the highest count) and display the result
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day)


    # TO DO: display the most common start hour
    # Extracting the hour from the 'Start Time' column and create a new 'hour' column
    df['hour'] = df['Start Time'].dt.hour
    # Finding the most common start hour (hour with the highest count) and display the result
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        # Finding the most commonly used start station (station with the highest count) 
        # and display the result
        commonly_start_station = df['Start Station'].value_counts().idxmax()
        print('The most commonly used start station:', commonly_start_station)
    except KeyError:
        # If 'Start Station' column is not available, handle the KeyError and display a message
        print('Start Station data not available in this dataset.')

    # TO DO: display most commonly used end station
    try:
        # Finding the most commonly used end station (station with the highest count) 
        # and display the result
        commonly_end_station = df['End Station'].value_counts().idxmax()
        print('The most commonly used end station:', commonly_end_station)
    except KeyError:
        # If 'End Station' column is not available, handle the KeyError and display a message
        print('End Station data not available in this dataset.')

    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['Combination'] = df['Start Station'] + ' to ' + df['End Station'] #create a new temporary column 'Combination' in the DataFrame concatenates 'Start Station' and 'End Station' with the string ' to '
        frequent_combination = df['Combination'].value_counts().idxmax() # finding the most common combination, and returns the index of the most frequent combination associated with the maximum count.
        print('The most frequent combination of start station and end station trip:', frequent_combination)
    except KeyError:
        print('Start Station or End Station data not available in this dataset.')

    # Drop the temporary 'Combination' column
    df.drop('Combination', axis=1, inplace=True) #droping the temporary 'Combination' column from the DataFrame
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        # Calculating the total travel time (sum of 'Trip Duration' column) and display the result
        total_travel_time = df['Trip Duration'].sum()
        print('Total travel time:', total_travel_time)
    except KeyError:
        # If 'Trip Duration' column is not available, handle the KeyError and display a message
        print('Trip Duration data not available in this dataset.')


    # TO DO: display mean travel time
    try:
        # Calculating the mean travel time (average of 'Trip Duration' column) and display the result
        mean_travel_time = df['Trip Duration'].mean()
        print('Mean travel time:', mean_travel_time)
    except KeyError:
        # If 'Trip Duration' column is not available, handle the KeyError and display a message
        print('Trip Duration data not available in this dataset.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Counting the occurrences of each user type and display the result
    user_types_counts = df['User Type'].value_counts()
    print('Counts of each user type:')
    print(user_types_counts)


    # TO DO: Display counts of gender
    try:
        # Counting the occurrences of each gender and display the result
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of each gender:')
        print(gender_counts)
    except KeyError:
        # If 'Gender' column is not available, handle the KeyError and display a message
        print('\nNo data available for gender in this dataset.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
         # Find the earliest, most recent, and most common birth year and display the results
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest birth year:', earliest_birth_year)
        print('The most recent birth year:', recent_birth_year)
        print('The most common birth year:', common_birth_year)
    except KeyError:
        # If 'Birth Year' column is not available, handle the KeyError and display a message
        print('\nNo data available for birth year in this dataset.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Asks the user if they want to see raw lines from the filtered DataFrame. by ansewring (yes or no)
    If yes: it displays 5 lines at a time and then keeps asking if they want to see more until the answer is no
    
    """
    print('\nDisplaying Raw Data...\n')
    start_row = 0
    end_row = 5
    while True:
        # Asking the user if they want to see raw data
        user_input = input('Would you like to see 5 lines of raw data? Enter "yes" or "no": ')
        
        if user_input.lower() == 'yes':
            # Displaying 5 lines 
            print(df.iloc[start_row:end_row])
            start_row += 5
            end_row += 5
        elif user_input.lower() == 'no':
            break
        else:
            print('Invalid input. Please enter "yes" or "no".')# if the answer is not yes or no, will keep asking for valid input

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
