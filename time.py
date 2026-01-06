from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'''
    <html>
        <head>
            <title>Текущее время</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }}
                .container {{
                    text-align: center;
                    padding: 20px;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                }}
                .time {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #007bff;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Текущая дата и время</h1>
                <div class="time">{current_time}</div>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)