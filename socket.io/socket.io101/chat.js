const express =  require('express');
const socketio = require('socket.io');
app = express();

app.use(express.static(__dirname + '/public'));

expressServer = app.listen(9000);

let io = socketio(expressServer);

io.on('connect', (socket) => {
  socket.emit('WelcomeFromServer', 'Welcome from server');
  socket.on('WelcomeFromClient',(data) => {
    console.log(data);
  });
  socket.on('messageFromClient',(data) => {
    io.emit('messageFromServer', data);
    //socket.disconnect(true);
  });
});
