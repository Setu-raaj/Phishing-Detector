from flask import Flask, request, jsonify, render_template
import re
import tldextract
from urllib.parse import urlparse

app = Flask(__name__)

def check_url(url):
    parsed = urlparse(url)
    ext = tldextract.extract(url)


    flags = []

    if len(url) > 75:
        flags.append("URL is very long")

    if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        flags.append("Uses IP address instead of domain name")

    if '@' in url:
        flags.append("Contains @ symbol")

    if ext.suffix in ['xyz', 'tk', 'pw', 'top', 'club']:
        flags.append(f"Suspicious domain extension: .{ext.suffix}")

    if parsed.scheme != 'https':
        flags.append("Not using HTTPS")

    subdomain_count = len(ext.subdomain.split('.')) if ext.subdomain else 0
    if subdomain_count > 2:
        flags.append("Too many subdomains")

   
    score = len(flags)
    if score == 0:
        verdict = "✅ Looks Safe"
    elif score <= 2:
        verdict = "⚠️ Suspicious"
    else:
        verdict = "🚨 Likely Phishing"

    return {
        "url": url,
        "verdict": verdict,
        "flags": flags,
        "risk_score": score
    }
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    result = check_url(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
