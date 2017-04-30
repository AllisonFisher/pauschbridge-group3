
/* (x, y)
 * (+, +): happy | high energy
 * (+, -): happy | low energy
 * (-, +): sad | high energy
 * (-, -): sad | low energy
*/


function findAngle (x, y) {
  var rad = Math.atan2(y, x);
  if (rad < 0) {
    rad += Math.PI * 2; 
  }
  return {radian: rad} 
}

function findColor (x, y, diag) {
  var intensity = Math.hypot(x, y);
  var radian = findAngle(x, y);
  rad = radian.radian; 
  
  // + +
  if (rad >= 0 && rad < Math.PI/2 ) {
    console.log("green");
    // green
    r = 255 * (1 - intensity/diag);
    b = 255 * (1 - intensity/diag);
    g = 255;
    if (rad >= Math.PI/4) {
      r += (255/4) * (rad-Math.PI/4)/(Math.PI/4);
      g -= (255/4) * (rad-Math.PI/4)/(Math.PI/4);
      
    } 
    else {
      r += (255/4) * (1 - rad/(Math.PI/4));
      b += (255/4) * (1 - rad/(Math.PI/4));
      g -= (255/4) * (1 - rad/(Math.PI/4));
    }
  }
  
  // - +
  else if (rad >= Math.PI/2 && rad < Math.PI ) {
    // red
    console.log("red");
    r = 255;
    g = 255 * (1 - intensity/diag);
    b = 255 * (1 - intensity/diag);
    if (rad <= Math.PI * 3/4) {
      r -= (255/2) * (1 - (rad-Math.PI/2)/(Math.PI/4));
      g += (255/2) * (1 - (rad-Math.PI/2)/(Math.PI/4));
      
    } 
    else {
      r -= (255/2) * (1 - (Math.PI - rad)/(Math.PI/4));
      b += (255/2) * (1 - (Math.PI - rad)/(Math.PI/4));
    }
  }

  // - -
  else if (rad >= Math.PI && rad < Math.PI * 3/2 ) {
    // blue
    console.log("blue");
    r = 255 * (1 - intensity/diag);
    g = 255 * (1 - intensity/diag);
    b = 255;
    if (rad <= Math.PI * 5/4) {
      r += (255/2) * (1 - (rad - Math.PI))/(Math.PI/4);
      b -= (255/2) * (1 - (rad - Math.PI))/(Math.PI/4);
      
    } 
    else {
      r += (255/2) * (rad - Math.PI * 5/4)/(Math.PI/4);
    }
  }
  
  // + + 
  else {
    console.log("pink");
    r = 255;
    g = 255 * (1 - intensity/diag);
    b = 255;
    if (rad >= Math.PI * 7/4) {
      r -= (255/2) * (rad-Math.PI * 7/4)/(Math.PI/4);
      b -= (255/2) * (rad-Math.PI * 7/4)/(Math.PI/4);
      g += (255/2) * (rad-Math.PI * 7/4)/(Math.PI/4);
    } 
    else {
      r -= (255/2) * (1 - (rad - Math.PI * 3/2)/(Math.PI/4));
    }
  }

  r = Math.floor(Math.min(255, r));
  g = Math.floor(Math.min(255, g));
  b = Math.floor(Math.min(255, b));

  return {r : r, g : g, b : b};
}
