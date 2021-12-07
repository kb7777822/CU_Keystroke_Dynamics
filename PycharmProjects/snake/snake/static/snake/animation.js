//const snake1 = {color: 'rgb(255,0,0)', squares:[0,1,2,11]};
//const snake2 = {color: 'rgb(0,0,255)', squares:[79,80]};
//snakes = [snake1, snake2];

function draw(snakes) {
    var canvas = document.getElementById('board');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        ctx.fillStyle = 'rgb(75, 75, 75)';
        ctx.fillRect(0,0,bwidth,bwidth);
        swidth = bwidth/rsquares;

        for (let r = 0; r < bwidth; r += swidth) {
            ctx.fillStyle = 'rgb(150,150,150)';
            for (let c = 0; c < bwidth; c += swidth) {
                ctx.fillRect(r + spacing, c + spacing, swidth - 2*spacing, swidth - 2*spacing);
            }
        }
        for (let i = 0; i < snakes.length; i++) {
            let snake = snakes[i];
            ctx.fillStyle = snake.color;
            for (let j = 0; j < snake.squares.length; j++) {
                let square = snake.squares[j];
                let c = Math.floor(square/rsquares)*swidth;
                let r = (square % rsquares)*swidth;
                ctx.fillRect(r + spacing,c + spacing,swidth - 2*spacing,swidth - 2*spacing);
            }
        }
    }
}

function dummy() {
    snake1.squares.push(12);
}

function listenForKeys() {
    window.onkeydown= function(gfg){
        //alert(gfg.key)
        let request = new XMLHttpRequest()
        request.onreadystatechange = function() {
            if (request.readyState != 4) return
            let response = JSON.parse(request.responseText);
            if (Array.isArray(response)) {
                draw(request)
            } else if (response.hasOwnProperty('error')) {
                displayError(response.error)
            } else {
                displayError(response)
            }
        }
        request.open("POST", 'get-snakes', true)
        request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        request.send("key="+gfg.key+"&csrfmiddlewaretoken="+getCSRFToken())
    }
    getSnakes()
}

function getSnakes() {
    let request = new XMLHttpRequest()
    request.onreadystatechange = function() {
        if (request.readyState != 4) return

        if (request.status != 200) {
            displayError("Received status code = " + request.status)
            return
        }
        let response = JSON.parse(request.responseText)
        if (Array.isArray(response)) {
            draw(response)
        } else if (response.hasOwnProperty('error')) {
            displayError(response.error)
        } else {
            displayError(response)
        }
    }
    request.open("GET", "get-snakes", true)
    request.send()
}

function createSnakes() {
    let request = new XMLHttpRequest();
    request.open("GET", "create-snakes", true)
    request.send()

}

function updateSnakes(snakes){
    for (let i=0; i < snakes.length; i++) {

    }
}

function displayError(message) {
    let errorElement = document.getElementById("error")
    errorElement.innerHTML = message
}

function getCSRFToken() {
    let cookies = document.cookie.split(";")
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim()
        if (c.startsWith("csrftoken=")) {
            return c.substring("csrftoken=".length, c.length)
        }
    }
    return "unknown"
}