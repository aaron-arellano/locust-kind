# main file
from locust import User, task, between, events
from web import github_page

class MyUser(User):
    @task
    def my_task(self):
        print("executing my_task")

    wait_time = between(0.5, 10)


# add locust init event listener to create new path in web-ui component
@events.init.add_listener
def locust_init(web_ui, **kwargs):
    '''
    Method listens to locust initialize event handler and pass the web_ui context to calling methods.
    '''
    github_page.web_init(web_ui)