function login(){
    $('.ui.green.basic.inverted.button').addClass("loading");
    $.post("/signin",{username:$('#username').val(),password:$('#password').val()},function(result){
    if(result == 'yes'){
        setTimeout(function(){
	  $('#loginform').submit();},1000);
    }else{
        setTimeout(function(){
	  $('#loginmsg').html('用户名或密码错误，请重新登录。');$('.ui.green.basic.inverted.button').removeClass("loading");},1000);

    }
  });
}
function logout(){
    $('#logoutform').submit();
}
function blogpost(){
    $('#blogpost').addClass('loading');
     var pre = pretext.$txt.html();
     var text = maintext.$txt.html();
    if($('#newtitle').val()==""){
                setTimeout(function(){
	  $('#blogpost').removeClass('loading');},1000);

        return false;
    }
    if($('#newtag').val()==""){
        setTimeout(function(){
	  $('#blogpost').removeClass('loading');},1000);
        return false;
    }
    $.post("blogpost",{title:$('#newtitle').val(),tag:$('#newtag').val(),pre:pre,text:text},function(msg){
    if(msg == 'yes'){
        $('#enteradmin').submit();
    }else{
     $('#blogpost').removeClass('loading');
     alert("服务器错误");

    }
  });
}
function blogedit(){
    $('#blogedit').addClass('loading');
     var pre = pretext.$txt.html().replace(/\'/g,"&#039;");
     var text = maintext.$txt.html().replace(/\'/g,"&#039;");
    $.post("../blogedit",{id:$('#editid').val(),title:$('#edittitle').val(),tag:$('#edittag').val(),pre:pre,text:text},function(msg){
    if(msg == 'yes'){
        $('#enteradmin').submit();
    }else{
        $('#blogedit').removeClass('loading');
        alert("服务器错误");

    }
  });
}
function commpost(){
    $("#send").addClass("loading");
    if ($('#nickname').val() ==""){
        $("#send").removeClass("loading");
        return false;
    }
        if ($('#pinglun').val() ==""){
        $("#send").removeClass("loading");
        return  false;
    }
        if ($('#vc').val() ==""){
        $("#send").removeClass("loading");
        return  false;
    }
        setTimeout(function(){
	  $('#commform').submit();},1000);

}
function search(){
     if ($('#kw').val() ==""){
        return false;}
     else{window.location.href="/search/"+$('#kw').val() ;}
}
