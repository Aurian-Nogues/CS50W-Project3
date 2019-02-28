//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

    $(document).on("click","#complete_order",complete_order);
    $(document).on("click","#cancel_order",cancel_order);

    

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


function complete_order(){
    //define variables to be passed
    price = $(this).closest('td').prev('td');
    a = $(price).closest('td').prev('td');
    order = $(a).closest('td').prev('td');
    order = order.text();
    status="completed"

    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/update_order",
        dataType: "json",
        data: {"order": order, "status": status},
    });
    //reload page
    location.reload();
};

function cancel_order(){
    //define variables to be passed
    a = $(this).closest('td').prev('td');
    b = $(a).closest('td').prev('td');
    c = $(b).closest('td').prev('td');
    order = $(c).closest('td').prev('td');
    order = order.text();
    alert(order);
    status="cancelled"

    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/update_order",
        dataType: "json",
        data: {"order": order, "status": status},
    });
    //reload page
    location.reload();
};

