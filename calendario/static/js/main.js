//const ROOT = "https://calendariocompras.raulgomes1.repl.co:3000/compras/";
const ROOT = "http://127.0.0.1:8000/compras/";

const infos = document.getElementsByClassName("link-info")

const showData = (result)=>{
    for(const campo in result){
        if(document.querySelector("#"+campo))
            document.querySelector("#"+campo).value = result[campo]
    }

}

function abreModal(evento){
    evento.preventDefault()
    const elemento = evento.target.parentNode.getAttribute('id')
    fetch(ROOT+elemento,
        { method : "GET" ,
          headers : new Headers() ,
          mode : 'cors' ,
          cache  : 'default'
        })
    .then( response => { response.json()
        .then( data => showData(data))
     })
    .catch(e => console.log('erro ao pegar as informações da compra'))
}


for (var i = 0; i < infos.length; i++) {
  
    infos[i].addEventListener("click", abreModal)

}
