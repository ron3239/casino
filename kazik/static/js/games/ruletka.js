function rotation() {
  const img = document.querySelector('.img_ruletka');
  const startButton = document.querySelector('.button_rul');
  startButton.style.pointerEvents = 'none';

  deg = Math.floor(5000 + Math.random() * 5000);
  res = deg / 360;

    img.style.transition = 'all 10s ease-out';
    // Rotate the wheel
    img.style.transform = `rotate(${deg}deg)`;

   //10.29
    //5.14
    const cellDegrees = {
      0: [-4.865, 4.865], // 9.73 / 2 = 4.865
      32: [4.865, 14.595],
      15: [14.595, 24.325],
      19: [24.325, 34.055],
      4: [34.055, 43.785],
      21: [43.785, 53.515],
      2: [53.515, 63.245],
      25: [63.245, 72.975],
      17: [72.975, 82.705],
      34: [82.705, 92.435],
      6: [92.435, 102.165],
      27: [102.165, 111.895],
      13: [111.895, 121.625],
      36: [121.625, 131.355],
      11: [131.355, 141.085],
      30: [141.085, 150.815],
      8: [150.815, 160.545],
      23: [160.545, 170.275],
      10: [170.275, 179.975],
      5: [179.975, 189.705],
      24: [189.705, 199.435],
      16: [199.435, 209.165],
      33: [209.165, 218.895],
      1: [218.895, 228.625],
      20: [228.625, 238.355],
      14: [238.355, 248.085],
      31: [248.085, 257.815],
      9: [257.815, 267.545],
      22: [267.545, 277.275],
      18: [277.275, 286.975],
      29: [286.975, 296.705],
      7: [296.705, 306.435],
      28: [306.435, 316.165],
      12: [316.165, 325.895],
      35: [325.895, 335.625],
      3: [335.625, 345.355],
      26: [345.355, 355.085],
    };

  console.error(deg,res);

  setTimeout(() => {
    startButton.style.pointerEvents = 'auto'; // Вернуть возможность нажатия кнопки
    const cellValue = Object.keys(cellDegrees).find(key => {
      const range = cellDegrees[key];
      return res >= range[0] && res < range[1];
    });
    // console.log(Значение ячейки: ${cellValue});
    // console.log(Градусная мера: ${res * 360} градусов);
  }, 10000);
}
