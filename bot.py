import telebot
import requests

# Your Configuration
API_TOKEN = '8989934132:AAHFRHQu7pSbRhVSx6ULCi4lzOarbB3ViuI'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['like'])
def handle_like(message):
    # Split the command (e.g., /like ind 5513136279)
    args = message.text.split()
    
    if len(args) < 3:
        bot.reply_to(message, "❌ **Usage:** `/like {region} {uid}`\nExample: `/like ind 5513136279`", parse_mode='Markdown')
        return

    region = args[1]
    uid = args[2]
    
    # Notify user processing
    sent_msg = bot.reply_to(message, "⏳ *Processing your request...*", parse_mode='Markdown')

    # API Call
    api_url = f"https://najmi-ob54-like.vercel.app/like?uid={uid}&server_name={region}&key=NJM"
    
    try:
        response = requests.get(api_url)
        data = response.json()

        # Mapping the API response to your template
        name = data.get('PlayerNickname', 'N/A')
        likes_before = data.get('LikesbeforeCommand', '0')
        likes_given = data.get('LikesGivenByAPI', '0')
        likes_after = data.get('LikesafterCommand', '0')
        remaining = data.get('remains', 'N/A')

        template = (
╔════════════════════════════════════════════════════╗
║            ⚡ 𝗫𝗧𝗢𝗫𝗜𝗖 • 𝗟𝗜𝗞𝗘 𝗦𝗬𝗦𝗧𝗘𝗠 ⚡            ║
╠════════════════════════════════════════════════════╣
║              🎉 𝗟𝗜𝗞𝗘 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 🎉               ║
╚════════════════════════════════════════════════════╝

👑 𝗣𝗟𝗔𝗬𝗘𝗥 𝗜𝗡𝗙𝗢
╭──────────────────────────────────────────────────╮
│ 👤 Name        : {name}                          │
│ 🆔 UID         : {uid}                           │
│ 🌍 Region      : {region.upper()}                │
╰──────────────────────────────────────────────────╯

❤️ 𝗟𝗜𝗞𝗘 𝗦𝗧𝗔𝗧𝗦
╭──────────────────────────────────────────────────╮
│ ❤️ Before      : {likes_before}                  │
│ 💙 Added       : +{likes_given}                  │
│ 💚 After       : {likes_after}                   │
╰──────────────────────────────────────────────────╯

📊 Remaining Requests : {remaining}

════════════════════════════════════════════════════

⚡ Status   : ✓ VERIFIED
🔐 Security : ENCRYPTED
⏰ Time     : {time}

════════════════════════════════════════════════════

👨‍💻 Developer : XTOXIC
📢 Telegram  : t.me/XTOXIC_GOD

╔════════════════════════════════════════════════════╗
║         ★ THANK YOU FOR USING XTOXIC ★           ║
╚════════════════════════════════════════════════════╝
        )
        
        bot.edit_message_text(template, chat_id=message.chat.id, message_id=sent_msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ **Error Connection to API**\n`{str(e)}`", 
                              chat_id=message.chat.id, message_id=sent_msg.message_id, parse_mode='Markdown')

if __name__ == "__main__":
    print("Bot is now online...")
    bot.infinity_polling()
