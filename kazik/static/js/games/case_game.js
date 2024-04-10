function random_win_lose(max) {
    var number = Math.floor(Math.random() * max);
    const url_dj = "case/win_lose/";
    if (number == 1) {
        $.ajax({
            type: 'POST',
            url: url_dj,
            data: {
                win: true,
                need: 2
            }
        });
    } else {
        $.ajax({
            type: 'POST',
            url: url_dj,
            data: {
                win: false,
                need: 5
            }
        });
    }
}