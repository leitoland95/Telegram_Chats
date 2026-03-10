from fastapi import FastAPI, Request
import threading
import time
import requests
import os
from telethon import TelegramClient

app = FastAPI()

# Inicializar Selenium al arrancar
@app.get("/chat_ids")
def chat_ids():
    api_id = 35177324   # tu api_id
    api_hash = "7975692bd48734fc89c8905a1addb23a"
    client = TelegramClient("session_name", api_id, api_hash)
    async def main():
    resultado = {}
    await client.start()
    async for dialog in client.iter_dialogs():
        resultado[dialog.name] = dialog.id
    return resultado
    with client:
        client.loop.run_until_complete(main())

# --- Keep Alive ---
def keep_alive():
    url = "https://srelemium-scraper.onrender.com"  # Render expone esta variable con tu dominio
    if not url:
        print("No se encontró RENDER_EXTERNAL_URL, keep_alive desactivado")
        return
    while True:
        try:
            requests.get(url)
            print(f"Ping a {url} para mantener vivo el servicio")
        except Exception as e:
            print(f"Error en keep_alive: {e}")
        time.sleep(60)  # cada 60 segundos

# Lanzar el hilo de keep_alive
threading.Thread(target=keep_alive, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)