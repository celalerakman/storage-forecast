# Storage Forecast

Storage capacity estimates from retention, replicas and daily growth.

The forecast estimates steady-state stored volume and storage-only monthly cost. Pricing is supplied as input; compute, requests and egress are excluded.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
