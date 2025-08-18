from server import app

if __name__ == '__main__':
    print("Server starting on http://0.0.0.0:5000")
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Failed to start server: {str(e)}")
