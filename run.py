from app import create_app

app = create_app("development")
app.run(host="0.0.0.0", port=5000)
