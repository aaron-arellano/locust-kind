"""
Locust uses Flask to serve the web UI and therefore it is easy to add web end-points to the web UI. 
By listening to the init event, we can retrieve a reference to the Flask app instance and use that 
to set up a new route.
"""
from locust import web

# build on this for later
def web_init(web_ui) -> None:
    """
    Web initialize method. Can plug in other methods here to initialize a new route on lcust init.

    web_ui is the web context of the locust tool.
    Returns none
    """

    @web_ui.app.route("/locust_kind")
    def github_page():
        return "https://github.com/aaron-arellano/locust-kind"
