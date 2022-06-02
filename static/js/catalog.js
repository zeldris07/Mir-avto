
let div_all = document.querySelector('.div_all')
let div_all1 = document.querySelector('.div_all1')

div_all.onclick = () =>{
   grid_wrap.classList.add('grid_style')
   div_all1.classList.add('class_active')
   div_all.style.display = 'none'
}
div_all1.onclick = () =>{
   grid_wrap.classList.remove('grid_style')
   div_all1.classList.remove('class_active')
   div_all.style.display = 'flex'
}
