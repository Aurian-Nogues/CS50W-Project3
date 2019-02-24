//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
    $(document).on("click",".pizza-button",test);

});

function test(){
    alert("I am here");
}