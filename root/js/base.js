function ajax(opt){
	opt.url = opt.url || '';
	opt.type = opt.type || 'GET';
	opt.data = opt.data || {};
	opt.success = opt.success || function(){}

	$.ajax({
		url:opt.url,
		type:opt.type,
		data:opt.data,
		success:function(res){
			
			
			opt.success(res);
		}
	});



	 $.ajax({
                            url:'check_db_exists.py',
                            type:'post',
                            data:{'db_url':db_url},
                            success:function(res){
                                console.log(res);
                            }

                        });
}