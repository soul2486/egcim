import FormPersistence from 'form-persistence';
let myForm = document.getElementById('form')
FormPersistence.persist(myForm, true)
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navigation").style.top = "0";
  } else {
    document.getElementById("navigation").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
} 
const selection=document.getElementById('multipleSelect')
const selection2=document.getElementsByTagName('native-select')
const ligne = document.getElementById("ligne");
const colone = document.getElementById("colone");
// json memmoire
$.ajax({
    type:'GET',
    url:'/memoire/consulter/',
    success: function(response){
      console.log(response.data)
      // const memoireData = response.data
      // memoireData.map(item=>{
      // const option = document.createElement('option')
      //   option.textContent = item.annee_academique
      //   option.setAttribute('value', item.id)
      //   selection.appendChild(option)

      // })
    },
    error: function(error){
      console.log(error)
    }
})
selection.addEventListener('change', e=>{
    const selected_filtre = e.target.value

    $.ajax({
        type:'GET',
        url:`/memoire/get_filtre/${selected_filtre}`,
        success: function(response){
          console.log(response.data)
          // console.log(response.etudiant)
          // const filtreData = response.data
          // const filtreEtudiant = response.etudiant
          // filtreData.map(item=>{
          //    const div1 = document.createElement('div')
          //    div1.setAttribute('class', 'col-6 col-md-4 col-xl-3 col-xxl-2')
          //    div1.setAttribute('id','div1')
          //    const div2 = document.createElement('div')
          //    div2.setAttribute('class', 'app-card app-card-doc shadow-sm h-100')
          //    div2.setAttribute('id','div2')
          //    const div3 = document.createElement('div')
          //    div3.setAttribute('class', 'app-card-thumb-holder p-3')
          //    div3.setAttribute('id','div3')
          //    const span1 = document.createElement('span')
          //    span1.setAttribute('class','icon-holder')
          //    span1.setAttribute('id','span1')
          //    const i1 = document.createElement('i')
          //    i1.setAttribute('class','fas fa-file-pdf pdf-file')
          //    span1.appendChild(i1)
          //    const span2 = document.createElement('span')
          //    span2.setAttribute('class','badge bg-success')
          //    span2.setAttribute('id','span2')
          //    span2.textContent = 'NEW'
          //    div3.appendChild(span1)
          //    div3.appendChild(span2)
          //    const div4 = document.createElement('div')
          //    div4.setAttribute('class', 'app-card-body p-3 has-card-actions')
          //    div4.setAttribute('id','div4')
          //    const h41 = document.createElement('h4')
          //    h41.setAttribute('class','app-doc-title truncate mb-0')
          //    h41.textContent = item.titre
          //    div4.appendChild(h41)
          //    const div5 = document.createElement('div')
          //    div5.setAttribute('class', 'app-doc-meta')
          //    div5.setAttribute('id','div5')
          //    const ul1 = document.createElement('ul')
          //    ul1.setAttribute('class', 'list-unstyled mb-0')
          //    ul1.setAttribute('id','ul1')
          //    const li1 = document.createElement('li')
          //    li1.setAttribute('class', 'list-unstyled mb-0')
          //    li1.setAttribute('id','li1')
          //    li1.textContent = item.etudiant_id.nom
          //    const li2 = document.createElement('li')
          //    li2.setAttribute('class', 'list-unstyled mb-0')
          //    li2.setAttribute('id','li2')
          //    li2.textContent = item.date_creation
          //    ul1.appendChild(li1)
          //    ul1.appendChild(li2)
          //    div5.appendChild(ul1)
          //    div4.appendChild(div5)
          //    div2.appendChild(div3)
          //    div2.appendChild(div4)
          //    div1.appendChild(div2)
          //    ligne.appendChild(div1)
            // const titre_doc = document.getElementById('titre_doc')
            
            // const nom_prenom = document.getElementById('nom_prenom')
            // const date = document.getElementById('date')
            // const parcours = document.getElementById('parcours')
            
            // nom_prenom.textContent = item.nom
            // parcours.textContent = item.parcours
            // date.textContent = item.date
          // })
        },
        error: function(error){
          console.log(error)
        }
    })
})