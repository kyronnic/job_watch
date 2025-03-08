from credentialer import get_api_key
from emailer import send_email
from history import *
from web_crawler import pull_ps_jobs

if __name__ == '__main__':
    scraped_jobs = pull_ps_jobs()
    all_new_jobs = create_update(scraped_jobs)
    if all_new_jobs is None:
        exit()
    else:
        new_jobs = look_for_specific_jobs(all_new_jobs)
        if new_jobs is None:
            exit()
        else:
            message_list = "\n\n".join([f'{job["Job Title"]}: {job["Link"]}' for job in new_jobs])
            message = f"I found some new PlayStation jobs for you!\n\n\n{message_list}"
            send_email(message)
