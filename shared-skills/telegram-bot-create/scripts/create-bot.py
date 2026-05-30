#!/usr/bin/env python3
import asyncio, json, os, re, sys, random, string
try:
    from pyrogram import Client, errors
except ImportError:
    print(json.dumps({"success": False, "error": "pyrogram not installed. Run: pip3 install pyrogram tgcrypto"}))
    sys.exit(1)

API_ID = os.environ.get("TELEGRAM_API_ID")
API_HASH = os.environ.get("TELEGRAM_API_HASH")
SESSION_STRING = os.environ.get("TELEGRAM_SESSION")

def rs(l=4):
    return "".join(random.choices(string.digits, k=l))

def sanitize(name):
    c = re.sub(r"[^a-zA-Z0-9]", "", name.lower())
    if not c: c = "agent"
    return c[:18] + rs(4) + "bot"

async def create_bot(agent_name, username=None):
    if not API_ID or not API_HASH or not SESSION_STRING:
        return {"success": False, "error": "Missing TELEGRAM_API_ID, TELEGRAM_API_HASH, or TELEGRAM_SESSION"}
    if not username: username = sanitize(agent_name)
    client = Client("bm", api_id=int(API_ID), api_hash=API_HASH, session_string=SESSION_STRING, in_memory=True)
    try:
        await client.connect()
        try:
            me = await client.get_me()
        except:
            return {"success": False, "error": "Session not authorized"}
        bf = "BotFather"
        await client.send_message(bf, "/newbot")
        await asyncio.sleep(2)
        h = client.get_chat_history(bf, limit=1)
        r = ""
        async for m in h: r = m.text or ""; break
        if "name" not in r.lower() and "what" not in r.lower():
            await client.send_message(bf, "/cancel")
            await asyncio.sleep(1)
            await client.send_message(bf, "/newbot")
            await asyncio.sleep(2)
        await client.send_message(bf, agent_name)
        await asyncio.sleep(2)
        h = client.get_chat_history(bf, limit=1)
        nr = ""
        async for m in h: nr = m.text or ""; break
        if any(w in nr.lower() for w in ["sorry","already","taken"]):
            username = sanitize(agent_name)
        await client.send_message(bf, username)
        await asyncio.sleep(3)
        h = client.get_chat_history(bf, limit=1)
        fr = ""
        async for m in h: fr = m.text or ""; break
        tm = re.search(r"(\d{8,12}:[A-Za-z0-9_\-]{35,})", fr)
        if tm: return {"success": True, "token": tm.group(1), "username": username, "display_name": agent_name}
        if any(w in fr.lower() for w in ["sorry","username","taken","already"]):
            nu = sanitize(agent_name)
            await client.send_message(bf, nu)
            await asyncio.sleep(3)
            h = client.get_chat_history(bf, limit=1)
            rr = ""
            async for m in h: rr = m.text or ""; break
            tm = re.search(r"(\d{8,12}:[A-Za-z0-9_\-]{35,})", rr)
            if tm: return {"success": True, "token": tm.group(1), "username": nu, "display_name": agent_name}
            return {"success": False, "error": "Username conflict: " + rr[:200]}
        return {"success": False, "error": "Unexpected: " + fr[:300]}
    except errors.FloodWait as e:
        return {"success": False, "error": "Flood wait: " + str(e.value) + "s"}
    except Exception as e:
        return {"success": False, "error": str(e)[:300]}
    finally:
        await client.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"success": False, "error": "Usage: python3 create-bot.py <name> [username]"}))
        sys.exit(1)
    result = asyncio.run(create_bot(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
    print(json.dumps(result))
    sys.exit(0 if result.get("success") else 1)
