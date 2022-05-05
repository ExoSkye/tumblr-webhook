import logging

import azure.functions as func
import pytumblr
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client = pytumblr.TumblrRestClient(
        os.environ["consumer_key"],
        os.environ["consumer_secret"],
        os.environ["oauth_key"],
        os.environ["oauth_secret"]
    )

    client.create_text("celldk", state="published", slug="testing-text-posts", title="Testing", body="testing1 2 3 4")

    return func.HttpResponse("Post created")