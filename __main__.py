from app import create_app
from models.categoryModel import Category
from flask import jsonify
from controller import categoryController


app=create_app()
# app.add_url_rule('/test',)

@app.route("/",methods=["DELETE"])
def hello_world():
    categories= categoryController.getAll()
    return categories

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()