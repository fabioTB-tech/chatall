const chat = document.getElementById('chat')
chat.scrollTop = chat.scrollHeight

const emoji_btn = document.getElementById('btn-emoji')
const msg_input = document.getElementById('msg-input')

async function getEmojis() {
  let emojis = await fetch('https://emojihub.yurace.pro/api/all')
  console.log(emojis)
}

emoji_btn.addEventListener('click', getEmojis)
