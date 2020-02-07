const addSubmarine = exports.addSubmarine = function (ocean, position1, position2) {
  let delta = (Math.abs(position1[0] - position1[1]) + Math.abs(position2[0] - position2[1]));


  if(position[0] < 10 && position[1] < 10 && position2[0] < 10 && position2[1] < 10 && delta === 2){
    let i = 0;
    if(position1[0] === position2 [0]){
      ocean[position1[0]].fill('S', position1[1], position2[1]);
    } else if(position2[1] === position1[1]){

    }
  } else {
    throw new Error(`INVALID POSITION: ${position}`);
  }


  return ocean;
}


addSubmarine(undefined, [11, 5]);




