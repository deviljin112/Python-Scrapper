from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import (
    ItJobsWatchHomePageTop30,
)
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from . import db
import pandas as pd
import os

main = Blueprint("main", __name__)

path_to_app = os.path.abspath(os.getcwd())


@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "pull" in request.form:
            print("pull request")

            top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
            Top30CSVGenerator().generate_top_30_csv(
                top_30.get_top_30_table_elements_into_array(),
                os.path.expanduser(f"{path_to_app}/csv/"),
                "ItJobsWatchTop30.csv",
                top_30.get_table_headers_array(),
            )

        file = pd.read_csv(f"{path_to_app}/csv/ItJobsWatchTop30.csv")
        table = list(file.values)

        head = [
            "Skill / Job Role",
            "Current Rank",
            "Rank Change Year-on-Year",
            "Median Salary",
            "Median Salary % Change",
            "Historical Ads",
            "Live Vacancies",
        ]

        return render_template(
            "index.html", page_name="Home Page", page=table, heading=head
        )

    elif request.method == "GET":
        return render_template("index.html", page_name="Home Page")


@main.route("/about/")
def about():
    return render_template("about.html", page_name="About Hubert")


@main.route("/panel/")
@login_required
def panel():
    return render_template(
        "panel.html", page_name="Administrator Panel", name=current_user.username
    )
