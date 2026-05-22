from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
from google import genai
from google.genai import types
import os, json, re

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-2.0-flash-lite"

HTML_PATH = os.path.expanduser("~/Downloads/specforge_final.html")

@app.route("/")
def index():
    html = open(HTML_PATH).read().replace("const API = 'http://localhost:5000'", "const API = ''").replace("const API = 'http://127.0.0.1:5000'", "const API = ''")
    return Response(html, mimetype="text/html", headers={"Cache-Control": "no-cache, no-store"})

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/chat", methods=["POST"])
def chat():
    messages = request.json.get("messages", [])
    system = "You are an expert Business Analyst. Ask ONE focused question at a time to gather software requirements. Cover: problem statement, stakeholders, goals, features, constraints, integrations, success metrics. After 8-10 exchanges write INTERVIEW_COMPLETE on its own line then thank them."
    history = []
    for m in messages[:-1]:
        role = "user" if m["role"] == "user" else "model"
        history.append(types.Content(role=role, parts=[types.Part(text=m["content"])]))
    last = messages[-1]["content"]
    response = client.models.generate_content(
        model=MODEL,
        contents=history + [types.Content(role="user", parts=[types.Part(text=last)])],
        config=types.GenerateContentConfig(system_instruction=system)
    )
    reply = response.text
    is_complete = "INTERVIEW_COMPLETE" in reply
    return jsonify({"reply": reply.replace("INTERVIEW_COMPLETE", "").strip(), "is_complete": is_complete})

@app.route("/api/analyze", methods=["POST"])
def analyze():
    transcript = request.json.get("transcript", "")
    response = client.models.generate_content(
        model=MODEL,
        contents=f"Analyze this requirements interview. Return ONLY valid JSON with keys: missing, ambiguities, contradictions, risks, assumptions (each an array of strings). No markdown.\n\nTRANSCRIPT:\n{transcript}"
    )
    text = re.sub(r"^```json\s*", "", response.text.strip())
    text = re.sub(r"\s*```$", "", text.strip())
    try:
        return jsonify(json.loads(text))
    except:
        return jsonify({"missing": [], "ambiguities": [], "contradictions": [], "risks": [], "assumptions": []})

@app.route("/api/generate-fsd", methods=["POST"])
def generate_fsd():
    data = request.json
    response = client.models.generate_content(
        model=MODEL,
        contents=f"Generate a comprehensive FSD as ONLY valid JSON (no markdown) with keys: project_title, version, date, executive_summary, project_overview(background/problem_statement/proposed_solution), stakeholders(array of role/responsibilities/impact), goals_and_objectives(primary_goals/success_metrics), scope(in_scope/out_of_scope), functional_requirements(array of id/title/description/priority/acceptance_criteria), non_functional_requirements(array of id/category/requirement/metric), assumptions_and_constraints(assumptions/constraints/dependencies), open_questions, recommended_next_steps.\n\nTRANSCRIPT:\n{data.get('transcript','')}\n\nGAPS:\n{json.dumps(data.get('gap_analysis', {}))}"
    )
    text = re.sub(r"^```json\s*", "", response.text.strip())
    text = re.sub(r"\s*```$", "", text.strip())
    try:
        return jsonify(json.loads(text))
    except:
        return jsonify({"project_title": "FSD", "version": "1.0", "date": "2026", "executive_summary": response.text[:300], "functional_requirements": [], "open_questions": [], "recommended_next_steps": []})

if __name__ == "__main__":
    app.run(debug=False, port=5000, host="127.0.0.1")
