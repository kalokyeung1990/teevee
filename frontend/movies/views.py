from flask import Blueprint, render_template

from teevee import logger, settings

# from teevee.movies import movie

blueprint = Blueprint("movies", __name__, template_folder="templates", static_folder="static", url_prefix="/movies")


@blueprint.route("/")
def movies():
    logger.info("Loading movies page")
    logger.debug(f"movies: {settings.show_list}")

    return render_template("movies.html", movies=settings.movie_list)
