#!/usr/bin/env python3
import click

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ["https://www.googleapis.com/auth/presentations"]


def get_slides_service():
    creds = None
    if os.path.exists("token.json"):
        from google.oauth2.credentials import Credentials

        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("slides", "v1", credentials=creds)
    return service


@click.group
def cli():
    pass


@cli.command()
def auth():
    """Authenticate to Google, allow the app to perform actions on Google slides.
    After this completes, you should have a `token.json` file available
    """
    service = get_slides_service()


if __name__ == "__main__":
    cli()
