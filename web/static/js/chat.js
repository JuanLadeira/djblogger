const roomName = JSON.parse(document.getElementById("room-name").textContent);


const chatSocket = new WebSocket(
    'WS://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
); 

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data)
    document.querySelector('#user-hello').innerHTML = (data.tester)
}
