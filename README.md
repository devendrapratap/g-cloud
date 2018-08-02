# google-cloud

### how to use.

    1.  Set Environment Variable on Target Machine
		export GOOGLE_APPLICATION_CREDENTIALS="[FILE_PATH]"

    	For example: export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/default.json"

    2.  Set Environment Variable on Target Machine
		export PROJECT_NAME="project ID"
	
		For example: export PROJECT_NAME="alis-sandbox-3"

	3.	Command to import

		> from gcloud import tasks, events