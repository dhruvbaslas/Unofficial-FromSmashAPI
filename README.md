# Unofficial-FromSmashAPI
This is an Unofficial Selenium and Python Based Toolkit of fromsmash.com


"1" is for generate a link mode and "2" is for send link to an email mode

Arguments for uploading a single file - (file path , mode)

	from FromSmashAPI import FromSmashAPI
	api = FromSmashAPI()
	print(api.upload_file("abc.jpeg", 2))
	
Arguments for uploading a multiple file - (list of file paths , mode)

	from FromSmashAPI import FromSmashAPI
	api = FromSmashAPI()
	api.upload_multiple_files(files_list, 1)
