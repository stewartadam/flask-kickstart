# flask-kickstart
Flask application template for kickstarting development of small to medium sized applications, focused on providing the framework for a simple DB + REST API.

For large applications with more features, I recommend [cburmeister/flask-bones](https://github.com/cburmeister/flask-bones).

## Features
* Boilerplate Flask app structure that separates out models, views and configuration
* Simple REST API for CRUD operations against the configured object models ([flask-restless](https://flask-restless.readthedocs.io/en/stable/))
* Provisions a simple SQLite database ([flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/))
* Captures and prints tracebacks on syntax error ([flask-failsafe](https://github.com/mgood/flask-failsafe))
* Rate limiting against routes and API endpoints ([flask-limiter](https://flask-limiter.readthedocs.io/en/stable/))

*Note: For more advanced REST APIs (i.e. those not tied to DB models), I recommend switching to [flask-restful](https://flask-restful.readthedocs.io/en/latest/) instead. It does less out of the box but is far more flexible.*

## Configuration
Configuration is loaded in the following order:
1. Individual environment variables (per code in `DefaultConfig` from `myapp/config.py`)
2. Flask config file `instance/myapp.cfg` if it exists (copy from `myapp.cfg.sample` to try it out)
3. Flask config file pointed to by the `CONFIG_FILE` environment variable

## Deployment
### Local (debugging only)
[pipenv](https://github.com/pypa/pipenv) is the [Python.org](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) recommended way to manage project dependencies and virtual environments.

Once installed, simply execute `pipenv install -r requirements.txt` to automatically create a virtualenv and install all project dependencies.

The server can be executed with `pipenv run python server.py`. It will automatically reload when changes are detected to the Python source files.

### Docker
A `Dockerfile` is provided in the project. To build and run the image:
```
docker build -t flask-kickstart .
docker run -it --rm -p 8000:80 --name flask-kickstart-runtime flask-kickstart
```

See [GrahamDumpleton/mod_wsgi-docker](https://github.com/GrahamDumpleton/mod_wsgi-docker) for additional usage and details.

### Azure App Service
The app is ready to deploy to App Service, just connect the Web App to your Git repo with these files in it.

For more details, see [Git Publishing](https://docs.microsoft.com/en-us/azure/app-service/web-sites-python-configure#git-publishing) and [Create a Python web app in Azure](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python).
