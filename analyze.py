"""Analysis helpers for lending club data"""
import pandas as pd
import re


def skip_nonnumeric_chars(string):
    return int(re.sub('[^0-9]', '', string))

def parse_percent(string):
    return float(re.sub(r'[ %]', '', string)) / 100


def load_loan_data():
    loan_data_path = 'data/LoanStats3a_securev1.csv'
    csv_dtypes = {
        'id': int,
        'member_id': int,
        'loan_amnt': float,
        'funded_amnt': float,
        'funded_amnt_inv': float,
        'term': int,
        'int_rate': float,
        'installment': float,
        'grade': str,
        'sub_grade': str,
        'emp_title': str,
        'dti': float,
        'fico_range_low': int,
        'fico_range_high': int
    }
    usecols = csv_dtypes.keys()
    converters = {
        'term': skip_nonnumeric_chars,
        'int_rate': parse_percent,
        'dti': parse_percent,
        'fico_range_low': int,
        'fico_range_high': int
    }

    with open(loan_data_path) as csv_file:
        df = pd.read_csv(csv_file,
                         dtype=csv_dtypes,
                         usecols=usecols,
                         converters=converters)
        return df
