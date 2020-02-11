const assign = require('./assignShip.js');


const makeShip = function(ocean, position1, position2, shipName) {

  let delta = (Math.abs(position1[0] - position2[0]) + Math.abs(position1[1] - position2[1]));
  
  let shipDes = assign.assignShip(shipName)[0];
  let shipType = assign.assignShip(shipName)[1];


  if (position1[0] < 10 && position1[1] < 10 && position2[0] < 10 && position2[1] < 10 && delta + 1 === shipType) {
    if (position1[0] === position2 [0]) {
      ocean[position1[0]].fill(shipDes, position1[1], position2[1] + 1);
    } else if (position2[1] === position1[1]) {
      let i = 0;
      while (i < delta + 1) {
        ocean[position1[0] + i][position1[1]] = shipDes;
        i++;
      }
    }
  } else {
    throw new Error(`INVALID POSITION FOR SHIP: ${position1}  ${position2}`);
  }


  return ocean;
};





module.exports = makeShip;
