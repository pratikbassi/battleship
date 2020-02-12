const makeGrid = require('./makeGrid');
const makeShip = require('./makeShip');

const addPlayer = function(playerName){
  let player = {
    playerName: playerName,
    playerGrid: makeGrid(10),
    targetGrid: makeGrid(10),
    toConsole: function(){
      console.log(`${this.playerName}`);
      console.log(`THIS IS THE TARGETING GRID: YOUR SHOTS APPEAR HERE`);
      console.log(this.targetGrid);
      console.log(`--------------------------------------------------`)
      console.log(`THIS IS ${this.playerName}'s GRID: YOUR SHIPS AND THEIR STATUS APPEARS HERE`)
      console.log(this.playerGrid)
      console.log(`--------------------------------------------------`)
    },
    addShips: function(shipObject){
      makeShip(this.playerGrid, shipObject['position1'], shipObject['position2'], shipObject['ship']);
    },
    fireShot: function(){
      
    }
  }
  




  return player;
}



module.exports = addPlayer;