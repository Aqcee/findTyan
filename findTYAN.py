import requests
import json 
file = open('/home/nikita/Рабочий стол/findTYAN/base', 'w')

i = 0
while True:
	request = requests.post('https://api.vk.com/method/groups.getMembers?group_id=bugurt_thread&fields=sex,city&offset='+str(i))
	parsed_string = json.loads(request.text)
	try_of_catch_TYAN = 0
	
	while True:
		default_string = ''
		try:
			def_id = parsed_string["response"]["users"][try_of_catch_TYAN]["uid"]
		except IndexError:
			break
		try: 
			gender = parsed_string["response"]["users"][try_of_catch_TYAN]["sex"]
		except IndexError:
			break
		try: 
			city = parsed_string["response"]["users"][try_of_catch_TYAN]["city"]
		except KeyError:
			None
		if (gender == 1):
			ID_BOGINI = parsed_string["response"]["users"][try_of_catch_TYAN]["uid"]
			default_string = default_string + 'Тян'
			if (city == 10):
				ID_BOGINI = parsed_string["response"]["users"][try_of_catch_TYAN]["uid"]
				default_string = (default_string + ' из моего города №'+str(city) + '. Айди ' +str(ID_BOGINI)+ '\n')
				file.write(default_string)
				print(('vk.com/id'+str(ID_BOGINI)))

			else: 
				default_string = (default_string + ', город номер '+str(city) + '. Айди ' +str(ID_BOGINI)+ '\n')
				file.write(default_string)
		else:
			default_string = (default_string + 'Мужчина' + '. Айди ' + str(def_id) + '\n')
			file.write(default_string)


		try_of_catch_TYAN = try_of_catch_TYAN + 1
	i = i + 1000