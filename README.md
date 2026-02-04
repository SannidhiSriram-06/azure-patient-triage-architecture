# Azure AI Patient Triage System (POC)

A Flask-based web application deployed on **Azure App Service** that accepts patient symptoms, sends them to **Azure OpenAI**, classifies the triage level, and logs every interaction into **Azure Table Storage**.

This project demonstrates a complete, working Azure architecture from compute → AI → storage, validated entirely through deployment evidence.

> ⚠️ All Azure resources were deleted after proof-of-deployment.
> This repository relies on screenshots as verifiable evidence.

---

## 🧠 Architecture Overview

User → Flask App (Azure App Service) → Azure OpenAI → Triage Result → Azure Table Storage (audit log)

This follows the POC architecture documented in the original design.

---

## ⚙️ Tech Stack

* Python 3.11
* Flask
* Gunicorn
* Azure App Service (Linux, B1)
* Azure OpenAI (model deployment: `triage-model`)
* Azure Table Storage
* Environment Variables for secrets (no Key Vault for POC stage)

---

## 🚀 What the App Does

1. User enters symptoms in a web form
2. Flask sends symptoms to Azure OpenAI
3. Model classifies into:

   * Urgent Care
   * Non-Urgent Visit
   * Self Care
4. Result is displayed to the user
5. Same result is logged into Azure Table Storage for audit

---

## 🔐 Secure Configuration

Secrets are **not hardcoded**.

The app uses App Service **Environment Variables**:

* `AZURE_OPENAI_ENDPOINT`
* `AZURE_OPENAI_API_KEY`
* `AZURE_OPENAI_DEPLOYMENT`
* `STORAGE_CONNECTION_STRING`

---

## 📸 Deployment Proof (see PDF)

The included PDF contains 13 screenshots proving:

| Proof                            | Evidence                         |
| -------------------------------- | -------------------------------- |
| All Azure resources created      | Resource group view              |
| Azure OpenAI model deployed      | Deployment list (`triage-model`) |
| Flask app running on App Service | Web App overview                 |
| Environment variables configured | Env vars page                    |
| Gunicorn startup                 | Startup command                  |
| Container boot logs              | Log stream                       |
| Working triage result            | Browser screenshot               |
| Data persisted to storage        | Table entities view              |
| App Service plan metrics         | Live compute metrics             |

This demonstrates a **real cloud integration**, not a local demo.

---

## 🧩 Repository Contents

* `app.py` — Flask application
* `requirements.txt` — Dependencies
* `templates/index.html` — UI
* `Azure_Triage_Deployment.pdf` — Deployment evidence

---

## 🧭 Why No URLs?

All Azure resources were intentionally deleted after validation to avoid unnecessary cost.
Screenshots serve as permanent, timestamped proof of deployment.

---

## 🎯 Purpose of This Project

This project was built to demonstrate practical understanding of:

* Azure App Service deployment mechanics
* Azure OpenAI integration in production-style apps
* Secure secret handling via environment variables
* Persistent logging using Azure Table Storage
* Debugging real-world Azure Linux container issues

---

## 🏁 Outcome

A fully working AI triage system deployed on Azure, validated through logs, storage entries, and runtime evidence.

This is a Proof-of-Concept implementation of a cloud-native AI application.
