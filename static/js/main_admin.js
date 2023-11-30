const chatRoom = document.querySelector('#room_uuid').textContent.replaceAll('"', '')
console.log('chatRoom:', chatRoom)
let chatSocket = null


const chatLogElement = document.getElementById('chat_log');
const chatInputElement = document.getElementById('chat_message_input');
const chatSubmitElement = document.getElementById('chat_message_submit');


function scrollToBottom(){
    chatLogElement.scrollTop = chatLogElement.scrollHeight
}


function sendMessage() {

    chatSocket.send(JSON.stringify({
        type: 'message',
        message: chatInputElement.value,
        name: document.querySelector('#user_name').textContent.replaceAll('"',''),
        agent: document.querySelector('#user_id').textContent.replaceAll('"',''),
    }));
    chatInputElement.value = '';
    console.log('Successfully send');
}


function onChatMessage(data) {
    console.log('onChatMessage', data);
    if (data.type == 'chat_message') {
        if (!data.agent) {
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


chatSocket = new WebSocket(`ws://${window.location.host}/ws/${chatRoom}/`)

chatSocket.onmessage = function(e){
    console.log('on message')

    onChatMessage(JSON.parse(e.data))

}

chatSocket.onopen = function(e){
    console.log('on open')
    scrollToBottom()
}

chatSocket.onclose = function(e){
    console.log('on close')
}

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