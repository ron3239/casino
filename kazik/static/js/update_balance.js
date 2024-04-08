function updateBalance(url,csrf_token) {
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrf_token
        },
        success: function(response) {
            $('.p_baza_2').text('Tokens: '+ response.tokens);
        },
        error: function(error) {
            console.error('Failed to update balance:', error);
        }
    });
}
