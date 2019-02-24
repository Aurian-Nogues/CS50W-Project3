//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
    $(document).on("click",".pizza-button",add_pizza);

});

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
}