from inf5190_projet_src import create_app

appplication = create_app()

if __name__ == "__main__":
    appplication.run(debug=True)