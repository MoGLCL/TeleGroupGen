from telethon import TelegramClient, functions
import asyncio
import datetime
import random

# --- إدخال البيانات من المستخدم ---
api_id = int(input("ادخل API ID: ").strip())
api_hash = input("ادخل API HASH: ").strip()
friend_number = input("ادخل رقم صديقك (بصيغة +20xxxxxxxxxx): ").strip()

# --- إنشاء العميل ---
client = TelegramClient("my_session", api_id, api_hash)

# --- قائمة رسائل متنوعة ---
messages = [
    "أهلاً بالجميع 🌹 هذا جروب تجريبي",
    "مرحبا 👋 اتمنى لكم يوماً سعيداً",
    "💡 هذا مجرد اختبار للنظام",
    "🔥 تم إنشاء الجروب بنجاح",
    "⚡️ بوت تجريبي يعمل الآن"
]

GROUPS_PER_DAY = 50  # عدد الجروبات اليومية

async def main():
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    for i in range(GROUPS_PER_DAY):
        group_name = f"جروب {today} - {i+1}"
        
        try:
            # إنشاء جروب وإضافة الصديق
            result = await client(functions.messages.CreateChatRequest(
                users=[friend_number],
                title=group_name
            ))
            
            chat = result.chats[0]
            chat_id = chat.id

            # اختيار 3 رسائل عشوائية مختلفة
            random_messages = random.sample(messages, 3)

            for msg in random_messages:
                await client.send_message(chat_id, msg)
                await asyncio.sleep(1)

            print(f"✅ تم إنشاء: {group_name} وبعت 3 رسايل")
        
        except Exception as e:
            print(f"❌ حصل خطأ في {group_name}: {e}")
            await asyncio.sleep(5)

with client:
    client.loop.run_until_complete(main())
