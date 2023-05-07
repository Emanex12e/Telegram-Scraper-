import time
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest

# Telegram API anahtarları
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# Telefon numarası ve oturum adı
phone_number = '+90 NUMARA...'
session_name = 'scraper'

# Telegram hesabına giriş yap
client = TelegramClient(session_name, api_id, api_hash)
client.start(phone_number)

# Gruplara eriş
from_group_name = 'cekecegin grup adı @ olmadan?'
to_group_name = 'kendi grubunun adı @ olmadan'
from_group = client.get_entity(from_group_name)
to_group = client.get_entity(to_group_name)

# grupdaki üyeleri çek
members = []
for member in client.iter_participants(from_group):
    members.append(member)

# Üyeleri kendi grubuna ekleyin
for member in members:
    try:
        client(InviteToChannelRequest(
            to_group,
            [member]
        ))
        print(f'{member.username} successfully invited to {to_group_name}')
    except PeerFloodError:
        print("Gruptaki üye davet etme limitine ulaşıldı. Program 1 saat boyunca duracak.")
        time.sleep(3600)
        client(InviteToChannelRequest(
            to_group,
            [member]
        ))
        print(f'{member.username} successfully invited to {to_group_name}')
    except Exception as e:
        print(f'Error inviting {member.username} to {to_group_name}: {str(e)}')
    time.sleep(30)

# Telegram hesabından çıkış yap
client.disconnect()
