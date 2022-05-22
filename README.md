# FastAPI Docker Template

This cookiecutter template can be used to create a containerized app (fastapi framework).

## Usage

### Install cookiecutter

Install cookiecutter in your system wide Python environment.

```bash
pip install cookiecutter
```

### Start your project

```bash
cookiecutter git+https://github.com/LeoYuanjieLi/fastapi_docker_template.git
```

or use the ssh version:

```bash
cookiecutter git+ssh://git@github.com:LeoYuanjieLi/fastapi_docker_template.git
```

Then fill out `service_name`, `author`, and `python_version`, `todays_date` and start coding!

*Note that for `python_version` just supply the number. For example `3.8`.*

### Precomit installation

Black is configured for usage as a pre-commit, but it needs to be installed. Once you create and set up your virtual environment from the `requirements-dev.txt`, run

```bash
pre-commit install
```

and you should be good to go. *Note that you have to be in a git repository for pre-commits to work. So you might need to run `git init` first.*