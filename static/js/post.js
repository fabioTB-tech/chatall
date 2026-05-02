document.addEventListener('click', async (event) => {
    const button = event.target.closest('.like-button');
    if (!button) return;
    const url = button.dataset.url;

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
          'Content-Type': 'application/json',
        },
        credentials: 'same-origin',
      });

      if (!response.ok) return;

      const data = await response.json();
      button.querySelector('i').classList.toggle('fa-regular', !data.liked);
      button.querySelector('i').classList.toggle('fa-solid', data.liked);
      button.querySelector('span').textContent = data.likes_count;
      
    } catch (error) {
      console.error('Error liking post:', error);
  }
});