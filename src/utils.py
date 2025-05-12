# src/utils.py

import pandas as pd
import os

def load_raw_data(path_raw='data/raw/'):
    """Carga los datasets originales desde la carpeta data/raw/"""
    contract = pd.read_csv(os.path.join(path_raw, 'contract.csv'))
    personal = pd.read_csv(os.path.join(path_raw, 'personal.csv'))
    internet = pd.read_csv(os.path.join(path_raw, 'internet.csv'))
    phone = pd.read_csv(os.path.join(path_raw, 'phone.csv'))
    return contract, personal, internet, phone

def merge_datasets(contract, personal, internet, phone):
    """Une todos los datasets usando customerID (left join sobre contract)"""
    df = contract.merge(personal, on='customerID', how='left')
    df = df.merge(internet, on='customerID', how='left')
    df = df.merge(phone, on='customerID', how='left')
    return df


def save_clean_data(df, path_clean='../data/clean/', filename='df_master.csv'):
    """Guarda el dataframe unificado en la carpeta correcta, incluso si se llama desde notebooks/"""
    os.makedirs(path_clean, exist_ok=True)
    df.to_csv(os.path.join(path_clean, filename), index=False)

