const makeGrid = require('./makeGrid');
const makeShip = require('./makeShip');
const shipPlacer = require('./shipPlacer')

const addPlayer = function(){
  let player = {
    playerName: '',
    playerGrid,
    targetGrid: makeGrid(10),
    toConsole: function(){
      console.log(`${this.playerName}`);
      console.log(`THIS IS THE TARGETING GRID: YOUR SHOTS APPEAR HERE`);
      console.log(`${this.targetGrid}`);
      console.log(`--------------------------------------------------`)
      console.log(`THIS IS ${this.playerName}'s GRID: YOUR SHIPS AND THEIR STATUS APPEARS HERE`)
      console.log(`${this.playerGrid}`)
      console.log(`--------------------------------------------------`)
    },
    addShips: function(shipObject){

    }
  }
  




  return player;
}



module.exports = addPlayer;