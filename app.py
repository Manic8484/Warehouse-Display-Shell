
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def tab_config():
    return [
        {
            "number": 1,
            "label": os.getenv("TAB1_LABEL", "Warehouse"),
            "url": os.getenv("TAB1_URL", ""),
        },
        {
            "number": 2,
            "label": os.getenv("TAB2_LABEL", "Movements"),
            "url": os.getenv(
                "TAB2_URL",
                "https://warehouse-movements-263201611680.europe-west2.run.app/board",
            ),
        },
        {
            "number": 3,
            "label": os.getenv("TAB3_LABEL", "Tab 3"),
            "url": os.getenv("TAB3_URL", ""),
        },
        {
            "number": 4,
            "label": os.getenv("TAB4_LABEL", "Tab 4"),
            "url": os.getenv("TAB4_URL", ""),
        },
    ]

@app.get("/")
def display():
    return render_template("display.html", tabs=tab_config())

@app.get("/health")
def health():
    return jsonify({"ok": True, "service": "warehouse-display"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
