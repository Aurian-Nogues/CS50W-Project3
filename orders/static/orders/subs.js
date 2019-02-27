//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

load_steak_and_cheese();

});


//hide non available toppings if not loading steak and cheese sub
function load_steak_and_cheese(){
    sub = document.querySelector('#sub_type').innerHTML
    if (sub != "Steak + Cheese***"){
        //document.getElementById('inputBox').style.visibility='visible';
        for (i = 0; i < 3; i++) { 
            document.getElementsByClassName('steak')[i].style.visibility = 'hidden';
          }

        return false
    } else {
        return false
    }
    

};