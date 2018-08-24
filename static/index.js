var socket = io();

show_login_button = document.getElementById('show_login_button');
login_div = document.getElementById('login_div');
username = document.getElementById('userbox');
password = document.getElementById('pwdbox');

function show_login() {
  show_login_button.style.opacity = 0;
  login_div.style.opacity = 1;
}

function login() {
  console.log('logging in...');
  socket.emit('auth', [username.value, password.value]);
}

socket.on('a-ok', function(){
  console.log('a-ok recieved');
});
