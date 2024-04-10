function updateBalance(url) {
    $.ajax({
      url: url,
      type: 'POST',
      data: {},
      success: function(response) {
        $('.p_baza_2').text('Tokens: '+ response.tokens);
      },
      error: function(error) {
        console.error('Failed to update balance:', error);
      }
    });
  }