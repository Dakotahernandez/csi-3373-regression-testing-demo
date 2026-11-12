"""
Run:  python app.py
Then open http://localhost:8000 in your browser.
Uses only the Python standard library (nothing to install).
"""

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from grades import letter_grade

PORT = 8000

PAGE = """<!doctype html>
<html>
<head><meta charset="utf-8"><title>Grade Calculator</title></head>
<body>
<h1>Grade Calculator</h1>
<form method="get" action="/">
  <label>Score (0-100): <input name="score" value="{score}" autofocus></label>
  <button type="submit">Get grade</button>
</form>
<p>{result}</p>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        raw = query.get("score", [""])[0].strip()

        result = ""
        if raw:
            try:
                score = float(raw)
                result = "Score {} = <b>{}</b>".format(escape(raw), letter_grade(score))
            except ValueError:
                result = "Please enter a number from 0 to 100."

        body = PAGE.format(score=escape(raw), result=result).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    print("Grade Calculator running at http://localhost:{}  (Ctrl+C to stop)".format(PORT))
    try:
        HTTPServer(("localhost", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
