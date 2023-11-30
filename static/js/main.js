const chatElement = document.getElementById('chat');
const chatOpenElement = document.getElementById('chat_open');
const chatJoinElement = document.getElementById('chat_join');
const chatIconElement = document.getElementById('chat_icon');
const chatWelcomeElement = document.getElementById('chat_welcome');
const chatRoomElement = document.getElementById('chat_room');
const chatNameElement = document.getElementById('chat_name');
const chatLogElement = document.getElementById('chat_log');
const chatInputElement = document.getElementById('chat_message_input');
const chatSubmitElement = document.getElementById('chat_message_submit');


let chatName = ''
let chatSocket = null
let chatWindowUrl = window.location.href
let chatRoomUuid = Math.random().toString(36).slice(2,12)


function scrollToBottom(){
    chatLogElement.scrollTop = chatLogElement.scrollHeight
}


function getCookie(name){
    var cookieValue = null

    if (document.cookie && document.cookie != ''){
        var cookies = document.cookie.split(';')

        for(var i = 0; i<cookies.length;i++){
            var cookie = cookies[i].trim()

            if(cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))

                break
            }
        }  
    }

    return cookieValue
}


function sendMessage() {
    if (!chatSocket || !chatInputElement.value || !chatName) {
        console.error('Missing chat socket, message, or name.');
        return;
    }

    console.log('called chatsubmit function');
        chatSocket.send(JSON.stringify({
            type: 'message',
            message: chatInputElement.value,
            name: chatName
        }));
        chatInputElement.value = '';
        console.log('Successfully send');
}



function onChatMessage(data) {
    console.log('onChatMessage', data);
    if (data.type == 'chat_message') {
        if (data.agent) {
            chatLogElement.innerHTML += `
                <div class="flex w-full mt-2 space-x-3 max-w-md">
                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300 text-center pt-2">${data.initials}</div>    
                <div>
                        <div class="bg-gray-300 p-3 rounded-l-lg rounded-br-lg">
                            <p class="text-sm">${data.message}</p>
                        </div>
                        <span class="text-xs text-gray-500 leading-none">${data.created_at} ago</span>
                    </div>
                </div>
            `;
        } else {
            chatLogElement.innerHTML += `
                <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                    <div>
                        <div class="bg-blue-300 p-3 rounded-l-lg rounded-br-lg">
                            <p class="text-sm">${data.message}</p>
                        </div>
                        <span class="text-xs text-gray-500 leading-none">${data.created_at} ago</span>
                    </div>
                    <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300 text-center pt-2">${data.initials}</div>
                </div>
            `;
        }
    }

    scrollToBottom()
}



async function joinChatRoom(){
    console.log('joinedChatRoom')

    chatName = chatNameElement.value

    console.log('Now getting chatName', chatName)

    const data = new FormData()
    data.append('name', chatName)
    data.append('url', chatWindowUrl)

    await fetch(`/api/create-room/${chatRoomUuid}/`,{
        method: 'POST',
        headers:{
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: data
    })
    .then(function(res){
        return res.json()
    })
    .then(function(data){
        console.log('data',data)
    })



    chatSocket = new WebSocket(`ws://${window.location.host}/ws/${chatRoomUuid}/`)


    chatSocket.onmessage = function(e){
        const receivedData = JSON.parse(e.data);
        onChatMessage(JSON.parse(e.data))
    }

    chatSocket.onopen = function(e){
        console.log('onOpen - chat socket was opened');
        scrollToBottom()
    }


    chatSocket.onerror = function(error){
        console.error('WebSocket Error:', error);
    }

    chatSocket.onclose = function(e){
        console.log('onClose - chat socket was closed');
    }
}


chatOpenElement.addEventListener('click', function(e) {
    e.preventDefault();
    chatIconElement.classList.add('hidden');
    chatWelcomeElement.classList.remove('hidden');
    return false;
});

chatJoinElement.addEventListener('click', function(e) {
    e.preventDefault();
    chatWelcomeElement.classList.add('hidden');
    chatRoomElement.classList.remove('hidden');
    

    console.log('test')

    joinChatRoom();
    
    
    return false;
});

chatSubmitElement.addEventListener('click', function(e){
    e.preventDefault();

    console.log('called chatsubmit')
    sendMessage();
});


chatInputElement.onkeyup = function(e){
    if (e.keyCode == 13){
        sendMessage();
    }
}
