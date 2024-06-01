function updateBalance(url) {
  $.ajax({
    url: url,
    type: 'POST',
    data: {},
    success: function(response) {
      $('.p_baza_2').text('Tokens: ' + response.tokens);
    },
    error: function(error) {
      console.error('Failed to update balance:', error);
    }
  });
}

function permission(kol_n,url, fun) {
  $.ajax({
    url: url, // Правильный URL
    type: 'POST',
    data: {'tokens': kol_n},
    success: function(data) {
      console.log('success:', data);
      if (data.permission === true) {
        fun();
      } else if (data.permission === false) {
        alert('no tokens');
      }
    },
    error: function(error) {
      console.error('error:', error);
    }
  });
}

function win_lose(win, kol,url) {
  $.ajax({
    url: url,
    type: 'POST',
    data: {
      'win': win,
      'kol': kol
    },
    error: function(error) {
      console.error('!----!')
      console.error(error)
    }
  });
}

// Объединенная функция для AJAX-запросов
function ajax_request(win, kol,url_win_lose,url_updateBalance) {
  win_lose(win, kol,url_win_lose);
  updateBalance(url_updateBalance);
}