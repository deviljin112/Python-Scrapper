from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import (
    ItJobsWatchHomePageTop30,
)
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
from flask import Blueprint, redirect, url_for, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
import pandas as pd
import os

main = Blueprint("main", __name__)

path_to_app = os.path.abspath(os.getcwd())

head = [
    "Skill / Job Role",
    "Current Rank",
    "Rank Change Year-on-Year",
    "Median Salary",
    "Median Salary % Change",
    "Historical Ads",
    "Live Vacancies",
]

file = pd.read_csv(f"{path_to_app}/csv/ItJobsWatchTop30.csv")
table = list(file.values)

jobs = [
    {
        "id": i,
        "skill_job_role": table[i][0],
        "current_rank": table[i][1],
        "rank_change": table[i][2],
        "median_salary": table[i][3],
        "median_salary_change": table[i][4],
        "historical_ads": table[i][5],
        "live_vacancies": table[i][6],
    }
    for i in range(len(table))
]


@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "pull" in request.form:

            top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
            Top30CSVGenerator().generate_top_30_csv(
                top_30.get_top_30_table_elements_into_array(),
                os.path.expanduser(f"{path_to_app}/csv/"),
                "ItJobsWatchTop30.csv",
                top_30.get_table_headers_array(),
            )

        return render_template(
            "index.html", page_name="Home Page", page=table, heading=head
        )

    elif request.method == "GET":
        return render_template("index.html", page_name="Home Page")


@main.route("/about/")
def about():
    return render_template("about.html", page_name="About Hubert")


@main.route("/panel/", methods=["GET", "POST"])
@login_required
def panel():
    if request.method == "POST":
        if "submit" in request.form:
            params = request.form

            id_num = params.get("id_number")
            job = params.get("job_role")
            rank = params.get("rank")

            query_builder = []

            if id_num:
                query_builder.append(f"id={id_num}")

            if job:
                query_builder.append(f"skill_job_role={job}")

            if rank:
                query_builder.append(f"current_rank={rank}")

            if not (id_num or job or rank):
                return page_not_found(404)

            query = "?" + "&".join(query_builder)

            return redirect("/api/v1/resources/jobs" + query)

    elif request.method == "GET":
        return render_template(
            "panel.html", page_name="User Panel", name=current_user.username
        )


@main.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", page_name="ERROR 404")


@main.route("/api/v1/resources/jobs/all", methods=["GET"])
def api_all():
    return jsonify(jobs)


@main.route("/api/v1/resources/jobs", methods=["GET"])
def api_id():
    params = request.args

    id_num = None
    job_name = None
    rank = None

    if "id" in params:
        id_num = int(params["id"])

    if "skill_job_role" in params:
        job_name = str(params["skill_job_role"])

    if "current_rank" in params:
        rank = int(params["current_rank"])

    results = []
    for job in jobs:
        if job["id"] == id_num:
            results.append(job)

        if job["skill_job_role"] == job_name:
            results.append(job)

        if job["current_rank"] == rank:
            results.append(job)

    if len(results) == 0:
        return page_not_found(404)

    return jsonify(results)
