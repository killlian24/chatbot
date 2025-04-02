# DSGVO-konformer AI-Chatbot mit Strapi-Inhalten, lokalem Modell (Mistral via Ollama) und Chroma

# Projektstruktur:
# chatbot/
# ├── app/
# │   ├── strapi_loader.py
# │   ├── build_index.py
# │   ├── chat_server.py
# │   └── web_frontend.html
# ├── Dockerfile
# ├── docker-compose.yml
# ├── README.md

# ---------- README.md ----------
# DSGVO-konformer Chatbot mit Strapi und Mistral (Ollama)

Dieses Projekt enthält einen KI-Chatbot, der Inhalte aus einem Strapi-CMS verwendet und mit einem lokal laufenden Mistral-Modell (über Ollama) arbeitet – vollständig DSGVO-konform.

## ✅ Voraussetzungen

- Synology NAS oder Linux-Server mit x86-Architektur
- Docker & Docker Compose installiert
- Strapi CMS mit Inhaltstyp `Artikel` unter `/api/artikel`
- Optional: SSH-Zugriff

## 📦 Installation

```bash
git clone https://github.com/dein-name/strapi-chatbot.git
cd strapi-chatbot
docker-compose up --build
```

## 🔁 Inhalte aus Strapi laden

```bash
docker exec -it strapi-chatbot-chatbot-1 python build_index.py
```

Dadurch werden deine Artikel aus dem CMS geladen, zerlegt und im Vektorspeicher abgelegt.

## 🌐 Webinterface öffnen

Im Browser:
```
http://<deine-nas-ip>:8000/web_frontend.html
```

## 🔗 In Webflow einbinden

```html
<iframe
  src="http://<deine-nas-ip>:8000/web_frontend.html"
  width="100%"
  height="600"
  style="border:none;">
</iframe>
```

## 💡 Hinweise

- Das Mistral-Modell wird beim ersten Start automatisch von Ollama geladen (~5–7 GB)
- Daten werden **nicht** an Dritte gesendet
- Ideal für medizinische, rechtliche oder vertrauliche Inhalte

---

## 📄 Lizenz
MIT – frei nutzbar und anpassbar.

---

# (Der restliche Code folgt wie gehabt)

# ---------- strapi_loader.py ----------
import requests

... (der bisherige Code bleibt unverändert)
