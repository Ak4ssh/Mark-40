""" © RiZoeLX """
from pyrogram import Client 
import time, os, sys
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

print("""
     ╒═════════════════════════╕
        Starting Your Mark-40 
     ╘═════════════════════════╛
""")

if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v1"

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
MARK = os.getenv("MARK", None)
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
ASSEM_HNDLR = "A"
BYE_HNDLR = "O"
CURSE_HNDLR = "C"

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list


sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [1517994352, 1789859817, 1432756163, 5136000092]
for x in DEVS:
    SUDO_USERS.append(x)


start_time = time.time()


MARK = Client(
    'mark',
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=MARK,
    plugins={'root': 'Mark.source'},
)


#-------------------------CLIENTS-----------------------------
if SESSION:
    Session = Client(name="Session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
    call_py1 = PyTgCalls(Session)
else:
    Session = None
    call_py1 = None

if SESSION2:
    Session2 = Client(name="Session2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
    call_py2 = PyTgCalls(Session2)
else:
    Session2 = None
    call_py2 = None

if SESSION3:
    Session3 = Client(name="Session3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
    call_py3 = PyTgCalls(Session3)
else:
    Session3 = None
    call_py3 = None

if SESSION4:
    Session4 = Client(name="Session4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
    call_py4 = PyTgCalls(Session4)
else:
    Session4 = None
    call_py4 = None

if SESSION5:
    Session5 = Client(name="Session5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
    call_py5 = PyTgCalls(Session5)
else:
    Session5 = None
    call_py5 = None

if SESSION6:
    Session6 = Client(name="Session6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6)
    call_py6 = PyTgCalls(Session6)
else:
    Session6 = None
    call_py6 = None
        
if SESSION7:
    Session7 = Client(name="Session7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7)
    call_py7 = PyTgCalls(Session7)
else:
    Session7 = None
    call_py7 = None

if SESSION8:
    Session8 = Client(name="Session8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8)
    call_py8 = PyTgCalls(Session8)
else:
    Session8 = None
    call_py8 = None

if SESSION9:
    Session9 = Client(name="Session9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9)
    call_py9 = PyTgCalls(Session9)
else:
    Session9 = None
    call_py9 = None

if SESSION10:
    Session10 = Client(name="Session10", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10)
    call_py10 = PyTgCalls(Session10)
else:
    Session10 = None
    call_py10 = None

if SESSION11:
    Session11 = Client(name="Session11", api_id=API_ID, api_hash=API_HASH, session_string=SESSION11)
    call_py11 = PyTgCalls(Session11)
else:
    Session11 = None
    call_py11 = None

if SESSION12:
    Session12 = Client(name="Session12", api_id=API_ID, api_hash=API_HASH, session_string=SESSION12)
    call_py12 = PyTgCalls(Session12)
else:
    Session12 = None
    call_py12 = None

if SESSION13:
    Session13 = Client(name="Session13", api_id=API_ID, api_hash=API_HASH, session_string=SESSION13)
    call_py13 = PyTgCalls(Session13)
else:
    Session13 = None
    call_py13 = None

if SESSION14:
    Session14 = Client(name="Session14", api_id=API_ID, api_hash=API_HASH, session_string=SESSION14)
    call_py14 = PyTgCalls(Session14)
else:
    Session14 = None
    call_py14 = None
        
if SESSION15:
    Session15 = Client(name="Session15", api_id=API_ID, api_hash=API_HASH, session_string=SESSION15)
    call_py15 = PyTgCalls(Session15)
else:
    Session15 = None
    call_py15 = None

if SESSION16:
    Session16 = Client(name="Session16", api_id=API_ID, api_hash=API_HASH, session_string=SESSION16)
    call_py16 = PyTgCalls(Session16)
else:
    Session16 = None
    call_py16 = None
    
if SESSION17:
    Session17 = Client(name="Session17", api_id=API_ID, api_hash=API_HASH, session_string=SESSION17)
    call_py17 = PyTgCalls(Session17)
else:
    Session17 = None
    call_py17 = None

if SESSION18:
    Session18 = Client(name="Session18", api_id=API_ID, api_hash=API_HASH, session_string=SESSION18)
    call_py18 = PyTgCalls(Session18)
else:
    Session18 = None
    call_py18 = None

if SESSION19:
    Session19 = Client(name="Session19", api_id=API_ID, api_hash=API_HASH, session_string=SESSION19)
    call_py19 = PyTgCalls(Session19)
else:
    Session19 = None
    call_py19 = None

if SESSION20:
    Session20 = Client(name="Session20", api_id=API_ID, api_hash=API_HASH, session_string=SESSION20)
    call_py20 = PyTgCalls(Session20)
else:
    Session20 = None
    call_py20 = None
