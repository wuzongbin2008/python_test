import os

def get_project_no(pro_name):
    UNISTORE_PROJECTS = {
	0 :   {
		"name" : 'sandbox',
		"max_size" :500000,
		"skey" : "11111111"
	},
	1 :   {
		"name" : 'video',
		"max_size" : 2000000000,
		"skey" : "os[n@cW8b8oKHpJJh%s_|9Ux5MN`AXK8"
	},
	2 :   {
		"name" : 'tuding',
		"max_size" : 3000000000,
		"skey" : "L:c|k/\yHo>pbW]E=qchLc^}`g$]z//B"
	},
	3 :   {
		"name" : 'miaopai',
		"max_size" :  500000000,
		"skey"	: "/n9WQl@=396]K/<=5LTRzF@g9[:+T]_&"
	},
	4 :   {
		"name" : 'wbcamer',
		"max_size" : 500000000,
		"skey" :"Om@Id$Quav{og(iAc>vi=ov+wuCs;E)O"
	},
}
    pro_no = None
    for pro_no in UNISTORE_PROJECTS:
        if UNISTORE_PROJECTS[pro_no]['name'] == pro_name.strip():
            return pro_no
    return pro_no

def implode():
    array = ['This', 'is', 'some', 'Python', 'code']
    s = '\n'.join([str(i) for i in array])
    print s

implode()
