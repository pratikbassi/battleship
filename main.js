let make = require('./makeGrid.js');
let add = require('./makeShip');


const init = function() {
  let grid1 = make.makeGrid(10);
  let grid2 = make.makeGrid(10);

  grid1 = add.makeShip(grid1, [8, 5], [8, 7], 'sub');
  grid1 = add.makeShip(grid1, [4,5], [7,5], 'bat');
  
  console.log(grid1);

  
};

init();