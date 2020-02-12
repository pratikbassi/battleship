const assignShip = function(boat) {

  console.log(`BOAT ${boat}`);

  let shipDes = '';
  let shipType = 0;

  if (boat === 'sub') {
    shipDes = 'S';
    shipType = 3;
  } else if (boat === 'des') {
    shipDes = 'D';
    shipType = 2;
  } else if (boat === 'cru') {
    shipDes = 'R';
    shipType = 3;
  } else if (boat === 'bat') {
    shipType = 4;
    shipDes = 'B';
  } else if (boat === 'car') {
    shipType = 5;
    shipDes = 'C';
  } else {
    throw new Error(`INVALID SHIP NAME ${boat}`);
  }

  return [shipDes, shipType];
};

module.exports = assignShip;