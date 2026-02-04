import os
from flask import Flask, request, render_template
from azure.data.tables import TableServiceClient
from openai import AzureOpenAI
from datetime import datetime

app = Flask(__name__)

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

table_service = TableServiceClient.from_connection_string(
    os.getenv("STORAGE_CONNECTION_STRING")
)
table_client = table_service.get_table_client("triagelogs")

def triage(symptoms):
    prompt = f"""
You are a medical triage assistant.
Classify the following symptoms into one of:
- Urgent Care
- Non-Urgent Visit
- Self Care

Symptoms: {symptoms}
Explain reasoning briefly.
"""
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        symptoms = request.form["symptoms"]
        result = triage(symptoms)

        table_client.create_entity({
            "PartitionKey": "triage",
            "RowKey": str(datetime.utcnow().timestamp()),
            "symptoms": symptoms,
            "result": result
        })

    return render_template("index.html", result=result)
