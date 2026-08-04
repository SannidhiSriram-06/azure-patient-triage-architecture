# Azure AI Patient Triage System (CSA Case Study)

> A cloud/DevOps case study: deploying and operating a Python web app on **Azure App Service**, wiring it to a managed backing service (**Azure Table Storage**) for persistent audit logging, and externalizing a stateful workload (LLM inference) to a managed API (**Azure OpenAI**). The AI classification is the workload — the point of the project is the cloud deployment and service composition around it.

---

## 🏗️ Architecture

**Flow:**

User → Flask App (Azure App Service, Linux) → Azure OpenAI (triage classification) → Azure Table Storage (audit log) → response back to user

**Key Characteristics:**

* Stateless web service, externalized AI inference
* Every request persisted to Table Storage for audit/traceability
* Compute, inference, and storage are separate managed services — no self-hosted infrastructure

---

## ⚙️ Tech Stack

| Layer   | Technology                                       |
| ------- | ------------------------------------------------- |
| Compute | Azure App Service (Linux, B1 tier)                |
| Backend | Python 3.11, Flask, Gunicorn                      |
| Storage | Azure Table Storage                               |
| AI/LLM  | Azure OpenAI (custom deployment: `triage-model`)  |
| Config  | Environment variables (App Service Configuration) |

---

## 🚀 Functionality

1. User submits symptoms via the web form (`index.html`)
2. Flask sends a structured prompt to Azure OpenAI (`app.py`)
3. Model returns a free-text triage classification and reasoning (prompted to pick one of: Urgent Care / Non-Urgent Visit / Self Care)
4. Result is rendered back to the user
5. The symptoms + result pair is written to the `triagelogs` Azure Table for audit

---

## 🔐 Configuration & Security

No secrets are hardcoded — all sensitive values are read from environment variables (set as App Service Configuration in deployment):

* `AZURE_OPENAI_ENDPOINT`
* `AZURE_OPENAI_KEY`
* `AZURE_OPENAI_DEPLOYMENT`
* `STORAGE_CONNECTION_STRING`

This is a POC-level deployment — see [Limitations](#-limitations-poc-scope) below for what a production hardening pass would add.

---

## 🧩 Repository Structure

```
AI-Patient-Triage-System-on-Azure-CSA-Case-Study-/
├── app.py                          # Flask app: routes, Azure OpenAI call, Table Storage write
├── index.html                      # Web form (rendered via Flask render_template)
├── requirements.txt                # flask, gunicorn, azure-data-tables, openai
├── Azure Architecture Diagram.png  # Architecture diagram
├── Azure Triage Deployment.pdf     # Deployment evidence / validation screenshots
└── AI Patient Triage System.docx   # Case study write-up
```

---

## 📦 Deployment Notes

* Deployed on Azure App Service (Linux runtime, Gunicorn as the WSGI server)
* Azure OpenAI configured with a dedicated model deployment (`triage-model`)
* Azure Table Storage used for structured, queryable logging of every request/response pair
* Runtime behavior and logging validated through Azure's built-in monitoring during deployment

> Azure resources were decommissioned after deployment validation to control cost.
> `Azure Triage Deployment.pdf` contains timestamped evidence of the live infrastructure, execution, and logging.

---

## ⚠️ Limitations (POC scope)

This is a proof of concept, not a production system:

* No authentication/authorization on the web form or any admin access to logs
* No input validation or rate limiting on the `/` POST route
* No retries or error handling around the Azure OpenAI call
* Single App Service instance (B1 tier) — no autoscaling or high-availability configuration
* No CI/CD pipeline wired up for this app (deployment was manual for this case study)

---

## 🎯 Objectives

This project demonstrates:

* Deploying a Python web app on Azure App Service
* Integrating a managed LLM service (Azure OpenAI) into a backend
* Using a managed NoSQL store (Table Storage) for audit logging
* Separation of compute, inference, and storage as distinct managed services
* Debugging and stabilizing a cloud-hosted application end to end

---

## 🏁 Outcome

A working triage system deployed on Azure with validated request handling, LLM inference, and persistent audit logging — used as a hands-on case study in composing Azure managed services rather than self-managing infrastructure.

---

## License

MIT
