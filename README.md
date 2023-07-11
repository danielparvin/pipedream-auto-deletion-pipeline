# Pipedream.com Auto-deletion Pipeline
I developed these Python scripts for a customer to automatically report inactive users of Horizon Web Ref, a sports officials scheduling app. These scripts are used in a weekly Pipedream.com cron job. I'm documenting them here as an example of Pipedream.com's Workflows feature.
 
## Details
I developed and chained together individual scripts in order to make the Workflow modular and maintainable. Pipedream.com Workflows allow developers to use the return values of scripts in subsequent steps. The order of the scripts is as follows:
1. get_access_token.py
2. get_all_users.py
3. filter_officials.py
4. filter_empty_postal_code_officials
5. update_data_store.py
	- This step uses Pipedream.com's Data Store feature to keep track of the registration date of new Horizon Web Ref users in a simple database, since the Horizon Web Ref API neglects to include a created_on field for users.
6. get_users_to_delete.py
7. format_users_to_delete_for_email.py

The last step of the workflow is an email step built into Pipedream.com. The workflow passes the return value of the format_users_to_delete_for_email.py script into the body of the email.
