//whenever we load the page, always display the first slide
var currentSlide = 0

//here we set how many slides we have using the .length property
//this is useful because we can use it as our max slide value
var totalSlides = $('.holder section').length


// 1. a function that deals with taking us to the next slide
var nextSlide = function(){
// increment our currentSlide value by reassigning it and increlenting 	   it by 1
  currentSlide = currentSlide + 1

  //a continuacion ponemos este codigo para que nuestras slides y numeros no sigan avanzando cuando lleguen a la 4ta
  //
  if(currentSlide >= totalSlides){
    currentSlide = 0
  }
// we are going to turn our currentSlide value into a negative vw unit
  var leftPosition = (-currentSlide * 100)  + 'vw'
// here we add the 'vw' unit into the end

// pass the vw unit into our css method below
//here we grab the holder and change it to the second slide
  $('.holder').css('left', leftPosition)

var slideNumber = currentSlide + 1
// here we set the text for the steps using currentSlide and total nubmer
$('.steps').text(slideNumber + ' / ' + totalSlides)
}

//2. a function that deals with taking us to the previous slide

var previousSlide = function(){
 //this is identical to our nextSlide function, apart from that we are decrementing the currentSlide value (taking us back rather than fowards)
  currentSlide = currentSlide - 1

 //a continuacion ponemos este codigo para que nuestras slides y numeros no sigan retrocediendo cuando lleguen al 0
 //
 if(currentSlide < 0){
    currentSlide = totalSlides - 1
 }

  var leftPosition = (-currentSlide * 100)  + 'vw'
  $('.holder').css('left', leftPosition)

var slideNumber = currentSlide + 1
// here we set the text for the steps using currentSlide and total nubmer
$('.steps').text(slideNumber + ' / ' + totalSlides)
}

//setInterval allows us to run a function every x amount of time
var autoSlide = setInterval(function(){
// here our nextSlide function will be run
nextSlide()
// runs every 3seconds (3000ms)
}, 3000)

//we also have setTimeout, wich is the same, but runs only once

$('.next').on('click', function(){
  //this is going to cancel our autoSlide interval function
  //as the user has taken over control of the slideshow
  clearInterval(autoSlide)
  // here we call the nextSlide function and fo to the next slide
  nextSlide()
})


$('.prev').on('click', function(){
  clearInterval(autoSlide)
  previousSlide()
})

$('body').on('keydown', function(event){
  var keyCode = event.keyCode
  if(keyCode ==37){
    clearInterval(autoSlide)
    previousSlide()
  }
   if(keyCode ==39){
    clearInterval(autoSlide)
    nextSlide()
   }
})








$(function(){
  // vars for testimonials carousel
  var $txtcarousel = $('#testimonial-list');
  var txtcount = $txtcarousel.children().length;
  var wrapwidth = (txtcount * 415) + 415; // 400px width for each testimonial item
  $txtcarousel.css('width',wrapwidth);
  var animtime = 750; // milliseconds for clients carousel
 
  // prev & next btns for testimonials
  $('#prv-testimonial').on('click', function(){
    var $last = $('#testimonial-list li:last');
    $last.remove().css({ 'margin-left': '-415px' });
    $('#testimonial-list li:first').before($last);
    $last.animate({ 'margin-left': '0px' }, animtime); 
  });
  
  $('#nxt-testimonial').on('click', function(){
    var $first = $('#testimonial-list li:first');
    $first.animate({ 'margin-left': '-415px' }, animtime, function() {
      $first.remove().css({ 'margin-left': '0px' });
      $('#testimonial-list li:last').after($first);
    });  
  });


  // vars for clients list carousel
  // http://stackoverflow.com/questions/6759494/jquery-function-definition-in-a-carousel-script
  var $clientcarousel = $('#clients-list');
  var clients = $clientcarousel.children().length;
  var clientwidth = (clients * 140); // 140px width for each client item 
  $clientcarousel.css('width',clientwidth);
  
  var rotating = true;
  var clientspeed = 1800;
  var seeclients = setInterval(rotateClients, clientspeed);
  
  $(document).on({
    mouseenter: function(){
      rotating = false; // turn off rotation when hovering
    },
    mouseleave: function(){
      rotating = true;
    }
  }, '#clients');
  
  function rotateClients() {
    if(rotating != false) {
      var $first = $('#clients-list li:first');
      $first.animate({ 'margin-left': '-140px' }, 600, function() {
        $first.remove().css({ 'margin-left': '0px' });
        $('#clients-list li:last').after($first);
      });
    }
  }
});