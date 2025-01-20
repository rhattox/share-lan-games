import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

# If modifying these SCOPES, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]
PARENT_FOLDER_ID = "10OxTLL4WM4mUceumzDsidsHbmgXIJJYp"


def authenticate_google_drive():
    """Authenticate the user and return the service object."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = service_account.Credentials.from_service_account_file(
            "token.json", scopes=SCOPES
        )
        return creds
    else:
        print("Not able to login")
        exit(1)


def main():
    # Authenticate and build the service
    credential = authenticate_google_drive()
    service = build("drive", "v3", credentials=credential)

    file_metadata = {"name": "save", "parents": [PARENT_FOLDER_ID]}
    file = (
        service.files()
        .create(body=file_metadata, media_body="requirements.txt")
        .execute()
    )


if __name__ == "__main__":
    main()
