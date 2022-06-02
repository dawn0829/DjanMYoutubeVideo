// script to validadeEmail
function validadeEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-z-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email)
}
function validadeAll() {
    var name = $("#name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var age = $("#age").val();
    var gender = $("#gender").val();
    

    if (name == '') {
        swal("Opsss ! ", "Name field cannot be empty", "error");console.log("name");
        return false;
    }
    else if (phone == '') {
        swal("Opsss ! ", "phone field cannot be empty", "error");
        return false;
    }   
    else if (email == '') {
        swal("Opsss ! ", "email field cannot be empty", "error");
        return false;
    }
    else if (!(validadeEmail(email))) {
        swal("Opsss ! ", "email format wrong", "error");
        return false;
    }
    else if (age == '') {
        swal("Opsss ! ", "age field cannot be empty", "error");
        
        return false;
    }
    else if (age > 120) {
        swal("Opsss ! ", "The maxium value is 120 years", "error");
        $("#age").val("")
        return false;
    }

    else if (gender == '') {
        swal("Opsss ! ", "gender field cannot be empty", "error");
        return false;
    }
    else {
        return true
    }
}
$("#btn-add").bind("click", validadeAll);

// script Name field
$(document).ready(function() {
    jQuery('input[name="name"').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });
    // prevent start with space
    $("input").on("keypress", function(e) {
        if (e.which === 32 && ! this.value.length)
        e.preventDefault();
    });
});

// First letter captalized
$("#name").keyup(function() {
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){ return $1.toUpperCase( );}));
});

// lower case in email
$(document).ready(function() {
    $("#email").keyup(function() {
        this.value = this.value.toLowerCase();
    });
});

// only allow number in age
$("#age").keyup(function() {
    if(!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9.]/).join('');
    }
});

// phone mask
$(document).ready(function() {
    $("#phone").inputmask("(99) 99999-999", {"onincomplete": function() {
        swal("Opsss !", "Incomplete phone Review", "error");
        return false;
        }
    });
});