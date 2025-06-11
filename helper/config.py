#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *
# config.py - Updated with robust error handling
from decouple import config
from . import LOGS

try:
    # Required variables
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    
    # Optional variables with defaults
    OWNER = config("OWNER_ID", default=1322549723, cast=int)
    
    # LOG_CHANNEL handling (force negative if provided)
    LOG = config("LOG_CHANNEL", default=0, cast=int)
    if LOG > 0:  # Convert to negative if positive ID provided
        LOG = -abs(LOG)
        
except Exception as e:
    LOGS.critical(f"❌ Config Error: {str(e)}")
    LOGS.info("Bot is shutting down...")
    exit(1)
