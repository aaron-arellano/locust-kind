"""
Locust uses Flask to serve the web UI and therefore it is easy to add web end-points to the web UI. 
By listening to the init event, we can retrieve a reference to the Flask app instance and use that 
to set up a new route.
"""

import os
from flask import Blueprint, render_template


# add required flask blueprint dependancies to render page correctly
path = os.path.dirname(os.path.abspath(__file__))
# re-use existing locust static resources
static_path = os.path.abspath("/usr/local/lib/python3.8/site-packages/locust/static")
project = Blueprint(
    "project",
    "webpage",
    static_folder=static_path,
    static_url_path="/project-repo/static/",
    template_folder=f"{path}/templates/",
)

# build on this for later
def web_init(web_ui) -> None:
    """
    Web initialize method. Can plug in other methods here to initialize a new route on lcust init.

    :param web_ui: is the web context of the locust tool.
    Returns None
    """

    @project.route("/project-repo")
    def github_page() -> str:
        web_ui.update_template_args()
        return render_template("github-page.html", **web_ui.template_args)

    web_ui.app.register_blueprint(project)
