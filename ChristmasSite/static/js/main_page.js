function userSelect(e) {
    var userInfo = sessionStorage.getItem('userInfo');
    var userSelect = document.getElementById('userSelect').value;
    var textBox = document.getElementById('christmasRequest');
    if (userInfo !== "" && userInfo != null) {
        userInfo = JSON.parse(userInfo);
        if (userSelect in userInfo) {
            textBox.value = userInfo[userSelect];
        } else {
            textBox.value = '';
        }
    } else {
        userInfo = {};
        userInfo[userSelect] = '';
        sessionStorage.setItem('userInfo', JSON.stringify(userInfo));
        textBox.value = '';
    }
}

function buttonClick(e) {
    var textValue = document.getElementById('christmasRequest').value;
    var userSelect = document.getElementById('userSelect').value;
    var userInfo = sessionStorage.getItem('userInfo');
    if (userInfo !== "" && userInfo != null) {
        userInfo = JSON.parse(userInfo);
    } else {
        userInfo = {};
    }
    userInfo[userSelect] = textValue;
    sessionStorage.setItem('userInfo', JSON.stringify(userInfo));
}

function clearStorage() {
    sessionStorage.removeItem('userInfo');
}

document.getElementById('submitRequest')
        .addEventListener("click", buttonClick, false);

document.getElementById('userSelect')
        .addEventListener("change", userSelect, false);

document.onload = clearStorage();
