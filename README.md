## Lambda mit FastAPI und Mangum

1. Virtual Enviroment

    Erstellt ein virtuelles Enviroment mit dem Namen "env"
    ```
    python -m venv env
    ```

    Virtuelles Enviroment aktivieren

    ```
    source env/bin/activate
    ```

    Je nach OS sind die Activate-Befehle unterschiedlich:
    https://docs.python.org/3/library/venv.html




2. Pakete installieren

    ```
    pip install fastapi uvicorn mangum
    ```

    Abhängigkeiten auflisten als requirements.txt

    ```
    pip freeze > requirements.txt
    ```

    Abhängigkeiten in einem seperaten "dependencies" Ordner installieren

    ```
    pip install -t dependencies -r requirements.txt
    ```

    ZIP File von dem Dependencies Ordner erstellen

    ```
    (cd dependencies; zip ../aws_lambda_artifact.zip -r .)
    ```