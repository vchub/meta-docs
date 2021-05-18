
### Local development setup


Install google-cloud SDK
https://cloud.google.com/sdk/docs/install


Install google-cloud packages

				conda install Flask requests

				pip install google-cloud-firestore

				conda install -c conda-forge google-cloud-bigquery


Install ngrok


run with firebase emulator

				firebase emulators:exec "python src/main.py"

or just start the app

				python src/main.py

run ngrok

				ngrok http 8085

example of ngrok url to put it as hook for a provider (mail, twilio )
http://1f7c2a18da98.ngrok.io/bot


email provider
http://c23f40f579fb.ngrok.io

current email:  82a8ecd4404dd9a81b5a@cloudmailin.net
