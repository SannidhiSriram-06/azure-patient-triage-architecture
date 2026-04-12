# Azure AI Patient Triage System (POC)

A cloud-deployed Flask application on **Azure App Service** that processes patient symptoms using **Azure OpenAI**, classifies triage priority, and records each interaction in **Azure Table Storage** for audit and traceability.

This project demonstrates an end-to-end Azure-based AI workflow: application hosting, LLM integration, and persistent logging.

---

## 🧠 Architecture

**Flow:**

User → Flask App (Azure App Service) → Azure OpenAI → Triage Classification → Azure Table Storage (Audit Log)

**Key Characteristics:**

* Stateless web service with externalized AI inference
* Persistent audit logging for every request
* Separation of compute, inference, and storage layers

---

## ⚙️ Tech Stack

| Layer   | Technology                                        |
| ------- | ------------------------------------------------- |
| Backend | Python 3.11, Flask, Gunicorn                      |
| AI/LLM  | Azure OpenAI (custom deployment: `triage-model`)  |
| Compute | Azure App Service (Linux, B1 tier)                |
| Storage | Azure Table Storage                               |
| Config  | Environment Variables (App Service Configuration) |

---

## 🚀 Functionality

1. User submits symptoms via a web interface
2. Backend sends structured prompt to Azure OpenAI
3. Model returns triage classification:

   * Urgent Care
   * Non-Urgent Visit
   * Self Care
4. Result is displayed to the user
5. Interaction is logged in Azure Table Storage for audit

---

## 🔐 Configuration & Security

* No secrets are hardcoded in the codebase

* All sensitive values are managed via **App Service environment variables**:

  * `AZURE_OPENAI_ENDPOINT`
  * `AZURE_OPENAI_API_KEY`
  * `AZURE_OPENAI_DEPLOYMENT`
  * `STORAGE_CONNECTION_STRING`

* Follows basic secure configuration practices for POC-level deployment

---

## 🧩 Repository Structure

* `app.py` — Flask application and API logic
* `requirements.txt` — Python dependencies
* `templates/index.html` — User interface
* `Azure_Triage_Deployment.pdf` — Deployment evidence and validation artifacts

---

## 📦 Deployment Notes

* Application deployed on Azure App Service (Linux runtime)
* Azure OpenAI configured with a dedicated model deployment
* Table Storage used for structured logging of each request/response pair
* Logging and runtime behavior validated through Azure monitoring tools

> Azure resources were decommissioned after deployment validation to optimize cost usage.
> The included deployment document provides timestamped evidence of infrastructure, execution, and logging.

---

## 🎯 Objectives

This project was designed to demonstrate:

* End-to-end deployment of an AI-powered application on Azure
* Integration of LLM inference into a production-style backend
* Use of managed cloud services for scalability and separation of concerns
* Implementation of persistent audit logging
* Debugging and stabilizing a cloud-hosted Python application

---

## 🏁 Outcome

A fully functional AI triage system successfully deployed on Azure, with validated request handling, LLM inference, and persistent logging.

This project represents a practical implementation of a cloud-native AI application with real-world deployment considerations.
