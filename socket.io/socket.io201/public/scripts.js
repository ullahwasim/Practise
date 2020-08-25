let username = prompt('Enter your username');
const socket = io('http://localhost:9000', {
  transports: ['websocket']
});

let ns, nsSocket;
// Join '/' Ns
socket.on('connect', () => {
  socket.emit('WelcomeFromClient', `Welcome from ${socket.id} Client`);
  socket.on('WelcomeFromServer', (data) => {
    console.log(data);
  });
  socket.on('namespaces', (namespaces) => {
    ns = namespaces;
    namespaces.forEach((curr, index, arr) => {
      document.querySelector('.col-sm-1').innerHTML += `<div class="namespace" ns="${curr.endpoint}"><img src="${curr.img}"></div>`;
    });
    Array.from(document.querySelectorAll('.namespace')).forEach((current) => {
      current.addEventListener('click', showRooms);
    });
    socket.close();
    joinNs(namespaces[0].endpoint);
  });
});


function buildHTML(fullMsg){
  const html = `
  <li>
      <div class="user-image">
          <img src="${fullMsg.avatar}" />
      </div>
      <div class="user-message">
          <div class="user-name-time">${fullMsg.username} <span>${fullMsg.time}</span></div>
          <div class="message-text">${fullMsg.text}</div>
      </div>
  </li>`;
  document.querySelector('#messages').innerHTML += html;
}
