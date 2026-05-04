
const emoji_btn = document.getElementById('btn-emoji')
const emoji_display = document.getElementById('emoji-display')
const emoji_container = document.getElementById('emoji-container')
const msg_input = document.getElementById('msg-input')
const categories = document.querySelectorAll('categories')

document.addEventListener('DOMContentLoaded', () => {
  msg_input.focus()
})


document.addEventListener('click', event => {
  const list = document.getElementById('c-list')
  if (emoji_container.classList.contains('active-emoji')) {
    if (event.target == document.getElementsByTagName('main')[0]) {
      emoji_container.classList.remove('active-emoji')
    }
  }
})

async function emojiCategorie(c) {
  const emojisCategories = await fetch('https://emojihub.yurace.pro/api/categories')
  const emojisCategoriesJson = await emojisCategories.json()
  return emojisCategoriesJson
}


async function getEmoji() {
  emoji_container.classList.toggle('active-emoji')
  try {
    const emojisObj = await fetch('https://emojihub.yurace.pro/api/all')
    emojisCarregados = await emojisObj.json()

    const emojisSelecionados = emojisCarregados

    console.log(emojisCarregados)

    emoji_display.innerHTML = emojisSelecionados.map(emoji =>
      `
      <div class="emoji fs-5" onclick="adicionarEmoji('${emoji.htmlCode[0]}')">
      ${emoji.htmlCode[0]}
      </div>
      `
    ).join('')
  } catch (erro) {
    console.error('Erro ao carregar emojis: ', erro)
    emoji_display.innerHTML = '<p>Erro ao carregar emojis</p>'
  }
}

function adicionarEmoji(emoji) {
  msg_input.value += emoji
}

emoji_btn.addEventListener('click', getEmoji)

const chat = document.getElementById('chat')
document.addEventListener('DOMContentLoaded', () => {
    chat.scrollTop = chat.scrollHeight
})
