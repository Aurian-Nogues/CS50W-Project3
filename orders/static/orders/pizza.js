//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
    //$(document).on("click",".pizza-button",add_pizza);
    load_cheese();
    $(document).on("click",".topping-button",add_topping);
    $(document).on("click","#reset_toppings",reset_toppings);
    $(document).on("click","#place_pizza_order",place_pizza_order);

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

//adds a topping to the topping list
function add_topping(){
    //get how many toppings are left to pick
    counter = document.querySelector('#toppings_counter').innerHTML;
    
    //if there are still some toppings to pick
    if(counter > 0){
        //get selected topping and add it to the list of existing topings
        topping = $(this).closest('td').prev('td');
        topping = topping.text();
        toppings_list = document.querySelector('#toppings_selected').innerHTML
        
        if (toppings_list == "None"){
            toppings_list = "";
        } else {
            toppings_list = document.querySelector('#toppings_selected').innerHTML + ' ';
        }
        toppings_list = toppings_list += topping;
        document.querySelector('#toppings_selected').innerHTML = toppings_list;

        //update number of toppings left to pick
        counter  = counter - 1;
        document.querySelector('#toppings_counter').innerHTML = counter;

        //if there are no toppings left to pick enable place order button
        if (counter == 0){
            document.getElementById("place_pizza_order").classList.remove('disabled');
        }

    //alert user if he is trying to go beyond his topping allowance
    } else{
        alert("Maximum number of toppings selected");
    }
}

//enable order button when loading pizza with no toppings
function load_cheese(){
    toppings = document.querySelector('#toppings_description').innerHTML;
    if (toppings == "Cheese"){
        document.getElementById("place_pizza_order").classList.remove('disabled');
    }
}

//reset toppings list and counter
function reset_toppings(){
    //get the type of pizza and deduct right topping allowance
    toppings = document.querySelector('#toppings_description').innerHTML;
    
    if (toppings == "Cheese"){
        counter = 0;
    } else if (toppings == "1 topping"){
        counter = 1;
    } else if (toppings == "2 toppings"){
        counter = 2;
    } else if (toppings == "3 toppings"){
        counter = 3;
    } else if (toppings == "Special"){
        counter = 5;
    }

    //reset all fields
    document.querySelector('#toppings_counter').innerHTML = counter;
    document.querySelector('#toppings_selected').innerHTML = "None"

    //if reset toppings button is active, disable it
    if (document.getElementById("place_pizza_order").classList.contains("disabled")){
        return false
    } else {
        document.getElementById("place_pizza_order").classList.add('disabled');
    }
}

//send order to Django to add it to database
function place_pizza_order(){
    if (this.classList.contains("disabled")){
        return false
    }

    //define variables to be passed
    pizza_type = document.querySelector('#pizza_type').innerHTML + ' ';
    pizza_topping = document.querySelector('#toppings_description').innerHTML;
    item = pizza_type + pizza_topping;
    price = document.querySelector('#pizza_price').innerHTML;
    toppings = document.querySelector('#toppings_selected').innerHTML;

    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/add_pizza",
        dataType: "json",
        data: {"item": item, "price": price, "toppings":toppings},

    });
    //redirect to next page
    window.location.pathname = 'home';
}

