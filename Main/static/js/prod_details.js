const product_main_img = document.getElementById("product-main-img")
const product_sub_img = document.getElementsByClassName("product-sub-image")

// product_sub_img
console.log(product_sub_img)
for(let e of product_sub_img){
    e.onclick = function(){
        let src = product_main_img.src
        product_main_img.src = e.src
        e.src = src
    }
}