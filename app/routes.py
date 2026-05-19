from flask import Blueprint, render_template, request, flash, redirect, url_for
from .data import coffee_menu, featured_products

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template(
        "home.html",
        active_page="home",
        featured_products=featured_products
    )


@main.route("/menu")
def menu():
    return render_template(
        "menu.html",
        active_page="menu",
        coffee_menu=coffee_menu
    )


@main.route("/about")
def about():
    return render_template(
        "about.html",
        active_page="about"
    )



@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please complete all fields before sending your message.", "error")
            return redirect(url_for("main.contact"))

        if "@" not in email or "." not in email:
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("main.contact"))

        print("New Contact Message")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        flash("Thank you. Your message has been received. Our team will contact you shortly.", "success")
        return redirect(url_for("main.contact"))

    return render_template(
        "contact.html",
        active_page="contact"
    )