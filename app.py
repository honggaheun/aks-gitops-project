from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {{ background-color: #FFF3E0; color: #0D47A1; font-family: Arial, sans-serif; text-align: center; padding-top: 100px; }}
            .container {{ border: 5px solid #2196F3; padding: 30px; border-radius: 20px; display: inline-block; background-color: white; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Version 3.0 (Green)</h1>
            <h2>Status: Running on AKS</h2>
            <p>Pod Name: {hostname}</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)