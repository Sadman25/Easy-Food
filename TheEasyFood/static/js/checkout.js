if (localStorage.getItem('cart') == null) {
    var cart = {}
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

console.log(cart);
var sum = 0;
var totalPrice = 0
if ($.isEmptyObject(cart)){
    myStr = `<p>Your Cart is Empty.. Please Add some item to your cart...</p>`
        $('#items').append(myStr);
}else{
    for(item in cart){
        let name = cart[item][1];
        let qty = cart[item][0];
        let itemPrice = cart[item][2];
        sum = sum+qty;
        totalPrice = totalPrice + qty*itemPrice;
        myStr = `<li class="list-group-item d-flex justify-content-between align-items-center">
        ${name}
        <span class="badge badge-primary badge-pill">${qty}</span>
    </li>`
        $('#items').append(myStr);
    }

}
document.getElementById('cart').innerHTML = sum;
document.getElementById('totalPrice').innerHTML = totalPrice;
$('#itemsJson').val(JSON.stringify(cart));


$('#placeOrder').on("click",function (){
    localStorage.clear();
})  
