
const addPlayer = require('./addPlayer');


const init = function() {

  let shipObject1 = {
    ship: 'bat', 
    position1: [2,3],
    position2: [2,6]
  }
  let shipObject2 = {
    ship: 'car',
    position1: [4,3],
    position2: [4,7]
  }
  let shipObject3 = {
    ship: 'des',
    position1: [6,3],
    position2: [6,4]
  }
  let shipObject4 = {
    ship: 'sub',
    position1: [8,3],
    position2: [8,5]
  }
  let shipObject5 = {
    ship: 'cru',
    position1: [0,3],
    position2: [0,5]
  }

  
  let player1 = addPlayer('Pratik')
  player1.addShips(shipObject1);
  player1.addShips(shipObject2);
  player1.addShips(shipObject3);
  player1.addShips(shipObject4);
  player1.addShips(shipObject5);
  player1.toConsole();
  
};

init();