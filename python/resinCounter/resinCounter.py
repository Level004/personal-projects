from dotenv import dotenv_values
import genshinstats as gs

env = dotenv_values(".env")
ltuid = int(env['LTUID'])
token = env['LTOKEN']
uid = int(env['GENSHINUID'])

gs.set_cookie(ltuid=ltuid, ltoken=token)

notes = gs.get_notes(uid)
print(f"Current resin: {notes['resin']}/{notes['max_resin']}")
print(f"Current realm currency: {notes['realm_currency']}/{notes['max_realm_currency']}")
print(f"Expeditions: {len(notes['expeditions'])}/{notes['max_expeditions']}")
input("Press enter to exit;")
