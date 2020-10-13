$(document).ready(function(){
    $('#searchbar').keyup(function(){
        var data = $(this).serialize() 
        $.ajax({
            method: "GET",
            url: '/usersearch',
            data: data
        })
        .done(function(res)
        {
            var inputVal = $("#searchbar").val();
            if( inputVal == '')
            {
                console.log("yes")
                $('#suggestions').html('');
            }
            else
            {
                $('#suggestions').html(res);
            } 
        })
        return false
    })
}) 