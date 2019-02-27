//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

    $(document).on("click",".delete-button",delete_item);
    $(document).on("click","#place_order",place_order);

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
    
//ajax request to delete items form basket
function delete_item(){
    //define variables to be passed
    price = $(this).closest('td').prev('td');
    extras = $(price).closest('td').prev('td');
    item = $(extras).closest('td').prev('td');
    price = price.text();
    extras = extras.text();
    item = item.text();
    order_number = document.querySelector('#order_number').innerHTML;
    
    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/delete_item",
        dataType: "json",
        data: {"item": item, "price": price, "extras":extras, "order_number":order_number},
    });

    //reload page
    location.reload();
};
    
function place_order(){
    total = document.querySelector('#total_amount').innerHTML;
    message = "Do you want to confirm you order for $" + total + " ?"

    //if customer confirms, move order to confirmed
    if (confirm(message)) {
        order_number = document.querySelector('#order_number').innerHTML;
        //make ajax post request
        $.ajax({
        type: "POST",
        url: "/confirm_order",
        dataType: "json",
        data: {"order_number":order_number},
    });
    window.location.pathname = 'home';
    } 
}