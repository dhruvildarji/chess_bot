function updateBoard(svg) {
    $('#chessboard').html(svg); // Update the board SVG
}

function updateMessage(message) {
    $('#gameMessage').html(message); // Update the message text
}


function submitMove() {
    const move = $('#move').val(); // Get the user move
    $.ajax({
        url: '/make_move',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({move: move}),
        success: function(response) {
            if(response.success) {
                updateBoard(response.board_svg); // Update the board SVG
                updateMessage(response.message); // Update the game message
            } else {
                alert('Error: ' + response.error); // Show error
            }
        }
    });
}

$(document).ready(function() {
    // Fetch and display the initial board state
    $.get('/initial_board', function(response) {
        updateBoard(response.board_svg);
        updateMessage(response.message); // Display the initial message
    });
});
