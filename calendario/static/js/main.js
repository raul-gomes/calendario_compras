console.log('hellor world')
var endpoint = document.getElementById('endpoint').getAttribute('href');
var modalBody = document.getElementById('modal-body')

$.ajax({
    type: 'GET',
    url: endpoint,
    success: function(response){
        console.log(response)
        const data = JSON.parse(response.data)
        data.forEach(el=>{
            console.log(el.fields)
        })
    },
    error: function(error){
        console.log(error)
    }
})