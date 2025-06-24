from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Triển khai Azure</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                color: #333;
                padding: 50px;
                text-align: center;
            }
            h1 {
                color: #2c3e50;
            }
            .box {
                background: white;
                padding: 30px;
                margin: auto;
                width: 60%;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Triển khai Microsoft Azure</h1>
            <p><strong>MSSV:</strong> 22DH113127</p>
            <p><strong>Họ tên:</strong> Lương Thanh Sơn</p>
            <p><em>Chạy bằng Flask - Python trên Azure App Service</em></p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
