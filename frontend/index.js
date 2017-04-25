function relMouseCoords (event) {
  var totalOffsetX = 0;
  var totalOffsetY = 0;
  var canvasX = 0;
  var canvasY = 0;
  var currentElement = this;

  var width = $(window).width();
  var height = $(window).height();
  do {
    totalOffsetX += currentElement.offsetLeft - currentElement.scrollLeft;
    totalOffsetY += currentElement.offsetTop - currentElement.scrollTop;
  }
  while(currentElement = currentElement.offsetParent)

  canvasX = event.pageX - totalOffsetX - width/2;
  canvasY = height/2 - (event.pageY - totalOffsetY);


  return {x:canvasX, y:canvasY}
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

function paintBlock( event ) {
  var x = event.pageX;
  var y = event.pageY;
}


$(function () {
  var $canvas = $("#mood-ring");
  var $window = $(window);
  $canvas.attr('width', $window.width()).attr('height', $window.height());
 
  drawAxis($canvas[0]);

  $canvas.on('click', function (event) {
    console.log(event.target.relMouseCoords(event));
    paintBlock(event);

  });


});
