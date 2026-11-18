# Login Demo — safe educational prank

This is a local Flask demo. It is not an Instagram login page and is not affiliated with Meta.

## Safety behavior
- Use only made-up demo credentials.
- The app does not store the test password.
- The app does not send the test password to Telegram.
- Telegram receives only the demo username and test-password length.
- The server binds to `127.0.0.1` (your computer only).

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set Telegram values in the current PowerShell window (optional):

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
$env:TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

Run:

```powershell
python app.py
```

Open `http://127.0.0.1:5000`.

## Telegram setup
1. In Telegram, open the official `@BotFather` account and create a bot.
2. Copy its token and set `TELEGRAM_BOT_TOKEN`.
3. Open your new bot and press Start.
4. Obtain your chat ID using a trusted Telegram bot-management method, then set `TELEGRAM_CHAT_ID`.
5. Never share your bot token. If it leaks, revoke it through BotFather.

Do not deploy this as a login clone or ask anyone for real account credentials.
