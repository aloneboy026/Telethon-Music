import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25058013"))
    API_HASH = os.environ.get("API_HASH", "8c03e5160bfcc564c95bbf0e3edd6067")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5648256018:AAHkUfQm7OkZJGL_gboU14XjpNNNKpM3cQ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIcBu5o_vSsExjSwj3kq940NxJPHFv-sEqMutuTd42vLw8E3HXh2gNvZoHHe7vgus3zder_IBeuFOUunZfYyot0AC0DuVbQ5sLbQDj_pMl_qnGwCdGrEDl9nRrutJFrsO9BVakyljFFqB_3KXbpNwCAtZzz4Zd11CnRUA0Gjpl9qqQXbKQxqHO-dbAypFIDEGk-zIYBJ-VmrkFPzoE3s2W2tVPC89cDIA0ca7Qmfe6QmcsqNk_aQsttxvK0FmY-IOKhmwt1zIFzIVKHvuAA9yflgAOAHw2Vq0af8hq0w2ndWWwLhfmWha-REzaNJsDNqOovbXFpSiibcJQCiB0OGe3oNjO0=")
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
