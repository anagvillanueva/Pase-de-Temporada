# lm.py
import requests
import json
import random

class LMSession:
    def __init__(self, endpoint="http://localhost:11434/api/chat", model="llama3.2"):
        self.model = model
        self.url = endpoint
        self.history = []

    def execute(self, prompt, temperature=None, format=None):
        self.history.append({"role": "user", "content": prompt})

        data = {
            "model": self.model,
            "stream": False,
            "messages": self.history,
            "options": {"seed": random.randint(1, 1000)}
        }
        if temperature is not None:
            data["options"]["temperature"] = float(temperature)

        # Solo manda 'format' si es exactamente 'json'
        if format == "json":
            data["format"] = "json"

        try:
            resp = requests.post(self.url, json=data, timeout=240)
            resp.raise_for_status()
            j = resp.json()
            content = j.get("message", {}).get("content")
            if not content:
                raise RuntimeError(f"Respuesta sin 'content': {j}")
            # opcional: guardar en history como assistant
            self.add_history(content)
            return content

        except Exception as e:
            # Revertir el último user message solo si hubo error
            if self.history and self.history[-1]["role"] == "user":
                self.history.pop()
            # Repropaga el error para que lo veas arriba si quieres,
            # o devuelve un mensaje claro:
            return f"[ERROR execute]: {e}"


