//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

load_steak_and_cheese();
$(document).on("click",".extra-button",add_extra);
$(document).on("click","#reset_extras",reset_extras);
$(document).on("click","#place_sub_order",place_sub_order);

////////////////////////////////////////////////////////////////
//These functions are required to obtain CSRF code and attach it to POST methods

        // CSRF code
        function getCookie(name) {
            var cookieValue = null;
            var i = 0;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (i; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');
    
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }); 
/////////////////////////////////////////////////////////////////
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


//adds extra toppings to list and price
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


//reset toppings and price
function reset_extras(){
    location.reload();
};

//place sub order
function place_sub_order(){
    
    //define variables to be passed
    sub_size = document.querySelector('#sub_size').innerHTML + ' ';
    sub_type = document.querySelector('#sub_type').innerHTML;
    item = sub_size + sub_type;
    price = document.querySelector('#sub_price').innerHTML;
    extras = document.querySelector('#sub_extras').innerHTML;

    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/add_sub",
        dataType: "json",
        data: {"item": item, "price": price, "extras":extras},

    });
    //redirect to next page
    window.location.pathname = 'home';
};