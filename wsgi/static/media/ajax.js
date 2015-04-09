$(function () {
    if ($.cookie('webwordedit_cookie') != 'Yes'){
	set_language("first");
    }else{
	set_language($.cookie('language_cookie'));
    }
});


var languages = {
    "Marathi":"mr",
    "Danish":"da",
    "Bengali":"bn",
    "German":"de",
    "Gujarati":"gu",
    "Hindi":"hi",
    "Kannada":"kn",
    "Telugu":"te",
    "Tamil":"ta",
    "Assami":"as",
    "Oriya":"or",
    "Punjabi":"pa"
};

var locales = {
    "mr": ["mr_in"],
    "da": ["da_dk"],
    "bn": ["bn_in"],
    "de": ["de_de"],
    "gu": ["gu_in"],
    "hi": ["hi_in"],
    "kn": ["kn_in"],
    "te": ["te_in"],
    "ta": ["ta_in"],
    "as": ["as_in"],
    "or": ["or_in"],
    "pa": ["pa_in"]
};


function set_language(lang){
    $("#language").empty();
    for ( var l in languages){
	$("#language").append('<option value='+languages[l]+'>'+l+'</option>');
    };
    if (lang != "first"){
	$("#language").val(lang);
	load_options('','first');
    }else{
	load_options('',$.cookie('locale_cookie'));
    }
    $.cookie('webwordedit_cookie', 'Yes',{ expires: 7, path: '/' });
};

function load_options(id,index){
    var selectedValue = document.getElementById("language").value;
    var lc = locales[selectedValue];
    $("#locale").empty();
    for( var lang_id in lc){
	$("#locale").append('<option value='+lc[lang_id]+'>'+lc[lang_id]+'</option>');
    };
    if(index!="first"){
	$("#locale").val(index);
    };
    $.cookie('language_cookie',document.getElementById("language").value,{ expires: 7, path: '/' });
    $.cookie('locale_cookie',document.getElementById("locale").value,{ expires: 7, path: '/' });
};



/*
function set_language(lang){
    $.ajax({
        url: "/language",
        dataType : 'json',
        type : 'GET',
        data : {},
        success : function(data) {
            $("#language").empty();
            $.each(data,function(index,val){
		alert(val.lang_code);
                $("#language").append('<option value='+val.lang_code+'>'+val.language+'</option>');
            });
            if (lang != "first"){
                $("#language").val(lang);
                load_options('','first');
            }else{
		 load_options('',$.cookie('locale_cookie'));
            }
            $.cookie('webwordedit_cookie', 'Yes',{ expires: 7, path: '/' });
        }
     });
};

function load_options(id,index){
    var selectedValue = document.getElementById("language").value;
    var urls = "/locale/" + selectedValue;
    $.ajax({
        url: urls,
        dataType : 'json',
	type : 'GET',
	data : {},
        success : function(data) {
            $("#locale").empty();
            $.each(data,function(index,val){
                $("#locale").append('<option value='+val.locale+'>'+val.locale+'</option>');
            });
            if(index!="first"){
                $("#locale").val(index);
            }

            $.cookie('language_cookie',document.getElementById("language").value,{ expires: 7, path: '/' });
            $.cookie('locale_cookie',document.getElementById("locale").value,{ expires: 7, path: '/' });
        }
    });
};

*/


function verify_list(){
    var langValue = document.getElementById("language").value;
    var localeValue = document.getElementById("locale").value;
    var new_url = $(this).attr("verifyList") + "/" + langValue + "/" + localeValue;
    $('#verifyList').attr('href',new_url);
};


function verified_list(){
    var langValue = document.getElementById("language").value;
    var localeValue = document.getElementById("locale").value;
    var new_url = $(this).attr("verifiedList") + "/" + langValue + "/" + localeValue;
    $('#verifiedList').attr('href',new_url);
};


