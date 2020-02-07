const makegrid = exports.makeGrid = function(size) {
  let returnArray = [];

  for(let i = 0; i < size; i++){
    let pushArray = []
    for(let j = 0; j < size; j++){
      pushArray.push(' ');
    }

    returnArray.push(pushArray);
  }


  return returnArray;
}

