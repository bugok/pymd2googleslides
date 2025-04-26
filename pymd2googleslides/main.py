#!/usr/bin/env python3
import click

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from marko.md_renderer import MarkdownRenderer
from marko.parser import Parser
import marko

SCOPES = ["https://www.googleapis.com/auth/presentations"]


def get_slides_service(client_secret_path):
    creds = None
    token_path: str = "token.json"
    if os.path.exists(token_path):
        from google.oauth2.credentials import Credentials

        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, "w") as token:
            token.write(creds.to_json())

    service = build("slides", "v1", credentials=creds)
    return service


@click.group
def cli():
    pass


@cli.command()
@click.option("--client-secret-path", type=click.Path(), default="client_secret.json")
def auth(client_secret_path: str):
    """Authenticate to Google, allow the app to perform actions on Google slides.
    After this completes, you should have a `token.json` file available.

    You need to get a client_secret.json file from Google Console.
    Here are the needed steps:

    Go to Google Cloud Console: https://console.cloud.google.com/

    Create a new project.

    Enable the Google Slides API.

    Go to APIs & Services > Credentials.

    Create OAuth 2.0 Client ID for Desktop App.

    Download the client_secret.json.
    """
    service = get_slides_service(client_secret_path)


@cli.command()
@click.argument(
    "input_file", type=click.Path(exists=True, readable=True, dir_okay=False)
)
def render(input_file: str):
    markdown = marko.Markdown(Parser, MarkdownRenderer) 
    with open(input_file) as f:
        result: str = markdown.convert(f.read())
        click.echo(result)


if __name__ == "__main__":
    cli()
