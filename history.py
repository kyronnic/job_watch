import pandas as pd
import os
import dotenv
from web_crawler import pull_ps_jobs
from typing import Optional

dotenv.load_dotenv()

def create_update(jobs: dict) -> Optional[pd.DataFrame]:
    history_filepath = f'{os.getenv("file_directory")}/history.csv'
    df = pd.DataFrame.from_dict(jobs, orient='index').reset_index()
    df.columns = ['Job Title', 'Link']
    df['Scraped On'] = pd.Timestamp.now()
    if os.path.exists(history_filepath):
        history_df = pd.read_csv(history_filepath)
        new_jobs = df[~df['Job Title'].isin(history_df['Job Title'])]
        if new_jobs.empty:
            return None
        history_df = pd.concat([history_df, new_jobs], ignore_index=True)
        history_df.to_csv(history_filepath)
        return new_jobs
    else:
        df.to_csv(history_filepath, index=False)
        return df

def look_for_specific_jobs(df: pd.DataFrame):
    keywords = ['analyst', 'data']
    anti_words = ['director', 'manager']

    titles = [x for x in df['Job Title']
                       if any([word in x.lower() for word in keywords])
                       and all([anti not in x.lower() for anti in anti_words])]

    interest_jobs = df[df['Job Title'].isin(titles)]
    return interest_jobs.to_dict('records')

if __name__ == '__main__':
    os.remove(f'{os.getenv("file_directory")}/history.csv')
    jobs = pull_ps_jobs()
    jobs_df = create_update(jobs)
    print(look_for_specific_jobs(jobs_df))
