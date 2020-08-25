function joinRoom(roomName){
  nsSocket.on('updateMembers', users => {
    document.querySelector('.curr-room-num-users').innerHTML = users;
  });
  nsSocket.emit('JoiningRoom', roomName);
  document.querySelector('#messages').innerHTML = '';
  nsSocket.on('CatchRoomHistory', history => {
    // console.log(history);
    document.querySelector('#messages').innerHTML = '';
    history.forEach(curr => {
      buildHTML(curr);
    });
  });
  doSearch();
}

function doSearch(){
  document.querySelector('#search-box').addEventListener('input', (event) => {
    // console.log(event.target.value);
    let messages = Array.from(document.getElementsByClassName('message-text'));
    // console.log(messages);
    messages.forEach((msg)=>{
        if(msg.innerText.toLowerCase().indexOf(event.target.value.toLowerCase()) === -1){
            // the msg does not contain the user search term!
            msg.style.display = "none";
        }else{
            msg.style.display = "block"
        }
    })
  });
}
