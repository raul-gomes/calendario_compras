const ROOT = "http://127.0.0.1:8000/compras/";

const infos = document.getElementsById("link-info")

const showData = (result)=>{
    for(const campo in result){
        if(document.querySelector("#"+campo))
            document.querySelector("#"+campo).value = result[campo]
    }

}

function abreModal(pk){
    console.log(pk)
    fetch(ROOT+pk,
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

    const pk = infos[i].getAttribute("href")

    infos[i].addEventListener("click", abreModal(pk))

}
