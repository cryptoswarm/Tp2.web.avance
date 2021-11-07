from inf5190_projet_src import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)