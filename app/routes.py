from flask import blueprints, render_template
from .data import coffee_menu, featured_products

main = blueprints("main", __name__)

@main.route("/")
def home():
    return render_template("home.html", featured_products=featured_products)

@main.route("/menu")
def menu():
    return render_template("menu.html", coffee_menu=coffee_menu)

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")

    