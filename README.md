# Django PDF download demo

For local development only. Add a trusted PDF at `files/sample.pdf`.

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

Open http://127.0.0.1:8000/download/ to download the PDF directly.
Do not deploy with the development SECRET_KEY or DEBUG=True.
