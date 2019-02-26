//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
    //$(document).on("click",".pizza-button",add_pizza);
    load_cheese();
    $(document).on("click",".topping-button",add_topping);
    $(document).on("click","#reset_toppings",reset_toppings);
    $(document).on("click","#place_pizza_order",place_pizza_order);

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

    alert("sending order");
}

function add_pizza(){
    var price = $(this).closest('td').prev('td');
    var topping = $(price).closest('td').prev('td');
    var size = $(topping).closest('td').prev('td');

    type= "standard pizza"
    price = price.text();
    price = parseFloat (price);
    topping = topping.text();
    size = size.text();

    console.log(type);
    console.log(price);
    console.log(topping);
    console.log(size);
    alert("here");
}

