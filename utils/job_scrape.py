from jobspy import scrape_jobs
import pandas as pd 

proxies = {
    'https': 'https://spkouufdnm:GyQi=2Xz1oM5m8mzyj@isp.decodo.com:10000'
}

def get_jobs():
    try:
        jobs = scrape_jobs(
            site_name=['indeed'],
            search_term='Software Engineer',
            location='San Francisco, CA',
            results_wanted=10,
            hours_old=168,
            country_indeed='USA',
            linkedin_fetch_description=True,
            proxies=proxies,
        )

        # write into csv file
        jobs.fillna('', inplace=True)
        return {'ready': True, 'data': jobs.to_dict(orient='records')}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

