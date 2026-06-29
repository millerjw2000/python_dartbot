function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function hideMessages() {
    for (let i = 1; i <= 3; i++) {
        const msg = document.getElementById(`message_${i}`);
        msg.textContent = "";
        msg.classList.replace("visible_delayed", "hidden");
    }
}

async function showMessage(index, text) {
    const msg = document.getElementById(`message_${index}`);
    msg.textContent = text;
    msg.classList.replace("hidden", "visible_delayed");
    await sleep(1000);
}

function renderBoard(gameState) {

    //document.getElementById('player_1_num_20s').textContent = gameState.player_1_board["20"][0]

    if (gameState.player_1_board["20"][0] >= 1) {
        document.getElementById('player_1_20s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["20"][0] >= 2) {
        document.getElementById('player_1_20s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["20"][0] >= 3) {
        document.getElementById('player_1_20s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["19"][0] >= 1) {
        document.getElementById('player_1_19s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["19"][0] >= 2) {
        document.getElementById('player_1_19s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["19"][0] >= 3) {
        document.getElementById('player_1_19s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["18"][0] >= 1) {
        document.getElementById('player_1_18s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["18"][0] >= 2) {
        document.getElementById('player_1_18s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["18"][0] >= 3) {
        document.getElementById('player_1_18s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["17"][0] >= 1) {
        document.getElementById('player_1_17s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["17"][0] >= 2) {
        document.getElementById('player_1_17s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["17"][0] >= 3) {
        document.getElementById('player_1_17s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["16"][0] >= 1) {
        document.getElementById('player_1_16s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["16"][0] >= 2) {
        document.getElementById('player_1_16s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["16"][0] >= 3) {
        document.getElementById('player_1_16s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["15"][0] >= 1) {
        document.getElementById('player_1_15s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["15"][0] >= 2) {
        document.getElementById('player_1_15s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["15"][0] >= 3) {
        document.getElementById('player_1_15s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_1_board["BULL"][0] >= 1) {
        document.getElementById('player_1_bulls_1').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["BULL"][0] >= 2) {
        document.getElementById('player_1_bulls_2').classList.replace('unselected','selected')
    }
    if (gameState.player_1_board["BULL"][0] >= 3) {
        document.getElementById('player_1_bulls_3').classList.replace('unselected','selected')
    }
    document.getElementById('player_1_score').textContent = gameState.player_1_score

    if (gameState.player_2_board["20"][0] >= 1) {
        document.getElementById('player_2_20s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["20"][0] >= 2) {
        document.getElementById('player_2_20s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["20"][0] >= 3) {
        document.getElementById('player_2_20s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["19"][0] >= 1) {
        document.getElementById('player_2_19s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["19"][0] >= 2) {
        document.getElementById('player_2_19s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["19"][0] >= 3) {
        document.getElementById('player_2_19s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["18"][0] >= 1) {
        document.getElementById('player_2_18s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["18"][0] >= 2) {
        document.getElementById('player_2_18s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["18"][0] >= 3) {
        document.getElementById('player_2_18s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["17"][0] >= 1) {
        document.getElementById('player_2_17s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["17"][0] >= 2) {
        document.getElementById('player_2_17s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["17"][0] >= 3) {
        document.getElementById('player_2_17s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["16"][0] >= 1) {
        document.getElementById('player_2_16s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["16"][0] >= 2) {
        document.getElementById('player_2_16s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["16"][0] >= 3) {
        document.getElementById('player_2_16s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["15"][0] >= 1) {
        document.getElementById('player_2_15s_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["15"][0] >= 2) {
        document.getElementById('player_2_15s_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["15"][0] >= 3) {
        document.getElementById('player_2_15s_3').classList.replace('unselected','selected')
    }

    if (gameState.player_2_board["BULL"][0] >= 1) {
        document.getElementById('player_2_bulls_1').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["BULL"][0] >= 2) {
        document.getElementById('player_2_bulls_2').classList.replace('unselected','selected')
    }
    if (gameState.player_2_board["BULL"][0] >= 3) {
        document.getElementById('player_2_bulls_3').classList.replace('unselected','selected')
    }
    document.getElementById('player_2_score').textContent = gameState.player_2_score

}

document.addEventListener("DOMContentLoaded", async function () {

    const response = await fetch("/update_game");

    const gameState = await response.json();

    console.log(gameState);
    renderBoard(gameState)

});

const board = document.getElementById("dartboard");

let throws = []

function renderEntries() {
    document.getElementById('dart1').textContent = throws[0] || ''
    document.getElementById('dart2').textContent = throws[1] || ''
    document.getElementById('dart3').textContent = throws[2] || ''
}

function getArea(r, angle) {
    
    let string = ''

    if (angle < 0) {
        angle = 360 - (-1 * angle)
    }

    if (r > 190) {
        return '0'
    }
    else if (r <= 190 && r > 180) {
        string = string.concat('D')
    }
    else if (r <= 180 && r > 120) {
        
    }
    else if (r <= 120 && r > 110) {
        string = string.concat('T')
    }
    else if (r <= 110 && r > 20) {
        
    }
    else if (r <= 20 && r > 8) {
        return 'BULL'
    }
    else {
        return 'DBULL'
    }

    if (angle >= 81 && angle < 99) {
        string = string.concat('20')
    }
    else if (angle >= 99 && angle < 117) {
        string = string.concat('5')
    }
    else if (angle >= 117 && angle < 135) {
        string = string.concat('12')
    }
    else if (angle >= 135 && angle < 153) {
        string = string.concat('9')
    }
    else if (angle >= 153 && angle < 171) {
        string = string.concat('14')
    }
    else if (angle >= 171 && angle < 189) {
        string = string.concat('11')
    }
    else if (angle >= 189 && angle < 207) {
        string = string.concat('8')
    }
    else if (angle >= 207 && angle < 225) {
        string = string.concat('16')
    }
    else if (angle >= 225 && angle < 243) {
        string = string.concat('7')
    }
    else if (angle >= 243 && angle < 261) {
        string = string.concat('19')
    }
    else if (angle >= 261 && angle < 279) {
        string = string.concat('3')
    }
    else if (angle >= 279 && angle < 297) {
        string = string.concat('17')
    }
    else if (angle >= 297 && angle < 315) {
        string = string.concat('2')
    }
    else if (angle >= 315 && angle < 333) {
        string = string.concat('15')
    }
    else if (angle >= 333 && angle < 351) {
        string = string.concat('10')
    }
    else if ((angle >= 351 && angle < 360) || (angle >= 0 && angle < 9)) {
        string = string.concat('6')
    }
    else if (angle >= 9 && angle < 27) {
        string = string.concat('13')
    }
    else if (angle >= 27 && angle < 45) {
        string = string.concat('4')
    }
    else if (angle >= 45 && angle < 63) {
        string = string.concat('18')
    }
    else if (angle >= 63 && angle < 81) {
        string = string.concat('1')
    }

    return string

}

board.addEventListener("click", function(event) {
    const rect = board.getBoundingClientRect();

    const x = event.clientX - rect.left - (board.width/2);
    const y = (event.clientY - rect.top - (board.height/2)) * -1;

    const r = Math.sqrt(x * x + y * y)

    const angle = Math.atan2(y,x) * (180/Math.PI)

    let loc = getArea(r,angle)

    if (throws.length < 3) {
        throws.push(loc);
        renderEntries();
    }

    console.log(loc)

});

document.getElementById("undo").onclick = function () {

    throws.pop();

    renderEntries();

}

document.getElementById("submit").addEventListener("click", async () => {
    
    const response = await fetch("/update_game", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            throws: throws
        })
    });

    const gameState = await response.json();

    console.log(gameState)

    renderBoard(gameState);

    throws = [];
    renderEntries();

    hideMessages();

    // Player wins immediately
    if (gameState.winner === 1) {
        //await showMessage(1, "Player 1 has won!");
        document.getElementById('message_1').textContent = 'Player 1 has won!'
        document.getElementById('message_1').classList.replace("hidden", "visible_delayed");
        document.getElementById('message_1').classList.add('announcement')
        return;
    }

    // Bot turn narration
    await sleep(1000)
    for (let i = 0; i < gameState.bot_history.length; i++) {
        await showMessage(i + 1, gameState.bot_history[i]);
    }

    // Bot wins after its turn
    if (gameState.winner === 2) {
        await sleep(1000);

        hideMessages();

        document.getElementById('message_1').textContent = 'Player 2 has won!'
        document.getElementById('message_1').classList.replace("hidden", "visible_delayed");
        document.getElementById('message_1').classList.add('announcement')
    }

});



