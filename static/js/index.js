//



let pass = document.querySelector('.pass')
let box_block = document.querySelector('.box_block')
let close0 = document.querySelector('.close')
let close1 = document.querySelector('.close1')
let close11 = document.querySelector('.close1')
let log_in_div = document.querySelector('.log_in_div')
let Pay_item = document.querySelector('.Pay_item')
let close12 = document.querySelector('.close12')
let one_div = document.querySelector('.one_div')
let log1 = document.querySelector('.log1')
let blur_bg = document.querySelector('.blur_bg')
let blur_bg12 = document.querySelector('.blur_bg12')
let retail = document.querySelector('.retail')
let blur_bg1 = document.querySelector('.blur_bg1')
let one_log = document.querySelector('.one_log')
let blur_bg_2 = document.querySelector('.blur_bg_2')
let grid_wrap = document.querySelector('.grid_wrap')
let first = document.querySelector('.first1')
let first_flex_block_in_container = document.querySelector('.first_flex_block_in_container')
let second_header_cont = document.querySelector('.second_header_cont')
let burg_menu = document.querySelector('.burg_menu')
let searc_log = document.querySelector('.searc_log')
let search_block = document.querySelector('.search_block')
let bg_block = document.querySelector('.bg_block')

searc_log.onclick = () =>{
    search_block.classList.toggle('search_block_active')
    bg_block.classList.toggle('bg_block_active')
}
bg_block.onclick = () =>{
    search_block.classList.toggle('search_block_active')
    bg_block.classList.toggle('bg_block_active')
}


burg_menu.onclick = () =>{
    first.classList.toggle('active_burg')
}


second_header_cont.onclick = () =>{
    first_flex_block_in_container.classList.toggle('first_flex_active')
}






