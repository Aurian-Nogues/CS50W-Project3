//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
    //$(document).on("click",".pizza-button",add_pizza);
    $(document).on("click",".topping-button",add_topping);

});


function add_topping(){

    
    counter = document.querySelector('#toppings_counter').innerHTML;
    if(counter > 0){

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

        counter  = counter - 1;
        document.querySelector('#toppings_counter').innerHTML = counter;
    } else{
        alert("counter at 0");
    }

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

