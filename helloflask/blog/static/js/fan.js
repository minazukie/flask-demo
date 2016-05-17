function login(){
    $('#load').show();
    $('#bar').hide();
    setTimeout(function(){
	  $('#load').hide();
    $('#bar').show();},2000);
    $.post("signin",{username:$('#username').val(),password:$('#password').val()},function(result){
    if(result == 'yes'){
        setTimeout(function(){
	  $('#loginform').submit();},2000);
    }else{
        setTimeout(function(){
	  $('#loginmsg').html('用户名或密码错误，请重新登录。');},2000);

    }
  });
}
function logout(){
    $('#logoutform').submit();
}
function blogpost(){
     var pre = CKEDITOR.instances.preTextArea.getData();
     var text = CKEDITOR.instances.textTextArea.getData();
    $.post("blogpost",{title:$('#newtitle').val(),tag:$('#newtag').val(),pre:pre,text:text},function(msg){
    if(msg == 'yes'){
        $('#loginform').submit();
    }else{
       alert("服务器错误");
    }
  });
}
function commpost(){
     $('#send').hide();
    $('#load2').show();


    if ($('#nickname').val() ==""){
        Materialize.toast('昵称不能为空！', 6000);
        $('#send').show();
    $('#load2').hide();
        return false;
    }
        if ($('#pinglun').val() ==""){
        Materialize.toast('评论不能为空！', 6000);
        $('#send').show();
    $('#load2').hide();
        return  false;
    }

        setTimeout(function(){
	  $('#commform').submit();},2000);

}