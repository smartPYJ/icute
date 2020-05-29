let counter = 0;
function count(){

   counter++;
   document.querySelector('#support').innerHTML=counter;
  

}
(function() {
  const cute = document.getElementById('cute');
  cute.addEventListener('click', function() {
    cute.classList.toggle('red');
  });
})();