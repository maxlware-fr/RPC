#  RRRR   PPPP    CCCC  
#  R   R  P   P  C      
#  RRRR   PPPP   C      
#  R R    P      C      
#  R  R   P      C      
#  R   R  P       CCCC  

from pypresence import Presence
import time

client_id = "YOUR_ID_HERE"

# =====================================
print("======================================")
print("RRRR   PPPP    CCCC")
print("R   R  P   P  C")
print("RRRR   PPPP   C")
print("R R    P      C")
print("R  R   P      C")
print("R   R  P       CCCC")
print("By Maxlware")
print("======================================")
# ======================================

print("[LOAD] Connexion...")

RPC = Presence(client_id)
RPC.connect()

details = "Focus max, pas de distractions"
state = "Concentration totale sur projet perso (je crois)"
large_image = "maxiii_logo"
large_text = ":D"
small_image = "footer"
small_text = "Mode turbo activé 🚀"
start_time = int(time.time())

RPC.update(
    details=details,
    state=state,
    large_image=large_image,
    large_text=large_text,
    small_image=small_image,
    small_text=small_text,
    start=start_time,
    buttons=[
        {"label": "Site officiel", "url": "https://maxlware.fr"},
        {"label": "Discord", "url": "https://discord.gg/7ZKnp9hYFj"}
    ]
)

print("[OK] Rich Presence activé.")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    RPC.clear()
    print("[STOP] Présence arrêtée.")
