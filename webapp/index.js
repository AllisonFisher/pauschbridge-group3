

function relMouseCoords (event) {
  var totalOffsetX = 0;
  var totalOffsetY = 0;
  var canvasX = 0;
  var canvasY = 0;
  var currentElement = this;

  var width = $(window).height();
  var height = $(window).height();
  do {
    totalOffsetX += currentElement.offsetLeft - currentElement.scrollLeft;
    totalOffsetY += currentElement.offsetTop - currentElement.scrollTop;
  }
  while(currentElement = currentElement.offsetParent)

  canvasX = event.pageX - totalOffsetX - width/2;
  canvasY = height/2 - (event.pageY - totalOffsetY);


  return {x:canvasX, y:canvasY, rX: event.pageX, rY: event.pageY};
}

HTMLCanvasElement.prototype.relMouseCoords = relMouseCoords;

function drawAxis ( canvas ) {
  var ctx = canvas.getContext("2d");
  var width = canvas.width;
  var height = canvas.height;
  
  // axes
  ctx.beginPath();
  ctx.moveTo(0, height/2);
  ctx.lineTo(width, height/2);
  ctx.stroke();

  ctx.beginPath();
  ctx.moveTo(width/2, 0);
  ctx.lineTo(width/2, height);
  ctx.stroke();

}

function paintBlock(canvas, x, y, color) {

  var ctx = canvas.getContext("2d");
  console.log(color);
  ctx.fillStyle = color;
  ctx.fillRect(x - 15, y - 15, 10, 10);
}


$(function () {
  var $canvas = $("#mood-ring");
  var $window = $(window);
  $canvas.attr('width', $window.height()).attr('height', $window.height());
 
  drawAxis($canvas[0]);

  $canvas.on('click', function (event) {
    var data = event.target.relMouseCoords(event);
    x = data.x;
    y = data.y;
    rx = data.rX;
    ry = data.rY;

    console.log(x, y);
    //paintBlock(event);
    size = $(window).height();
    diag = (Math.sqrt(2) * size)/2;
    var color = findColor(x, y, diag);
    r = color.r;
    g = color.g;
    b = color.b;
    console.log(color);
    code = "rgb(" + r + "," + g + "," + b + ")";
    paintBlock($canvas[0], rx, ry, code); 
    
  });

});
