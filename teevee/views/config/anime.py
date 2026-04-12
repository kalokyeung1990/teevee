import os

from tornado.web import addslash

import teevee.start
from teevee import settings
from teevee.oldbeard import config, filters, ui
from teevee.views.common import PageTemplate
from teevee.views.routes import Route

from .index import Config


@Route("/config/anime(/?.*)", name="config:anime")
class ConfigAnime(Config):
    @addslash
    def index(self):
        t = PageTemplate(rh=self, filename="config_anime.mako")

        return t.render(
            submenu=self.ConfigMenu(),
            title=_("Config - Anime"),
            header=_("Anime"),
            topmenu="config",
            controller="config",
            action="anime",
        )

    def saveAnime(self, use_anidb=None, anidb_username=None, anidb_password=None, anidb_use_mylist=None, split_home=None, split_home_in_tabs=None):
        settings.USE_ANIDB = config.checkbox_to_value(use_anidb)
        settings.ANIDB_USERNAME = anidb_username
        settings.ANIDB_PASSWORD = filters.unhide(settings.ANIDB_PASSWORD, anidb_password)
        settings.ANIDB_USE_MYLIST = config.checkbox_to_value(anidb_use_mylist)
        settings.ANIME_SPLIT_HOME = config.checkbox_to_value(split_home)
        settings.ANIME_SPLIT_HOME_IN_TABS = config.checkbox_to_value(split_home_in_tabs)

        teevee.start.save_config()
        ui.notifications.message(_("Configuration Saved"), os.path.join(settings.CONFIG_FILE))

        return self.redirect("/config/anime/")
