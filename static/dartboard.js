const board = document.getElementById("dartboard");

board.addEventListener("click", function(event) {
    const rect = board.getBoundingClientRect();

    const x = event.clientX - rect.left - (board.width/2);
    const y = (event.clientY - rect.top - (board.height/2)) * -1;

    const r = Math.sqrt(x * x + y * y)

    const angle = Math.atan2(y,x) * (180/Math.PI)

    console.log(x, y, r, angle);

    if (r > 190) {
    console.log('miss')
    }
    else if (r <= 190 && r > 180) {
        console.log('double')
    }
    else if (r <= 180 && r > 120) {
        console.log('single')
    }
    else if (r <= 120 && r > 110) {
        console.log('triple')
    }
    else if (r <= 110 && r > 20) {
        console.log('single')
    }
    else if (r <= 20 && r > 8) {
        console.log('bull')
    }
    else {
        console.log('dbull')
    }

});