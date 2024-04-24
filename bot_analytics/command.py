import importlib

TELEGRAM_BOT_COMMANDS = {
    "/start": "bot_analytics.commands.start",
    "/mulai": "bot_analytics.commands.start",
    "/tanya": "bot_analytics.commands.tanya",
    "/cari": "bot_analytics.commands.cari",
    "/broadcast": "bot_analytics.commands.broadcast",
    "Pengertian✍️️": "bot_analytics.commands.materi_pengertian",
    "Menyiapkan Ukuran📏": "bot_analytics.commands.materi_ukuran",
    "Pola📐": "bot_analytics.commands.materi_pola",
    "Bahan🧵": "bot_analytics.commands.materi_bahan",
    "Vidio Tutorial▶️": "bot_analytics.commands.materi_vidio",
    "Bolero Skala Kecil": "bot_analytics.commands.materi_pola_bolero_kecil",
    "Bolero Skala Besar": "bot_analytics.commands.materi_pola_bolero_besar",
    "Rompi Skala Kecil": "bot_analytics.commands.materi_pola_rompi_kecil",
    "Rompi Skala Besar": "bot_analytics.commands.materi_pola_rompi_besar"
}
