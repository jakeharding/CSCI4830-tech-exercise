$(document).ready(function() {

  changeAnimation();
});

function changeAnimation() {
  var h = $(window).height() - 50;
  var w = $(window).width() - 250;

  var nh = Math.floor(Math.random() * h);
  var nw = Math.floor(Math.random() * w);

  $('div').animate({top: nh, left: nw}, 2000, 'linear',changeAnimation);
}