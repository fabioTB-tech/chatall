const bio = document.querySelector('div#bio')
const galeria = document.querySelector('div#galeria')
const link_bio = document.querySelector('button#nav-bio')
const link_galeria = document.querySelector('button#nav-galeria')
const links = document.getElementsByClassName('nav-link')

link_bio.addEventListener('click', event => {
  bio.classList.remove('d-none')
  if (galeria.classList != 'd-none') {
    galeria.classList.add('d-none')
  }
  if (link_bio.classList == 'active') {
    return
  } else {
    link_bio.classList.add('active')
    link_galeria.classList.remove('active')
  }
})

link_galeria.addEventListener('click', event => {
  galeria.classList.remove('d-none')
  if (bio.classList != 'd-none') {
    bio.classList.add('d-none')
  }
  if (link_galeria.classList == 'active') {
    return
  } else {
    link_galeria.classList.add('active')
    link_bio.classList.remove('active')
  }
})