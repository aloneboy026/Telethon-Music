import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25058013"))
    API_HASH = os.environ.get("API_HASH", "8c03e5160bfcc564c95bbf0e3edd6067")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5648256018:AAHkUfQm7OkZJGL_gboU14XjpNNNKpM3cQ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQF-Wt0AOIbtP8SlzuKnC5_JRBV1qxQ7nkcXwnCMVdy3LZhimeXGOcZm3icDmVFM8ntyHI_ilen_FQbYElp1E-KX8WD8psKIVdLH94bLMdmS8wAsRfKKHlwW1N-LwOhSxEvVf04vu6s9MAnzxZ_AQ6mLpzKlAyZTQMkG6sIje885OAQqoj2DZKQxc2MI6s5mPUmZJyB7iAkq1OEWPzV5-_LjiwcFahYMXrTETYw2psMfs5q1gEiXiyOZe8EdoUs2d06YsPyUf6Wkw9lgOpi_lL3lhLDjat9bpJxrLDdU8GVdgJRDww0PnpyCT_SPbRXTbKzJ8_fSnGQApecpsR1eRN2YSJDh0wAAAAFhEMyxAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "cutecat_robot")
    SUPPORT = os.environ.get("SUPPORT", "mondoclub") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "mondo_lover") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/93a8cad5a043351ac89d0.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/468cf34a0ae5d4eea9cb0.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5923458225")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "False"
