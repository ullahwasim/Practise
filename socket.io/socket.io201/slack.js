const express = require('express');
const socketio = require('socket.io');
const namespaces = require('./data/namespaces');

let app = express();
app.use(express.static(__dirname + '/public'));

expressServer = app.listen(9000);

let io = socketio(expressServer);

io.on('connect', (socket) => {
  // little authentication // origin header is not included in polling
  if(socket.handshake.headers.origin !== 'http://localhost:9000')
    socket.disconnect(true);
  // console.log(socket.handshake.headers.origin);
  socket.emit('WelcomeFromServer', 'Welcome to /');
  socket.on('WelcomeFromClient', (data) => {
    console.log(data);
  });
  socket.emit('namespaces', namespaces);
});

namespaces.forEach((curr) => {
  io.of(curr.endpoint).on('connect', (socket) => {
    // little authentication // origin header is not included in polling
    if(socket.handshake.headers.origin !== 'http://localhost:9000')
      socket.disconnect(true);
    // console.log(socket.handshake);
    // console.log(socket.handshake.headers.origin);
    socket.emit('WelcomeFromServer', 'Welcome to ' + curr.endpoint);
    socket.on('WelcomeFromClient', (data) => {
      console.log(data);
    });
    socket.on('JoiningRoom', (data) => {
      // console.log(socket.rooms);
      const roomToLeave = Object.keys(socket.rooms)[1];
      // console.log(roomToLeave);
      socket.leave(roomToLeave);
      updateMembers(curr, roomToLeave);
      let roomObject = curr.rooms.find(current => current.roomTitle === data);
      socket.join(data);
      updateMembers(curr, data);
      socket.emit('CatchRoomHistory', roomObject.history);
    });
    socket.on('SendMessageFromClient', (msg) => {
      const room = Object.keys(socket.rooms)[1];
      let roomObject = curr.rooms.find(current => current.roomTitle === room);
      const fullMsg = {
                text: msg,
                time: new Date(new Date().getTime() + 4*60*60*1000).toLocaleTimeString(),
                username: socket.handshake.query.username,
                avatar: 'https://via.placeholder.com/30'
            }
      io.of(curr.endpoint).to(room).emit('SendMessageFromServer', fullMsg);
      roomObject.history.push(fullMsg);
      // socket.to(data).emit('SendMessageFromServer', msg);
    });
  });
});


function updateMembers(curr, data){
  io.of(curr.endpoint).to(data).clients((error,clients)=>{
    // console.log(`There are ${clients.length} in this room`);
    io.of(curr.endpoint).to(data).emit('updateMembers',clients.length)
  })
}

module.exports = {
  io
}
