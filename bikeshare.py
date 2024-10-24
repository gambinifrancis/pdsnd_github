import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTHS = ["january", "february", "march", "april", "may", "june"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_month()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()

    print("-" * 40)
    return city, month, day


def get_city():
    while True:
        city = (
            input(
                "Would you like to see data for Chicago, New York City, or Washington?\n"
            )
            .strip()
            .lower()
        )
        if city in list(CITY_DATA.keys()):
            break
    return city


def get_month():
    while True:
        month = (
            input(
                "What month would you like to see data for? [All, January, February, ..., June]\n"
            )
            .strip()
            .lower()
        )
        if month in MONTHS or month == "all":
            break
    return month


def get_day():
    while True:
        day = (
            input(
                "What day would you like to see data for? [All, Monday, Tuesday, ..., Sunday]\n"
            )
            .strip()
            .lower()
        )
        if day in DAYS or day == "all":
            break
    return day


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
    filename = CITY_DATA[city]

    df = pd.read_csv(filename, parse_dates=[1, 2])
    df.drop(df.columns[0], axis=1, inplace=True)

    if month != "all":
        df = df[df["Start Time"].dt.month == MONTHS.index(month) + 1]

    if day != "all":
        df = df[df["Start Time"].dt.dayofweek == DAYS.index(day)]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    if month == "all":
        months_counts = df["Start Time"].dt.month.value_counts()
        common_month = months_counts.index[0]
        common_month_count = months_counts[common_month]

        print(
            f"Most common month: {
            MONTHS[common_month - 1].title()}. Count: {common_month_count}"
        )

    # TO DO: display the most common day of week
    if day == "all":
        days_counts = df["Start Time"].dt.dayofweek.value_counts()
        common_day = days_counts.index[0]
        common_day_count = days_counts[common_day]

        print(
            f"Most common day: {
            DAYS[common_day].title()}. Count: {common_day_count}"
        )

    # TO DO: display the most common start hour
    hours_counts = df["Start Time"].dt.hour.value_counts()
    common_hour = hours_counts.index[0]
    common_hour_count = hours_counts[common_hour]

    print(f"Most common hour: {common_hour} hrs. Count: {common_hour_count}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_counts = df["Start Station"].value_counts()
    common_start_station = start_station_counts.index[0]
    common_start_station_count = start_station_counts[common_start_station]

    print(
        f"Most common start station: {
          common_start_station}. Count: {common_start_station_count}"
    )

    # TO DO: display most commonly used end station
    end_station_counts = df["End Station"].value_counts()
    common_end_station = end_station_counts.index[0]
    common_end_station_count = end_station_counts[common_end_station]

    print(
        f"Most common end station: {
          common_end_station}. Count: {common_end_station_count}"
    )

    # TO DO: display most frequent combination of start station and end station trip
    start_end_counts = (df["Start Station"] + " - " + df["End Station"]).value_counts()
    common_start_end = start_end_counts.index[0]
    common_start_end_count = start_end_counts[common_start_end]

    print(
        f"Most common start-end station combination: {common_start_end}. Count: {common_start_end_count}"
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df["Trip Duration"].sum()
    print(f"Total travel time: {travel_time} seconds")

    # TO DO: display mean travel time
    travel_time_mean = df["Trip Duration"].mean()
    print(f"Travel time mean: {travel_time_mean} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()

    print("User Types:")

    for user_type, count in user_types.items():
        print(f"\t{user_type}. Count: {count}")

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("Genders:")

        gender_types = df["Gender"].value_counts()

        for gender_type, count in gender_types.items():
            print(f"\t{gender_type}. Count: {count}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("Birth year statistics:")

        earliest_bd = df["Birth Year"].min()
        latest_bd = df["Birth Year"].max()

        bd_counts = df["Birth Year"].value_counts()
        common_bd = bd_counts.index[0]
        common_bd_count = bd_counts[common_bd]

        print(f"\tEarlies birth year: {int(earliest_bd)}")
        print(f"\tLatest birth year: {int(latest_bd)}")
        print(
            f"\tMost common birth year: {
              int(common_bd)}. Count: {common_bd_count}"
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def show_individual_data(df):
    """Display 5 records at a time until user stops it or there are no more records to show."""

    for i in range(0, len(df), 5):
        df_rows = df.iloc[i : i + 5]
        print(df_rows)

        see_more = input("Want to see 5 more records? (yes/no).\n").lower()

        if see_more == "no":
            break


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        show_records = input("Would you like to view individual trip data? (yes/no).\n")
        if show_records.lower() == "yes":
            show_individual_data(df)

        restart = input("\nWould you like to restart? (yes/no).\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
