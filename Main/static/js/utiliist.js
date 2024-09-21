function showSection(id){
    document.getElementById('show-home').classList.add('hidden');
    document.getElementById('more-vegetable-product').classList.add('hidden')
    // document.getElementById('electronics').classList.add('hidden')
    document.getElementById('more-electronics-product').classList.add('hidden')
    document.getElementById('more-colddrinks-product').classList.add('hidden')
    document.getElementById(id).classList.remove('hidden')
}