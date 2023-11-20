//const schemListElement = document.querySelector(`.schem_list`);
//const schemElements = tasksListElement.querySelectorAll(`.schem_item`);
//
//window.onload = function() {
//    // Перебираем все элементы списка и присваиваем нужное значение
//    for (const element of schemElements) {
//      element.draggable = true;
//    }
//};
//
//
//schemListElement.addEventListener(`dragstart`, (evt) => {
//  evt.target.classList.add(`selected`);
//})
//
//schemListElement.addEventListener(`dragend`, (evt) => {
//  evt.target.classList.remove(`selected`);
//});
//
function onDragStart(event) {
  event
    .dataTransfer
    .setData('text/plain', event.target.id);

  event
    .currentTarget
    .style
    .backgroundColor = 'yellow';

}

function onDragOver(event) {
  event.preventDefault();
}

function onDrop(event) {
  const id = event
    .dataTransfer
    .getData('text');

  // Объявляем перетаскиваемый объект
  const draggableElement = document.getElementById(id);
  const dropzone = event.target;

  // Очищаем прошлые объекты
  const old_id = dropzone.id+'element'
  var old_element = document.getElementById(old_id);
//  console.log('id=', old_id)
//  console.log('element=', old_element);
  if(old_element !== null){
    dropzone.removeChild(old_element);
    }

  // Клонируем и вставляем объект
  const clone = draggableElement.cloneNode(true);
  clone.id = dropzone.id+'element';
  dropzone.appendChild(clone);

  // Отображаем тип схемы
//  console.log('schem_part=',  dropzone.dataset.part);
//  console.log('type=', draggableElement.dataset.type);
  const schem = document.getElementById('schem-type').value.replaceAll(',', '');
  type = schem.split('');
//  console.log('all_type=', type);
  type.splice(dropzone.dataset.part - 1, 1, draggableElement.dataset.type);
//  console.log('toStr=', type.toString().replaceAll(',', ''))
  document.getElementById('schem-type').value = type.toString().replaceAll(',', '');
  // Сброс объект dataTransfer:
  event
    .dataTransfer
    .clearData();

}

