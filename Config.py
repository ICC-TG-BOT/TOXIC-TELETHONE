import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13976276"))
    API_HASH = os.environ.get("API_HASH", "7f024cbc744a2f44569c3641b5ccecb7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052195748:AAFpuknQjZ9OOnqoTKoL2515BhhneWW_ZRI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHsBuy2g59aeQBQ9bdFelHsW_9wCiUucQ4JzKI6uzq5Ta7xiy10n-b8dcgOmJsiAYkK1pm9_kI1nACliB59ymeEmTCcV_pwwgSOIdj63pZNDWD5craiqOjVwg_lZYflNgmvOnQ6aEbPeV-ZEQSxM1naBRpkg5RTNQ-AB7bOOktDpusvBV_G4nXFKA-FvzA9feTg3rxm5L20djiSJMt8sE-CP45nlSW2y64C0dbknej0SBrYz_2eBXl2z3KYyUUBqoIEQM5PWv2a2hi56mDTRYVlZ4BSAdaBBKwp5vUbpuJ0AwUCKXCncUJYBUMon-rN06KDfLn0gxtv3c9ADMREVqG5HOR4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ICC_ToXiC_MuSiC_BoT")
    SUPPORT = os.environ.get("SUPPORT", "indian_chatting_club_offical") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TOXIC_UPDATES_OFFICIAL") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5503679152")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
