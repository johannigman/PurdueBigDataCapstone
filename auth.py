from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Client ID and client secret file downloaded from Google Developers Console
CLIENT_SECRET_FILE = './client_secret.json'

# Scopes (permissions) needed for Gmail access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Run the OAuth 2.0 authorization flow
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_local_server(port=0)

# Print the access token and refresh token
print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)

# You can now use the credentials to build the Gmail service
service = build('gmail', 'v1', credentials=credentials)
