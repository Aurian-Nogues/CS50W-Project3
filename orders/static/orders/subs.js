//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

load_steak_and_cheese();
$(document).on("click",".extra-button",add_extra);

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

function add_extra(){
    //get selected extra and price
    price = $(this).closest('td').prev('td');
    extra = $(price).closest('td').prev('td');
    price = price.text();
    extra = extra.text();

    //update list of extras
    extras_list = document.querySelector('#sub_extras').innerHTML;
    if (extras_list == "None"){
        extras_list = "";
    } else {
        extras_list = document.querySelector('#sub_extras').innerHTML + ' ';
    }
    extras_list = extras_list += extra
    document.querySelector('#sub_extras').innerHTML = extras_list;

    //update total order price
    price = parseFloat(price);
    previous_price = document.querySelector('#sub_price').innerHTML;
    previous_price = parseFloat(previous_price);
    new_price = previous_price += price;
    document.querySelector('#sub_price').innerHTML = new_price;


};