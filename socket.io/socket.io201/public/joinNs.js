let showRooms = function(event){
  const nsEndpoint = event.currentTarget.getAttribute('ns');
  nsSocket.close();
  joinNs(nsEndpoint);
}


function joinNs(endpoint){
  // Array.from(document.querySelectorAll('.namespace')).forEach((current) => {
  //   current.removeEventListener('click', showRooms);
  // });
  // if(typeof nsSocket !== 'undefined')
  //   nsSocket.close();
  nsSocket = io(`http://localhost:9000${endpoint}`, {
    // transports: ['polling'],
    transports: ['websocket'],
    query: {
        username
    }
  });
  nsSocket.on('connect', () => {
    nsSocket.emit('WelcomeFromClient', `Welcome from ${socket.id} Client`);
    nsSocket.on('WelcomeFromServer', (data) => {
      console.log(data);
    });
    const namespace = ns.find(curr => curr.endpoint === endpoint);
    document.querySelector('.room-list').innerHTML = '';
    namespace.rooms.forEach((curr, index, arr) => {
      let roomVisibility = !curr.privateRoom ? 'glyphicon-globe' : 'glyphicon-lock';
      document.querySelector('.room-list').innerHTML += `<li onclick="joinRoom('${curr.roomTitle}')"><span class="glyphicon ${roomVisibility}"></span>${curr.roomTitle}</li>`;
    });
    joinRoom(namespace.rooms[0].roomTitle);
    // document.querySelector('#user-input').removeEventListener('submit', userInput);
    document.querySelector('#user-input').addEventListener('submit', userInput);
    nsSocket.on('SendMessageFromServer', fullMsg => {
      // console.log(msg);
      buildHTML(fullMsg);
    });
  });
}

let userInput = event => {
  event.preventDefault();
  let enteredValue = document.querySelector('#user-message').value;
  nsSocket.emit('SendMessageFromClient', enteredValue);
  document.querySelector('#user-message').value = '';
}
