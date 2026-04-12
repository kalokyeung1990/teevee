class TeeVeeException(Exception):
    """
    Generic TeeVee Exception - should never be thrown, only sub-classed
    """


class AuthException(TeeVeeException):
    """
    Your authentication information are incorrect
    """


class CantRefreshShowException(TeeVeeException):
    """
    The show can't be refreshed right now
    """


class CantRemoveShowException(TeeVeeException):
    """
    The show can't removed right now
    """


class CantUpdateShowException(TeeVeeException):
    """
    The show can't be updated right now
    """


class EpisodeDeletedException(TeeVeeException):
    """
    This episode has been deleted
    """


class EpisodeNotFoundException(TeeVeeException):
    """
    The episode wasn't found on the Indexer
    """


class EpisodePostProcessingFailedException(TeeVeeException):
    """
    The episode post-processing failed
    """


class FailedPostProcessingFailedException(TeeVeeException):
    """
    The failed post-processing failed
    """


class MultipleEpisodesInDatabaseException(TeeVeeException):
    """
    Multiple episodes were found in the database! The database must be fixed first
    """


class MultipleShowsInDatabaseException(TeeVeeException):
    """
    Multiple shows were found in the database! The database must be fixed first
    """


class MultipleShowObjectsException(TeeVeeException):
    """
    Multiple objects for the same show were found! Something is very wrong
    """


class NoNFOException(TeeVeeException):
    """
    No NFO was found
    """


class ShowDirectoryNotFoundException(TeeVeeException):
    """
    The show directory was not found
    """


class ShowNotFoundException(TeeVeeException):
    """
    The show wasn't found on the Indexer
    """


class UpdaterException(TeeVeeException):
    """
    The updater encountered an error
    """
