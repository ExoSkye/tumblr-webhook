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

    json_data = req.get_json()

    event = req.headers.get("X-GitHub-Event")

    if event == "push":
        data = client.create_text("celldk", state="published", slug=f"new-commit-{json_data['after']}", title=f"New commit to {json_data['repository']['name']}", body=f"New commit ID: {json_data['after']}\nMessage: {json_data['commits'][0]['message']}\nCI: TBD")
        logging.info(data)

    if event == "workflow_run":
        if json_data["action"] == "completed":
            if json_data["workflow_run"]["conclusion"] != "success":
                logging.info("CI Failed")
            else:
                logging.info("CI Succeeded")

    return func.HttpResponse("Post created")