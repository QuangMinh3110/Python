import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

def dataset_title():
    print('Dataset illustration weather parameters for August from 1999 to 2019')
dataset_title()


def read_csv():
    dt = pd.read_csv('C:\\Users\\Quang\\Documents\\data.csv')
    df = pd.DataFrame(dt)
    return df
#print(read_csv())


def client_show(day, year):
    filt = (read_csv()['Day'] == day) & (read_csv()['Year'] == year)
    df = read_csv().loc[filt]
    return df
#client_show()



def adress_client_requirement():
    global day, year
    while True:
#address day
        try:
            day_requirement = input('enter your day: ')
            day = int(day_requirement)

            if day<1 or day>31:
                print('Invalid Day Number >> Enter Again!')
            else : break

        except:
            print('Invalid Day Number >> Enter Again!')



#address year
    while True:
        try:
            year_requirement = input('enter your year: ')
            year = int(year_requirement)
            if year<1999 or year>2019:
                print('Invalid Year Number >> Enter Again!')
            else:
                break
        except ValueError:
            error_text = "Invalid Year Number. Enter Again!"
            print(error_text)

    print(client_show(day, year))


adress_client_requirement()


def export_user_dataset():
    exp = client_show(day, year).to_csv('userfile.csv')
    return exp
#export_user_dataset()


def printing_suggesting():
    user_file = 'userfile.csv'
    global yes, no
    while True:
        try:
            yes = 'y'
            no = 'n'
            inp = str(input('Do you want to print an userfile?  y/n?       '))
            if inp != yes and inp != no:
                print('The answer must be y or n. please enter again!')
            elif inp == yes:
                export_user_dataset()
                print('File named {} has been exported!'.format(user_file))
                break
            elif inp == no:
                return adress_client_requirement()
            else:
                break
        except:
            print('The answer must be y or n. please enter again!')
printing_suggesting()







