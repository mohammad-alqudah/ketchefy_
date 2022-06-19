function formData(e){
    PreventDefaults(e);
    
    console.log(e.target);
}

$( document ).ready(function() {
    document.getElementById("filterForm").addEventListener("submit", formData)
});

