# 🚀 From Zero to Observable: Instrument Your App with OpenTelemetry & SigNoz (Self-Hosted)

### 👤 Audience:

Mid-scale tech teams facing production downtime and seeking their first real observability setup.

---

## 🔧 Why Observability?

Downtime is an inevitable part of any production system. However, experiencing issues without the ability to understand their root cause is no longer acceptable. Traditional logging often falls short in providing complete visibility—what modern teams need are metrics, traces, and logs that not only reveal what failed, but also why.

This tutorial walks you through setting up observability using OpenTelemetry and a self-hosted instance of SigNoz, enabling you to monitor and debug your applications with clarity and confidence.

---

## 🗺️ What You'll Build

A basic Python Flask app, instrumented with **OpenTelemetry SDKs** and sending data to **self-hosted SigNoz** via **OTLP** (OpenTelemetry Protocol).

---

## ✅ Prerequisites

* Docker & Docker Compose installed
* Git installed
* Python 3.8+ installed
* Familiarity with terminal/CLI and Docker basics

---

## 1️⃣ Step 1: Set Up SigNoz (Self-Hosted)

### 🔹 Clone SigNoz repo

```bash
git clone -b main https://github.com/SigNoz/signoz.git
cd signoz/deploy/
```

### 🔹 Start SigNoz with Docker

```bash
docker-compose -f docker-compose.yaml up -d
```

🕐 Wait a few seconds. Visit [http://localhost:3301](http://localhost:3301) to confirm SigNoz is up.

📦 This setup includes:

* **SigNoz UI**: Dashboard
* **OTEL Collector**: Accepts telemetry data
* **ClickHouse**: Stores metrics/traces
* **Query Service**: Powers the UI

---

## 2️⃣ Step 2: Create a Sample Flask App

### 📁 Project structure

```
basic-observability-app/
├── app.py
├── requirements.txt
└── otel-config.yaml
```

### 📄 `app.py`

```python
from flask import Flask
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Observable App!"

@app.route('/work')
def do_work():
    time.sleep(1)
    return "Simulated work done."

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 3️⃣ Step 3: Install OpenTelemetry SDK & Exporters

### 📄 `requirements.txt`

```txt
flask
opentelemetry-api
opentelemetry-sdk
opentelemetry-instrumentation
opentelemetry-exporter-otlp
opentelemetry-instrumentation-flask
```

### 🔹 Install the dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Step 4: Instrument the App with OpenTelemetry

### 📄 Create an OTLP config (optional but good practice)

`otel-config.yaml`:

```yaml
exporters:
  otlp:
    endpoint: http://localhost:4317
    insecure: true
```

### 🔹 Run your app with auto-instrumentation

```bash
opentelemetry-instrument \
  --traces_exporter otlp \
  --metrics_exporter none \
  --exporter_otlp_endpoint http://localhost:4317 \
  python app.py
```

✅ This wraps your Flask app with OpenTelemetry auto-instrumentation and starts sending trace data to the SigNoz OTLP endpoint.

---

## 5️⃣ Step 5: View Traces in SigNoz

Head back to [http://localhost:3301](http://localhost:3301):

* Click **"Traces"** tab.
* Search for service = `unknown_service:flask` (default if not named).
* You’ll see spans for `/` and `/work` routes.

💡 Pro Tip: You can explicitly name your service using:

```bash
OTEL_SERVICE_NAME=my-flask-app opentelemetry-instrument ...
```

---

## 🧠 Bonus: Add Custom Spans

To trace custom operations inside your Flask views:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

@app.route('/custom')
def custom_logic():
    with tracer.start_as_current_span("custom-operation"):
        time.sleep(0.5)
    return "Custom trace created."
```

---

## ✅ Recap

| Step | Description                              |
| ---- | ---------------------------------------- |
| 1️⃣  | Deploy self-hosted SigNoz using Docker   |
| 2️⃣  | Build a sample Flask app                 |
| 3️⃣  | Install OpenTelemetry SDKs and exporters |
| 4️⃣  | Instrument and run the app               |
| 5️⃣  | Monitor traces in SigNoz UI              |

---

## 🛠️ What’s Next?

* Add metrics: Use `opentelemetry-instrument --metrics_exporter otlp`
* Collect logs: Use OTEL log exporters
* Instrument other services (e.g., Node.js, Java, etc.)
* Deploy SigNoz on your internal infra (VM, Kubernetes, etc.)

---

## 🧩 Final Thoughts

Setting up observability doesn’t need to be complex. With **OpenTelemetry** and **SigNoz**, you gain immediate visibility into your app’s behavior. For any mid-sized company recovering from downtime, this is a game-changer.

Start small, go deep—**instrument the core services first**, expand to metrics and logs gradually, and you'll soon have a robust observability stack ready to catch issues before your users do.



---

## 📎 References & Credits

This tutorial is built using:

- [OpenTelemetry](https://opentelemetry.io/)
- [SigNoz](https://signoz.io/)

All trademarks, names, and logos are the property of their respective owners.

[![Powered by SigNoz](https://img.shields.io/badge/Powered%20By-SigNoz-orange)](https://signoz.io/)


---
