const diff_1 = document.getElementById('diff_1')
const diff_2 = document.getElementById('diff_2')
const diff_3 = document.getElementById('diff_3')
const new_game_submit_button = document.getElementById('new_game_submit_button')
let selected_diff = 0

diff_1.addEventListener("click", function(event) {
    
    diff_1.classList.replace('unselected','selected')
    diff_2.classList.replace('selected','unselected')
    diff_3.classList.replace('selected','unselected')
    selected_diff = 1

});

diff_2.addEventListener("click", function(event) {
    
    diff_2.classList.replace('unselected','selected')
    diff_1.classList.replace('selected','unselected')
    diff_3.classList.replace('selected','unselected')
    selected_diff = 2

});

diff_3.addEventListener("click", function(event) {
    
    diff_3.classList.replace('unselected','selected')
    diff_2.classList.replace('selected','unselected')
    diff_1.classList.replace('selected','unselected')
    selected_diff = 3

});

new_game_submit_button.addEventListener("click", function(event) {

    if (selected_diff === 0) {
        return
    }

});