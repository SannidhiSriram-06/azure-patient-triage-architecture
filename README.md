AI Patient Triage System on Azure
Cloud Solution Architect (CSA) Case Study using Azure AI, App Services, and Data Platform
📌 Overview

This project demonstrates how a rural healthcare problem can be translated into a repeatable Azure AI solution architecture using Microsoft cloud services.

Rural clinics often lack 24/7 medical staff. Patients are unsure whether their symptoms require urgent care, a doctor visit, or simple self-care. This leads to delayed treatment and overcrowded emergency rooms.

This case study shows how a Cloud Solution Architect can design an Agentic AI triage system using Azure OpenAI, Azure App Service, and supporting Azure platform services to solve this problem in a secure, scalable, and reusable manner.

🎯 Objective

Design a POC → MVP → Production-ready Azure architecture that:

Accepts patient symptoms through a web interface

Uses AI reasoning to classify triage severity

Logs triage results for audit and compliance

Notifies clinic staff for urgent cases

Follows healthcare-aligned security and governance practices

Can be reused across multiple clinics as repeatable IP

🧠 CSA Thinking Demonstrated

This project is intentionally written as an architecture mapping document rather than a coding exercise.

For each part of the problem, the following is defined:

Requirement → Azure Service → Why this service over alternatives

This mirrors how Microsoft Cloud Solution Architects design solutions during customer engagements.

🏗️ Azure Services Used
Requirement	Azure Service	Reason for Selection
Patient symptom input via web	Azure App Service	Managed web hosting, HTTPS, fast MVP, no VM overhead
Symptom reasoning & triage	Azure OpenAI (GPT-4/4o)	Agentic natural language reasoning without model training
Triage logging & audit trail	Azure Storage Account	Low-cost, durable storage for logs without DB complexity
Urgent case notifications	Azure Logic Apps	No-code workflow automation for alerts
Monitoring & telemetry	Azure Monitor + App Insights	Observability for requests, errors, and performance
Secret management	Azure Key Vault	Secure storage of API keys and credentials
🤖 Agentic AI Triage Logic

The AI follows structured prompt orchestration:

Interpret symptoms

Assess severity

Classify triage category

Provide explanation

This simulates agent behavior using Azure OpenAI without requiring complex orchestration platforms.

🔁 POC to Production Evolution
Stage	Architecture Characteristics
POC	Single App Service + Azure OpenAI + Storage for validation
MVP	Add Logic Apps alerts, App Insights dashboards, RBAC
Production	Multi-region deployment, private endpoints, enhanced compliance
🔐 Security & Compliance Considerations

The design is HIPAA-aligned at architecture level by ensuring:

HTTPS encrypted communication

Secure secret storage with Key Vault

Role-based access control (RBAC)

Isolated resource groups per deployment

Audit logging of triage decisions

♻️ Repeatable IP

This architecture is designed as repeatable IP, allowing the same pattern to be rapidly deployed across multiple rural clinics with minimal customization.

📄 Documentation

The full architecture mapping document is available here:

AI Patient Triage System – Azure Architecture Mapping.docx

This document contains detailed service justification and screenshots of Azure resources used.

🧩 Key Takeaway

This project demonstrates how Azure AI and platform services can be combined to deliver a real-world healthcare solution using Cloud Solution Architect principles rather than focusing purely on application code.
