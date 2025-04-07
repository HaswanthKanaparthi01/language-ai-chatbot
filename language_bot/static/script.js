async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = input.value.trim();
  
    if (!message) return;
  
    // Show user message
    const userMsg = document.createElement('p');
    userMsg.innerHTML = `<strong>You:</strong> ${message}`;
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  
    // Clear input
    input.value = '';
  
    // Get bot reply
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
  
    const data = await res.json();
  
    const botMsg = document.createElement('div');
botMsg.classList.add('bot-message');
botMsg.innerHTML = `<strong>Bot:</strong><div class="bot-content">${data.reply}</div>`;
chatBox.appendChild(botMsg);

  }
  
 
  