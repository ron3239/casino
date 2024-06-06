// function card_check() {
//     const front = document.querySelector('.front');
//     const back = document.querySelector('.back');
//     let status = front.style.transform === 'perspective(600px) rotateY(-180deg)';
  
//     if (status) {
        
//       front.style.transition = 'transform 2s ease-out';
//       front.style.transform = 'perspective(600px) rotateY(0deg)';
//       back.style.transition = 'transform 2s ease-out';
//       back.style.transform = 'perspective(600px) rotateY(180deg)';
//     } else {
//       front.style.transition = 'transform 2s ease-out';
//       front.style.transform = 'perspective(600px) rotateY(-180deg)';
//       back.style.transition = 'transform 2s ease-out';
//       back.style.transform = 'perspective(600px) rotateY(0deg)';
//     }
//   }
  
        // for(let i=0;i<front.lenght;i++){
        //     front[i].style.transition = 'all 2s ease-out';
        //     front[i].style.transform = 'rotateY(-180deg)';
        // }
        // for(let i=0;i<front.lenght;i++){
        //     back[i].style.transition = 'all 2s ease-out';
        //     back[i].style.transform = 'rotateY(-180deg)';
        // }


// function card_check() {
//     const front = document.querySelector('.front');
//     const back = document.querySelector('.back');
//     let status = front.style.transform === 'perspective(600px) rotateY(-180deg)';
    
//     if (status) {
//         for(let i=0;i<front.lenght;i++){
//             front[i].style.transition = 'transform 2s ease-out';
//             front[i].style.transform = 'perspective(600px) rotateY(0deg)';
//             back[i].style.transition = 'transform 2s ease-out';
//             back[i].style.transform = 'perspective(600px) rotateY(180deg)';
//         }

//     } else {
//         for(let i=0;i<front.lenght;i++){
//             front[i].style.transition = 'transform 2s ease-out';
//             front[i].style.transform = 'perspective(600px) rotateY(-180deg)';
//             back[i].style.transition = 'transform 2s ease-out';
//             back[i].style.transform = 'perspective(600px) rotateY(0deg)';
//         }

//     }
//     }

function card_check() {
    const fronts = document.querySelectorAll('.front');
    const backs = document.querySelectorAll('.back');

    for (let i = 0; i < fronts.length; i++) {
        let front = fronts[i];
        let back = backs[i];

        let status = front.style.transform === 'perspective(600px) rotateY(-180deg)';

        if (status) {
            front.style.transition = 'transform 2s ease-out';
            front.style.transform = 'perspective(600px) rotateY(0deg)';
            back.style.transition = 'transform 2s ease-out';
            back.style.transform = 'perspective(600px) rotateY(180deg)';
        } else {
            front.style.transition = 'transform 2s ease-out';
            front.style.transform = 'perspective(600px) rotateY(-180deg)';
            back.style.transition = 'transform 2s ease-out';
            back.style.transform = 'perspective(600px) rotateY(0deg)';
        }
    }
}

          
