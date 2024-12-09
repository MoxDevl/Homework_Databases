import pandas as pd
import sqlite3


def main():
    log1_csv = 'last\\log1.csv'
    users_csv = 'last\\users1.csv'

    log_df = pd.read_csv(
        log1_csv, names=['user_id', 'time', 'bet', 'win'], encoding='utf-8', sep=',')

    users_df = pd.read_csv(
        users_csv, names=['user_id', 'email', 'geo'], encoding='koi8-r', sep='\t')

    conn = sqlite3.connect('last\\last-db.s3db')

    log_df.to_sql('log', conn, if_exists='replace', index=False)
    users_df.to_sql('users', conn, if_exists='replace', index=False)

    conn.close()


if __name__ == '__main__':
    main()
