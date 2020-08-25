const socket = io('http://localhost:9000');

socket.on('connect', () => {
  socket.emit('WelcomeFromClient', 'Welcome from client');
  socket.on('WelcomeFromServer',(data) => {
    console.log(data);
  });
});

document.querySelector('#sendMessage').addEventListener('submit', (event) => {
  event.preventDefault();
  let message = document.querySelector('#message').value;
  document.querySelector('#message').value = '';
  //document.querySelector('ul').innerHTML += `<li>${message}</li>`;
  socket.emit('messageFromClient', message);
});

socket.on('messageFromServer',(data) => {
  document.querySelector('ul').innerHTML += `<li>${data}</li>`;
  //socket.close();
});
