import pandas as pd
import numpy as np

def set_pandas_option():
    pd.set_option('display.max_rows', None)


# pd.set_option('display.max_columns', None)

def dataset_title():
    print('Dataset illustrate weather oscillations for August from 1999 to 2019')





def read_dataset():
    dt = pd.read_csv('C:\\Users\\Quang\\Documents\\data.csv')
    df = pd.DataFrame(dt)
    return df



def filt_by_day(day):
    filt = (read_dataset()['Day'] == day)
    df = read_dataset().loc[filt]
    return df


def filt_by_day_year(day, year):
    filt = (read_dataset()['Day'] == day) & (read_dataset()['Year'] == year)
    df = read_dataset().loc[filt]
    return df


# client_show()


def solve_input_data():
    global day, year
    print(read_dataset())
    dataset_title()
    while True:
    # address day
        try:
            inp_day = input('enter your day: ')
            day = int(inp_day)

            if day < 1 or day > 31:
                print('Invalid Day Number >> Enter Again!')
            else:
                break

        except:
            print('Invalid Day Number >> Enter Again!')

    print(filt_by_day(day))

    # address year
    while True:
        try:
            inp_year = input('enter your year: ')
            year = int(inp_year)
            if year < 1999 or year > 2019:
                print('Invalid Year Number >> Enter Again!')
            else:
                break
        except ValueError:
            error_text = "Invalid Year Number. Enter Again!"
            print(error_text)

    print(filt_by_day_year(day, year))


solve_input_data()


def export_user_file():
    exp = filt_by_day_year(day, year).to_csv('userfile.csv')
    return exp


# export_user_dataset()


def exported_file_name(file_name):
    pass


def show_exported_suggestion():
    user_file = 'userfile.csv'
    global inp
    while True:
        try:
            yes = 'y'
            no = 'n'
            inp = str(input('Do you want to print an userfile?  y/n?       '))
            if inp != yes and inp != no:
                print('The answer must be y or n. please enter again!')

            else:
                break
        except:
            print('The answer must be y or n. please enter again!')

        if inp == yes:
            export_user_file()
            print('File named {} has been exported!'.format(user_file))
            break
        elif inp == no:
            return solve_input_data()
show_exported_suggestion()



