# {{cookiecutter.service_name}}
## Usage



## Contributing

1. Clone the repo and use `requirements-dev.txt` to set up your virtual environment.

2. Set up the pre-commit hook:

    ```bash
        pre-commit install
    ```

3. Any new function/method you write should also have a test. To run the tests, pip install this library in your virtual environment then run pytest.

    ```bash
        pip install -e .
        pytest tests/ -vs
    ```